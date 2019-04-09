from flask import Flask, render_template, request
import ml

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predictIncome():

    algorithm = request.form.get('algorithm')
    if algorithm == 'nb':
        classifier = ml.classifierNB
        algorithm = 'Naive Bayes'
    elif algorithm == 'dt':
        classifier = ml.classifierDT
        algorithm = 'Decision Tree'
    elif algorithm == 'rf':
        classifier = ml.classifierRF
        algorithm = 'Random Forest'
    elif algorithm == 'xg':
        classifier = ml.classifierXG
        algorithm = 'Extreme Boost'

    age = int(request.form.get('age'))
    educationNum = int(request.form.get('educationNum'))
    mstatus = int(request.form.get('mstatus'))
    relationship = int(request.form.get('relationship'))
    gender = int(request.form.get('gender'))
    gain = int(request.form.get('gain'))
    loss = int(request.form.get('loss'))
    hours = int(request.form.get('hours'))

    accuracy = ml.crossValidateData(classifier)

    prediction = classifier.predict([[age, educationNum, mstatus, relationship, gender, gain, loss, hours]])

    if prediction[0] == 0:
        prediction = 'will be less than or equal to $50K :('
    else:
        prediction = 'will be more than $50K :)'

    return render_template('result.html', algorithm=algorithm, prediction=prediction, accuracy=accuracy)


app.run(host='0.0.0.0', port=5000)
