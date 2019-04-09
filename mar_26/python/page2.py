import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def accuracy(cm):
    # calculate the total
    # total = 0
    # for row in cm:
    #     for value in row:
    #         total += value
    #
    # calculate the diagonal
    # accurate

    total = cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1]
    accurate = cm[0][0] + cm[1][1]
    accuracyPercent = (accurate / total) * 100
    print('accuracy: {}%'.format(accuracyPercent))

# step 1: load the data
df = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 1/Social_Network_Ads.csv')
x = df.iloc[:, 2:4].values
y = df.iloc[:, 4].values

# step 2: clean the data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# step 3: prepare the model/formula/equation
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier = classifier.fit(x_train, y_train)

# step 4: predict the value(s)
predictions = classifier.predict(x_test)
# print(predictions)


# step 5: test the result
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, predictions)
accuracy(cm)

# testing  real records
df_real = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 1/Social_Network_Ads_1.csv')
x = df_real.iloc[:, 2:4].values
predictions_real = classifier.predict(x)
print(predictions_real)

predictions_real_2 = classifier.predict(np.array([[60, 40000]]))
print(predictions_real_2)

# step 6: visualize the result
