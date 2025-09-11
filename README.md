---

## 🎯 Objectives
- Design a **Star Schema** with fact and dimension tables.
- Generate and transform a **synthetic retail dataset**.
- Write **SQL scripts** for table creation, data loading, and KPI queries.
- Perform **Python analysis** with pandas, matplotlib, and seaborn.
- Build an **interactive Power BI dashboard** with key business insights.

---

## 📊 Deliverables

1. **Data Modeling**
   - Star Schema diagram (dbdiagram.io / draw.io).
   - Fact table: Transactions.
   - Dimensions: Products, Customers, Stores.

2. **EDA (Exploratory Data Analysis)**
   - Initial EDA to validate dataset quality and business logic.

3. **SQL**
   - Table creation (DDL) and data loading (DML).
   - KPI queries: Total Revenue, Avg Order Value, Revenue by Country, Top Products.

4. **Python**
   - Narrative business analysis with 3–4 visualizations.

5. **Power BI**
   - Dashboard with KPIs, segmentation, top products, revenue by category, and map visualization.

---
---

## 📑 Dataset Documentation

### Products
- **product_id (PK):** Unique product identifier (8-digit code, barcode style).
- **product_name:** Realistic fake product name.
- **category:** Product category (Electronics, Clothing, Home, Beauty, Sports, Toys).
- **cost_price:** Acquisition cost per unit.
- **sale_price:** Sale price per unit (always higher than cost).

### Customers
- **customer_id (PK):** Unique customer identifier (7–9 digit number).
- **customer_name:** Fake realistic customer name.
- **country:** Country of residence (USA, Spain, Germany, France, UK, Italy, Mexico, Brazil).
- **loyalty_program:** Loyalty program category (Basic, Silver, Gold, Platinum, Diamond).

### Stores
- **store_id (PK):** Unique store identifier (5-digit code).
- **store_name:** Store name (Store_1…Store_50).
- **country:** Country where the store is located.

### Transactions
- **transaction_id (PK):** Unique transaction identifier.
- **date:** Date of transaction (2023–2024).
- **customer_id (FK):** References Customers.
- **product_id (FK):** References Products.
- **store_id (FK):** References Stores.
- **quantity:** Number of units purchased.
- **total_amount:** Total sales amount (quantity × sale_price).

---
## 🌟 Star Schema
The project uses a **Star Schema** to structure the retail dataset for analytics.

- **Fact table:** Transactions (sales data).
- **Dimension tables:** Products, Customers, Stores.

![Star Schema](images/star_schema.png)

---

## 🔄 Workflow
- Generate synthetic retail dataset with realistic customers, products, and stores.
- Perform **initial Exploratory Data Analysis (EDA)** to validate data quality and consistency.
- Build Star Schema for efficient querying.
- Run SQL queries to extract KPIs.
- Create Python visualizations and Power BI dashboard.

---

## 🧑‍💻 Tech Stack
- **Python** (pandas, matplotlib, seaborn)
- **SQL** (DDL, DML, KPIs)
- **Power BI** (interactive dashboard)
- **Git/GitHub** (project management)

---

## 📌 Key Learnings
This project highlights the importance of **Data Modeling** in analytics.  
A well-designed **Star Schema** improves SQL performance, simplifies queries, and enables efficient BI reporting.

---

## 📜 License
This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
