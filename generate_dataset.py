import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from faker import Faker

# reproducibility
random.seed(42)
np.random.seed(42)
fake = Faker()

# ---------------------------
# 1. Products (500)
# ---------------------------
categories = ["Electronics", "Clothing", "Home", "Beauty", "Sports", "Toys"]

products = []
for i in range(1, 501):
    product_id = 10000000 + i  # 8-digit barcode style
    category = random.choice(categories)
    product_name = f"{fake.word().capitalize()} {category[:-1]}"  # e.g. "Smart Electronic"
    cost_price = round(random.uniform(5, 500), 2)
    sale_price = round(cost_price * random.uniform(1.2, 2.5), 2)  # markup
    products.append([product_id, product_name, category, cost_price, sale_price])

products = pd.DataFrame(products, columns=["product_id", "product_name", "category", "cost_price", "sale_price"])

# ---------------------------
# 2. Customers (10,000)
# ---------------------------
# Loyalty levels corregidos: sin "Diamond"
loyalty_levels = ["Basic", "Bronze", "Silver", "Gold", "Platinum"]

customers = []
for i in range(1, 10001):
    customer_id = random.randint(1000000, 999999999)  # 7-9 digits
    customer_name = fake.name()
    country = random.choice(["USA", "Spain", "Germany", "France", "UK", "Italy", "Mexico", "Brazil"])
    loyalty = random.choices(loyalty_levels, weights=[30, 25, 20, 15, 10])[0]  # distribución ajustada
    customers.append([customer_id, customer_name, country, loyalty])

customers = pd.DataFrame(customers, columns=["customer_id", "customer_name", "country", "loyalty_program"])

# ---------------------------
# 3. Stores (50)
# ---------------------------
stores = []
for i in range(1, 51):
    store_id = 10000 + i
    store_name = f"Store_{i}"
    country = random.choice(["USA", "Spain", "Germany", "France", "UK", "Italy", "Mexico", "Brazil"])
    stores.append([store_id, store_name, country])

stores = pd.DataFrame(stores, columns=["store_id", "store_name", "country"])

# ---------------------------
# 4. Transactions (~150k)
# ---------------------------
transactions = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

# Convertir a listas para asegurar consistencia
customer_ids = customers["customer_id"].tolist()
store_ids = stores["store_id"].tolist()

for i in range(1, 150001):
    trans_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    customer = random.choice(customer_ids)   # Siempre válido
    product_row = products.sample(1).iloc[0]
    store = random.choice(store_ids)         # Siempre válido
    quantity = np.random.randint(1, 6)

    total_amount = round(quantity * product_row["sale_price"], 2)

    transactions.append([
        i, trans_date.strftime("%Y-%m-%d"), customer,
        product_row["product_id"], store, quantity, total_amount
    ])

transactions = pd.DataFrame(
    transactions,
    columns=["transaction_id", "date", "customer_id", "product_id", "store_id", "quantity", "total_amount"]
)

# ---------------------------
# Save to /data
# ---------------------------
products.to_csv("data/products.csv", index=False)
customers.to_csv("data/customers.csv", index=False)
stores.to_csv("data/stores.csv", index=False)
transactions.to_csv("data/transactions.csv", index=False)

print("✅ Realistic dataset generated without FK/constraint issues!")
print("Products:", products.shape)
print("Customers:", customers.shape)
print("Stores:", stores.shape)
print("Transactions:", transactions.shape)
