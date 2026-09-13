import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_excel("Online Retail.xlsx")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

# Remove missing customer IDs
df = df.dropna(subset=["CustomerID"])

# Remove cancelled/negative quantities and prices
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# Create Total Amount
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# RFM features
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (pd.to_datetime(df["InvoiceDate"]).max() - pd.to_datetime(x).max()).days,
    "InvoiceNo": "nunique",
    "TotalAmount": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

print("\nRFM Summary:")
print(rfm.describe())

# Standardisation
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# Elbow Method
inertia = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(rfm_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(2, 11), inertia, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()

# Apply K-Means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

# Cluster profile
profile = rfm.groupby("Cluster")[["Recency", "Frequency", "Monetary"]].mean()

print("\nCluster Profiles:")
print(profile)

# Number of customers per cluster
plt.figure(figsize=(8, 5))
rfm["Cluster"].value_counts().sort_index().plot(kind="bar")
plt.title("Number of Customers per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Number of Customers")
plt.show() 

# Scatter plot: Frequency vs Monetary
plt.figure(figsize=(8, 5))
plt.scatter(rfm["Frequency"], rfm["Monetary"], c=rfm["Cluster"])
plt.title("Customer Segments: Frequency vs Monetary")
plt.xlabel("Purchase Frequency")
plt.ylabel("Monetary Value")
plt.show()

# Scatter plot: Recency vs Monetary
plt.figure(figsize=(8, 5))
plt.scatter(rfm["Recency"], rfm["Monetary"], c=rfm["Cluster"])
plt.title("Customer Segments: Recency vs Monetary")
plt.xlabel("Recency")
plt.ylabel("Monetary Value")
plt.show()

print("\nMarketing Insights:")
print("Cluster 0: Analyse as a customer segment and target according to its RFM behaviour.")
print("Cluster 1: Focus on personalised offers and retention.")
print("Cluster 2: Encourage repeat purchases with targeted promotions.")
print("Cluster 3: Reward valuable customers and build loyalty.")