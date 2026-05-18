from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from your_module import kNearestNeighbor, findMostOccur

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    values = [float(request.form[f'input_{i}']) for i in range(1, 14)]

    # Load and preprocess data
    data = pd.read_csv("heart.csv")
    y = data['target']
    X = data.drop('target', axis=1)

    # Split data into train and test sets
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2)

    # Convert input values to numpy array
    point = np.array(values)

    # Run k-Nearest Neighbors algorithm
    predicted_label = findMostOccur(
        kNearestNeighbor(X_train.values, point, k=3))

    return render_template('result.html', predicted_label=predicted_label)


if __name__ == '__main__':
    app.run(debug=True)
