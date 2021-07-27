import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def kmeans_trainer(df, n_clusters):
    '''kmeans_trainer:
        this function will train the algorithm with N clusters and the df data
        returns: kmeans and centroids'''
    kmeans = KMeans(n_clusters=n_clusters).fit(df)
    centroids = kmeans.cluster_centers_

    return kmeans, centroids

def plot_clustur(df, kmeans, centroids, centroids_color):
    '''plot_clustur:
        this function will plot the data and the centroids of clusters
        returns: None'''

    plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], c=centroids_color, s=50)
    plt.show()