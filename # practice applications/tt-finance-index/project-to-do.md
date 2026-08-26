Absolutely. And I'd structure it so you **learn Python while building the project**, rather than turning it into a giant research project.

# 🇹🇹 TT Finance Index — To-Do List

Your overall workflow should be:

**Research → Collect → Structure → Store → Validate → Analyze → Compare → Rank**

---

# Phase 1 — Define the Dataset

### 🎯 Goal

Decide exactly **what information you're collecting** before you start researching.

### Tasks

* [ ] Decide which financial institutions to include initially
* [ ] Start with **5 institutions**
* [ ] Decide which product categories to include

  * [ ] Savings accounts
  * [ ] Fixed deposits
  * [ ] Term deposits
  * [ ] Investment accounts
  * [ ] Money market products
  * [ ] Other low-risk products
* [ ] Decide which currencies you'll support

  * [ ] TTD
  * [ ] USD
  * [ ] CAD
  * [ ] GBP
  * [ ] EUR

### Don't do yet

* ❌ APIs
* ❌ Web scraping
* ❌ Pandas
* ❌ SQLite
* ❌ Streamlit
* ❌ AI

Your project specification already calls for manual collection first.

---

# Phase 2 — Build Your Institution List

### 🎯 Goal

Create your initial `institutions.csv`.

### Tasks

* [ ] Find the official list of licensed financial institutions from the Central Bank
* [ ] Choose your first 5 institutions
* [ ] Visit each institution's official website
* [ ] Record:

```text
institution_id
name
type
regulator
website
country
deposit_insured
last_verified
source_url
```

### Example

```text
1
First Citizens
Commercial Bank
Central Bank of Trinidad and Tobago
https://...
Trinidad and Tobago
True
2026-08-26
https://...
```

### Deliverable

```text
data/
└── institutions.csv
```

---

# Phase 3 — Research Financial Products

### 🎯 Goal

Find the actual products offered by each institution.

For **each institution**:

* [ ] Find savings products
* [ ] Find fixed deposits
* [ ] Find term deposits
* [ ] Find other relevant low-risk products
* [ ] Open the product page
* [ ] Read the product details
* [ ] Find the rate information
* [ ] Find the minimum deposit
* [ ] Find withdrawal restrictions
* [ ] Find fees
* [ ] Find terms/lock-in periods

Don't just copy the product name.

You're trying to answer:

> **"If I put $60,000 into this product, what would actually happen?"**

---

# Phase 4 — Create Your Research Spreadsheet

Before writing Python, I'd actually use a spreadsheet.

Create:

```text
tt_finance_research.xlsx
```

Have columns like:

| Institution | Product | Type | Currency | Rate | Rate Type | Minimum | Term | Liquidity | Fees | Restrictions | Source | Date |
| ----------- | ------- | ---- | -------- | ---: | --------- | ------: | ---: | --------- | ---- | ------------ | ------ | ---- |

### Tasks

* [ ] Enter every product you find
* [ ] Record the exact rate
* [ ] Record the rate type
* [ ] Record minimum deposit
* [ ] Record term
* [ ] Record liquidity
* [ ] Record fees
* [ ] Record restrictions
* [ ] Record source URL
* [ ] Record date researched

**Do not skip the source column.**

That's going to become one of the most important parts of your application.

---

# Phase 5 — Verify the Data

Financial information changes.

So before putting something into your actual dataset:

* [ ] Confirm the source is official
* [ ] Check whether the rate has an effective date
* [ ] Check whether the rate is current
* [ ] Check whether the rate applies to your particular balance
* [ ] Check whether there are conditions attached
* [ ] Check whether the product is still offered
* [ ] Record `last_verified`

You want to avoid:

```text
Bank A → 4.5%
```

and instead have:

```text
Bank A
Product: XYZ Savings
Rate: 4.5%
Rate Type: Variable
Source: official product page
Verified: 2026-08-26
```

---

# Phase 6 — Create Your CSV Files

