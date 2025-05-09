# Source.py - Data Processing and Recommendation System

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Sample Student Data
data = {
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'time_spent': [120, 150, 200, 80, 60, 90, 130, 170, 140, 110],
    'assignments_completed': [8, 6, 9, 5, 4, 7, 8, 10, 6, 5],
    'quiz_score': [85, 78, 92, 70, 65, 80, 88, 94, 76, 72],
    'test_score': [88, 75, 90, 65, 60, 78, 85, 92, 80, 70]
}

# Create DataFrame
df = pd.DataFrame(data)

# Data Preprocessing
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['time_spent', 'assignments_completed', 'quiz_score', 'test_score']])

# KMeans Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_data)

# Dimensionality Reduction using PCA
pca = PCA(n_components=2)
pca_components = pca.fit_transform(scaled_data)
df['pca1'] = pca_components[:, 0]
df['pca2'] = pca_components[:, 1]

# Calculate Silhouette Score
sil_score = silhouette_score(scaled_data, df['cluster'])
print(f"Silhouette Score: {sil_score}")

# Visualization
plt.figure(figsize=(8, 5))
plt.scatter(df['pca1'], df['pca2'], c=df['cluster'], cmap='viridis')
plt.title('Student Clusters based on Engagement and Performance')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.colorbar(label='Cluster')
plt.show()

# Recommendations based on Clusters
recommendations = {
    0: 'Review materials more actively, focus on quizzes to boost test scores.',
    1: 'Engage more with assignments and review learning materials daily.',
    2: 'Great performance! Continue with the same pace and explore advanced topics.'
}

# Print Recommendations
for idx, row in df.iterrows():
    cluster = row['cluster']
    print(f"Student {row['student_id']} (Cluster {cluster}): {recommendations[cluster]}")


The Source.py file for data processing and recommendations is ready in the canvas. Let me know if you need any changes or additional features.

