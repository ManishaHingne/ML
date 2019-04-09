import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def printAccuracy(cm, type):
    total = sum(sum(cm))
    accurate = sum(np.diagonal(cm))
    accuracy = (accurate / total) * 100
    print('{} gives accuracy {:.2f}%'.format(type, accuracy))
    print('-*-' * 40)

# step 1: load the data
# df = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 1/Social_Network_Ads.csv')
# x = df.iloc[:, 2:4].values
# y = df.iloc[:, 4].values

df = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/data 1/Wine.csv')
x = df.iloc[:, 0:13].values
y = df.iloc[:, 13].values

# step 2: clean the data
from sklearn.model_selection  import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123456)

# step 3: prepare the model/formula/equation
def svmClassification():
    from sklearn.svm import SVC
    classifier = SVC()
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    # print(predictions)
    cm = confusion_matrix(y_test, predictions)
    printAccuracy(cm, 'SVM')

def randomForestClassification():
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators=50)
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    # print(predictions)
    cm = confusion_matrix(y_test, predictions)
    printAccuracy(cm, 'Random Forest')

def adaptiveBoostingClassification():
    from sklearn.ensemble import AdaBoostClassifier
    classifier = AdaBoostClassifier(n_estimators=50)
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    cm = confusion_matrix(y_test, predictions)
    printAccuracy(cm, 'Adaptive Boosting')

def gradientBoostingClassification():
    from sklearn.ensemble import GradientBoostingClassifier
    classifier = GradientBoostingClassifier(n_estimators=50)
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    cm = confusion_matrix(y_test, predictions)
    printAccuracy(cm, 'Gradient Boosting')


def xgBoostClassification():
    from xgboost import XGBClassifier
    # classifier = XGBClassifier(n_estimators=50, booster='gblinear')
    classifier = XGBClassifier(n_estimators=50, booster='gbtree')
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    cm = confusion_matrix(y_test, predictions)
    printAccuracy(cm, 'XGBoost')


svmClassification()
randomForestClassification()
adaptiveBoostingClassification()
gradientBoostingClassification()
xgBoostClassification()
