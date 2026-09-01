# TT Finance Index — Phase 1 Plan

**Project:** [TT Finance Index](https://github.com/linciasw/python-applications/tree/main/%23%20practice%20applications/tt-finance-index)

Related files in the repo:
- `project-to-do.md`
- `tt-finance-index.md`

## Project Summary

TT Finance Index is a project to compare Trinidad & Tobago financial products — savings accounts, fixed deposits, term deposits, money-market products, etc. — across institutions.

Constraints (explicitly decided): **no APIs, scraping, Pandas, SQLite, Streamlit, or AI yet.**

Current Phase 1 (from `project-to-do.md`):
- Decide which financial institutions to include initially
- Start with 5 institutions
- Decide which product categories to include
- Decide which currencies you'll support

## Step-by-Step Breakdown of Phase 1

### Step 1 — Choose the initial 5 institutions
Don't start researching products yet. Create a simple list of 5 institutions you want the first version to cover.

### Step 2 — Define what counts as a financial institution
For example:
- Commercial banks
- Credit unions
- Investment institutions
- Other deposit-taking institutions

Make this explicit so you don't randomly add things later.

### Step 3 — Define your initial product categories
Current proposal:
- Savings accounts
- Fixed deposits
- Term deposits
- Investment accounts
- Money market products
- Other low-risk products

Recommendation: keep the first version narrower rather than trying to cover everything.

### Step 4 — Define supported currencies
Current plan:
- TTD
- USD
- CAD
- GBP
- EUR

Distinguish between:
- "The institution supports this currency"
- "The particular financial product is available in this currency"

This distinction will matter later.

### Step 5 — Define the minimum dataset
Before researching anything, decide exactly what information every product must eventually have. Example fields:
- institution
- product
- product_type
- currency
- interest_rate
- rate_type
- minimum_deposit
- term
- liquidity
- fees
- restrictions
- source
- last_verified

### Step 6 — Write the Phase 1 specification
Turn the loose to-do list into the project's rules.

### Step 7 — Create the Phase 1 GitHub issue/checklist
Work through it like a real open-source project:

```
Phase 1
│
├── Define institutions
├── Define product categories
├── Define currencies
├── Define dataset fields
├── Define inclusion/exclusion rules
└── Complete specification
```

Only move to Phase 2 once all Phase 1 items are checked off.


