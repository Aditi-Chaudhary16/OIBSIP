# OIBSIP - Data Cleaning

## Task 3: Cleaning Data

### Objective

The objective of this project is to demonstrate professional data cleaning skills by transforming a messy Cafe Sales dataset into a clean and analysis-ready dataset.

## Dataset

The dataset contains 10,000 cafe sales transactions and 8 columns:

- Transaction ID
- Item
- Quantity
- Price Per Unit
- Total Spent
- Payment Method
- Location
- Transaction Date

## Data Quality Issues Identified

The raw dataset contained:

- Missing values
- `ERROR` values
- `UNKNOWN` values
- Incorrect data types
- Invalid transaction dates
- Statistical outliers
- No duplicate rows

## Data Cleaning Steps

### 1. Initial Data Inspection

The dataset was inspected for:

- Number of rows and columns
- Column names
- Data types
- Missing values
- Duplicate records
- Unique values
- `ERROR` and `UNKNOWN` values

### 2. Handling ERROR and UNKNOWN Values

`ERROR` and `UNKNOWN` values were converted into missing values (`NaN`) so they could be handled consistently.

### 3. Handling Missing Values

- Numeric columns were converted to numeric data types.
- Missing numeric values were filled using the median.
- Missing categorical values were filled using the mode.
- Transaction dates were converted to datetime format.
- Missing transaction dates were filled using the most common date.

### 4. Duplicate Check

Duplicate rows were checked before and after cleaning.

Result:

- Duplicate rows: 0

### 5. Outlier Detection

The Interquartile Range (IQR) method was used to detect statistical outliers.

A total of 259 outliers were identified in the `Total Spent` column.

Instead of deleting potentially valid transactions, extreme values were capped using the IQR limits.

### 6. Final Validation

After cleaning:

- Rows: 10,000
- Columns: 8
- Missing values: 0
- Duplicate rows: 0
- Outliers: handled

## Before vs After

| Quality Check | Before Cleaning | After Cleaning |
|---|---:|---:|
| Rows | 10,000 | 10,000 |
| Columns | 8 | 8 |
| Missing Values | 7,856 | 0 |
| Duplicate Rows | 0 | 0 |
| Total Spent Outliers | 259 | Handled |

## Files

- `dirty_cafe_sales.csv` - Original messy dataset
- `data_cleaning.py` - Python cleaning script
- `data_quality_report.csv` - Initial data quality report
- `cleaned_cafe_sales.csv` - Final cleaned dataset

## Tools Used

- Python
- Pandas
- NumPy

## Conclusion

The messy Cafe Sales dataset was successfully transformed into a clean, structured, and analysis-ready dataset. Missing values, invalid entries, incorrect data types, invalid dates, and statistical outliers were systematically addressed while preserving the original number of transactions.