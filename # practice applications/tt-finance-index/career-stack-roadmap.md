# TT Finance Index — Career Stack Roadmap

**What this document is:** a plan for turning TT Finance Index into a portfolio project that qualifies you for remote **Data Engineering / AI Engineering** roles, using the stack recommended in the Nov 2026 career research.

**How it relates to the other files in this folder:**

| File | Role |
| --- | --- |
| `tt-finance-index.md` | The product spec: *what* the app does. Still the source of truth. |
| `project-to-do.md` | The original 19 phases, focused on learning core Python. |
| `phase-1-to-do.md` | The detailed breakdown of Phase 1 (define the dataset). |
| **`career-stack-roadmap.md`** (this file) | *How* to build it with industry tools, in what order, and what to learn at each stage. |

Nothing in the existing plan is thrown away. Your Phases 1–16 become **Stages 1–2** below. After that, this roadmap replaces the "Intermediate / Advanced" stack in section 21 of the spec with the tools remote employers actually hire for.

---

## 1. The Target Stack, Mapped to This Project

| Skill area | Tools | Where it shows up in TT Finance Index |
| --- | --- | --- |
| Python (professional level) | type hints, `pydantic`, `pytest`, `pandas` | Product models, validation, calculations, tests |
| SQL | PostgreSQL, CTEs, window functions, indexes | Product + historical rate storage; "how have rates changed?" queries |
| Backend | FastAPI | `/products`, `/compare`, `/rank`, `/emergency-fund` endpoints |
| Data collection (ETL) | `httpx`, BeautifulSoup, Playwright, `pdfplumber` | Pulling rates from bank websites and PDF rate sheets |
| Orchestration | GitHub Actions (cron) → Prefect later (optional) | Scheduled weekly data refresh |
| DevOps | Docker, docker-compose, GitHub Actions CI | One-command setup; tests on every push |
| Front end | Streamlit | A simple page non-technical people can use |
| Deployment | Render (or similar) | A live public link for your portfolio |
| AI / LLM | structured outputs, `pgvector`, RAG, evals | Extracting rates from PDFs; Q&A over product terms with citations |

### Deliberately skipped (for now)

- **Airflow**: too heavy for a few dozen institutions. GitHub Actions cron does the job, and Prefect is the lighter upgrade if you want orchestration on your CV.
- **Snowflake / BigQuery**: built for data far larger than this. PostgreSQL is the right tool here, and SQL skills transfer directly.
- **dbt**: optional. Add it only if you target analytics-engineering roles.
- **Pinecone / Qdrant**: `pgvector` keeps vectors in the same Postgres database, so there's one less system to run.

---

## 2. The Build Stages

Each stage has a **Learn** list, a **Build** list, and a **Done when** test. Don't move on until the "Done when" is true.

Time estimates assume **~5–6 hours/week** alongside the Master's. Scale up during semester breaks.

### Stage 0 — Project setup (1 week)

**Learn:** virtual environments (`uv` or `venv`), project layout, `.gitignore`, basic `git` branching.

**Build:**
- [ ] Give the project **its own repository** (`tt-finance-index`). A standalone repo with a README, tests and a live link stands out to recruiters much more than a folder inside `python-applications`.
- [ ] Create the layout from section 18 of the spec (`data/`, `src/`, `tests/`, `docs/`).
- [ ] Add `pyproject.toml` and `pytest`, and make sure `pytest` runs (even with zero tests).

**Done when:** you can clone the repo on a fresh machine, install it, and run `pytest`.

---

### Stage 1 — Define and collect the data (3–4 weeks)

*This is your existing Phases 1–6. Do it manually; it can't be skipped.*

**Learn:** how deposit products work in T&T (savings vs fixed vs term deposits, money-market funds), and what the regulators are (CBTT for banks, Commissioner for Co-operative Development for credit unions, TTSEC for investment products). Check which products **deposit insurance** covers. This matters for the "safety" score.

**Build:**
- [ ] Finish `phase-1-to-do.md` (5 institutions, categories, currencies, field list).
- [ ] Research 15–20 products by hand into a spreadsheet, **with a source URL and date on every row**.
- [ ] Export to `data/institutions.csv` and `data/products.csv`.
- [ ] **New:** write a `pydantic` model (`Product`, `Institution`) and a script that loads the CSVs and reports every invalid row.

**Done when:** `python -m src.validate` loads every row with zero errors, and every product has a source and a `last_verified` date.

