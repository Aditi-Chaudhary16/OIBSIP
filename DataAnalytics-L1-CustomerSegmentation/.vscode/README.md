# Customer Segmentation Analysis

## Project Overview

This project performs customer segmentation analysis on an e-commerce retail dataset using RFM (Recency, Frequency, Monetary) analysis and K-Means clustering.

The objective is to group customers based on their purchasing behavior and provide useful marketing insights for each customer segment.

## Dataset

The project uses the Online Retail dataset.

The dataset contains transactional information such as:

- Invoice Number
- Stock Code
- Product Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Excel dataset
- K-Means Clustering

## Data Cleaning

The following data cleaning steps were performed:

- Removed records with missing Customer IDs.
- Removed transactions with negative or zero quantities.
- Removed transactions with zero or negative unit prices.

## RFM Analysis

RFM analysis was performed using three customer behavior features:

- Recency – Number of days since the customer's most recent purchase.
- Frequency – Number of unique purchases made by the customer.
- Monetary – Total amount spent by the customer.

## Customer Segmentation

The RFM features were standardized using StandardScaler.

K-Means clustering was then applied to group customers based on their purchasing behavior.

The Elbow Method was used to evaluate different numbers of clusters.

## Visualizations

The project includes the following visualizations:

1. Elbow Method
2. Number of Customers per Cluster
3. Recency vs Monetary
4. Frequency vs Monetary

## Cluster Profiling

The customer clusters were analyzed using their average Recency, Frequency, and Monetary values.

This helps identify differences in customer purchasing behavior and allows businesses to target different customer groups with suitable marketing strategies.

## Marketing Insights

- High-value and frequent customers can be targeted with loyalty programs and exclusive offers.
- Less active customers can be targeted with personalized offers and retention campaigns.
- Customers with high spending can receive premium offers and special promotions.
- Customer segments can be used to create more targeted marketing campaigns.

## Conclusion

Customer segmentation helps businesses understand different types of customers based on their purchasing behavior.

Using RFM analysis and K-Means clustering, customers can be grouped into meaningful segments. These segments can help businesses improve customer retention, personalize marketing campaigns, and focus on high-value customers.

## Project Files

- `customer_segmentation.py` – Python source code
- `Online Retail.xlsx` – Dataset
- `elbow_method.png` – Elbow Method visualization
- `customers_per_cluster.png` – Customer count by cluster
- `frequency_vs_monetary.png` – Frequency vs Monetary visualization
- `recency_vs_monetary.png` – Recency vs Monetary visualization