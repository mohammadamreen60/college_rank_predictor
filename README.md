# college_rank_predictor
This college predictor application predicts college according to the marks or entrance marks of a student. The app is implemented with Flask, and implelment a ML model to predict the item.
Project: College Predictor
This project aims to predict the most suitable college for a student based on their academic data (e.g., marks, entrance exam scores). The web app is built using Flask and integrates a trained machine learning model to provide predictions.

File Descriptions:
app.py: This is the main Flask app that runs the web server and handles HTTP requests. It loads the trained model (college_model.pkl) and label encoder (label_encoder.pkl), processes user inputs through the web form, makes predictions using the trained model, and renders the result on the result.html page.

train_model.py: This script is responsible for training the machine learning model. It reads data from the college_cutoff_data.csv file, processes it, and trains a model (likely using algorithms like Random Forest, SVM, etc.). The trained model and label encoder are then saved as college_model.pkl and label_encoder.pkl for later use in the Flask app.

college_model.pkl: This is the trained machine learning model, which is used to make predictions in the app. It is generated from running train_model.py and contains the final model after training on the dataset.

label_encoder.pkl: This file contains the label encoder that encodes categorical variables (like college names) into numeric values. It ensures consistency when making predictions after the model is deployed.

college_cutoff_data.csv: A CSV file that contains historical data about college cutoff scores for various courses. This data is used to train the model and to inform predictions about which colleges a student might get into based on their academic data.

put index.html and result.html in templates folder

index.html: The main webpage that serves as an input form where users can enter their academic data, such as marks and exam scores, to make a prediction.
result.html: This page displays the prediction result to the user, showing which college they are most likely to be admitted to based on the provided data.

