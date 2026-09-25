# Validation Report

## Dataset QA
- Expected rows: **3,000**
- Duplicate transaction IDs: **0**
- Missing cells: **0**
- Minimum basket size: **2**
- Maximum basket size: **8**
- Average basket size: **3.843**
- Deterministic generation seed: **20260925**

## Analysis validation
The analysis checks that:
1. every transaction has at least two parsed products;
2. basket_size equals the parsed item count;
3. the one-hot matrix contains one row per transaction;
4. frequent-itemset support is computed as transaction coverage;
5. association confidence and lift are calculated from the same transaction universe.

## Review status
**PASS —** the committed synthetic dataset satisfies the defined schema and quality constraints. The notebook contains executable checks before analysis.
