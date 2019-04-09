# prints the accuracy of the model
printAccuracy = function(cm) {
  correct.predictions = sum(diag(cm))
  total.predictions = sum(cm)
  accuracy = (correct.predictions / total.predictions) * 100
  print(accuracy)
}

# step 1: load the data
df = read.delim('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data\ 1/Restaurant_Reviews.tsv', sep='\t', quote = "\"'")

# step 2: clean the data
library(tm)
# library(SnowballC)

# get the corpus
corpus = VCorpus(VectorSource(df$Review))

# to lower

# remove all the special characters/punctuations
corpus = tm_map(corpus, removePunctuation)

# remove all the numbers
corpus = tm_map(corpus, removeNumbers)

# remove all the whitespaces
corpus = tm_map(corpus, stripWhitespace)

# stem the document
corpus = tm_map(corpus, stemDocument)

# remove the stop words
corpus = tm_map(corpus, removeWords, stopwords('english'))

# build the new df
dtm = DocumentTermMatrix(corpus)
df.new = data.frame(as.matrix(dtm))
df.new$liked = df$Liked

df.new$liked = factor(df.new$liked)

# split the data into train and test
library(caTools)
results = sample.split(df.new$liked, SplitRatio = 0.8)
df.train = df.new[results == TRUE, ]
df.test = df.new[results == FALSE, ]


# NB
library(e1071)
classifier = naiveBayes(liked ~ ., data = df.train)
predictions = predict(classifier, newdata = df.test)
printAccuracy(table(df.test$liked, predictions))

# SVM
classifier = svm(liked ~ ., data = df.train)
predictions = predict(classifier, newdata = df.test)
printAccuracy(table(df.test$liked, predictions))

# DT
library(rpart)
classifier = rpart(liked ~ ., data = df.train)
predictions = predict(classifier, newdata = df.test, type='class')
printAccuracy(table(df.test$liked, predictions))

# RF
library(randomForest)
classifier = randomForest(liked ~ ., data = df.train)
predictions = predict(classifier, newdata = df.test)
printAccuracy(table(df.test$liked, predictions))

