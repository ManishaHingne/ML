# step 1: load the data
df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Mall_Customers.csv')

# step 2: clean the data
df = df[4:5]

info = hclust(d = dist(df, method = "euclidean"))
plot(info)