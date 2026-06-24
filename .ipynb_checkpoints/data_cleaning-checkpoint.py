import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# ==========================
# 1. Clean NAV History
# ==========================

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]

nav.to_csv("data/processed/02_nav_history_clean.csv", index=False)

print("NAV History cleaned successfully")
print(nav.shape)

# ==========================
# 2. Clean Investor Transactions
# ==========================

transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.upper()
)

transactions = transactions[
    transactions["amount_inr"] > 0
]

transactions = transactions.drop_duplicates()

transactions.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions cleaned successfully")
print(transactions.shape)

# ==========================
# Summary
# ==========================

print("\nData Cleaning Completed")