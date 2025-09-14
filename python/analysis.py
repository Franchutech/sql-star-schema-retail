# /python/analysis.py
# Narrative analysis script in Python
# Author: Francella Rojas (FranchuTech)
# Project: SQL Star Schema Retail

# 1. Import libraries
import os  
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns 
from matplotlib.ticker import FuncFormatter, MultipleLocator

# 2. Define directories
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # project root
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "outputs")
IMG_DIR = os.path.join(BASE_DIR, "images")

# 3. Load datasets
customers = pd.read_csv(os.path.join(DATA_DIR, "customers.csv"))
products = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))
stores = pd.read_csv(os.path.join(DATA_DIR, "stores.csv"))
transactions = pd.read_csv(os.path.join(DATA_DIR, "transactions.csv"))

# 4. Confirm load
print("Datasets loaded successfully 🚀")
print("Transactions shape:", transactions.shape)
print(transactions.head())

# 5. Calculate Revenue, Cost, and Profit
transactions["revenue"] = transactions["total_amount"]

transactions = transactions.merge(
    products[["product_id", "cost_price", "product_name"]],
    on="product_id",
    how="left"
)

transactions["total_cost"] = transactions["quantity"] * transactions["cost_price"]
transactions["profit"] = transactions["revenue"] - transactions["total_cost"]

print("Example transactions with revenue and profit:")
print(transactions.head())

# 6. Global KPIs
total_revenue = transactions["revenue"].sum()
total_profit = transactions["profit"].sum()
avg_order_value = transactions["revenue"].mean()
num_transactions = transactions["transaction_id"].nunique()

print("\n===== Global KPIs =====")
print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Total Profit: {total_profit:,.2f}")
print(f"Average Order Value (AOV): {avg_order_value:,.2f}")
print(f"Number of Transactions: {num_transactions:,}")

# 7. Export KPIs to CSV
kpis = {
    "total_revenue": [total_revenue],
    "total_profit": [total_profit],
    "avg_order_value": [avg_order_value],
    "num_transactions": [num_transactions]
}

df_kpis = pd.DataFrame(kpis)

os.makedirs(OUTPUT_DIR, exist_ok=True)
output_file = os.path.join(OUTPUT_DIR, "kpis_python.csv")
df_kpis.to_csv(output_file, index=False)

print(f"\nKPIs successfully exported to {output_file} ✅")

# 8. Visualization: Revenue by Country (Improved with better x-axis)

from matplotlib.ticker import FuncFormatter, MaxNLocator

# Prepare revenue by country
revenue_by_country = transactions.merge(
    customers[["customer_id", "country"]],
    on="customer_id",
    how="left"
).groupby("country")["revenue"].sum().reset_index()

revenue_by_country = revenue_by_country.sort_values(by="revenue", ascending=False)

# Plot
plt.figure(figsize=(10,6))
sns.barplot(x="revenue", y="country", data=revenue_by_country, palette="viridis")

# Format x-axis to millions
formatter = FuncFormatter(lambda x, _: f'{int(x/1e6)}M')
plt.gca().xaxis.set_major_formatter(formatter)

# Force more ticks on the x-axis (e.g., 10 divisions)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10))

plt.title("Total Revenue by Country (in Millions USD)", fontsize=14)
plt.xlabel("Revenue (Millions USD)")
plt.ylabel("Country")
plt.tight_layout()

os.makedirs(IMG_DIR, exist_ok=True)
output_img = os.path.join(IMG_DIR, "revenue_by_country.png")
plt.savefig(output_img)
plt.close()

print(f"\nImproved plot saved at {output_img} ✅")

# 9. Visualization: Profit by Country

profit_by_country = transactions.merge(
    customers[["customer_id", "country"]],
    on="customer_id",
    how="left"
).groupby("country")["profit"].sum().reset_index()

profit_by_country = profit_by_country.sort_values(by="profit", ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x="profit", y="country", data=profit_by_country, palette="crest")

# Format x-axis to millions
formatter = FuncFormatter(lambda x, _: f'{int(x/1e6)}M')
plt.gca().xaxis.set_major_formatter(formatter)

# Force more ticks for clarity
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10))

plt.title("Total Profit by Country (in Millions USD)", fontsize=14)
plt.xlabel("Profit (Millions USD)")
plt.ylabel("Country")
plt.tight_layout()

output_img = os.path.join(IMG_DIR, "profit_by_country.png")
plt.savefig(output_img)
plt.close()

print(f"\nPlot saved at {output_img} ✅")

# 10. Visualization: Profit Distribution (per transaction)

plt.figure(figsize=(10,6))
sns.histplot(transactions["profit"], bins=50, kde=True, color="skyblue")

# Format x-axis to thousands for readability
formatter = FuncFormatter(lambda x, _: f'{int(x/1000)}K')
plt.gca().xaxis.set_major_formatter(formatter)

plt.title("Distribution of Profit per Transaction", fontsize=14)
plt.xlabel("Profit (Thousands USD)")
plt.ylabel("Number of Transactions")
plt.tight_layout()

output_img = os.path.join(IMG_DIR, "profit_distribution.png")
plt.savefig(output_img)
plt.close()

print(f"\nPlot saved at {output_img} ✅")

# 11. Visualization: Top 10 Stores by Revenue (Zoomed)

revenue_by_store = transactions.merge(
    stores[["store_id", "store_name"]],
    on="store_id",
    how="left"
).groupby("store_name")["revenue"].sum().reset_index()

top_stores = revenue_by_store.sort_values(by="revenue", ascending=False).head(10)

top_stores["revenue_millions"] = top_stores["revenue"] / 1e6

min_val = top_stores["revenue_millions"].min()
max_val = top_stores["revenue_millions"].max()

plt.figure(figsize=(10,6))
sns.barplot(x="revenue_millions", y="store_name", data=top_stores, palette="flare")
plt.title("Top 10 Stores by Revenue (Zoomed Scale)", fontsize=14)
plt.xlabel("Revenue (Millions USD)")
plt.ylabel("Store")

# Zoom the x-axis to focus on differences
plt.xlim(min_val * 0.98, max_val * 1.02)

plt.tight_layout()

output_img = os.path.join(IMG_DIR, "top_stores.png")
plt.savefig(output_img)
plt.close()

print(f"\nZoomed plot saved at {output_img} ✅")

# 12. Visualization: Top 10 Products by Revenue

revenue_by_product = transactions.groupby("product_name")["revenue"].sum().reset_index()

top_products = revenue_by_product.sort_values(by="revenue", ascending=False).head(10)
top_products["revenue_millions"] = top_products["revenue"] / 1e6

plt.figure(figsize=(10,6))
sns.barplot(x="revenue_millions", y="product_name", data=top_products, palette="mako")
plt.title("Top 10 Products by Revenue (in Millions USD)", fontsize=14)
plt.xlabel("Revenue (Millions USD)")
plt.ylabel("Product")
plt.tight_layout()

output_img = os.path.join(IMG_DIR, "top_products.png")
plt.savefig(output_img)
plt.close()

print(f"\nPlot saved at {output_img} ✅")
