import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# step 1: load the data
df = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 1/Social_Network_Ads.csv')
x = df.iloc[:, 2:4].values
y = df.iloc[:, 4].values

# step 2: clean the data

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=343238)

# step 3: prepare the model/formula/equation
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier = classifier.fit(x_train, y_train)

# step 4: predict the value(s)
predictions = classifier.predict(x_test)
print(predictions)

# step 5: test the result
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, predictions)
print(cm)


# step 6: visualize the result