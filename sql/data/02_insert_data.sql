-- Products
COPY retail.products(product_id, product_name, category, cost_price, sale_price)
FROM '/mnt/c/Users/Demi/dev/sql-star-schema-retail/data/products.csv'
DELIMITER ',' CSV HEADER;

-- Customers
COPY retail.customers(customer_id, customer_name, country, loyalty_program)
FROM '/mnt/c/Users/Demi/dev/sql-star-schema-retail/data/customers.csv'
DELIMITER ',' CSV HEADER;

-- Stores
COPY retail.stores(store_id, store_name, country)
FROM '/mnt/c/Users/Demi/dev/sql-star-schema-retail/data/stores.csv'
DELIMITER ',' CSV HEADER;

-- Transactions
COPY retail.transactions(transaction_id, date, customer_id, product_id, store_id, quantity, total_amount)
FROM '/mnt/c/Users/Demi/dev/sql-star-schema-retail/data/transactions.csv'
DELIMITER ',' CSV HEADER;
