
# read the data  training data
df = read.csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 4/adult.data', header = FALSE)

# change the column names to proper columns
print(head(df))
print(tail(df))

# str => structure of df
print(str(df))

# print all the columns in the df
print(names(df))

# change  the column names
names(df) = c("Age", "Workclass", "FinalWeight", "Education", "EducationNum", "MaritalStatus", "Occupation", "Relationship", "Race", "Gender", "CapitalGain", "CapitalLoss", "Hours", "Country", "Income")

# convert categorical columns to numeric
df$Income = factor(df$Income, levels = c(' <=50K', ' >50K'), labels = c(1, 2))
df$Income = as.numeric(df$Income)

df$Workclass = as.numeric(df$Workclass)
df$Education = as.numeric(df$Education)
df$MaritalStatus = as.numeric(df$MaritalStatus)
df$Occupation = as.numeric(df$Occupation)
df$Relationship = as.numeric(df$Relationship)
df$Race = as.numeric(df$Race)
df$Gender = as.numeric(df$Gender)
df$Country = as.numeric(df$Country)

# library(caret)
# dummyVars(df)

library(psych)
# pairs(df)
# pairs.panels(df)
# panels(df)

