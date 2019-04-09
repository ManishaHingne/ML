# load the contents of myfunctions.R
# similar to #include <stdio.h>
source('/Volumes/Data/Sunbeam/2019/Feb/DBDA/ml/mar_29/R/myfunctions.R')

# step 1: load the data
df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Wine.csv')

# step 2: clean the data
df = df[c(1, 4, 6, 7, 10, 12, 13, 14)]

library(caTools)
set.seed(12345678)
results = sample.split(df$Customer_Segment, SplitRatio = 0.8)
df.train = df[results == TRUE, ]
df.test = df[results == FALSE, ]

# step 3: prepare the model/formula/equation
findIndepedentColumns = function() {
  regressor = lm(Customer_Segment ~ ., data = df.train)
  print(summary(regressor))  
}
# findIndepedentColumns()


crossValidateModel = function(algorithm, predictions, cm.required) {
  cm = table(df.test$Customer_Segment, predictions)
  accuracy = get.accuracy(cm)
  print(paste0(algorithm, ' accuracy: ', accuracy))
  # sprintf("%s Accuracy: %.2f %%", algorithm, accuracy)
  
  if (cm.required == TRUE) {
    print(cm)  
  }
}

visualizeResult = function(predictions, df.test) {
  library(ggplot2)
  ggplot() +
    # geom_point(
    #   aes(x = df.test$Alcohol, 
    #       y = df.test$Ash_Alcanity, 
    #       color=ifelse(df.test$Customer_Segment == 1, 'red', ifelse(df.test$Customer_Segment == 2, 'green', 'blue')))) +
    geom_point(
      aes(x = df.test$Alcohol, 
          y = df.test$Ash_Alcanity, 
          color=ifelse(predictions == 1, '#FFD700', ifelse(predictions == 2, '#6B8E23', '#008080')))) +
    
    theme(legend.position = 'none')
}

# using Logistic Regression
logisticRegression = function(visualize = FALSE, cm.required = FALSE) {
  classifier = glm(Customer_Segment ~., data = df.train)
  predictions = predict(classifier, newdata = df.test)
  
  # 1: < 1.5
  # 2: >= 1.5 and < 2.5
  # 3: >= 2.5

  # convert the regression values to classification values
  # predictions = ifelse(predictions >= 2.5, 3, ifelse(predictions >= 1.5, 2, 1))
  predictions = ifelse(predictions >= 3, 3, ifelse(predictions >= 2, 2, 1))
  
  crossValidateModel('Logistic Regresssion', predictions, cm.required)
  
  if (visualize == TRUE) {
    visualizeResult(predictions, df.test)
  }
}

# using KNN
knnClassification = function(visualize = FALSE, cm.required = FALSE) {
  library(class)
  predictions = knn(train = df.train[-8], test = df.test[-8], cl = df.train$Customer_Segment, k = 5)
  crossValidateModel('KNN', predictions, cm.required)
  if (visualize == TRUE) {
    visualizeResult(predictions, df.test)
  }
}

svmClassification = function(visualize = FALSE, cm.required = FALSE) {
  library(e1071)
  classifier = svm(Customer_Segment ~., data = df.train, type = 'C-classification')
  predictions = predict(classifier, newdata = df.test)
  
  crossValidateModel('SVM', predictions, cm.required)
  if (visualize == TRUE) {
    visualizeResult(predictions, df.test)
  }
}


nbClassification = function(visualize = FALSE, cm.required = FALSE) {
  df.train.nb = df.train
  df.train.nb$Customer_Segment = factor(df.train.nb$Customer_Segment)
  
  classifier = naiveBayes(Customer_Segment ~., data = df.train.nb)
  predictions = predict(classifier, newdata = df.test)
  
  crossValidateModel('Naive Bayes', predictions, cm.required)
  if (visualize == TRUE) {
    visualizeResult(predictions, df.test)
  }
}

decisionTreeClassification = function(visualize = FALSE, cm.required = FALSE) {
  df.train.dt = df.train
  df.train.dt$Customer_Segment = factor(df.train.dt$Customer_Segment)
  
  df.test.dt = df.test
  df.test.dt$Customer_Segment = factor(df.test.dt$Customer_Segment)
  
  library(rpart)
  classifier = rpart(Customer_Segment ~., data = df.train.dt)
  predictions = predict(classifier, newdata = df.test.dt, type='class')
  
  crossValidateModel('Decision Tree', predictions, cm.required)
  if (visualize == TRUE) {
    visualizeResult(predictions, df.test.dt)
  }
}

randomForestClassification = function(visualize = FALSE, cm.required = FALSE) {
  df.train.rf = df.train
  df.train.rf$Customer_Segment = factor(df.train.rf$Customer_Segment)
  
  df.test.rf = df.test
  df.test.rf$Customer_Segment = factor(df.test.rf$Customer_Segment)
  
  library(randomForest)
  classifier = randomForest(Customer_Segment ~., data = df.train.rf)
  predictions = predict(classifier, newdata = df.test.rf, type='class')
  
  crossValidateModel('Random Forest', predictions, cm.required)
  if (visualize == TRUE) {
    visualizeResult(predictions, df.test.rf)
  }
}

nbClassification()
logisticRegression()
knnClassification()
svmClassification()
decisionTreeClassification()
randomForestClassification()



