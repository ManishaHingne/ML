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
set.seed(12345)
results = sample.split(df$Purchased, SplitRatio = 0.8)
df.train = df[results == TRUE, ]
df.test = df[results == FALSE, ]

# step 3: prepare the model/formula/equation
testKnn = function() {
  library(class)
  predictions.knn = knn(train = df.train[-3], test = df.test[-3], cl = df.train$Purchased, k = 33)
  cm = table(df.test$Purchased, predictions.knn)
  printAccuracy(cm)
  
  library(ggplot2)
  
  ggplot() +
    geom_point(aes(x = df.test$Age, y = df.test$EstimatedSalary, color=ifelse(predictions == 0, 'red', 'green'))) +
    theme(legend.position = 'none')
}

testSVM = function() {
  library(e1071)
  classifier = svm(Purchased ~ ., data = df.train, type = 'C-classification')
  print(classifier)
  
  predictions = predict(classifier, newdata = df.test)
  cm = table(df.test$Purchased, predictions)
  printAccuracy(cm)
  
  library(ggplot2)
  
  ggplot() +
    geom_point(aes(x = df.test$Age, y = df.test$EstimatedSalary, color=ifelse(predictions == 0, 'red', 'green'))) +
    theme(legend.position = 'none')
  
}

testKnn()
testSVM()


