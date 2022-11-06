import numpy
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score

# carico il dataset con path passato come stringa
def importdata(dataset):
    balance_data = pd.read_csv(dataset, sep=',', header=None)
    return balance_data


# genero il train set dal dataset importato
def set_training(balance_data, test):
    X = balance_data.values[:, 0:5]
    Y = balance_data.values[:, 5]

    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.000001, random_state=0)

    X_test = test

    return X, Y, X_train, X_test, y_train, y_test

# addestro il classificatore usando come parametro di split l'entropia
def train_using_entropy(X_train, y_train):
    clf_entropy = DecisionTreeRegressor(
        criterion="friedman_mse", random_state=0,
        max_depth=4, max_features='sqrt', min_samples_split=5)
    clf_entropy.fit(X_train, y_train)
    return clf_entropy

# effettuo la predizione della feature target
def prediction(X_test, clf_object):
    y_pred = clf_object.predict(X_test)
    return y_pred

# richiamo la pipeline del classificatore
def classify(test, dataset):
    data = importdata(dataset)
    X, Y, X_train, X_test, y_train, y_test = set_training(data, test)
    clf_entropy = train_using_entropy(X_train, y_train)
    y_pred = prediction(X_test, clf_entropy)
    predict = numpy.round(y_pred, 0)
    return int(predict)

def cross_validation():
    data = importdata("DataSet.csv")
    X = data.values[:, 0:5]
    Y = data.values[:, 5]

    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.000001, random_state=0)

    clf = DecisionTreeRegressor(
        criterion="friedman_mse", random_state=0,
        max_depth=4, max_features='sqrt', min_samples_split=5)

    score = cross_val_score(clf, X_train, y_train, cv=5)
    accurancy = numpy.round(score.mean(),2)
    deviation = numpy.round(score.std(),2)
    print("Risultati cross validation:\nAccurancy: " + str(accurancy) + "\nDeviation: " + str(deviation))

def metrix_test():
    data = importdata("DataSet.csv")
    X = data.values[:, 0:5]
    Y = data.values[:, 5]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

    clf = DecisionTreeRegressor(
        criterion="friedman_mse", random_state=0,
        max_depth=4, max_features='sqrt', min_samples_split=5)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test, clf)

    mean = numpy.round(mean_squared_error(y_test, y_pred), 2)
    score = numpy.round(r2_score(y_test, y_pred), 2)
    print("Risultati delle metriche:\nMean squared error: " + str(mean) + "\nr-quadro score: " + str(score))

def test():
    print("-----------Test classificatore-----------")
    cross_validation()
    metrix_test()
    print("---------------------------------------- ")