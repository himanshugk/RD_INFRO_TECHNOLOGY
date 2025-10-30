# ---------------------------------------------------
# Task 1: Data Collection (Real Retail Dataset)
# ---------------------------------------------------

import pandas as pd
import requests

# 1️⃣ Load the dataset
df = pd.read_csv("retail_sales_dataset.csv")
print("✅ Retail data loaded successfully!")
print(df.head())

# 2️⃣ Fetch exchange rates from public API
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

# 3️⃣ Extract INR and JPY rates
usd_to_inr = data["rates"]["INR"]
usd_to_jpy = data["rates"]["JPY"]
print(f"✅ USD→INR: {usd_to_inr}, USD→JPY: {usd_to_jpy}")

# 4️⃣ Add rate columns
df["USD_TO_INR"] = usd_to_inr
df["USD_TO_JPY"] = usd_to_jpy

# 5️⃣ Save merged dataset
df.to_csv("raw_sales_data.csv", index=False)
print("📁 raw_sales_data.csv created successfully!")
