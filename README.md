# Mutual Fund Analytics Capstone Project

## Project Overview

This project was developed as part of the Bluestock Fintech Capstone Internship. The objective is to analyze mutual fund industry data, perform data cleaning and exploratory data analysis, compute performance metrics, and build an interactive Power BI dashboard for business insights.

---

## Project Objectives

- Import and clean mutual fund datasets
- Store processed data using SQLite
- Perform Exploratory Data Analysis (EDA)
- Calculate mutual fund performance metrics
- Build an interactive Power BI dashboard
- Generate business insights from investment data

---

## Technology Stack

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Power BI Desktop
- Git & GitHub
- Jupyter Notebook

---

## Project Structure

```
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── compute_metrics.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Bluestock_Mutual_Fund_Analytics_Final_Report.pdf
│   └── Presentation.pptx
│
└── README.md
```

---

## Datasets Used

- Fund Master
- NAV History
- AUM by Fund House
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

---

## Dashboard Pages

### Page 1 – Industry Overview
- Total AUM
- SIP Inflows
- Total Folios
- Total Schemes
- Fund House Analysis
- Benchmark Performance

### Page 2 – Fund Performance
- Risk vs Return
- Fund Scorecard
- NAV vs Benchmark
- Performance KPIs

### Page 3 – Investor Analytics
- Transaction Analysis
- State-wise Investments
- Age Group Analysis
- Monthly Transactions

### Page 4 – SIP & Market Trends
- SIP Trend
- Category Inflows
- Heatmap
- Top Categories

---

## Key Findings

- Mutual fund AUM showed consistent growth.
- SIP inflows increased over the analysis period.
- Large fund houses managed the highest AUM.
- Equity funds attracted significant investments.
- Interactive dashboards help users analyze market trends effectively.

---

## Future Improvements

- Live NAV integration using APIs
- Machine Learning-based fund recommendations
- Portfolio optimization
- Automated dashboard refresh

---

## Author

**Denis T**

Bluestock Fintech Capstone Project
