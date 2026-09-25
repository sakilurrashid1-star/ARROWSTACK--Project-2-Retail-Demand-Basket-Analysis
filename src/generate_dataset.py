"""Deterministic synthetic retail transaction generator for Arrowstack Project 2."""
from pathlib import Path
import pandas as pd

SEED = 20260925
N_TRANSACTIONS = 3000
PRODUCTS = ["Bread","Milk","Eggs","Butter","Cheese","Coffee","Tea","Biscuits","Cereal","Juice","Chips","Pasta","Tomato Sauce","Chicken","Yogurt"]
BASE = {"Bread":.42,"Milk":.45,"Eggs":.34,"Butter":.22,"Cheese":.20,"Coffee":.28,"Tea":.22,"Biscuits":.25,"Cereal":.20,"Juice":.18,"Chips":.24,"Pasta":.22,"Tomato Sauce":.18,"Chicken":.20,"Yogurt":.18}

class LCG:
    def __init__(self, seed):
        self.state = seed & 0xFFFFFFFF
    def random(self):
        self.state = (1664525 * self.state + 1013904223) & 0xFFFFFFFF
        return self.state / 4294967296.0

def generate():
    rng = LCG(SEED)
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
        for product, probability in BASE.items():
            if product not in basket and rng.random() < probability * 0.42:
                basket.add(product)
        if len(basket) < 2:
            basket.add(PRODUCTS[int(rng.random() * len(PRODUCTS))])
        if len(basket) > 8:
            items = sorted(basket)
            while len(items) > 8:
                items.pop(int(rng.random() * len(items)))
            basket = set(items)
        rows.append({
            "transaction_id": f"T{i:05d}",
            "transaction_date": f"2026-{((i-1)%12)+1:02d}-{((i-1)%28)+1:02d}",
            "customer_segment": ["Value","Regular","Premium"][int(rng.random()*3)],
            "items": "|".join(sorted(basket)),
            "basket_size": len(basket),
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    out = Path(__file__).resolve().parents[1] / "data" / "retail_transactions.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    generate().to_csv(out, index=False)
    print(f"Wrote {N_TRANSACTIONS} transactions to {out}")
