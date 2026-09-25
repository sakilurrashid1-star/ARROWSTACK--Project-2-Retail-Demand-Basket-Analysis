"""Deterministic synthetic retail transaction generator for Arrowstack Project 2."""
from pathlib import Path
import random
import pandas as pd

SEED = 20260925
N_TRANSACTIONS = 3000
PRODUCTS = ["Bread","Milk","Eggs","Butter","Cheese","Coffee","Tea","Biscuits","Cereal","Juice","Chips","Pasta","Tomato Sauce","Chicken","Yogurt"]
BASE = {"Bread":0.42,"Milk":0.45,"Eggs":0.34,"Butter":0.22,"Cheese":0.2,"Coffee":0.28,"Tea":0.22,"Biscuits":0.25,"Cereal":0.2,"Juice":0.18,"Chips":0.24,"Pasta":0.22,"Tomato Sauce":0.18,"Chicken":0.2,"Yogurt":0.18}

def generate():
    rng = random.Random(SEED)
    rows = []
    for i in range(1, N_TRANSACTIONS + 1):
        basket = set()
        u = rng.random()
        if u < 0.30:
            basket.update(["Bread", "Butter"])
            if rng.random() < 0.65: basket.add("Milk")
        elif u < 0.55:
            basket.update(["Coffee", "Biscuits"])
            if rng.random() < 0.60: basket.add("Milk")
        elif u < 0.75:
            basket.update(["Pasta", "Tomato Sauce"])
            if rng.random() < 0.55: basket.add("Cheese")
        elif u < 0.90:
            basket.update(["Cereal", "Milk"])
            if rng.random() < 0.50: basket.add("Yogurt")
        else:
            basket.update(["Chicken", "Pasta"])
            if rng.random() < 0.50: basket.add("Tomato Sauce")
        for p, prob in BASE.items():
            if p not in basket and rng.random() < prob * 0.42:
                basket.add(p)
        while len(basket) < 2:
            basket.add(rng.choice(PRODUCTS))
        rows.append({
            "transaction_id": f"T{i:05d}",
            "transaction_date": f"2026-{((i-1)%12)+1:02d}-{((i-1)%28)+1:02d}",
            "customer_segment": rng.choice(["Value", "Regular", "Premium"]),
            "items": "|".join(sorted(basket)),
            "basket_size": len(basket),
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    out = Path(__file__).resolve().parents[1] / "data" / "retail_transactions.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    generate().to_csv(out, index=False)
    print(f"Wrote {len(generate())} transactions to {out}")
