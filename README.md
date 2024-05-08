# Clustering
Clustering is the task of dividing the population or data points into several groups such that data points in the same groups are more similar to other data points in the same group and dissimilar to the data points in other groups. It is a collection of objects based on similarity and dissimilarity between them. 

## Parameters used:

1. Silhouette - The silhouette score is specialized for measuring cluster quality when the clusters are convex-shaped, and may not perform well if the data clusters have irregular shapes or are of varying sizes. The silhouette can be calculated with any distance metric, such as the Euclidean distance or the Manhattan distance.

    ![image](https://github.com/nitleenk/Clustering/assets/127779292/c21f8d59-e30f-431f-af77-7a88b6b1e4ea)


2. Calinski Harabasz - Calinski–Harabasz index (CHI), also known as the Variance Ratio Criterion (VRC), is a metric for evaluating clustering algorithms. It is an internal evaluation metric, where the assessment of the clustering quality is based solely on the dataset and the clustering results, and not on external, ground-truth labels. For instance,

    ![image](https://github.com/nitleenk/Clustering/assets/127779292/7ad083fa-838b-4013-b455-5eb5c863ec43)

3. Davies Bouldins - The Davies-Bouldin Index is a validation metric that is used to evaluate clustering models. It is calculated as the average similarity measure of each cluster with the cluster most similar to it. In this context, similarity is defined as the ratio between inter-cluster and intra-cluster distances.

    ![image](https://github.com/nitleenk/Clustering/assets/127779292/d8c49cac-3814-4e95-b5d4-cb07aa5f5632)

## Techniques used:

1. K-means Clustering - K-Means clustering is an unsupervised learning algorithm. There is no labeled data for this clustering, unlike in supervised learning. K-Means performs the division of objects into clusters that share similarities and are dissimilar to the objects belonging to another cluster.

2. Hierarchical Clustering - Hierarchical clustering is an unsupervised learning method for clustering data points. The algorithm builds clusters by measuring the dissimilarities between data. Unsupervised learning means that a model does not have to be trained, and we do not need a "target" variable.

3. K-means Shift Clustering - Mean-shift clustering is a non-parametric, density-based clustering algorithm that can be used to identify clusters in a dataset. It is particularly useful for datasets where the clusters have arbitrary shapes and are not well-separated by linear boundaries.
