from sklearn import datasets
from sklearn.cluster import KMeans, AgglomerativeClustering, MeanShift
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

# Load dataset
iris = datasets.load_iris()
X = iris.data

# Define numbers of clusters
clusters = [3, 4, 5]

# Define preprocessing pipelines
preprocessing_options = {
    'no_preprocessing': None,
    'transform': StandardScaler(),
    'pca': PCA(n_components=2),
    'transform_normalization': Pipeline([
        ('normalization', StandardScaler()),
    ]),
    'transform_normalization_pca': Pipeline([
        ('normalization', StandardScaler()),
        ('pca', PCA(n_components=2))
    ]),
}

# Define clustering algorithms
clustering_algorithms = {
    'KMeans': KMeans,
    'Hierarchical': AgglomerativeClustering,
    'MeanShift': MeanShift,
}

# Iterate over each clustering algorithm
for algorithm_name, algorithm_class in clustering_algorithms.items():
    print(f"Clustering Algorithm: {algorithm_name}")

    # Initialize clustering algorithm
    if algorithm_name == 'MeanShift':
        # MeanShift does not require specifying the number of clusters
        algorithm_instance = algorithm_class()
    else:
        algorithm_instance = algorithm_class()

    # Iterate over each preprocessing option
    for preprocessing_name, preprocessor in preprocessing_options.items():
        print(f"Preprocessing: {preprocessing_name}")

        for c in clusters:
            print(f"Number of clusters: {c}")

            if preprocessor is None:
                X_processed = X
            else:
                X_processed = preprocessor.fit_transform(X)

            if algorithm_name != 'MeanShift':
                # Fit clustering algorithm
                algorithm_instance.set_params(n_clusters=c)
                labels = algorithm_instance.fit_predict(X_processed)
            else:
                labels = algorithm_instance.fit_predict(X_processed)
                c = len(set(labels))

            # Calculate evaluation metrics
            silhouette = silhouette_score(X_processed, labels)
            calinski = calinski_harabasz_score(X_processed, labels)
            davies = davies_bouldin_score(X_processed, labels)

            print(f"Silhouette Score: {silhouette}")
            print(f"Calinski-Harabasz Index: {calinski}")
            print(f"Davies-Bouldin Index: {davies}")
            print("-----------------------------")
        print("\n")
