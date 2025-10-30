# ---------------------------------------------------------
# Task 2: Data Cleaning
# ---------------------------------------------------------

import pandas as pd

# Step 1: Load raw dataset
df = pd.read_csv("../Task1_DataCollection/raw_sales_data.csv")
print("✅ Raw data loaded successfully!")
print("Initial shape:", df.shape)

# Step 2: Remove duplicate rows
df = df.drop_duplicates()
print("✅ Duplicates removed. New shape:", df.shape)

# Step 3: Handle missing values
# Fill numeric columns with mean, text columns with mode
for col in df.columns:
    if df[col].dtype in ["float64", "int64"]:
        df[col].fillna(df[col].mean(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)
print("✅ Missing values handled.")

# Step 4: Convert 'Date' to datetime
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    print("✅ Date column converted to datetime.")

# Step 5: Remove invalid values
if "Quantity" in df.columns:
    df = df[df["Quantity"] > 0]
if "Unit price" in df.columns:
    df = df[df["Unit price"] > 0]
print("✅ Invalid values removed.")

# Step 6: Save cleaned dataset
df.to_csv("clean_sales_data.csv", index=False)
print("📁 clean_sales_data.csv saved successfully!")