Once your research spreadsheet is reasonably complete:

### Create

```text
data/
│
├── institutions.csv
├── products.csv
└── historical_rates.csv
```

Initially, you can leave `historical_rates.csv` empty.

### Tasks

* [ ] Create `institutions.csv`
* [ ] Create `products.csv`
* [ ] Create headers
* [ ] Enter your researched data
* [ ] Make sure IDs are consistent
* [ ] Make sure every product has an institution ID
* [ ] Make sure every product has a source
* [ ] Make sure dates are consistent

---

# Phase 7 — Learn to Read the CSV With Python

Now you start programming.

Build a small program that can:

* [ ] Open `products.csv`
* [ ] Read the data
* [ ] Print every product
* [ ] Print product names
* [ ] Print institution names
* [ ] Print interest rates

At first, don't worry about fancy architecture.

Something like:

```text
Load CSV
     ↓
Read rows
     ↓
Loop through rows
     ↓
Print information
```

---

# Phase 8 — Build Product Search

Now make the dataset useful.

Create:

```python
search_products()
```

The user should be able to do something like:

```text
Search: savings
```

and get:

```text
Product              Institution       Rate
------------------------------------------------
Savings Account      Bank A             3.5%
Premium Savings      Bank B             4.0%
Easy Saver           Bank C             3.75%
```

### Tasks

* [ ] Search by product name
* [ ] Search by institution
* [ ] Search by product type
* [ ] Search by currency

---

# Phase 9 — Build Product Filtering

Create:

```python
filter_products()
```

Allow the user to ask:

```text
Show TTD products
```

or:

```text
Show products above 3%
```

or:

```text
Show products with high liquidity
```

Practice:

* [ ] `if`
* [ ] `for`
* [ ] lists
* [ ] dictionaries
* [ ] functions
* [ ] comparisons

This is where your CS50 Python skills start becoming practical.

---

# Phase 10 — Build Financial Calculations

Create:

```python
calculate_simple_interest()
```

Then:

```python
calculate_compound_interest()
```

Then:

```python
calculate_interest_earned()
```

For example:

```text
Initial Investment: $60,000
Interest Rate: 4%
Term: 1 year

Interest Earned: $2,400
Final Balance: $62,400
```

### Tasks

* [ ] Simple interest
* [ ] Compound interest
* [ ] Interest earned
* [ ] Final balance
* [ ] Different time periods
* [ ] Different interest rates

---

# Phase 11 — Build the Emergency Fund Calculator

Now connect it to your original purpose.

Create:

```python
calculate_emergency_fund()
```

User enters:

```text
Monthly expenses: $5,000
Months required: 12
```

Program calculates:

```text
Emergency Fund Target
= $5,000 × 12

= $60,000
```

Then:

* [ ] Current emergency fund
* [ ] Target emergency fund
* [ ] Amount still needed
* [ ] Months currently covered

---

# Phase 12 — Compare Products

Create:

```python
compare_products()
```

Allow the user to select two or more products.

Example:

```text
                    Product A       Product B
------------------------------------------------
Interest Rate          3.50%           4.00%
Minimum Deposit        $500            $5,000
Liquidity              High            Medium
Term                   None            12 months
Risk                   Low             Low
```

This is where your data model becomes genuinely useful.

---

# Phase 13 — Build the Scoring System

Now implement the scoring system already defined in your project.

Your specification proposes:

```text
Liquidity          30%
Interest Rate      25%
Safety/Risk        25%
Historical Return  10%
Minimum Deposit     5%
Fees/Penalties      5%
```

### Tasks

* [ ] Create `calculate_score()`
* [ ] Score liquidity
* [ ] Score interest rate
* [ ] Score risk
* [ ] Score minimum deposit
* [ ] Score fees
* [ ] Combine scores
* [ ] Produce final score

---

# Phase 14 — Rank the Products

Create:

```python
rank_products()
```

Output:

