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
# print(x)

# step 2: clean the data
from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()

# convert Geography to numeric
x[:, 1] = labelEncoder.fit_transform(x[:, 1])

# convert Gender to numeric
x[:, 2] = labelEncoder.fit_transform(x[:, 2])


# pip3 install tensorflow
# pip3 install theona
# pip3 install keras

def NN(epochs):
    from keras.models import Sequential
    from keras.layers import Dense

    # container
    classifier = Sequential()

    # add input layer
    classifier.add(Dense(units=16, input_shape=(10, ), activation='relu'))

    # add hidden layer
    classifier.add(Dense(units=10, activation='linear'))

    classifier.add(Dense(units=3, activation='sigmoid'))

    # add output layer
    classifier.add(Dense(units=1, activation='sigmoid'))

    # compile the container
    classifier.compile(optimizer='adam', loss='mean_squared_error')


    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    classifier.fit(x_train, y_train, epochs=epochs)

    # predictions = classifier.predict(x_test)
    # print(predictions)
    #
    # from sklearn.metrics import confusion_matrix
    # cm = confusion_matrix(y_test, predictions)
    # printAccuracy(cm)
    # #       0       1
    # #   0   10      0
    # #   1   5       20
    #
    # print('-' * 30)

    # actual values
    customer = [[450, 0, 1, 30, 1, 0, 1, 0, 1, 50000]]
    prediction = classifier.predict(np.array(customer))
    print(prediction)
    print('-' * 100)

NN(5)
NN(10)
NN(15)
NN(20)

