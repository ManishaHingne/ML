# step 1: load the data
# df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Market_Basket_Optimisation.csv')
# df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/50_Startups.csv', header = FALSE)

library(arules)

transactions = read.transactions('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Market_Basket_Optimisation.csv', rm.duplicates = TRUE, sep = ',')
itemFrequencyPlot(transactions, topN=10)
rules = apriori(transactions, parameter = list(confidence = 0.4, support = 0.04))
summary(rules)
inspect(rules)