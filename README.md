# RD INFRO TECHNOLOGY — Retail Sales Analytics & Forecasting

**Intern:** Himanshu Gurjar  
**Role:** Data Analytics Intern  
**Organization:** RD INFRO TECHNOLOGY  
**Duration:** October–November 2025  
**Environment:** WSL (Ubuntu 24.04) · Jupyter Notebook · Python 3.12 · Git & GitHub  

---

## 📌 Internship Objective

Build an end-to-end **Retail Sales Analytics Pipeline** consisting of:

1. **Data Collection**  
2. **Data Cleaning**  
3. **Data Transformation**  
4. **Visualization & Insights**  
5. **Machine Learning–based Sales Forecasting**

The project is divided into **3 core tasks** and **2 full projects**.

---

## 🧱 Core Tasks (Pipeline)

### **Task 1 — Data Collection**
**Folder:** `Task1_DataCollection/`  
- Loaded raw CSV datasets  
- Inspected schema & combined retail dataset  
- Exported `raw_sales_data.csv`  

Files:  
`Task1.ipynb`, `data_collection.py`

---

### **Task 2 — Data Cleaning**
**Folder:** `Task2_DataCleaning/`  
- Handled missing values  
- Removed duplicates  
- Converted datatypes  
- Exported `clean_sales_data.csv`

Files:  
`Task2.ipynb`, `data_cleaning.py`

---

### **Task 3 — Data Transformation**
**Folder:** `Task3_DataTransformation/`  
- Created new columns (Revenue, Profit, Tax, etc.)  
- Aggregated and grouped data  
- Prepared ML-ready dataset  
- Exported `transformed_sales_data.csv`

Files:  
`Task3.ipynb`, `data_transformation.py`

---

## 📊 Project A — Visualization & Insights Dashboard

**Folder:** `FullProject_Visualization/`  
**Notebook:** `visualization.ipynb`  
**Script:** `full_project_visualization.py`

### Key Visualizations
- Revenue vs Profit (Category-wise)  
- Monthly Revenue Trend  
- Customer Age vs Revenue Heatmap  
- Gender-wise Purchase Distribution  

### Output Images
- `revenue_profit_by_category.png`  
- `monthly_revenue_trend.png`  
- `age_revenue_heatmap.png`  
- `gender_distribution.png`

---

## 🤖 Project B — Sales Forecasting (Machine Learning)

**Folder:** `FullProject_SalesForecasting/`  
**Notebook:** `salesforecasting.ipynb`  
**Script:** `full_sales_forecasting.py`

### Model Workflow
1. Feature Engineering  
2. Random Forest Regression  
3. Model Evaluation (MAE, R²)  
4. Forecast Visualization  

### Output Images
- `actual_vs_predicted.png`  
- `feature_importance.png`  

---

## 🧰 Tech Stack

| Category | Tools / Libraries |
|----------|------------------|
| Language | Python 3.12 |
| Analytics | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Machine Learning | scikit-learn |
| Notebook | Jupyter Notebook |
| Environment | WSL (Ubuntu 24.04) |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```text
RD-INFRO-TECHNOLOGY/
├── Task1_DataCollection/
│   ├── Task1.ipynb
│   ├── data_collection.py
├── Task2_DataCleaning/
│   ├── Task2.ipynb
│   ├── data_cleaning.py
├── Task3_DataTransformation/
│   ├── Task3.ipynb
│   ├── data_transformation.py
├── FullProject_Visualization/
│   ├── visualization.ipynb
│   ├── full_project_visualization.py
│   ├── *.png
├── FullProject_SalesForecasting/
│   ├── salesforecasting.ipynb
│   ├── full_sales_forecasting.py
│   ├── *.png
├── .gitignore
└── README.md



▶️ How to Run This Project

git clone https://github.com/himanshugk/RD_INFRO_TECHNOLOGY
cd RD_INFRO_TECHNOLOGY
conda create -n rdtech python=3.12
conda activate rdtech
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook

Run notebooks in this order:

Task1_DataCollection

Task2_DataCleaning

Task3_DataTransformation

FullProject_Visualization

FullProject_SalesForecasting

🔍 Key Business Insights

Electronics & Fashion are top revenue categories

Customers aged 25–35 contribute the highest spending

Quantity and Unit Price are major revenue drivers

Random Forest provides reliable sales predictions

🧑‍💻 Author

Himanshu Gurjar
B.Tech CSE (AIML) · Data Analytics & AI Enthusiast

GitHub: https://github.com/himanshugk
