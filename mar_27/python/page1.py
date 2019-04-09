import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# step 1: load the data
df = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 1/Social_Network_Ads.csv')
x = df.iloc[:, 2:4].values
y = df.iloc[:, 4].values

# step 2: clean the data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# print(df.iloc[:, 2].values)
# print(df.iloc[:, 3].values)

def testKNN():
    from sklearn.neighbors import KNeighborsClassifier
    classifier = KNeighborsClassifier(n_neighbors=33)
    classifier = classifier.fit(x_train, y_train)

    predictions = classifier.predict(x_test)

    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, predictions)
    accurate_values = sum(np.diagonal(cm))
    total_values = sum(sum(cm))
    accuracy = (accurate_values / total_values) * 100
    print('accuracy: {}%'.format(accuracy))

# testKNN()

def testSVR():
    from sklearn.svm import  SVR
    regressor = SVR()
    regressor = regressor.fit(x_train, y_train)
    predictions_reg = regressor.predict(x_test)
    print(predictions_reg)


def testSVC():
    from sklearn.svm import SVC
    classifier = SVC(gamma=0.5, kernel='linear')
    # classifier = SVC(gamma=0.5)
    classifier = classifier.fit(x_train, y_train)

    predictions = classifier.predict(x_test)

    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, predictions)
    accurate_values = sum(np.diagonal(cm))
    total_values = sum(sum(cm))
    accuracy = (accurate_values / total_values) * 100
    print('accuracy: {}%'.format(accuracy))

    x_coord = df.iloc[:, 2].values
    y_coord = df.iloc[:, 3].values

    predictions_all = classifier.predict(x)

    colors = []
    for value in predictions_all:
        if value == 0:
            colors.append('red')
        else:
            colors.append('green')

    # colors = ['red' if value == 0 else 'green' for value in predictions_all]

    plt.scatter(x_coord, y_coord, c=colors)
    plt.show()

testSVC()
testSVR()












