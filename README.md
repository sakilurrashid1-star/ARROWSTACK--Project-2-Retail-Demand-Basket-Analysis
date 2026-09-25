# Arrowstack Project 2 — Retail Demand & Basket Analysis

**Intern:** Alkamah Sakilur Rashid  
**Track:** Data Science — Technical Track • Intermediate  
**Project:** Retail Demand & Basket Analysis  
**Data:** Deterministic synthetic retail transactions (no customer PII)

## Executive summary
This project analyzes historical-style retail transactions to answer two practical questions:
1. Which products and basket patterns drive demand?
2. Which products are repeatedly purchased together strongly enough to inform merchandising, bundles, or cross-sell experiments?

The workflow includes data validation, business-question EDA, basket-level association analysis, evidence-based recommendations, limitations, and a reproducible handoff.

## Key evidence
- Transactions analyzed: **3,000**
- Average basket size: **3.843 items**
- Basket size range: **2–8 items**
- Most frequently purchased item: **Milk (1,745 baskets; 58.2%)**
- Strong association examples are evaluated using support, confidence and lift rather than frequency alone.
- Top lift pair in the generated dataset: **Cereal + Yogurt (lift 2.747, support 8.3%)**

## Stakeholder and success criteria
**Primary stakeholder:** retail merchandising / category manager.  
**Decision enabled:** identify products and combinations worth testing in bundles, adjacent placement, or targeted cross-sell.  
**Success criteria:** clean transaction-level input; traceable basket transformation; interpretable demand and association metrics; validation evidence; documented limitations.

## Repository structure
```
data/retail_transactions.csv
src/generate_dataset.py
notebooks/01_retail_demand_basket_analysis.ipynb
docs/data_dictionary.md
docs/requirements.md
docs/decision_log.md
docs/validation_report.md
presentation/final_presentation.md
requirements.txt
README.md
```

## Method
1. Validate schema, identifiers, dates, basket sizes and missingness.
2. Parse pipe-delimited baskets into transaction-item form.
3. Measure item frequency and basket-size distribution.
4. Build a one-hot transaction matrix.
5. Mine frequent itemsets and association rules.
6. Compare support, confidence and lift.
7. Translate evidence into testable business actions.
8. Record limitations and next steps.

## Important interpretation rule
Association is **not causation**. A high-lift pair indicates co-purchase concentration in this dataset; it does not prove that placing one product beside another will cause incremental sales.

## Reproduce
```bash
pip install -r requirements.txt
python src/generate_dataset.py
jupyter notebook notebooks/01_retail_demand_basket_analysis.ipynb
```

## Data provenance
The dataset is synthetic and deterministic for portfolio/internship use. It contains no real customer identities, payment information, or private records.

## Handoff
The notebook is the main review artifact. The validation report records quality checks, while the presentation summarizes stakeholder framing, evidence, recommendations, limitations and next steps.
