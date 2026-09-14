import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dirty_cafe_sales.csv")

print("===== DATASET PREVIEW =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== UNIQUE VALUES =====")
for column in df.columns:
    print(f"\n{column}:")
    print(df[column].unique()[:15])

# ==============================
# DATA QUALITY REPORT
# ==============================

quality_report = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values,
    "Data Type": df.dtypes.astype(str).values,
    "Unique Values": df.nunique().values
})

print("\n===== DATA QUALITY REPORT =====")
print(quality_report)

# Count ERROR and UNKNOWN values
print("\n===== ERROR / UNKNOWN COUNTS =====")

for column in df.columns:
    error_count = (df[column] == "ERROR").sum()
    unknown_count = (df[column] == "UNKNOWN").sum()

    if error_count > 0 or unknown_count > 0:
        print(
            f"{column}: ERROR = {error_count}, "
            f"UNKNOWN = {unknown_count}"
        )

# Save quality report
quality_report.to_csv("data_quality_report.csv", index=False)

print("\nData quality report saved as data_quality_report.csv")

# ==============================
# HANDLE ERROR AND UNKNOWN VALUES
# ==============================

# Replace invalid text values with NaN
df = df.replace(["ERROR", "UNKNOWN"], np.nan)

print("\n===== AFTER REPLACING ERROR/UNKNOWN =====")
print(df.isnull().sum())

# ==============================
# HANDLE MISSING VALUES
# ==============================

# Convert numeric columns to numeric
numeric_columns = ["Quantity", "Price Per Unit", "Total Spent"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Fill numeric missing values with median
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill categorical missing values with mode
categorical_columns = ["Item", "Payment Method", "Location"]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# Convert Transaction Date to datetime
df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce"
)

# Fill missing dates using the most common date
df["Transaction Date"] = df["Transaction Date"].fillna(
    df["Transaction Date"].mode()[0]
)

print("\n===== AFTER HANDLING MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DATA TYPES AFTER CLEANING =====")
print(df.dtypes)

# ==============================
# OUTLIER DETECTION
# ==============================

print("\n===== OUTLIER DETECTION =====")

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print(f"{column}: {len(outliers)} outliers")

# Check duplicates after cleaning
print("\n===== DUPLICATES AFTER CLEANING =====")
print("Duplicate rows:", df.duplicated().sum())

# ==============================
# HANDLE OUTLIERS
# ==============================

outlier_summary = {}

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outlier_count = (
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ).sum()

    outlier_summary[column] = outlier_count

    # Cap extreme values instead of deleting valid transactions
    df[column] = df[column].clip(
        lower=lower_limit,
        upper=upper_limit
    )

print("\n===== OUTLIERS HANDLED =====")
for column, count in outlier_summary.items():
    print(f"{column}: {count} outliers capped")

# Verify remaining outliers
print("\n===== OUTLIERS AFTER HANDLING =====")

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    remaining = (
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ).sum()

    print(f"{column}: {remaining}")

    # ==============================
# SAVE CLEANED DATASET
# ==============================

output_file = "cleaned_cafe_sales.csv"

df.to_csv(output_file, index=False)

print("\n===== FINAL CLEANED DATASET =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

print(f"\nCleaned dataset saved as: {output_file}")

# ==============================
# BEFORE vs AFTER COMPARISON
# ==============================

print("\n===== BEFORE vs AFTER CLEANING =====")

print("Before cleaning:")
print("Rows:", 10000)
print("Columns:", 8)
print("Missing values:", 7856)
print("Duplicate rows:", 0)
print("Outliers in Total Spent:", 259)

print("\nAfter cleaning:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

print("\nData cleaning completed successfully!")