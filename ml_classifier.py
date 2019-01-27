from collections import Counter
import pandas as pd
import numpy as np
from sklearn import svm, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
import preprocessing

def do_ml(ticker):
    X, y, df = preprocessing.extract_featuresets(ticker)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    #clf = neighbors.KNeighborsClassifier()
    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])

    clf.fit(X_train, y_train)

    confidence = clf.score(X_test, y_test)
    print('Accuracy: ', confidence)
    predictions = clf.predict(X_test)
    print('Predicted spread: ', Counter(predictions))

    return confidence

do_ml('AAPL')
