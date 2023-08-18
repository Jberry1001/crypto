import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
from pandas import datetime
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.stattools import acf
from matplotlib.animation import FuncAnimation

import yfinance as yf
def ARIMAMethod(stockData):
    model = ARIMA(stockData, order=(1, 1, 0))
    modelFit = model.fit(disp=-1)
    fc, se, conf = modelFit.forecast(15, alpha=.05)

    fc_series = pd.Series(fc, index=range(0, 15))
    lower_series = pd.Series(conf[:, 0], index=range(0, 15))
    upper_series = pd.Series(conf[:, 1], index=range(0, 15))

    # fig = plt.figure(figsize=(12, 5), dpi=100)
    # plt.xlabel("Year-Month")
    # plt.ylabel("Stock Value ($)")
    # plt.title('Forecasted Stock Value (ARIMA)')
    # plt.legend(loc='upper left', fontsize=8)
    # plt.plot(data.Close.index, stockData, label='Transformed Data')
    # # plt.plot(data.Close.index[trainData.size:(trainData.size + testData.size)], stockData[trainData.size:(trainData.size + testData.size - 4)], label='Actual (Test)')
    # plt.plot(data.Close.index[-15:], fc_series, label='Forecast')
    return fc_series

    # def animate(i):
    #     graph.set_data(data.Close.index[0:(trainData.size - 1)][:i+1], stockData[1:trainData.size][:i+1])
    #     return graph
    #
    # def animate1(i):
    #     graph1.set_data(data.Close.index[0:(trainData.size - 1)][:i+1], stockData[trainData.size:(trainData.size + testData.size - 4)])
    #     return graph1
    #
    # def animate2(i):
    #     graph2.set_data(data.Close.index[(trainData.size):(trainData.size + 15)], fc_series)
    #     return graph2
    #
    # ani = FuncAnimation(fig, animate, frames = 1000, interval = 10)
    # ani1 = FuncAnimation(fig, animate1, frames = 1000, interval = 10)
    # ani2 = FuncAnimation(fig, animate2, frames = 1, interval = 200)
    # plt.show()

    # sum = 0
    # for i in range(0, 15):
    #     dif = stockData[trainData.size + i] - fc_series.values[i]
    #     sum += dif ** 2
    # MSE = sum / 15
    # print(MSE)

    # error = mean_squared_error(testData, predictions)
    # print(error)
    # plt.plot(data.Close.index, data.Close.values, color = 'blue', label='Original Stock Values')
    # plt.plot(data.Close.index[math.floor(.66 * len(stockData)):len(stockData)], predictions[0:(len(predictions) - 4)], color = 'red', label='Predicted Stock Values (Test Segment)')
    # plt.xlabel("Year-Month")
    # plt.ylabel("Stock Price ($)")
    # plt.legend()
    # plt.title("Stock Price Time-Series Forecasting using ARIMA Model (Stock = AAPL)")
    # plt.show()

