import pandas as pd
import numpy as np
import os

# ==========================================
# Compute Mutual Fund Performance Metrics
# ==========================================

os.makedirs("data/processed", exist_ok=True)

# Load NAV History
nav = pd.read_csv("data/processed/02_nav_history_clean.csv")

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Sort data
nav = nav.sort_values(["amfi_code", "date"])


# ==========================================
# Calculate Daily Returns
# ==========================================

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
       .pct_change()
)

# ==========================================
# Annualized Return
# ==========================================

annual_return = (
    nav.groupby("amfi_code")["daily_return"]
       .mean() * 252
)

# ==========================================
# Annualized Risk (Standard Deviation)
# ==========================================

annual_risk = (
    nav.groupby("amfi_code")["daily_return"]
       .std() * np.sqrt(252)
)

# ==========================================
# Sharpe Ratio
# ==========================================

risk_free_rate = 0.06

sharpe_ratio = (
    (annual_return - risk_free_rate)
    / annual_risk
)

# ==========================================
# Create Metrics DataFrame
# ==========================================

metrics = pd.DataFrame({
    "annual_return": annual_return,
    "annual_risk": annual_risk,
    "sharpe_ratio": sharpe_ratio
})

metrics.reset_index(inplace=True)

# ==========================================
# Save Metrics
# ==========================================

metrics.to_csv(
    "data/processed/fund_metrics.csv",
    index=False
)

print("=" * 50)
print("Performance Metrics Computed Successfully")
print("=" * 50)

print(metrics.head())