import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import yfinance as yf


def SVRMethod(newData):
    data = yf.download('AAPL', '2012-01-01', '2014-12-01')
    dates = data.Close.index
    dates = np.reshape(dates.values, (len(dates.values), 1))
    prices = newData
    prices.ravel()
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    # svr_lin = SVR(kernel='linear', C=1e3)
    svr_rbf.fit(dates, prices[0:len(dates)])
    # svr_lin.fit(dates, prices[0:len(dates)])

    plt.scatter(dates, prices[0:len(dates)], color='black', label='Data')  # plotting the initial datapoints
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')  # plotting the line made by the RBF kernel
    # plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')  # plotting
    plt.legend(loc='upper left')
    plt.xlabel("Year-Month")
    plt.ylabel("Stock Price ($)")
    plt.title('Stock Price Time-Series Forecasting using SVR Model (Stock = AAPL)')
    plt.show()
