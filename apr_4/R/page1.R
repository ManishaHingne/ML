# prints the accuracy of the model
printAccuracy = function(cm) {
  correct.predictions = sum(diag(cm))
  total.predictions = sum(cm)
  accuracy = (correct.predictions / total.predictions) * 100
  print(accuracy)
}

# step 1: load the data
df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Churn_Modelling.csv')

# step 2: clean the data
df = df[4:14]

# convert the categorical to numerical
df$Geography = factor(df$Geography, levels = c('France', 'Spain', 'Germany'), labels = c(1, 2, 3))
df$Gender = factor(df$Gender, levels = c('Male', 'Female'), labels = c(1, 2))

# add the dummy columns
# Gender1 Gender2
# 1       0
# 0       1

df$Exited = factor(df$Exited)

library(caTools)
results = sample.split(df$Exited, SplitRatio = 0.8)
df.train = df[results == TRUE, ]
df.test = df[results == FALSE, ]

# step 3: prepare the model/formula/equation
checkColumns = function() {
  regressor = lm(Exited ~ ., data = df)
  print(summary(regressor))
}

# checkColumns()

library(randomForest)
classifier = randomForest(Exited ~ ., data = df.train, ntree = 100)

# step 4: predict the value(s)
predictions = predict(classifier, newdata = df.test)

# step 5: test the result
cm = table(df.test$Exited, predictions)
printAccuracy(cm)

# step 6: visualize the result
