age = 12
gender = 1
strand = 0
admissionScore = 90
status = 1
gradeGWA = 1
oldProgram = 1

#Run here recommend program
#import libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#read the dataset
DATA_CSV_FILE = pd.read_csv('data-set-shifter.csv')
#preparing data for training and testing
X = pd.DataFrame(np.c_[DATA_CSV_FILE['AGE'],DATA_CSV_FILE['GENDER'], DATA_CSV_FILE['STRAND'], DATA_CSV_FILE['ADMISSION_TEST'], DATA_CSV_FILE['STATUS'], DATA_CSV_FILE['GRADE'], DATA_CSV_FILE['OLD_PROGRAM'], ], columns=['AGE','GENDER','STRAND','ADMISSION_TEST','STATUS','GRADE','OLD_PROGRAM'])
y = DATA_CSV_FILE['NEW_PROGRAM']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#use decision tree classifier
clf = DecisionTreeClassifier()
#fit the model
clf.fit(X_train, y_train)
#accuracy of the model
print(clf.score(X_test, y_test))
#predict the input
example_input = [[age, gender, strand, admissionScore, status, gradeGWA, oldProgram], [age, gender, strand, admissionScore, status, gradeGWA, oldProgram]]

predict = clf.predict(example_input)
recommendedProgram = predict[0]
print(predict)