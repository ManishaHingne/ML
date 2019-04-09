# prints the accuracy of the model
printAccuracy = function(cm) {
  correct.predictions = sum(diag(cm))
  total.predictions = sum(cm)
  accuracy = (correct.predictions / total.predictions) * 100
  print(accuracy)
}


# step 1: load the data
df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/titanic.csv')

# step 2: clean the data
df.titanic = df[, c(1, 2, 4, 5, 6, 7, 9, 11)]

# add a new column pclass
df.titanic$pclass = df.titanic$X...pclass


# remove X...pclass
df.titanic$X...pclass = NULL

# add a new column gender
df.titanic$gender = factor(df.titanic$sex, levels = c('male', 'female'), labels = c(1, 2))

# remove sex column
df.titanic$sex = NULL

# replace NA in age
df.titanic$age = ifelse(is.na(df.titanic$age), mean(df.titanic$age, na.rm = TRUE), df.titanic$age)

# sample
library(caTools)

results = sample.split(df.titanic$survived, SplitRatio = 0.2)
df.train = df.titanic[results == FALSE, ]
df.test = df.titanic[results == TRUE, ]

# step 3: prepare the model/formula/equation

# simple linear
regressor.simple = lm(survived ~ pclass, data = df.train)
print(summary(regressor.simple))
predictions = predict(regressor.simple, newdata = df.test)
predictions = ifelse(predictions >= 0.5, 1, 0)
cm = table(df.test$survived, predictions)
printAccuracy(cm)
print(regressor.simple$coefficients)

# multiple linear
regressor.multiple = lm(survived ~ pclass + gender + sibsp + age, data = df.train)
print(summary(regressor.multiple))
predictions = predict(regressor.multiple, newdata = df.test)
predictions = ifelse(predictions >= 0.5, 1, 0)
cm = table(df.test$survived, predictions)
printAccuracy(cm)

# logistic
regressor.logistic = glm(survived ~ pclass + gender + sibsp + age, data = df.train)
print(summary(regressor.logistic))
predictions = predict(regressor.logistic, newdata = df.test)
predictions = ifelse(predictions >= 0.5, 1, 0)
cm = table(df.test$survived, predictions)
printAccuracy(cm)
print(regressor.multiple$coefficients)

# step 4: predict the value(s)

# step 5: test the result

# step 6: visualize the result