> 💡 This hand-checked dataset becomes your **ground truth** later. In Stage 7 you'll measure whether the AI extracts the same rates you found by hand. Keep it accurate.

---

### Stage 2 — Core logic in Python (4–6 weeks)

*This is your existing Phases 7–15, done with professional habits from day one.*

**Learn:** type hints, writing a test before or alongside each function, `pytest` fixtures, then `pandas` for filtering and sorting.

**Build** (each function gets tests):
- [ ] `search_products()`, `filter_products()`
- [ ] `calculate_simple_interest()`, `calculate_compound_interest()`, `calculate_real_return()`
- [ ] `calculate_emergency_fund()`
- [ ] `calculate_score()` and `rank_products()` using the weights in spec section 14
- [ ] A thin CLI menu last (Phase 16)

**Done when:** the CLI ranks real T&T products for a sample emergency fund, and `pytest` passes with tests for every calculation.

---

### Stage 3 — SQL and PostgreSQL (3–4 weeks)

*SQL is the most-tested skill in data engineering interviews, so it comes before the API.*

**Learn:** Postgres basics, `CREATE TABLE`, primary/foreign keys, `JOIN`s, CTEs (`WITH ...`), window functions (`LAG`, `RANK`, `ROW_NUMBER`), indexes and `EXPLAIN`. Also Docker basics, enough to run Postgres with `docker-compose`.

**Build:**
- [ ] `docker-compose.yml` that starts Postgres.
- [ ] Schema: `institutions`, `products`, `rate_history` (one row per product per observed rate), `sources`.
- [ ] A loader that moves validated CSV data into Postgres (this is your first **ETL** step).
- [ ] Rewrite the ranking to read from the database.
- [ ] Write 5 analytical queries and save them in `sql/`, for example:
  - Rate change since last observation per product (`LAG`)
  - Top 3 products per category (`RANK() OVER (PARTITION BY ...)`)
  - Products whose data is older than 60 days (data-freshness check)

**Done when:** `docker-compose up` plus one load command gives you a populated database, and your 5 queries run.

---

### Stage 4 — FastAPI service (2–3 weeks)

**Learn:** FastAPI routing, request/response models with pydantic, dependency injection for the DB session, `httpx` test client.

**Build:**
- [ ] `GET /products` (with filters: currency, type, liquidity)
- [ ] `GET /products/{id}`
- [ ] `POST /emergency-fund` (expenses + months → target, plus ranked products)
- [ ] `GET /compare?ids=1,2,3`
- [ ] API tests in `tests/`
- [ ] GitHub Actions workflow that runs `pytest` on every push (CI)

**Done when:** the auto-generated docs page at `/docs` lets you try every endpoint, and CI is green.

---

### Stage 5 — Automated data collection (4–6 weeks)

*This is where the project becomes a real data pipeline.*

**Learn:** HTTP basics, `httpx`, HTML parsing with BeautifulSoup, Playwright for JavaScript-heavy pages, `pdfplumber` for PDF tables, retries and logging. Also scraping etiquette: check each site's terms and `robots.txt`, keep request rates low, and identify your scraper.

**Build:**
- [ ] One collector **per institution**, starting with the easiest site. Don't try to build a generic scraper.
- [ ] Each collector outputs the **same pydantic `Product` model** from Stage 1, so validation is reused.
- [ ] Change detection: when a scraped rate differs from the database, insert a new `rate_history` row instead of overwriting.
- [ ] A GitHub Actions **scheduled workflow** (weekly) that runs the collectors and loads results.
- [ ] Failure handling: if a site changes layout, the run logs an error and keeps the last good data, marked stale.

**Done when:** the pipeline runs weekly without you, and at least 3 institutions update automatically.

---

### Stage 6 — Front end and deployment (2 weeks)

**Learn:** Streamlit basics, environment variables and secrets, deploying containers.

**Build:**
- [ ] Streamlit app that calls your API: enter expenses and months, see your target and ranked products with **source links and "last verified" dates**.
- [ ] Deploy API + database + Streamlit (Render or similar).
- [ ] A clear on-page note: *"Comparisons based on published information. Not financial advice. Verify with the institution."*

**Done when:** you can send someone a link and they can use it on their phone.

---

### Stage 7 — AI layer (4–6 weeks)

*Two features, each with a real reason to exist. Not a chatbot bolted on.*

**Learn:** LLM APIs, **structured outputs** (forcing the model to return your pydantic schema), embeddings, `pgvector`, chunking, hybrid search (vector + keyword), and **evals**.

