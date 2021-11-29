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
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
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

if __name__ == "__main__":
    app.run(debug=True)