# ---------------------------------------------------------
# Task 4: Full Project Visualization & Insights Dashboard
# ---------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load transformed dataset
df = pd.read_csv("../Task3_DataTransformation/transformed_sales_data.csv")
print("✅ Transformed data loaded successfully!")

# 2️⃣ Global style
sns.set(style="whitegrid", palette="muted")

# 3️⃣ Revenue vs Profit by Product Category
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Product Category", y="Revenue", color="#6FA8DC", label="Revenue")
sns.barplot(data=df, x="Product Category", y="Profit", color="#F6B26B", label="Profit")
plt.title("Revenue vs Profit by Product Category")
plt.legend()
plt.tight_layout()
plt.savefig("revenue_profit_by_category.png")
plt.show()

# 4️⃣ Monthly Revenue Trend
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Month"] = df["Date"].dt.to_period("M").astype(str)
monthly = df.groupby("Month")["Revenue"].sum().reset_index()

plt.figure(figsize=(9, 5))
sns.lineplot(data=monthly, x="Month", y="Revenue", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue_trend.png")
plt.show()

# 5️⃣ Age vs Revenue Heatmap
age_rev = df.pivot_table(values="Revenue", index="Age",
                         columns="Product Category", aggfunc="sum", fill_value=0)
plt.figure(figsize=(10, 6))
sns.heatmap(age_rev, cmap="YlGnBu")
plt.title("Age vs Revenue by Product Category")
plt.tight_layout()
plt.savefig("age_revenue_heatmap.png")
plt.show()

# 6️⃣ Gender Distribution Pie Chart
gender_counts = df["Gender"].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%",
        startangle=90, colors=["#6FA8DC", "#F6B26B"])
plt.title("Customer Gender Distribution")
plt.savefig("gender_distribution.png")
plt.show()

print("📊 All visualizations created successfully!")
