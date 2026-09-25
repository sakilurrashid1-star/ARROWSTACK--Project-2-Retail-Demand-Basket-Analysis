# Validation Report

## Dataset QA
- Rows: **3,000**
- Duplicate transaction IDs: **0**
- Missing cells: **0**
- Basket sizes: **2–8**
- Average basket size: **3.843**
- Deterministic seed: **20260925**

## Analysis QA
- Parsed item count matches `basket_size` for every row.
- Customer segment values are restricted to Value, Regular and Premium.
- Transaction-item matrix preserves one row per transaction.
- Association metrics use the same transaction universe for support, confidence and lift.
- Notebook ends with explicit assertion-based QA checks.

**Status: PASS**
