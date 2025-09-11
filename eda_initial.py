import pandas as pd

# Load CSVs
products = pd.read_csv("data/products.csv")
customers = pd.read_csv("data/customers.csv")
stores = pd.read_csv("data/stores.csv")
transactions = pd.read_csv("data/transactions.csv")

print("\n✅ DATASET OVERVIEW")
print("Products:", products.shape)
print("Customers:", customers.shape)
print("Stores:", stores.shape)
print("Transactions:", transactions.shape)

print("\n📦 SAMPLE ROWS")
print("\nProducts\n", products.head(5))
print("\nCustomers\n", customers.head(5))
print("\nStores\n", stores.head(5))
print("\nTransactions\n", transactions.head(5))

print("\n📊 Transactions Summary (quantity & total amount)")
print(transactions[["quantity", "total_amount"]].describe())
