import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

DATA_CSV_FILE = pd.read_csv('sample_data_first-year.csv')


#Preparing Data for training and testing
X = pd.DataFrame(np.c_[DATA_CSV_FILE['TEST'],DATA_CSV_FILE['IT102'], DATA_CSV_FILE['PE10'], DATA_CSV_FILE['NSTP10'],DATA_CSV_FILE['STS101']], columns=['TEST','IT102','PE10','NSTP10', 'STS101'])
y = DATA_CSV_FILE['PROGRAM']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X)

clf = DecisionTreeClassifier()

clf.fit(X_train, y_train)

#Accuracy of the model
print(clf.score(X_test, y_test))

#Predict Sample input

example_input = [[90,1,1.5,1.25,2],[80,1,1,1,1]]
predict = clf.predict(example_input)
print(predict)