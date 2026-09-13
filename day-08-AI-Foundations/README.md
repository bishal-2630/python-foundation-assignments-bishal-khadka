# Assignment 5 — Banking ETL Pipeline

```sql
CREATE TABLE IF NOT EXISTS loans (
    loan_id       SERIAL PRIMARY KEY,
    customer_id   INTEGER REFERENCES customers(customer_id),
    principal     NUMERIC(12, 2) NOT NULL,
    interest_rate NUMERIC(5, 2) NOT NULL,
    status        TEXT NOT NULL CHECK (status IN ('active','paid_off','defaulted')),
    start_date    DATE NOT NULL DEFAULT CURRENT_DATE
);
```

**New columns on `account_summary`:**

- `total_loan_exposure NUMERIC` — sum of `principal` across a customer's `active` loans only.
- `active_loan_count INTEGER` — count of a customer's `active` loans only.

Both are added via `ALTER TABLE ... ADD COLUMN IF NOT EXISTS`, since `account_summary` already existed before this assignment and `CREATE TABLE IF NOT EXISTS` alone won't modify an existing table.

**Business rule change:** `categorize()` now takes a `has_defaulted_loan` flag. If a customer has even one loan with status `defaulted`, their category is forced to `"At Risk"`, overriding the normal transaction-total thresholds (Premium ≥ 20,000 / Standard ≥ 5,000 / else Basic).

## Task Summary

1.  Extend the Schema loans table, 2 new account_summary columns, seeded with 6 sample loans across 3 customers
2.  Harden the Connection with_retry decorator
3.  Extend the Transform Step transform_loans() and updated categorize()
4.  Load & Verify load_summary() upsert extended with the 2 new columns; verify() now reports a full reconciliation table including loan data
5.  Unit Tests test_transform.py — 16 tests covering category boundaries, the defaulted-loan override, zero-loan input, and the high-value flag

## Project Files

```
etl_assignment.ipynb   Main pipeline notebook (run top to bottom)
test_transform.py      Standalone unit tests for the pure transform logic
etl.log                Log output from running the pipeline (includes a deliberate Task 2 failure/retry demonstration)
.env                   required credentials
README.md              This file
```

## Setup

1. Install dependencies:
   ```
   pip install psycopg2-binary python-dotenv pytest
   ```
2. Create a .env file in this same folder

3. Make sure PostgreSQL is running locally and a database named db_bank exists

## How to Run

Run `etl_assignment.ipynb` top to bottom, in order

## Running the Tests

From a terminal, in this same folder:

```
pytest test_transform.py -v
```
