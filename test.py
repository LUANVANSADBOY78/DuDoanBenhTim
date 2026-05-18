import csv
import numpy as np
import math
import pandas as pd

from sklearn.model_selection import train_test_split

data = pd.read_csv("heart.csv")
y = data['target']
X = data.drop('target', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# sử dụng Euclidean tính khoảng cách 2 điểm
def calcDistancs(pointA, pointB, numOfFeature=4):
    tmp = 0
    for i in range(numOfFeature):
        tmp += (float(pointA[i]) - float(pointB[i])) ** 2
    return math.sqrt(tmp)


# tính khoảng cách giữa điểm truyền vào với những điểm trong tập dữ liệu ban đầu.
def kNearestNeighbor(trainSet, point, k):
    distances = []
    for item in trainSet:
        distances.append({
            "label": item[-1],
            "value": calcDistancs(item, point)
        })
    distances.sort(key=lambda x: x["value"])
    labels = [item["label"] for item in distances]
    return labels[:k]

#  tìm và trả về nhãn xuất hiện nhiều nhất trong một danh sách các nhãn.
def findMostOccur(arr):
    labels = set(arr)  # set label
    ans = ""
    maxOccur = 0
    for label in labels:
        num = arr.count(label)
        if num > maxOccur:
            maxOccur = num
            ans = label
    return ans


def test(trainSet, testSet, k):
    correct_predictions = 0
    for point in testSet:
        predicted_label = findMostOccur(kNearestNeighbor(trainSet, point, k))
        if predicted_label == point[-1]:
            correct_predictions += 1
    accuracy = correct_predictions / len(testSet)
    return accuracy


trainSet = np.column_stack((X_train, y_train))
testSet = np.column_stack((X_test, y_test))
k = 3
accuracy = test(trainSet, testSet, k)

# In kết quả đánh giá hiệu suất của mô hình
print("Accuracy:", 100*accuracy)
test_data = [
    [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1],
    [1, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1],

]

def predict_target(test_data, trainSet, k):
    predictions = []
    for point in test_data:
        predicted_label = findMostOccur(kNearestNeighbor(trainSet, point, k))
        predictions.append(predicted_label)
    return predictions


# Predict targets for the test data
predicted_targets = predict_target(test_data, trainSet, k)
# Print the predicted targets
for i, target in enumerate(predicted_targets, start=1):
    print(f"Test {i}: Predicted Target: {target}")
