"""Offline tests: scoring rules and each parser on small sample pages.

Run from the job-hunter folder:  python -m pytest -q
"""
import yaml
from pathlib import Path

from job_hunter.models import Job
from job_hunter.scoring import Scorer
from job_hunter.sources import icims, links, oracle_hcm, successfactors, workday

ROOT = Path(__file__).resolve().parent.parent
PROFILE = yaml.safe_load((ROOT / "config" / "profile.yaml").read_text())
S = Scorer(PROFILE)


def job(title, location="Port of Spain", desc=""):
    return Job(title=title, url=f"https://x/{title}", company="X", source="t",
               location=location, description=desc)


# ---------- scoring ----------
def test_software_and_data_roles_score_high():
    for t in ["Software Developer", "Back End Developer", "Programmer Analyst", "Data Analyst",
              "Automation Engineer", "Business Intelligence Analyst"]:
        j = job(t)
        assert S.keep(j, "tt"), t
        assert j.score >= 8, (t, j.score)


def test_tracks_pick_the_right_resume():
    assert (j := job("Data Engineer")) and S.score(j) and j.track == "data"
    assert (j := job("Full Stack Developer")) and S.score(j) and j.track == "software"
    assert (j := job("RPA Developer - Automation")) and S.score(j) and j.track in {"software", "automation"}


def test_non_ict_roles_are_dropped():
    for t in ["Petroleum Engineer", "Electrical Engineer", "Teller (Temporary)", "Sales Representative",
              "Legal Counsel", "Inventory Accounting Assistant", "Heavy-T Truck Driver"]:
        assert not S.keep(job(t), "tt"), t


def test_strong_ict_word_overrides_exclusion():
    assert S.keep(job("Electrical Engineer - Automation Systems"), "tt")


def test_location_filter():
    assert S.keep(job("Software Engineer", "Trincity, Trinidad and Tobago"), "filter")
    assert not S.keep(job("Software Engineer", "Houston, Texas"), "filter")
    j = job("Data Analyst", "Remote - Anywhere")
    assert S.keep(j, "filter") and j.remote


def test_seniority_and_skills_adjust_score():
    a, b = job("IT Director"), job("IT Officer")
    S.score(a), S.score(b)
    assert a.score < b.score
    c = job("Data Analyst", desc="Python, SQL, pandas and Power BI required")
    d = job("Data Analyst")
    S.score(c), S.score(d)
    assert c.score > d.score


# ---------- parsers ----------
WD_CFG = {"name": "Shell", "company": "Shell", "base_url": "https://shell.wd3.myworkdayjobs.com",
          "tenant": "shell", "site": "ShellCareers"}


def test_workday_parse():
    data = {"total": 1, "jobPostings": [{"title": "Data Engineer", "externalPath": "/job/Port-of-Spain/Data-Engineer_R1",
                                         "locationsText": "Port of Spain", "postedOn": "Posted Today"}]}
    [j] = workday.parse(data, WD_CFG)
    assert j.url == "https://shell.wd3.myworkdayjobs.com/en-US/ShellCareers/job/Port-of-Spain/Data-Engineer_R1"
    assert j.location == "Port of Spain"


def test_oracle_parse():
    cfg = {"name": "G", "company": "Guardian", "base_url": "https://fa.example.com", "site_number": "CX_1020"}
    data = {"items": [{"TotalJobsCount": 1, "requisitionList": [
        {"Id": "1807", "Title": "Developer", "PrimaryLocation": "Port of Spain, Trinidad and Tobago",
         "PostedDate": "2026-11-20", "ShortDescriptionStr": "Python and SQL",
         "secondaryLocations": [{"Name": "Kingston, Jamaica"}]}]}]}
    jobs, total = oracle_hcm.parse(data, cfg)
    assert total == 1 and jobs[0].url.endswith("/sites/CX_1020/job/1807")
    assert "Jamaica" in jobs[0].location


def test_successfactors_parse():
    html = """
    <span class="paginationLabel">Results <b>1 – 2</b> of <b>2</b></span>
    <table><tr class="data-row"><td><a class="jobTitle-link" href="/job/Port-of-Spain-Developer/123/">Developer</a></td>
      <td><span class="jobLocation">Port of Spain, TT</span></td><td><span class="jobDate">Nov 20, 2026</span></td></tr>
    <tr class="data-row"><td><a class="jobTitle-link" href="/job/Kingston-Analyst/456/">Analyst</a></td>
      <td><span class="jobLocation">Kingston, JM</span></td></tr></table>"""
    cfg = {"name": "FCB", "company": "FCB", "base_url": "https://careers.firstcitizenstt.com"}
    jobs, total = successfactors.parse(html, cfg)
    assert total == 2 and len(jobs) == 2
    assert jobs[0].url == "https://careers.firstcitizenstt.com/job/Port-of-Spain-Developer/123/"
    assert jobs[0].location == "Port of Spain, TT"


def test_icims_parse():
    html = """<div class="row"><a href="https://careers-lla.icims.com/jobs/7001/data-analyst/job?in_iframe=1">
      <span>Title</span> Data Analyst</a><span>TT-Trincity</span></div>"""
    cfg = {"name": "LLA", "company": "LLA", "base_url": "https://careers-lla.icims.com"}
    [j] = icims.parse(html, cfg)
    assert j.title == "Data Analyst" and j.location.startswith("TT-Trincity")


def test_links_parse_caribbeanjobs():
    html = """<div class="job-result"><h2><a href="/System-Engineer-Job-242091.aspx">System Engineer</a></h2>
      <span>Voice Outsourcing Ltd</span><span>Port-of-Spain</span></div>
      <a href="/Login.aspx">Login</a>"""
    cfg = {"name": "CJ", "company": "", "title_from": "caribbeanjobs",
           "link_regex": r"^https?://(www\.)?caribbeanjobs\.com/[^/?#]+-Job-\d+\.aspx$"}
    [j] = links.parse_links(html, "https://www.caribbeanjobs.com/ShowResults.aspx", cfg)
    assert j.title == "System Engineer" and "Port-of-Spain" in j.location


def test_page_watch_finds_vacancies():
    html = """<nav><a href="/about">About</a></nav>
      <main><a href="/wp-content/uploads/ICT-Analyst-Vacancy.pdf">ICT Analyst – Vacancy Notice</a>
      <a href="/contact">Contact</a></main>"""
    cfg = {"name": "NGC", "company": "NGC"}
    jobs = links.parse_page_watch(html, "https://ngc.co.tt/career-opportunities/", cfg)
    assert [j.title for j in jobs] == ["ICT Analyst – Vacancy Notice"]
