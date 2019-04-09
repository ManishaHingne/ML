# step 1: load the data
df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Mall_Customers.csv')

# step 2: clean the data
df = df[4:5]

# info.1 = kmeans(df, centers = 1, iter.max = 100)
# info.2 = kmeans(df, centers = 2, iter.max = 100)

# elbow method
wcss = vector()
for (k in 1:10) {
  info = kmeans(df, centers = k, iter.max = 100)
  # fitting is not required
  wcss[k] = info$tot.withinss
}

plot(1:10, wcss)

info = kmeans(df, centers = 5, iter.max = 100)

# step 6: visualize the result

library(cluster)
clusplot(df, info$cluster, lines = FALSE, shade = TRUE, color = TRUE)




