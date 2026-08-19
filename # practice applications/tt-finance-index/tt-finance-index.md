# FinAtlas TT — Project Specification Sheet

## Table of Contents

- [FinAtlas TT — Project Specification Sheet](#finatlas-tt--project-specification-sheet)
  - [Table of Contents](#table-of-contents)
- [1. Project Overview](#1-project-overview)
- [2. Project Goal](#2-project-goal)
- [3. Problem Statement](#3-problem-statement)
- [4. Core Objectives](#4-core-objectives)
- [5. Initial Scope](#5-initial-scope)
  - [Version 1](#version-1)
- [6. Future Scope](#6-future-scope)
- [7. Data Model](#7-data-model)
- [8. Institution Data](#8-institution-data)
- [9. Financial Product Data](#9-financial-product-data)
- [10. Data Collection](#10-data-collection)
  - [Initial Method](#initial-method)
  - [Important Rule](#important-rule)
- [11. Data Validation](#11-data-validation)
    - [Interest rate](#interest-rate)
    - [Minimum deposit](#minimum-deposit)
    - [Currency](#currency)
    - [Liquidity](#liquidity)
    - [Risk](#risk)
    - [Product type](#product-type)
- [12. Financial Calculations](#12-financial-calculations)
  - [Simple Interest](#simple-interest)
  - [Compound Interest](#compound-interest)
  - [Interest Earned](#interest-earned)
  - [Real Return](#real-return)
- [13. Emergency Fund Analysis](#13-emergency-fund-analysis)
- [14. Product Scoring](#14-product-scoring)
- [15. Ranking System](#15-ranking-system)
- [16. Core Python Features](#16-core-python-features)
  - [Fundamentals](#fundamentals)
  - [Data Structures](#data-structures)
  - [Control Flow](#control-flow)
  - [Functions](#functions)
  - [Exception Handling](#exception-handling)
- [17. Application Features](#17-application-features)
  - [Main Menu](#main-menu)
- [18. Project Architecture](#18-project-architecture)
- [19. Development Phases](#19-development-phases)
  - [Phase 1 — Python Prototype](#phase-1--python-prototype)
  - [Phase 2 — CSV Data](#phase-2--csv-data)
  - [Phase 3 — Emergency Fund Calculator](#phase-3--emergency-fund-calculator)
  - [Phase 4 — Product Ranking](#phase-4--product-ranking)
  - [Phase 5 — Historical Data](#phase-5--historical-data)
  - [Phase 6 — Pandas](#phase-6--pandas)
  - [Phase 7 — Visualization](#phase-7--visualization)
  - [Phase 8 — Database](#phase-8--database)
  - [Phase 9 — Automated Data Collection](#phase-9--automated-data-collection)
  - [Phase 10 — Streamlit Application](#phase-10--streamlit-application)
- [20. Testing](#20-testing)
  - [Calculations](#calculations)
  - [Input Validation](#input-validation)
  - [Edge Cases](#edge-cases)
- [21. Future Technology Stack](#21-future-technology-stack)
  - [Current](#current)
  - [Intermediate](#intermediate)
  - [Advanced](#advanced)
  - [Possible AI Layer](#possible-ai-layer)
- [22. Example User Flow](#22-example-user-flow)
- [23. Success Criteria](#23-success-criteria)
- [24. Potential Future Features](#24-potential-future-features)
  - [Personal Financial Profile](#personal-financial-profile)
  - [Goal Planning](#goal-planning)
  - [Portfolio Analysis](#portfolio-analysis)
  - [Automated Rate Monitoring](#automated-rate-monitoring)
  - [Historical Rate Database](#historical-rate-database)
  - [Emergency Fund Recommendation Engine](#emergency-fund-recommendation-engine)
- [Final Project Vision](#final-project-vision)
- [Development Principle](#development-principle)

---

# 1. Project Overview

**Project Name:** FinAtlas TT

**Project Type:** Financial data analysis and comparison application

**Primary Language:** Python

**Primary Country:** Trinidad & Tobago

**Initial Application Type:** Command-line application

**Future Application Type:** Streamlit web application

---

# 2. Project Goal

Build a Python application that collects, organizes, analyzes, compares, and ranks financial products available in Trinidad & Tobago.

The initial focus will be on identifying suitable financial instruments for building an emergency fund.

The application should eventually answer questions such as:

* What financial institutions operate in Trinidad & Tobago?
* What savings and investment products do they offer?
* What interest rates are available?
* What is the minimum deposit?
* How liquid is the product?
* What are the withdrawal restrictions?
* What is the investment term?
* How much interest could my emergency fund earn?
* Which products are most suitable for an emergency fund?
* Which products provide the best balance between return, safety, and liquidity?
* How have rates changed historically?

---

# 3. Problem Statement

Financial-product information in Trinidad & Tobago is spread across many different institutions and sources.

A person researching where to place an emergency fund may need to manually compare:

* Commercial banks
* Credit unions
* Finance companies
* Investment institutions
* Fixed deposits
* Savings accounts
* Investment accounts
* Term deposits
* Other low-risk financial products

FinAtlas TT will centralize this information into a structured dataset and provide analytical tools for comparing the products.

---

# 4. Core Objectives

The application should:

1. Create a centralized database of financial institutions.
2. Create a centralized database of financial products.
3. Record interest rates and historical rates.
4. Record minimum deposits and investment requirements.
5. Record liquidity characteristics.
6. Record terms and lock-in periods.
7. Record withdrawal restrictions and penalties.
8. Calculate projected returns.
9. Compare financial products.
10. Rank products according to user-defined criteria.
11. Analyze emergency-fund suitability.
12. Record the source and verification date for financial information.

---

# 5. Initial Scope

## Version 1

The first version should focus on:

* Manual data entry
* CSV data storage
* Python dictionaries and lists
* Functions
* Loops
* Conditionals
* Exception handling
* Basic calculations
* Sorting
* Filtering
* Product comparison
* Emergency-fund ranking

Do **not** start with:

* APIs
* Web scraping
* Machine learning
* AI recommendations
* Databases
* Complex web applications

Those will be introduced later.

---

# 6. Future Scope

Potential future versions may include:

```text
Version 1
Python CLI
    ↓
Version 2
CSV + automated calculations
    ↓
Version 3
Pandas data analysis
    ↓
Version 4
SQLite/PostgreSQL database
    ↓
Version 5
Automated data collection
    ↓
Version 6
Web/API integrations
    ↓
Version 7
Streamlit dashboard
    ↓
Version 8
Personal financial analysis
    ↓
Version 9
AI-assisted financial research
```

---

# 7. Data Model

The application should eventually contain the following major entities:

```text
Institution
    ↓
Financial Product
    ↓
Interest Rate
    ↓
Historical Rate
    ↓
Fees
    ↓
Restrictions
    ↓
Suitability Score
```

Potential data entities:

* Institutions
* Products
* Rates
* Historical Rates
* Fees
* Requirements
* Liquidity
* Risk
* Sources

---

# 8. Institution Data

Each institution should contain information such as:

```text
Institution ID
Institution Name
Institution Type
Regulator
Website
Country
Currency
Deposit Insurance Status
Active Status
Last Verified
Source
```

Example:

```python
institution = {
    "id": 1,
    "name": "Example Bank",
    "type": "Commercial Bank",
    "regulator": "Central Bank of Trinidad and Tobago",
    "country": "Trinidad and Tobago",
    "deposit_insured": True,
    "website": "https://example.com",
    "last_verified": "2026-08-18"
}
```

---

# 9. Financial Product Data

Each product should contain:

```text
Product ID
Institution ID
Product Name
Product Type
Currency
Interest Rate
Rate Type
Minimum Deposit
Maximum Deposit
Term
Liquidity
Risk Level
Withdrawal Restrictions
Early Withdrawal Penalty
Fees
Eligibility
Historical Return
Last Verified
Source
Notes
```

Example:

```python
product = {
    "id": 1,
    "institution_id": 1,
    "name": "Example Savings Account",
    "type": "Savings Account",
    "currency": "TTD",
    "interest_rate": 3.5,
    "rate_type": "Variable",
    "minimum_deposit": 500,
    "term_months": 0,
    "liquidity": "High",
    "risk_level": "Low",
    "early_withdrawal_penalty": 0,
    "last_verified": "2026-08-18"
}
```

---

# 10. Data Collection

## Initial Method

Financial-product information will initially be entered manually into CSV files.

Potential sources include:

* Financial institution websites
* Product brochures
* Rate sheets
* Annual reports
* Financial statements
* Regulatory publications
* Publicly available documents
* Official announcements

Every record should include:

```text
Source
Source URL
Date Collected
Date Verified
```

## Important Rule

The application should never treat an old rate as a current rate without indicating when the information was collected.

---

# 11. Data Validation

The program should validate incoming information.

Examples:

### Interest rate

```text
Must be numeric
Must not be negative
```

### Minimum deposit

```text
Must be numeric
Must not be negative
```

### Currency

Allowed examples:

```text
TTD
USD
CAD
GBP
EUR
```

### Liquidity

Possible values:

```text
High
Medium
Low
```

### Risk

Possible values:

```text
Very Low
Low
Medium
High
Very High
```

### Product type

Possible values:

```text
Savings Account
Fixed Deposit
Term Deposit
Investment Account
Credit Union Account
Bond
Mutual Fund
Money Market Fund
Other
```

Invalid data should generate useful error messages.

---

# 12. Financial Calculations

The application should eventually support:

## Simple Interest

```text
Interest = Principal × Rate × Time
```

## Compound Interest

```text
A = P(1 + r/n)^(nt)
```

Where:

```text
P = Principal
r = Annual interest rate
n = Number of compounding periods
t = Number of years
A = Final amount
```

## Interest Earned

```text
Interest Earned = Final Balance - Initial Principal
```

## Real Return

The application should eventually account for inflation.

Basic approximation:

```text
Real Return ≈ Interest Rate - Inflation Rate
```

A more precise calculation can be added later.

---

# 13. Emergency Fund Analysis

The application should allow the user to enter:

```text
Monthly Expenses
Desired Number of Months
Current Emergency Fund
Target Emergency Fund
```

Example:

```text
Monthly expenses: $5,000 TTD
Target coverage: 12 months
```

Calculation:

```text
Emergency Fund Target
= Monthly Expenses × Months of Coverage
```

Example:

```text
$5,000 × 12
= $60,000 TTD
```

The application should then determine:

```text
Current Emergency Fund
Target Emergency Fund
Amount Remaining
Months Covered
```

---

# 14. Product Scoring

Each product should receive an emergency-fund suitability score.

Initial proposed weighting:

| Factor            | Weight |
| ----------------- | -----: |
| Liquidity         |    30% |
| Interest Rate     |    25% |
| Safety/Risk       |    25% |
| Historical Return |    10% |
| Minimum Deposit   |     5% |
| Fees/Penalties    |     5% |

Total:

```text
100%
```

The weighting system should eventually be customizable.

For example, a user may decide:

```text
Liquidity = 40%
Safety = 30%
Interest = 20%
Fees = 10%
```

---

# 15. Ranking System

Products should be ranked based on the calculated suitability score.

Example:

```text
Rank | Product | Institution | Rate | Score
------------------------------------------------
1    | Product A | Bank A     | 4.50% | 91.4
2    | Product B | Bank B     | 4.25% | 88.7
3    | Product C | CU A       | 5.00% | 86.2
4    | Product D | Bank C     | 4.00% | 82.9
```

The ranking should not be based solely on interest rate.

A product with a higher return may rank lower if:

* It has poor liquidity.
* It has a long lock-in period.
* It has high withdrawal penalties.
* It carries greater risk.
* It has a high minimum deposit.

---

# 16. Core Python Features

The first version should intentionally practice the following Python concepts:

## Fundamentals

* Variables
* Data types
* Strings
* Integers
* Floats
* Booleans

## Data Structures

* Lists
* Dictionaries
* Nested dictionaries
* Lists of dictionaries

## Control Flow

* `if`
* `elif`
* `else`
* `for`
* `while`

## Functions

Examples:

```python
calculate_simple_interest()
calculate_compound_interest()
calculate_emergency_fund()
calculate_real_return()
calculate_score()
rank_products()
filter_products()
compare_products()
```

## Exception Handling

Use:

```python
try
except
else
finally
```

to handle invalid user input.

---

# 17. Application Features

## Main Menu

The CLI application could eventually contain:

```text
========================================
          FINATLAS TT
========================================

1. View institutions
2. View financial products
3. Search products
4. Filter products
5. Compare products
6. Calculate emergency fund
7. Calculate projected returns
8. Rank emergency-fund products
9. View historical rates
10. Add financial product
11. Update financial product
12. Exit

Select an option:
```

---

# 18. Project Architecture

Initial structure:

```text
finatlas-tt/
│
├── README.md
│
├── data/
│   ├── institutions.csv
│   ├── products.csv
│   └── historical_rates.csv
│
├── src/
│   ├── main.py
│   ├── calculations.py
│   ├── products.py
│   ├── institutions.py
│   ├── ranking.py
│   ├── validation.py
│   └── emergency_fund.py
│
├── tests/
│   ├── test_calculations.py
│   ├── test_products.py
│   └── test_validation.py
│
└── docs/
    └── methodology.md
```

The initial version does not need all these files immediately.

Start small and split the program into modules as it grows.

---

# 19. Development Phases

## Phase 1 — Python Prototype

Goal:

Build a working command-line program.

Features:

* Store products in lists/dictionaries
* Display products
* Search products
* Filter products
* Calculate interest
* Compare products

---

## Phase 2 — CSV Data

Add:

```text
CSV reading
CSV writing
Data validation
```

The application should no longer require all products to be hard-coded.

---

## Phase 3 — Emergency Fund Calculator

Allow the user to enter:

```text
Monthly expenses
Desired months of coverage
Current savings
```

Calculate:

```text
Target emergency fund
Current coverage
Remaining amount
```

---

## Phase 4 — Product Ranking

Implement:

```text
Liquidity score
Risk score
Interest score
Fee score
Minimum deposit score
Historical return score
```

Calculate an overall suitability score.

---

## Phase 5 — Historical Data

Add:

```text
Institution
Product
Date
Interest Rate
Source
```

Allow the application to analyze rate changes over time.

---

## Phase 6 — Pandas

Introduce:

```python
import pandas as pd
```

Use Pandas for:

* Data cleaning
* Filtering
* Sorting
* Grouping
* Aggregation
* Statistical analysis
* Missing-value handling

---

## Phase 7 — Visualization

Create visualizations for:

* Interest-rate comparisons
* Historical rate changes
* Projected emergency-fund growth
* Product rankings
* Liquidity vs return
* Risk vs return

---

## Phase 8 — Database

Move from CSV to:

```text
SQLite
```

Later potentially:

```text
PostgreSQL
```

---

## Phase 9 — Automated Data Collection

Investigate:

* APIs
* Web scraping
* Public datasets
* PDF extraction
* Excel downloads
* Official rate sheets

The system should record:

```text
Source
Date collected
Date verified
```

---

## Phase 10 — Streamlit Application

Create a web interface with:

```text
Dashboard
Institutions
Products
Comparison
Emergency Fund Calculator
Historical Rates
Rankings
Charts
```

---

# 20. Testing

The application should test:

## Calculations

Test:

```text
Simple interest
Compound interest
Real return
Emergency fund target
Product score
```

## Input Validation

Test:

```text
Negative values
Invalid interest rates
Invalid product types
Missing data
Invalid menu selections
Invalid numbers
```

## Edge Cases

Examples:

```text
0% interest
0 deposit
0 months
Very large deposit
Missing historical data
No available products
Multiple products with identical scores
```

---

# 21. Future Technology Stack

## Current

```text
Python
CSV
VS Code
Git
GitHub
```

## Intermediate

```text
Python
Pandas
NumPy
Matplotlib
SQLite
```

## Advanced

```text
Streamlit
PostgreSQL
REST API
Web scraping
Automated data pipelines
```

## Possible AI Layer

Eventually:

```text
LLM
    ↓
Financial product database
    ↓
User requirements
    ↓
Explainable recommendations
```

AI should not replace the underlying calculations or source data.

---

# 22. Example User Flow

```text
START
  ↓
Enter monthly expenses
  ↓
Enter desired emergency-fund coverage
  ↓
Calculate emergency-fund target
  ↓
Load financial products
  ↓
Filter for TTD products
  ↓
Filter for suitable liquidity
  ↓
Filter based on risk
  ↓
Calculate projected returns
  ↓
Calculate suitability scores
  ↓
Rank products
  ↓
Display results
  ↓
Compare selected products
  ↓
END
```

---

# 23. Success Criteria

The first working version is successful when the program can:

* [ ] Load financial products.
* [ ] Display financial products.
* [ ] Search financial products.
* [ ] Filter financial products.
* [ ] Validate user input.
* [ ] Calculate simple interest.
* [ ] Calculate compound interest.
* [ ] Calculate emergency-fund requirements.
* [ ] Compare products.
* [ ] Score products.
* [ ] Rank products.
* [ ] Display the top emergency-fund options.
* [ ] Show the source of financial information.
* [ ] Show when information was last verified.

---

# 24. Potential Future Features

## Personal Financial Profile

Allow users to enter:

```text
Monthly income
Monthly expenses
Current savings
Debt
Emergency fund
Risk tolerance
Investment horizon
```

---

## Goal Planning

Examples:

```text
Emergency Fund
Down Payment
Vacation
Retirement
Education
Investment Goal
```

---

## Portfolio Analysis

Eventually allow:

```text
Savings
Fixed Deposits
Bonds
Mutual Funds
ETFs
USD Investments
```

to be analyzed together.

---

## Automated Rate Monitoring

The system could eventually detect:

```text
Rate increased
Rate decreased
New product
Product discontinued
Minimum deposit changed
Term changed
Fee changed
```

---

## Historical Rate Database

Store:

```text
Product
Institution
Date
Rate
Previous Rate
Change
Source
```

Then answer:

> "Which institutions have consistently offered competitive rates?"

---

## Emergency Fund Recommendation Engine

The final system could take:

```text
Emergency Fund Target: $60,000
Monthly Expenses: $5,000
Required Liquidity: High
Risk Tolerance: Low
Time Horizon: Immediate
```

and return:

```text
Recommended Allocation

High-liquidity savings      $20,000
Short-term deposit          $20,000
Other low-risk instrument   $20,000
```

The recommendation should always explain **why** a product was selected rather than simply producing a ranking.

---

# Final Project Vision

FinAtlas TT should ultimately become:

> **A data-driven financial-product research and comparison platform for Trinidad & Tobago.**

The long-term system should answer:

```text
"What financial products are available?"

"What do they pay?"

"How safe are they?"

"How liquid are they?"

"How have their rates changed?"

"What would my money earn?"

"Which products fit my goals?"

"Why is this product ranked above the others?"
```

The project should prioritize:

**Accurate data → Transparent calculations → Useful analysis → Explainable recommendations**

rather than simply producing a "best investment" number.

---

# Development Principle

Build the simplest working version first.

Do not start by trying to automate everything.

Start with:

```text
Python
    ↓
A few products
    ↓
Calculations
    ↓
Comparison
    ↓
Ranking
```

Then progressively introduce:

```text
CSV
    ↓
Pandas
    ↓
Historical Data
    ↓
Database
    ↓
Automation
    ↓
Streamlit
    ↓
API
    ↓
Advanced Analytics
```

The goal is to build the project **while learning the technology**, not to learn every technology before starting the project.
