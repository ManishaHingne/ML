# step 1: load the data
df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Position_Salaries.csv')

# step 2: clean the data
df$Position = NULL
df$Level2 = df$Level ^ 2
df$Level3 = df$Level ^ 3
df$Level4 = df$Level ^ 4
  
library(caTools)
# set.seed(1234)
results = sample.split(df$Salary, SplitRatio = 0.8)
df.train = df[results == TRUE, ]
df.test = df[results == FALSE, ]

# step 3: prepare the model/formula/equation
# Salary ~ Level
regressor = lm(Salary ~ Level + Level2 + Level3 , data = df.train)
print(summary(regressor))

# step 4: predict the value(s)
predictions = predict(regressor, newdata=df.test)

# step 5: test the result

# step 6: visualize the result

train.predictions = predict(regressor, newdata = df.train)
library(ggplot2)
# ggplot() +
#   geom_line(aes(x = df.train$Level, y = df.train$Salary, color='blue')) + 
#   geom_point(aes(x = df.train$Level, y = df.train$Salary, color='red')) +
#   geom_line(aes(x = df.train$Level, y = train.predictions, color='green')) + 
#   geom_point(aes(x = df.train$Level, y = train.predictions, color='yellow')) 

ggplot() +
  geom_line(aes(x = df.test$Level, y = df.test$Salary, color='blue')) + 
  geom_point(aes(x = df.test$Level, y = df.test$Salary, color='red')) +
  geom_line(aes(x = df.test$Level, y = predictions, color='green')) + 
  geom_point(aes(x = df.test$Level, y = predictions, color='yellow')) 


# ggplot() +
#   geom_line(aes(x = df$Level2, y = df$Salary, color='blue')) + 
#   geom_point(aes(x = df$Level2, y = df$Salary, color='red')) 
  




