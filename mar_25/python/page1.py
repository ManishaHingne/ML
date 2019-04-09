import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# step 1: load the data
df = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 1/Social_Network_Ads.csv')
x = df.iloc[:, 2:4].values
y = df.iloc[:, 4].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# step 2: clean the data

# step 3: prepare the model/formula/equation
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(x_train, y_train)

# step 4: predict the value(s)
predictions = regressor.predict(x_test)

for index in range(len(predictions)):
    if predictions[index] >= 0.5:
        predictions[index] = 1
    else:
        predictions[index] = 0

predictions = np.array(predictions, dtype=np.int16)
print(predictions)

# step 5: test the result
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, predictions)
correct_predictions = cm[0][0] + cm[1][1]
total_predictions = cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1]
accuracy = (correct_predictions / total_predictions) * 100
print('accuracy: {}'.format(accuracy))

# step 6: visualize the result


















