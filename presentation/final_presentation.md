# Final Presentation — Retail Demand & Basket Analysis

## 1. Title
**Retail Demand & Basket Analysis**  
Arrowstack Data Science Internship — Project 2  
Alkamah Sakilur Rashid

## 2. Business question
Which products drive demand, and which combinations are repeatedly purchased together?

## 3. Stakeholder & success
Primary stakeholder: retail merchandising/category management.  
Success: validated transaction inputs, traceable basket analysis, interpretable association metrics and actionable—but testable—insights.

## 4. Dataset
3,000 deterministic synthetic transactions • 15 products • no real customer PII.  
Average basket: 3.843 items; basket range 2–8.

## 5. Data quality
0 duplicate transaction IDs • 0 missing cells • valid segments • basket_size reconciles with parsed items.

## 6. Demand pattern
Top product coverage:
1. Milk — 58.2%
2. Bread — 42.5%
3. Butter — 36.8%
4. Pasta — 35.8%
5. Coffee — 33.7%

## 7. Association analysis
Rules are evaluated using support, confidence and lift. Highest-lift pair:
**Cereal + Yogurt** — lift 2.754, support 8.3%.

## 8. Business use
Use sufficiently supported high-lift combinations as candidates for bundle or placement experiments. Measure incremental outcomes rather than assuming association causes sales.

## 9. Limitations
Synthetic data; no price, margin, promotion, stockout, store or time-of-day fields. Association does not establish causation.

## 10. Next steps
Add authorized real transaction data, commercial variables and controlled experiments; monitor incremental basket value, conversion and revenue.

## 11. Handoff
README + data dictionary + reproducible generator + notebook + validation report + decision log are included in the GitHub repository.
