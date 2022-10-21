#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 01:04:34 2022

@author: nayaabsharma
"""

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram


def plot_dendrogram(model, y, **kwargs):
    # Create linkage matrix and then plot the dendrogram
    # create the counts of samples under each node
    
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, leaf_rotation=90, 
               leaf_font_size=8, labels=y, **kwargs)


def clustering(X, y):
    model = AgglomerativeClustering(distance_threshold=0, 
                                    n_clusters=None)
    
    model = model.fit(X)
    plt.title("Hierarchical Clustering Dendrogram")

    plot_dendrogram(model, y, truncate_mode="level", p=3)
    plt.xlabel("EXERCISE")
    plt.show()




data = pd.read_csv('MovingJoints.csv')
X = data.iloc[:, :8].copy()
# Labels for the dendogram
y = np.asarray(data.iloc[:, 8].copy())
clustering(X, y)
