CREATE SCHEMA IF NOT EXISTS retail;

-- Tabla de Productos
CREATE TABLE IF NOT EXISTS retail.products (
    product_id    INT PRIMARY KEY,
    product_name  VARCHAR(100) NOT NULL,
    category      VARCHAR(50) NOT NULL,
    cost_price    DECIMAL(10,2) NOT NULL CHECK (cost_price >= 0),
    sale_price    DECIMAL(10,2) NOT NULL CHECK (sale_price >= 0)
);


-- Tabla de Clientes
CREATE TABLE IF NOT EXISTS retail.customers (
    customer_id     INT PRIMARY KEY,   
    customer_name   VARCHAR(100) NOT NULL,
    country         VARCHAR(50) NOT NULL,
    loyalty_program VARCHAR(20) CHECK (loyalty_program IN ('Basic','Bronze','Silver','Gold','Platinum'))
);


-- Tabla de Tiendas
CREATE TABLE IF NOT EXISTS retail.stores (
    store_id    INT PRIMARY KEY,
    store_name  VARCHAR(100) NOT NULL,
    country     VARCHAR(50) NOT NULL
);

-- Tabla de Transacciones (Hechos)
CREATE TABLE IF NOT EXISTS retail.transactions (
    transaction_id  SERIAL PRIMARY KEY,
    date            DATE NOT NULL,
    customer_id     INT NOT NULL,
    product_id      INT NOT NULL,
    store_id        INT NOT NULL,
    quantity        INT NOT NULL CHECK (quantity > 0),
    total_amount    DECIMAL(10,2) NOT NULL,

    -- Relaciones
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES retail.customers(customer_id),
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES retail.products(product_id),
    CONSTRAINT fk_store FOREIGN KEY (store_id) REFERENCES retail.stores(store_id)
);
