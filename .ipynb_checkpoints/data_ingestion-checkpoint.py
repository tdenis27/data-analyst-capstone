import pandas as pd
import os

files = os.listdir("data/raw")

summary = []

for file in files:
    if file.endswith(".csv"):
        df = pd.read_csv(f"data/raw/{file}")

        print("\n", file)
        print("Shape:", df.shape)
        print(df.head())

        summary.append({
            "File": file,
            "Rows": df.shape[0],
            "Columns": df.shape[1],
            "Missing Values": df.isnull().sum().sum()
        })

summary_df = pd.DataFrame(summary)
print(summary_df)

# AMFI Validation
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("\nAMFI Validation")
print("Missing Codes:", len(missing_codes))