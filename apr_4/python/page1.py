import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def printAccuracy(cm):
    total = sum(sum(cm))
    accurate = sum(np.diagonal(cm))
    accuracy = (accurate / total) * 100
    print('accuracy: {}%'.format(accuracy))


# step 1: load the data
df = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 1/Churn_Modelling.csv')
x = df.iloc[:, 3:13].values
y = df.iloc[:, 13].values

# step 2: clean the data
from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()

# convert Geography to numeric
x[:, 1] = labelEncoder.fit_transform(x[:, 1])

# convert Gender to numeric
x[:, 2] = labelEncoder.fit_transform(x[:, 2])

# add dummy columns
from sklearn.preprocessing import OneHotEncoder
# add dummy columns for the Gender (having index = 2)
# oneHotEncoder = OneHotEncoder(categorical_features=[2])
# x = oneHotEncoder.fit_transform(x)
# recordNo      Gender0     Gender1
# 0             1           0
# 1             1           0
# 2             1           0
# 3             1           0
# 4             1           0
# 5             0           1
# 6             0           1
# 7             1           0

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# step 3: prepare the model/formula/equation
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100)
classifier = classifier.fit(x_train, y_train)

# step 4: predict the value(s)
predictions = classifier.predict(x_test)
print(predictions)

# step 5: test the result
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, predictions)
printAccuracy(cm)

# step 6: visualize the result
