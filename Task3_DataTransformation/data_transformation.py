# ---------------------------------------------------------
# Task 3: Data Transformation
# ---------------------------------------------------------

import pandas as pd

# Step 1 – Load cleaned data
df = pd.read_csv("../Task2_DataCleaning/clean_sales_data.csv")
print("✅ Clean data loaded successfully!")
print("Shape:", df.shape)

# Step 2 – Add calculated columns
# Revenue = Quantity × Price per Unit
if "Quantity" in df.columns and "Price per Unit" in df.columns:
    df["Revenue"] = df["Quantity"] * df["Price per Unit"]

# Assume tax rate of 5 % and profit margin of 10 %
df["Tax"] = df["Revenue"] * 0.05
df["Profit"] = df["Revenue"] * 0.10
print("✅ Calculated columns added.")

# Step 3 – Create aggregated summary (by Product Category only)
summary = (
    df.groupby(["Product Category"], as_index=False)
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Profit=("Profit", "sum"),
        Avg_Unit_Price=("Price per Unit", "mean"),
        Transactions=("Transaction ID", "count"),
    )
)
print("✅ Summary data created by Product Category.")


# Step 4 – Save both outputs
df.to_csv("transformed_sales_data.csv", index=False)
summary.to_csv("sales_summary.csv", index=False)
print("📁 Files saved: transformed_sales_data.csv & sales_summary.csv")