**Build:**
- [ ] **AI extraction:** for institutions that only publish PDF rate sheets, use an LLM with structured output to extract products into your `Product` model.
- [ ] **Extraction evals:** compare the AI's output against your hand-collected Stage 1 data. Report accuracy per field (rate, minimum deposit, term). Log cost and latency per document.
- [ ] **RAG Q&A:** index product terms and fee schedules in `pgvector`. Answer questions like *"Which savings accounts charge a fee below a minimum balance?"* with **citations to the source document and page**.
- [ ] **RAG evals:** a set of 20–30 questions with known answers. Measure retrieval recall and answer faithfulness.

**Done when:** your README shows a table of eval results, and the Q&A refuses to answer when the documents don't support an answer.

> This stage covers "Project B" from the career research, inside the same product.

---

### Stage 8 — Portfolio polish (1–2 weeks, plus ongoing)

- [ ] README: problem, demo link, screenshot, architecture diagram, `docker-compose up` quick start, example output.
- [ ] `docs/decisions.md`: short notes on *why* you chose things (Postgres over Snowflake, GitHub Actions over Airflow, your chunking strategy, your scoring weights). Interviewers ask about trade-offs.
- [ ] `docs/methodology.md`: how scores are calculated (already planned in the spec).
- [ ] Add the project to your portfolio site and CV with outcome-style bullets, e.g. *"Built a weekly ETL pipeline tracking N products across N T&T institutions, with validated schema and rate history."*

---

## 3. Rough Timeline

At ~5–6 hours/week:

| Stages | Approx. duration | What you can show afterwards |
| --- | --- | --- |
| 0–2 | ~2–3 months | A tested Python app with real T&T data |
| 3–4 | ~1.5 months | A Dockerized Postgres + FastAPI backend with SQL analytics |
| 5–6 | ~2 months | A live, automatically updating data product |
| 7–8 | ~1.5–2 months | AI extraction and RAG with measured evals |

That's about **7–9 months** in total. Semester breaks will shorten it. **Start applying after Stage 6.** A live, automated pipeline is already a strong data-engineering portfolio piece, and the AI layer can be "in progress" during interviews.

---

## 4. Learning Resources (one per topic, don't collect more)

| Topic | Resource |
| --- | --- |
| Python testing | *pytest* official "Get Started" docs |
| Pydantic | pydantic.dev official docs (Models + Validators) |
| SQL + window functions | *Mode SQL Tutorial* (advanced section), or *PostgreSQL Tutorial* (postgresqltutorial.com) |
| Docker | Docker's official "Get Started" guide |
| FastAPI | The official FastAPI tutorial (fastapi.tiangolo.com) |
| Scraping | *Automate the Boring Stuff*, web scraping chapter, then Playwright for Python docs |
| Data engineering overall | *DataTalksClub Data Engineering Zoomcamp* (free; pick only the modules you need) |
| LLM / RAG / evals | Your LLM provider's docs on structured outputs and embeddings, plus the `pgvector` README |

Rule: learn just enough to finish the current stage, then build. Don't finish a course before starting.

---

## 5. Your First Steps (the next two weeks)

**Week 1**
1. [ ] Create a new GitHub repo, `tt-finance-index`, and copy these four planning docs into its `docs/` folder.
2. [ ] Set up the folder layout, a virtual environment, and `pytest` (Stage 0).
3. [ ] Finish Phase 1 decisions from `phase-1-to-do.md`: write down the 5 institutions, 3 product categories (suggestion: savings, fixed deposits, money-market funds), and TTD + USD only for v1.
4. [ ] Open the CBTT list of licensed institutions (linked in the spec, section 10) and confirm your 5 are on it.

**Week 2**
5. [ ] Collect your first **10 products** into the spreadsheet, with source URLs and dates.
6. [ ] Write `src/models.py` with a pydantic `Product` model.
7. [ ] Write `src/validate.py`, which loads `products.csv` and prints any invalid rows.
8. [ ] Write your first test: one valid product passes, and one with a negative rate fails.
9. [ ] Commit and push. That's your first milestone:

> **"I have real T&T financial data in a validated CSV, and tests prove my validation works."**

---

## 6. Ground Rules

- **Source and date on everything.** An old rate is never shown as current.
- **Comparisons, not advice.** Show the criteria and the reasoning; let users decide.
- **Rank on suitability, not just rate** (spec section 15).
- **Respect websites.** Follow terms of use, rate-limit requests, prefer official published documents.
- **AI never replaces the data or the calculations.** It extracts and explains; the database and the formulas stay the source of truth.
