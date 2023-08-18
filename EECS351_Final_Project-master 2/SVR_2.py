import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_squared_error
import math

def SVRMethod(stockData, forecast):
    stockData['predictions'] = stockData[['data']].shift(-forecast)
    trainData = np.array(stockData.drop(['predictions', 'dates'], 1))
    trainData = trainData[:-forecast]
    resultTrainData = np.array(stockData['predictions'])
    resultTrainData = resultTrainData[:-forecast]
    trainDataUse = trainData[0:math.floor(.8*len(trainData))]
    trainDataResult = resultTrainData[0:math.floor(.8*len(resultTrainData))]
    # testDataUse = trainData[math.floor(.8*len(trainData)):len(trainData)]
    # testDataResult = resultTrainData[math.floor(.8*len(resultTrainData)):len(resultTrainData)]
    svrRBF = SVR(kernel='rbf', C=1e3, gamma=.1)
    svrRBF.fit(trainDataUse, trainDataResult)
    svrPredict = np.array(stockData.drop(['predictions', 'dates'], 1))[-forecast:]
    svrPredictVals = svrRBF.predict(svrPredict)
    return svrPredictVals