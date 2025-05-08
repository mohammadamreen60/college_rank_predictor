from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('college_model.pkl')
encoder = joblib.load('label_encoder.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    rank = int(request.form['rank'])
    prediction_code = model.predict([[rank]])[0]
    college_name = encoder.inverse_transform([prediction_code])[0]
    return render_template('result.html', name=name, college=college_name)

if __name__ == '__main__':
    app.run(debug=True)
