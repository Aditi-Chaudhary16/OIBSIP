import pandas as pd 
import seaborn as sns

df = pd.read_csv("retail_sales_dataset.csv")

print(df.head())

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDescriptive Statistics:")
print(df.describe())

import matplotlib.pyplot as plt

df["Date"] = pd.to_datetime(df["Date"])

daily_sales = df.groupby("Date")["Total Amount"].sum()

plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales.values)
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(7, 5))
plt.bar(gender_counts.index, gender_counts.values)
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.title("Customer Distribution by Gender")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(df["Age"], bins=10)
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.title("Customer Age Distribution")
plt.tight_layout()
plt.show()

category_sales = df.groupby("Product Category")["Total Amount"].sum().sort_values(ascending=False)

print("\nSales by Product Category:")
print(category_sales)

plt.figure(figsize=(8, 5))
plt.bar(category_sales.index,category_sales.values)
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.title("Sales by Product Category")
plt.tight_layout()
plt.show()

# --------------------------------
# Correlation Heatmap
# --------------------------------

plt.figure(figsize=(8, 6))

numeric_data = df.select_dtypes(include="number")

sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# --------------------------------
# Additional Visualization
# Sales by Gender
# --------------------------------

gender_sales = df.groupby("Gender")["Total Amount"].sum()

plt.figure(figsize=(8, 5))

plt.bar(gender_sales.index, gender_sales.values)

plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.title("Sales by Gender")

plt.tight_layout()
plt.show()


# -------------------------------
# Final Analysis / Key Insights
# -------------------------------

print("\n========== FINAL ANALYSIS ==========")

# Overall sales
print("\nTotal Sales:", df["Total Amount"].sum())
print("Average Sales:", df["Total Amount"].mean())
print("Maximum Sale:", df["Total Amount"].max())
print("Minimum Sale:", df["Total Amount"].min())

# Gender analysis
print("\nCustomer Count by Gender:")
print(df["Gender"].value_counts())

# Age analysis
print("\nAverage Customer Age:", df["Age"].mean())
print("Minimum Customer Age:", df["Age"].min())
print("Maximum Customer Age:", df["Age"].max())

# Product category analysis
category_sales = df.groupby("Product Category")["Total Amount"].sum()

print("\nSales by Product Category:")
print(category_sales)

print("\nHighest Selling Category:",
      category_sales.idxmax())

print("Highest Category Sales:",
      category_sales.max())

print("\nLowest Selling Category:",
      category_sales.idxmin())

print("Lowest Category Sales:",
      category_sales.min())

print("\n========== CONCLUSION ==========")
print("The analysis shows the overall sales performance,")
print("customer distribution by gender and age, and")
print("sales performance across product categories.")