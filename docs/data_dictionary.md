# Data Dictionary

| Field | Type | Description | Quality rule |
|---|---|---|---|
| transaction_id | string | Unique transaction identifier | Unique, non-null |
| transaction_date | date | Synthetic transaction date | Parseable ISO date |
| customer_segment | categorical | Value, Regular, or Premium segment | Allowed set only |
| items | string | Pipe-delimited products in a basket | At least 2 products |
| basket_size | integer | Number of products in the basket | Equals parsed item count; 2–8 |

**Unit of analysis:** one row = one transaction/basket.

**Privacy:** synthetic data only; no direct identifiers or sensitive personal attributes are included.
