# step 1: load the data
df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Mall_Customers.csv')
print(head(df))

# step 2: droping the columns
df = df[4:5]

# step 3: find the optimum no of clusters
#         by using Elbow Method

wcss = vector()
for (k in 1:10) {
  info = kmeans(df, centers = k)
  wcss[k] = info$tot.withinss
}

print(wcss)
plot(1:10, wcss)

# # k = 1
# info.1 = kmeans(df, centers = 1)

# # k = 2
# info.2 = kmeans(df, centers = 2)

# # k = 3 
# info.3 = kmeans(df, centers = 3)

# # k = 4 
# info.4 = kmeans(df, centers = 4)


# k = 5 (after inspecting the Elbow point in the wcss plot)
info.5 = kmeans(df, centers = 5)

library(cluster)
clusplot(df, info.5$cluster, shade = TRUE, color = TRUE, lines = FALSE)