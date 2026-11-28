# job-hunter

Every morning this checks T&T employers' careers sites and job boards, keeps the ICT jobs
that fit my resumes, and posts the new ones to a GitHub Issue. It runs on GitHub Actions
at 6:17 AM Trinidad time.

**Phase 1 (this version):** find and rank jobs. No auto-applying.

## Where to read the results

| File | What it is |
|---|---|
| Issues tab | One issue per day that something new shows up (you get a GitHub notification) |
| [`results/latest.md`](results/latest.md) | Every matching job open right now, best first, grouped Software / Data / Automation |
| [`results/sources.md`](results/sources.md) | Which sites worked today, plus the ones to check by hand |
| [`results/jobs.csv`](results/jobs.csv) | Every match ever seen, with first and last seen dates |
| [`TARGET_EMPLOYERS.md`](TARGET_EMPLOYERS.md) | Employers to target and why |

Each job shows which resume to send: **Software**, **Data** or **Automation / IT**.

## How matching works

`config/profile.yaml` holds keywords taken from the three resumes:

1. **Title must look ICT.** Weighted patterns such as *developer* 9, *data analyst* 10,
   *automation* 9, and *IT/technology* 5 as a catch-all. The best match sets the score and
   the resume track.
2. **Non-ICT titles are dropped** (petroleum engineer, teller, sales and so on) unless a
   strong ICT word is also in the title.
3. **Adjustments:** director/head/chief −4, intern/trainee −4, senior/lead +1, and +1 per
   resume skill found in the description, up to +6. Remote-only roles get −1.
4. **Location:** sources marked `location: filter` only keep jobs in T&T, or remote ones.
5. Jobs scoring under `min_score` (5) are hidden.

To change what counts as a good job, edit `profile.yaml`. The next run picks it up.

## Adding a site

Add an entry to `config/sources.yaml`. Supported platforms:

| type | Recognise it by | Example |
|---|---|---|
| `workday` | `*.myworkdayjobs.com` | Shell, TransUnion |
| `oracle_hcm` | `fa-*.oraclecloud.com/hcmUI/CandidateExperience` | Guardian Group |
| `successfactors` | `careers.x.com/go/...` or `/search/?q=` | First Citizens, ANSA, Digicel, Scotiabank |
| `icims` | `*.icims.com` | Liberty Latin America |
| `links` | any page where each job is a link with a recognisable URL | CaribbeanJobs, EmployTT, JobsTT |
| `page_watch` | plain careers page or PDF adverts | NGC, Republic, JMMB |
| `manual` | needs a login or a browser | LinkedIn, UWI, Sagicor |

## Run it yourself

```bash
cd "# practice applications/job-hunter"
pip install -r requirements.txt
python -m pytest -q                       # offline tests
python -m job_hunter.main --dry-run       # full run, doesn't save state
python -m job_hunter.main --only Shell    # one source
```

You can also run it from GitHub: **Actions → job-hunter daily → Run workflow**.

## Roadmap

- [x] Phase 1: daily scrape, resume-based ranking, GitHub Issue digest
- [ ] Track applications (applied / interview / rejected) in `jobs.csv`
- [ ] Read full job descriptions for better skill scoring
- [ ] Draft a tailored cover letter per job
- [ ] Add more employers from `TARGET_EMPLOYERS.md` → "Still to add"
