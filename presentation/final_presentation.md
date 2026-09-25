# Final Presentation — Retail Demand & Basket Analysis

## 1. Title
**Retail Demand & Basket Analysis**  
Arrowstack Data Science Internship — Project 2  
Alkamah Sakilur Rashid

## 2. Business question
Which products drive demand, and which combinations are consistently purchased together?

## 3. Stakeholder & success
Primary stakeholder: retail merchandising/category management.  
Success: clean inputs, traceable basket analysis, interpretable association metrics and validated evidence.

## 4. Dataset
3,000 synthetic transactions, 15 product categories, no real customer PII.  
Average basket: 3.843 items.

## 5. Data quality
0 duplicate IDs • 0 missing cells • basket sizes 2–8 • deterministic seed 20260925.

## 6. Demand pattern
Top items by transaction coverage:
1. Milk — 58.2%
2. Bread — 42.5%
3. Butter — 36.8%
4. Pasta — 35.8%
5. Coffee — 33.7%

## 7. Basket associations
Strong pairs are assessed with support, confidence and lift. Example:
- Cereal + Yogurt: lift 2.747, support 8.3%
- Pasta + Tomato Sauce: lift 2.390, support 26.1%
- Biscuits + Coffee: lift 2.326, support 25.8%

## 8. Business implications
Use high-lift, sufficiently supported combinations as candidates for bundle or placement experiments. Prioritize measurement of incremental basket value rather than assuming association creates causation.

## 9. Limitations
Synthetic data; no price, margin, stockout, promotion, store, or time-of-day variables. Association rules describe co-purchase structure and cannot establish causal impact.

## 10. Next steps
Add real authorized transaction data, margin and promotion features; test recommendations through controlled experiments; monitor incremental revenue, basket value and conversion.

## 11. Handoff
Notebook + dataset + validation report + decision log + requirements mapping are included in the repository.
