from pandas_datareader import data
import yahoo_fin as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pywt

def Decisions(stockData, predictions, dayOfCycle, initStockPrice):
    data = yf.download('AAPL', '2010-01-01', '2012-03-31')
    percentChange = (predictions.values - stockData.Close.values[-1]) / stockData.Close.values[-1]




# data = yf.download('RTN', '2019-01-01', '2019-12-01')
# stockPrice = data.Close[0]
# stockCount = 100;
# initialInvestment = stockCount * stockPrice
# netCash = -1 * initialInvestment
# boughtSaved = []
# soldSaved = []
#
# print("Initial Investment: $" + str(initialInvestment))
# for index, value in enumerate(data.itertuples()):
#     if ((value.Close - stockPrice) * -1) >= (stockPrice * .1):
#         stockCount += 100
#         netCash -= (value.Close * 100)
#         print("After buying, current cash: $" + str(netCash))
#         stockPrice = value.Close
#         boughtSaved.append(index)
#
#     if (value.Close - stockPrice) >= (stockPrice * .1):
#         if stockCount >= 50:
#             stockCount -= 50
#             netCash += (value.Close * 50)
#             stockPrice = value.Close
#             print("After selling, current cash: $" + str(netCash))
#             soldSaved.append(index)
