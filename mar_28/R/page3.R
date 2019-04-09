# prints the accuracy of the model
printAccuracy = function(cm) {
  correct.predictions = sum(diag(cm))
  total.predictions = sum(cm)
  accuracy = (correct.predictions / total.predictions) * 100
  print(accuracy)
}

# step 1: load the data
df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Social_Network_Ads.csv')

# step 2: clean the data
df = df[3:5]

library(caTools)
results = sample.split(df$Purchased, SplitRatio = 0.8)
df.train = df[results == TRUE, ]
df.test = df[results == FALSE, ]

# step 3: prepare the model/formula/equation
library(randomForest)
classifier = randomForest(Purchased ~ ., data = df.train, ntree=100)

# step 4: predict the value(s)
predictions = predict(classifier, newdata = df.test)

# step 5: test the result
cm = table(df.test$Purchased, predictions)
printAccuracy(cm)

# step 6: visualize the result
