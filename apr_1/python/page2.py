import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# step 1: load the data
df = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 1/Mall_Customers.csv')
x = df.iloc[:, 3:5].values


from sklearn.cluster import AgglomerativeClustering
info = AgglomerativeClustering(n_clusters=5, linkage='average')
info = info.fit(x)
print(info.labels_)

# step 6: visualize the result
def visualizeRecords1():
    records_cluster_0 = x[info.labels_ == 0, :]
    records_cluster_1 = x[info.labels_ == 1, :]
    records_cluster_2 = x[info.labels_ == 2, :]
    records_cluster_3 = x[info.labels_ == 3, :]
    records_cluster_4 = x[info.labels_ == 4, :]

    plt.scatter(records_cluster_0[:, 0], records_cluster_0[:, 1], c='red')
    plt.scatter(records_cluster_1[:, 0], records_cluster_1[:, 1], c='blue')
    plt.scatter(records_cluster_2[:, 0], records_cluster_2[:, 1], c='green')
    plt.scatter(records_cluster_3[:, 0], records_cluster_3[:, 1], c='brown')
    plt.scatter(records_cluster_4[:, 0], records_cluster_4[:, 1], c='yellow')
    plt.show()

def visualizeRecords2():
    colors = ('red', 'blue', 'green', 'brown', 'yellow')
    for index in range(5):
        records_cluster = x[info.labels_ == index, :]
        plt.scatter(records_cluster[:, 0], records_cluster[:, 1], c=colors[index])
    plt.show()

visualizeRecords2()


