SELECT * FROM fact_nav LIMIT 10;

SELECT amfi_code, AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

SELECT city, SUM(amount_inr)
FROM fact_transactions
GROUP BY city;

SELECT amfi_code, MAX(nav)
FROM fact_nav
GROUP BY amfi_code;

SELECT amfi_code, MIN(nav)
FROM fact_nav
GROUP BY amfi_code;

SELECT COUNT(*)
FROM fact_transactions;

SELECT COUNT(DISTINCT investor_id)
FROM fact_transactions;

SELECT COUNT(DISTINCT amfi_code)
FROM fact_nav;