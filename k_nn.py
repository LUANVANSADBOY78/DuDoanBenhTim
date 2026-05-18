import csv
import numpy as np
import math
import pandas as pd

from sklearn.model_selection import train_test_split

data = pd.read_csv("heart.csv")
y = data['target']
X = data.drop('target', axis=1)

#print(data.head(10))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)