CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT
);

CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date DATE,
    nav REAL
);

CREATE TABLE fact_transactions (
    investor_id INTEGER,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL
);