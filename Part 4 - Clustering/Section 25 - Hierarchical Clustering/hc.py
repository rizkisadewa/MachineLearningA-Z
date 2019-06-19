# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:28:15 2019

@author: rizky
"""

# Hierarchical Clustering

# Importing the Library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the Mall dataset with Pandas 
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values

# Using the Dendogram to find the optimal number of cluster
import scipy.cluster.hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendogram')
plt.xlabel('Clusters')
plt.ylabel('Euclidean Distance')
plt.show()

# Fitting Hierarchical Clustering to the Mall Dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(X)

# Visualising the Cluster
# Visualizing the Cluster 
plt.scatter(X[y_hc==0,0],X[y_hc==0,1], s=100, c='red', label='Careful')
plt.scatter(X[y_hc==1,0],X[y_hc==1,1], s=100, c='blue', label='Standard')
plt.scatter(X[y_hc==2,0],X[y_hc==2,1], s=100, c='green', label='Target')
plt.scatter(X[y_hc==3,0],X[y_hc==3,1], s=100, c='cyan', label='Careless')
plt.scatter(X[y_hc==4,0],X[y_hc==4,1], s=100, c='magenta', label='Sensible')
plt.title("Cluster of clients")
plt.xlabel('Anual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()