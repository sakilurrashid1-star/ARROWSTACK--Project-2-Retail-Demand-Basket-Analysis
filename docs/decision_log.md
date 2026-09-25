# Decision Log

| Decision | Rationale |
|---|---|
| Use synthetic transactions | Keeps the internship artifact safe, reproducible and free of real customer PII. |
| Use basket as unit of analysis | Matches the business question around product associations. |
| Report support + confidence + lift | Frequency alone can overstate popular-item relationships. |
| Treat rules as associative, not causal | Prevents unsupported business claims. |
| Keep recommendations testable | Retail actions should be validated with controlled measurement before rollout. |
