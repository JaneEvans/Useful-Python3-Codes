#!/bin/python3

import sys

def predictOfficePrice(_trainList, _testList, _F):
	import numpy as np
	train = np.array(_trainList)
	trainData = train[: , 0:_F]
	trainValue = train[:, _F]
	testData = np.array(_testList)

	from sklearn.preprocessing import PolynomialFeatures
	from sklearn import linear_model
	poly = PolynomialFeatures(degree = 3)
	trainData_ = poly.fit_transform(trainData)
	testData_ = poly.fit_transform(testData)

	clf = linear_model.LinearRegression()
	clf.fit(trainData_, trainValue)

	return clf.predict(testData_)

_data = []
trainList = []
testList = []

F, N = input().strip().split(" ") # F is the number of observed features.
F, N = int(F), int(N)  # N is the train sample size
for i in range(N):
    rowData = input().strip()
    _data=rowData.split(" ")
    trainList.append(list(map(float,_data)))

M = int(input())  # M is the test sample size
for i in range(M):
    rowData = input().strip()
    _data=rowData.split(" ")
    testList.append(list(map(float,_data)))

for testValue in predictOfficePrice(trainList, testList, F):
    print(round(testValue, 2))