```text
TT FINANCE INDEX
Emergency Fund Ranking

Rank  Product              Institution      Score
---------------------------------------------------
1     Product A            Bank A            91.4
2     Product B            Bank B            88.7
3     Product C            Credit Union A    86.2
```

### Important

Don't rank purely by interest rate.

Your project is supposed to answer:

> **What is the best product for an emergency fund?**

not:

> **What product has the highest interest rate?**

Those are different questions.

---

# Phase 15 — Add Exception Handling

Now deliberately break your program.

Try:

```text
Interest rate: abc
Minimum deposit: hello
Months: twelve
Product: doesn't exist
```

Make sure your program doesn't crash.

Practice:

```python
try:
except
else
finally
```

### Tasks

* [ ] Invalid numbers
* [ ] Missing products
* [ ] Invalid menu choices
* [ ] Empty input
* [ ] Invalid CSV values

---

# Phase 16 — Build the CLI

Now bring everything together.

```text
========================================
          TT FINANCE INDEX
========================================

1. View institutions
2. View products
3. Search products
4. Filter products
5. Compare products
6. Calculate emergency fund
7. Calculate projected returns
8. Rank products
9. Add product
10. Exit
```

Build the menu **last**, not first.

That's important.

The menu is just the interface. The real work is the functions underneath it.

---

# Phase 17 — Testing

Create tests for:

* [ ] Simple interest
* [ ] Compound interest
* [ ] Emergency fund calculation
* [ ] Product filtering
* [ ] Product ranking
* [ ] Invalid input
* [ ] Missing data
* [ ] CSV loading

Example:

```text
$60,000 at 4% for 1 year
Expected: $2,400 interest
```

---

# Phase 18 — GitHub Cleanup

Once the project works:

```text
tt-finance-index/
│
├── README.md
├── data/
│   ├── institutions.csv
│   ├── products.csv
│   └── historical_rates.csv
│
├── src/
│   ├── main.py
│   ├── products.py
│   ├── calculations.py
│   ├── ranking.py
│   └── validation.py
│
└── tests/
```

### README should explain:

* [ ] What the project does
* [ ] Why you built it
* [ ] Data sources
* [ ] How the data is collected
* [ ] How to run it
* [ ] Example output
* [ ] What you learned
* [ ] Future improvements

---

# 🚀 Phase 19 — Only Then Automate

This is where your **API/HTTP learning** comes back into the project.

Once the manual version works:

```text
MANUAL
   ↓
CSV
   ↓
PYTHON
   ↓
ANALYSIS
```

you can eventually move toward:

```text
Financial Institution
        ↓
Website / API
        ↓
HTTP Request
        ↓
Python requests
        ↓
JSON / HTML
        ↓
Data extraction
        ↓
Validation
        ↓
Database
        ↓
TT Finance Index
```

Then you can investigate:

* [ ] Does the institution have an API?
* [ ] Does it publish machine-readable data?
* [ ] Can `requests` retrieve the information?
* [ ] Is the information JSON?
* [ ] If not, can the page be parsed?
* [ ] How frequently should data be updated?
* [ ] How do we detect changed rates?
* [ ] How do we preserve historical rates?

---

# Your Immediate Next Steps

Don't look at all 19 phases and think you have to do everything now.

**This week, I'd only do these:**

### 1. Research

* [ ] Pick 5 institutions
* [ ] Find their official websites
* [ ] Find their savings/fixed-deposit/term-deposit products

### 2. Collect

* [ ] Create your research spreadsheet
* [ ] Collect 10–20 products
* [ ] Record the source for every product

### 3. Structure

* [ ] Design `institutions.csv`
* [ ] Design `products.csv`

### 4. Python

* [ ] Write a program that reads `products.csv`
* [ ] Print the products
* [ ] Search products

**Stop there.**

That gives you a very manageable first milestone:

> **"I have real Trinidad & Tobago financial data in a CSV, and I can use Python to read and search it."**

Once you accomplish that, we'll have a very natural next step instead of you trying to build the entire Finance Index at once.