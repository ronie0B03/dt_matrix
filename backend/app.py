from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods = ['GET'])
def get_articles():
    #Run h
    return jsonify({"Hello":"World"})

#Set the recommended program here
recommendedProgram = "NA"

@app.route('/recommend-program', methods = ['GET', 'POST'])
def recommend_program():
    if request.method == 'POST':
        gwa = request.form.get('gwa')
        strand = request.form.get('strand')
        admissionScore = request.form.get('admissionScore')
        #Run here recommend program
        #import libraries
        import numpy as np
        import pandas as pd
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.model_selection import train_test_split
        from sklearn.tree import DecisionTreeClassifier
        #read the dataset
        DATA_CSV_FILE = pd.read_csv('data-set-shs.csv')
        #preparing data for training and testing
        X = pd.DataFrame(np.c_[DATA_CSV_FILE['GWA'],DATA_CSV_FILE['STRAND'], DATA_CSV_FILE['ADMISSION_SCORE']], columns=['GWA','STRAND','ADMISSION_SCORE'])
        y = DATA_CSV_FILE['PROGRAM']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        #use decision tree classifier
        clf = DecisionTreeClassifier()
        #fit the model
        clf.fit(X_train, y_train)
        #accuracy of the model
        print(clf.score(X_test, y_test))
        #predict the input
        example_input = [[gwa,strand, admissionScore],[gwa,strand, admissionScore]]

        predict = clf.predict(example_input)
        recommendedProgram = predict[0]
        print(predict)

        return jsonify({"program":recommendedProgram})
    else:
        return jsonify({"program: ":'Please submit the fields first.'})

@app.route('/recommend-shift-program', methods = ['GET', 'POST'])
def recommend_shift_program():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        gender = int(request.form.get('gender'))
        strand = int(request.form.get('strand'))
        admissionScore = int(request.form.get('admissionScore'))
        status = int(request.form.get('status'))
        gradeGWA = int(request.form.get('gradeGWA'))
        currentProgram = int(request.form.get('currentProgram'))

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
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
        #use decision tree classifier
        clf = DecisionTreeClassifier()
        #fit the model
        clf.fit(X_train, y_train)
        #accuracy of the model
        print(clf.score(X_test, y_test))
        #predict the input
        example_input = [[age, gender, strand, admissionScore, status, gradeGWA, currentProgram],[age, gender, strand, admissionScore, status, gradeGWA, currentProgram]]

        predict = clf.predict(example_input)
        recommendedProgram = int(predict[0])
        print(predict)

        return jsonify({"program": recommendedProgram})
    else:
        return jsonify({"Recommended Program: ":'Please submit the fields first.'})


@app.route('/check-subject-hard-time', methods = ['GET', 'POST'])
def check_subject_hard_time():
    if request.method == 'POST':
        program = int(request.form.get('program'))
        #import libraries
        import numpy as np
        import pandas as pd
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.model_selection import train_test_split
        from sklearn.tree import DecisionTreeClassifier
        #read the dataset
        if program == 0:
            DATA_CSV_FILE = pd.read_csv('data-set-bsit.csv')
            #preparing data for training and testing
            subjects_df = pd.DataFrame(np.c_[DATA_CSV_FILE['IT105'],DATA_CSV_FILE['IT106'], DATA_CSV_FILE['IT107'], DATA_CSV_FILE['PCM101'], DATA_CSV_FILE['MMW101'], DATA_CSV_FILE['UTS101'], DATA_CSV_FILE['PE11'], DATA_CSV_FILE['NSTP11']], columns=['IT105','IT106','IT107','PCM101','MMW101','UTS101','PE11','NSTP11'])
        elif program == 1:
            DATA_CSV_FILE = pd.read_csv('data-set-beed.csv')
            #preparing data for training and testing
            subjects_df = pd.DataFrame(np.c_[DATA_CSV_FILE['MMW101'],DATA_CSV_FILE['RPH101'], DATA_CSV_FILE['AAP101'], DATA_CSV_FILE['DRAW102'], DATA_CSV_FILE['ARP101'], DATA_CSV_FILE['PE10'], DATA_CSV_FILE['NSTP10']], columns=['MMW101','RPH101','AAP101','DRAW102','ARP101','PE10','NSTP10'])
        elif program == 2:
            DATA_CSV_FILE = pd.read_csv('data-set-foods.csv')
            #preparing data for training and testing
            subjects_df = pd.DataFrame(np.c_[DATA_CSV_FILE['UTS101'],DATA_CSV_FILE['PAL101'], DATA_CSV_FILE['STS101'], DATA_CSV_FILE['PCM101'], DATA_CSV_FILE['IIT102'], DATA_CSV_FILE['ID103'], DATA_CSV_FILE['F102'], DATA_CSV_FILE['FC103'], DATA_CSV_FILE['PE10'], DATA_CSV_FILE['NSTP10'], DATA_CSV_FILE['MST101A']], columns=['UTS101','PAL101','STS101','PCM101','IIT102','ID103','F102','FC103','PE10','NSTP10','MST101A'])             
        elif program == 3:
            DATA_CSV_FILE = pd.read_csv('data-set-bafm.csv')
            #preparing data for training and testing
            subjects_df = pd.DataFrame(np.c_[DATA_CSV_FILE['PCM101'],DATA_CSV_FILE['MMW101'], DATA_CSV_FILE['UTS101'], DATA_CSV_FILE['ELEC102'], DATA_CSV_FILE['ARP101'], DATA_CSV_FILE['SMP102'], DATA_CSV_FILE['BC102'], DATA_CSV_FILE['PE10'], DATA_CSV_FILE['NSTP10']], columns=['PCM101','MMW101','UTS101','ELEC102','ARP101','SMP102','BC102','PE10','NSTP10'])
        elif program == 4:
            DATA_CSV_FILE = pd.read_csv('data-set-coe.csv')
            #preparing data for training and testing
            subjects_df = pd.DataFrame(np.c_[DATA_CSV_FILE['MMW101'],DATA_CSV_FILE['UTS101'], DATA_CSV_FILE['PCM101'], DATA_CSV_FILE['COE102'], DATA_CSV_FILE['COE103'], DATA_CSV_FILE['COE103L'], DATA_CSV_FILE['CPE102L'], DATA_CSV_FILE['CPE103'], DATA_CSV_FILE['PE10'], DATA_CSV_FILE['NSTP10']], columns=['MMW101','UTS101','PCM101','COE102','COE103','COE103L','CPE102L','CPE103','PE10','NSTP10'])   
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
        firstThreeSubjectsToString = ", ".join(map(str, firstThreeSubjects))
        return jsonify({"subjects": firstThreeSubjectsToString})
    else:
        return jsonify({"Recommended Program: ":'Please submit the fields first.'})

if __name__ == "__main__":
    app.run(debug=True)