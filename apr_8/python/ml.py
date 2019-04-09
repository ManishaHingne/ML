import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def preprocessData(file):
    # step 1: load the data
    df = pd.read_csv(file, header=None)
    x = df.iloc[:, [0, 4, 5, 7, 9, 10, 11, 12]].values
    y = df.iloc[:, 14].values

    # step 2: clean the data
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()

    # marital status
    x[:, 2] = encoder.fit_transform(x[:, 2])

    # relationship:
    x[:, 3] = encoder.fit_transform(x[:, 3])

    # sex
    x[:, 4] = encoder.fit_transform(x[:, 4])

    # income
    y[:] = encoder.fit_transform(y[:])

    # change the data types of x, y  from list of objects to list int64
    x = np.array(x, dtype=np.int64)
    y = np.array(y, dtype=np.int64)

    return x, y


# step 3: prepare the model/formula/equation
def crossValidateData(classifier):
    x_test, y_test = preprocessData('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 4/adult.test')

    from sklearn.metrics import confusion_matrix

    predictions = classifier.predict(x_test)
    cm = confusion_matrix(y_test, predictions)

    total = sum(sum(cm))
    accurate = sum(np.diagonal(cm))
    accuracy = (accurate / total) * 100
    return accuracy


def nbClassifier(x_train, y_train):
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier = classifier.fit(x_train, y_train)
    return classifier

def dtClassifier(x_train, y_train):
    from sklearn.tree import DecisionTreeClassifier
    classifier = DecisionTreeClassifier()
    classifier = classifier.fit(x_train, y_train)
    return classifier

def rfClassifier(x_train, y_train):
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier()
    classifier = classifier.fit(x_train, y_train)
    return classifier

def xgClassifier(x_train, y_train):
    from xgboost import XGBClassifier
    classifier = XGBClassifier()
    classifier = classifier.fit(x_train, y_train)
    return classifier

x_train, y_train = preprocessData('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 4/adult.data')

classifierNB = nbClassifier(x_train, y_train)
classifierDT = dtClassifier(x_train, y_train)
classifierRF = rfClassifier(x_train, y_train)
classifierXG = xgClassifier(x_train, y_train)
