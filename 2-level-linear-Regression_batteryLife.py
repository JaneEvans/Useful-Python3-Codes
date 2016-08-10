def batterLife_chargeLessThen4(chargeTime):    
    import numpy as np
    trainDataArr = np.genfromtxt("trainingdata_batteryLife.txt", delimiter = ",")
    trainDataArr = trainDataArr[trainDataArr[ :,0] <= 4]
    trainData = trainDataArr[:, 0]
    trainData = trainData.reshape(-1,1)
    trainValue = trainDataArr[:,1]
    testData = np.array(chargeTime)
    testData = testData.reshape(-1,1)
    
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn import linear_model
    
    # Plot outputs
    import matplotlib.pyplot as plt
    plt.scatter(trainData, trainValue,  color='black')
    plt.xticks(())
    plt.yticks(())
    plt.show()

    # Fit regression model
    poly = PolynomialFeatures(degree = 1)
    trainData_ = poly.fit_transform(trainData)
    testData_ = poly.fit_transform(testData)
    
    clf = linear_model.LinearRegression()
    clf.fit(trainData_, trainValue)
    return clf.predict(testData_)

def batterLife_chargeMoreThan4(chargeTime):    
    import numpy as np
    trainDataArr = np.genfromtxt("trainingdata_batteryLife.txt", delimiter = ",")
    trainDataArr = trainDataArr[trainDataArr[ :,0] > 4]
    trainData = trainDataArr[:, 0]
    trainData = trainData.reshape(-1,1)
    trainValue = trainDataArr[:,1]
    testData = np.array(chargeTime)
    testData = testData.reshape(-1,1)
    
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn import linear_model
    
    # Plot outputs
    import matplotlib.pyplot as plt
    plt.scatter(trainData, trainValue,  color='black')
    plt.xticks(())
    plt.yticks(())
    plt.show()

    # Fit regression model
    poly = PolynomialFeatures(degree = 1)
    trainData_ = poly.fit_transform(trainData)
    testData_ = poly.fit_transform(testData)
    
    clf = linear_model.LinearRegression()
    clf.fit(trainData_, trainValue)
    return clf.predict(testData_)

#!/bin/python3

#import sys
# chargeTime = float(input().strip())

chargeTime = 5
if chargeTime <= 4:
    batterLifePredict = batterLife_chargeLessThen4(chargeTime)
    print(batterLifePredict[0])
else:
    batterLifePredict = batterLife_chargeMoreThan4(chargeTime)
    print(batterLifePredict[0])
    