from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model1.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    gender = int(request.form['gender'])
    family_history = int(request.form['family_history'])
    # Add more inputs here...

    data = np.array([[age, gender, family_history]])  # Update shape according to your model
    prediction = model.predict(data)

    return f"<h2>Prediction: {'Needs Treatment' if prediction[0] == 1 else 'No Treatment Needed'}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
