-- ========================================================
-- KPI QUERIES – SQL Star Schema Retail
-- ========================================================

-- 1. Total Revenue (usando total_amount de la tabla de hechos)
SELECT 
    SUM(total_amount) AS total_revenue
FROM retail.transactions;

-- 1b. Total Revenue (calculado dinámicamente con sale_price * quantity)
SELECT 
    SUM(p.sale_price * t.quantity) AS total_revenue_calc
FROM retail.transactions t
JOIN retail.products p ON t.product_id = p.product_id;


-- 2. Average Order Value (AOV)
-- Usando total_amount
SELECT 
    AVG(total_amount) AS avg_order_value
FROM retail.transactions;

-- Calculando dinámicamente
SELECT 
    AVG(order_value) AS avg_order_value_calc
FROM (
    SELECT 
        t.transaction_id,
        SUM(p.sale_price * t.quantity) AS order_value
    FROM retail.transactions t
    JOIN retail.products p ON t.product_id = p.product_id
    GROUP BY t.transaction_id
) sub;


-- 3. Revenue by Country (según país del cliente)
-- Usando total_amount
SELECT 
    c.country,
    SUM(t.total_amount) AS revenue
FROM retail.transactions t
JOIN retail.customers c ON t.customer_id = c.customer_id
GROUP BY c.country
ORDER BY revenue DESC;

-- Calculando dinámicamente
SELECT 
    c.country,
    SUM(p.sale_price * t.quantity) AS revenue_calc
FROM retail.transactions t
JOIN retail.products p ON t.product_id = p.product_id
JOIN retail.customers c ON t.customer_id = c.customer_id
GROUP BY c.country
ORDER BY revenue_calc DESC;


-- 4. Top 5 Products by Revenue
-- Usando total_amount
SELECT 
    p.product_name,
    SUM(t.total_amount) AS revenue
FROM retail.transactions t
JOIN retail.products p ON t.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 5;

-- Calculando dinámicamente
SELECT 
    p.product_name,
    SUM(p.sale_price * t.quantity) AS revenue_calc
FROM retail.transactions t
JOIN retail.products p ON t.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue_calc DESC
LIMIT 5;


-- 5. Revenue by Customer Segment (loyalty program)
-- Usando total_amount
SELECT 
    c.loyalty_program,
    SUM(t.total_amount) AS revenue
FROM retail.transactions t
JOIN retail.customers c ON t.customer_id = c.customer_id
GROUP BY c.loyalty_program
ORDER BY revenue DESC;

-- Calculando dinámicamente
SELECT 
    c.loyalty_program,
    SUM(p.sale_price * t.quantity) AS revenue_calc
FROM retail.transactions t
JOIN retail.products p ON t.product_id = p.product_id
JOIN retail.customers c ON t.customer_id = c.customer_id
GROUP BY c.loyalty_program
ORDER BY revenue_calc DESC;
