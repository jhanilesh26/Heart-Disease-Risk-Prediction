from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model_path = 'model/heart.pkl'  # Update this path as per your directory structure
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        # Prepare input features for prediction
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Make the prediction
        prediction = model.predict(features)

        # Generate the result message
        if prediction[0] == 1:
            result_message = "The patient has heart disease."
        else:
            result_message = "The patient does not have heart disease."

        # Redirect to the result page with the message
        return redirect(url_for('show_result', message=result_message))

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/result')
def show_result():
    # Display the result message on the predict.html page
    message = request.args.get('message', 'No result available.')
    return render_template('predict.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
