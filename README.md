Mental Health Prediction App

This project is a Machine Learning and Flask based web application that predicts whether a person is likely to need mental health treatment based on personal and workplace-related factors.

Project Overview
Mental health is just as important as physical health. This project aims to provide a basic system that helps raise awareness by predicting the need for mental health support using real-world survey data.

Features

Takes input on Age, Gender, Family History, Work Interference, and more.
Predicts if the user should seek mental health treatment.
Displays results instantly on a user-friendly web interface.
Trained using a Random Forest Classifier with high accuracy on selected features.
Tech Stack

Python for programming
Pandas and NumPy for data cleaning and manipulation
Scikit-learn for model training
Jupyter Notebook for development and visualization
Flask for deploying the web app
HTML/CSS for the frontend
Machine Learning Workflow

Data Preprocessing
Encoded categorical variables using LabelEncoder
Handled missing values and cleaned dataset
Feature Selection
Identified most important features using Random Forest feature importance
Model Training
Trained using RandomForestClassifier
Evaluated using train-test split and accuracy score
Web Deployment
Built a Flask app with a web form
Integrated the ML model for real-time prediction
How to Run Locally

Clone the repository
Install the required libraries using pip
Run the Flask app
Open http://127.0.0.1:5000 in your browser
Folder Structure

app.py → Flask Web App
model.pkl → Trained Machine Learning model
template/index.html → Web UI
mental_health_model.ipynb → Jupyter Notebook for EDA and training
README.md → Project description
