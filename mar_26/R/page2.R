accuracy = function(cm) {
  total = sum(cm)
  accurate.records = sum(diag(cm))
  accuracy = (accurate.records/total) * 100
  print(accuracy)
}

# step 1: load the data
df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Social_Network_Ads.csv')

# step 2: clean the data
# df$User.ID = NULL
# df$Gender = NULL
# 
# df = df[, c(3, 4, 5)]
# df = df[, 3:5]
df = df[3:5]
# df$Purchased = factor(df$Purchased)

library(caTools)
results = sample.split(df$Purchased, SplitRatio = 0.8)
df.train = df[results == TRUE, ]
df.test = df[results == FALSE, ]


# step 3: prepare the model/formula/equation
# step 4: predict the value(s)
library(class)
predictions = knn(train = df.train[-3], test = df.test[-3], cl = df.train$Purchased, k = 23)

# step 5: test the result
cm = table(df.test$Purchased, predictions)
accuracy(cm)

# step 6: visualize the result
library(ggplot2)

ggplot() +
  geom_point(aes(x = df$Age, y = df$EstimatedSalary))

















