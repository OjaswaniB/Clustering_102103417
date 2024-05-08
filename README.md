# Clustering
Clustering is the process of grouping a population or data points into several clusters, where points within the same cluster are more similar to each other than to those in other clusters. It's a fundamental technique in unsupervised learning used for exploring data structure and identifying patterns.
![image](https://github.com/OjaswaniB/Clustering_102103417/assets/118871180/f84c8266-a65a-4987-a0bd-cfffd19a05c4)

## Parameters used:

- Silhouette Score: The silhouette score measures the compactness and separation of clusters. It quantifies how similar an object is to its own cluster compared to other clusters. It's particularly useful for convex-shaped clusters but may not perform well with irregularly shaped clusters.

- Calinski–Harabasz Index (CHI): Also known as the Variance Ratio Criterion (VRC), CHI is an internal evaluation metric for clustering algorithms. It assesses clustering quality solely based on dataset characteristics and clustering results, without external labels.

- Davies-Bouldin Index:The Davies-Bouldin Index evaluates clustering models by measuring the average similarity of each cluster to the most similar one. It considers both intra-cluster cohesion and inter-cluster separation.

## Techniques used:
- K-means Clustering:K-means is a popular unsupervised learning algorithm that partitions objects into k clusters based on their features' similarities. It iteratively assigns objects to the nearest cluster centroid, minimizing the within-cluster variance.
  ![image](https://github.com/OjaswaniB/Clustering_102103417/assets/118871180/cba2d732-5143-45b4-a852-e3e251c2d98c)

- Hierarchical Clustering:Hierarchical clustering builds a hierarchy of clusters by recursively merging or splitting them based on data dissimilarities. It doesn't require a predefined number of clusters and is useful for exploring data structures at different granularity levels.

- Mean-shift Clustering:Mean-shift is a density-based clustering algorithm that identifies clusters by locating high-density regions in the feature space. It iteratively shifts cluster centroids towards the mode of the data distribution, making it suitable for datasets with arbitrary cluster shapes.
