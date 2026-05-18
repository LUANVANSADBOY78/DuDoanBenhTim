from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import views, status

import math
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from django.utils.html import format_html

from DuDoanBenhTim.helpers import custom_response, parse_request

data = pd.read_csv("heart.csv")
y = data['target']
X = data.drop('target', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
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


def predict_target(test_data, trainSet, k):

    predictions = []
    for point in test_data:
        predicted_label = findMostOccur(kNearestNeighbor(trainSet, point, k))
        predictions.append(predicted_label)
# Đối với mỗi điểm dữ liệu, sử dụng hàm kNearestNeighbor để tìm các nhãn của các điểm lân cận gần nhất trong tập huấn luyện.
# Tiếp theo, sử dụng hàm findMostOccur để xác định nhãn xuất hiện nhiều nhất trong các nhãn này.
# Nhãn dự đoán được thêm vào danh sách predictions.
# Cuối cùng, danh sách predictions chứa các nhãn dự đoán cho từng điểm dữ liệu trong test_data, và nó được trả về từ hàm.
    return predictions


# Predict targets for the test data
# Print the predicted targets
class HeartAPIView(views.APIView):
    def post(self, request):
        data = parse_request(request)
        # data = request.POST.dict()  # Get form data as dictionary
        keys = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# Use list comprehension to construct point list
        point = [data.get(key, 0) for key in keys]
        test_data = [
            point,
        ]
        predicted_targets = predict_target(test_data, trainSet,  k)

        result = 0
        content = ""
        for i, target in enumerate(predicted_targets, start=1):
            result = target

        return custom_response('Successfully!', 'Success', result, 201)


def submit_form(request):
    if request.method == 'POST':
        data = request.POST.dict()  # Get form data as dictionary
        keys = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# Use list comprehension to construct point list
        point = [data.get(key, 0) for key in keys]
        test_data = [
            point,
        ]
        predicted_targets = predict_target(test_data, trainSet,  k)

        result = 0
        content = ""
        for i, target in enumerate(predicted_targets, start=1):
            result = target
        return JsonResponse({'message': result})
    else:
        # Handle GET requests or other methods if needed
        return JsonResponse({'error': 'Only POST requests are allowed'})

    # if request.method == 'POST':
    #     # Get input data from the form
    #     age = int(request.POST.get('age'))
    #     sex = int(request.POST.get('sex'))
    #     cp = int(request.POST.get('cp'))
    #     trestbps = int(request.POST.get('trestbps'))
    #     chol = int(request.POST.get('chol'))
    #     fbs = int(request.POST.get('fbs'))
    #     restecg = int(request.POST.get('restecg'))
    #     thalach = int(request.POST.get('thalach'))
    #     exang = int(request.POST.get('exang'))
    #     oldpeak = float(request.POST.get('oldpeak'))
    #     slope = int(request.POST.get('slope'))
    #     ca = int(request.POST.get('ca'))
    #     thal = int(request.POST.get('thal'))

    #     # Predict the target value using KNN
    #     point = [age, sex, cp, trestbps, chol, fbs, restecg,
    #              thalach, exang, oldpeak, slope, ca, thal]
    #     test_data = [
    #         point,
    #     ]
    #     predicted_targets = predict_target(test_data, trainSet,  k)

    #     result = 0
    #     content = ""
    #     for i, target in enumerate(predicted_targets, start=1):
    #         result = target
    #     if result == 0:
    #         content = "Hông có chi"
    #     else:
    #         content = "Bạn sắp tèo @@"
    #     html_response = format_html(
    #         "<h1>Kết quả khám nghiệm: {}</h1>", content)

    #     # Return the predicted target value as the HTTP response
    #     return HttpResponse(html_response)
    # else:
    #     return HttpResponse("Invalid request method.")


def home(request):
    return render(request, 'home.html')
