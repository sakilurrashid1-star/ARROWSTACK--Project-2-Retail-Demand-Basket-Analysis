# Arrowstack Project 2 — Retail Demand & Basket Analysis

**Intern:** Alkamah Sakilur Rashid  
**Track:** Data Science — Technical Track • Intermediate  
**Project:** Retail Demand & Basket Analysis  
**Data:** Deterministic synthetic retail transactions (no customer PII)

## Executive summary
This project analyzes historical-style retail transactions to identify demand patterns and product associations that a merchandising stakeholder can evaluate for bundle, placement, or cross-sell experiments.

## Evidence snapshot
- Transactions: **3,000**
- Products: **15**
- Average basket size: **3.843 items**
- Basket size range: **2–8 items**
- Highest transaction coverage: **Milk (58.2%)**
- Highest-lift observed pair: **Cereal + Yogurt (lift 2.754, support 8.3%)**

## Stakeholder & success criteria
**Primary stakeholder:** retail merchandising / category manager.  
**Decision enabled:** identify product combinations worth testing in bundles, adjacent placement, or targeted cross-sell.  
**Success criteria:** clean transaction input; traceable basket transformation; interpretable demand and association metrics; validation evidence; documented limitations.

## Workflow
1. Validate schema, identifiers, dates, segments and basket sizes.
2. Parse basket contents into a transaction-item matrix.
3. Measure product coverage and basket-size distribution.
4. Mine frequent itemsets and association rules.
5. Compare support, confidence and lift.
6. Convert evidence into testable business actions.
7. Document limitations and next steps.

## Repository
- `data/retail_transactions.csv` — 3,000 synthetic transactions
- `src/generate_dataset.py` — exact deterministic generator
- `notebooks/01_retail_demand_basket_analysis.ipynb` — reproducible analysis
- `docs/` — requirements, data dictionary, decision log, validation
- `presentation/final_presentation.md` — concise final handoff

## Reproduce
```bash
pip install -r requirements.txt
python src/generate_dataset.py
jupyter notebook notebooks/01_retail_demand_basket_analysis.ipynb
```

## Interpretation
Association is not causation. High lift means products co-occur more often than expected from their individual transaction coverage; it does not prove that a merchandising action will create incremental sales.

## Data provenance & responsible use
The dataset is synthetic and deterministic. It contains no real customer identities, payment information, or private records.

## Limitations
The dataset does not include price, margin, promotion, stockout, store, or time-of-day variables. Results should be treated as portfolio/internship analysis, not a claim about a real retailer.

## Next steps
Add authorized real transaction data and commercial variables; then test bundle/placement ideas with controlled experiments and measure incremental basket value, conversion and revenue.
