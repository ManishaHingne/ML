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
df$User.ID = NULL
df$Gender = NULL

library(caTools)
results = sample.split(df$Purchased, SplitRatio = 0.8)
df.train = df[results == TRUE, ]
df.test = df[results == FALSE, ]

# step 3: prepare the model/formula/equation
# y = b0 + b1x1 + b2x2
regressor = lm(Purchased ~ ., data = df.train)

# values for b0 (Intercept), b1 (Age), b2 (EstimatedSalary)
print(regressor$coefficients)

# value for error for every point
# error =  residual = predicted value - observed value
print(regressor$residuals)

# step 4: predict the value(s)
predictions = predict(regressor, newdata = df.test)
predictions = ifelse(predictions >= 0.5, 1, 0)

# step 5: test the result
cm = table(df.test$Purchased, predictions)
# correct.values = diag(cm)
# total.correct.values = sum(correct.values)
# print(total.correct.values)

# total.values = sum(cm)
# print(total.values)

# total.incorrect.values = total.values - total.correct.values
# print(total.incorrect.values)

# accuracy = (total.correct.values / total.values) * 100
# print(accuracy)
printAccuracy(cm)

# step 6: visualize the result
library(ggplot2)

ggplot() +
  geom_point(aes(x = df$Age, y = df$Purchased, color='red'))