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
DATA_CSV_FILE = pd.read_csv('data-set-bsit.csv')
#preparing data for training and testing
subjects_df = pd.DataFrame(np.c_[DATA_CSV_FILE['IT105'],DATA_CSV_FILE['IT106'], DATA_CSV_FILE['IT107'], DATA_CSV_FILE['PCM101'], DATA_CSV_FILE['MMW101'], DATA_CSV_FILE['UTS101'], DATA_CSV_FILE['PE11'], DATA_CSV_FILE['NSTP11']], columns=['IT105','IT106','IT107','PCM101','MMW101','UTS101','PE11','NSTP11'])

subjectMean = []
subjectTitle = []

subjectDictionary = {}

for subject in subjects_df:
    # print(subject)
    subjectTitle.append(str(subject))
    subjectMean.append(subjects_df[str(subject)].mean())
    subjectDictionary[str(subject)] = subjects_df[str(subject)].mean()

max_value = max(subjectMean)
min_index = subjectMean.index(max_value)

# print(subjectTitle[min_index])

sort_subjects = sorted(subjectDictionary.items(), key=lambda x: x[1], reverse=True)

firstThreeSubjects = []
counter = 0
print()
for key in sort_subjects:
    if counter == 3:
        break
    firstThreeSubjects.append(key[0])
    counter+=1

print(str(firstThreeSubjects))