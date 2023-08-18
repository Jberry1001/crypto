from Wavelet import WaveletTransformation
from ARIMA import ARIMAMethod
from FinalPlot import plotOutcome
from SVR_2 import SVRMethod
from FFT import FFTMethod
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import math
import warnings

# Data Collection
warnings.filterwarnings("ignore")
stockTicker = 'AAPL'
data = yf.download(stockTicker, '2010-01-01', '2012-03-16')
boughtSaved = []
soldSaved = []
dateBoughtSaved = []
dateSoldSaved = []
budget = 10000
cashAfter = budget
forecast = 15
stockPrice = data.Close[0]
stockCount = math.floor((cashAfter * .9) / stockPrice)
overallStockCount = stockCount
investedPrice = data.Close.values[1]
initialInvestment = stockCount * -investedPrice
cashAfter += initialInvestment
boughtSaved.append(data.Close[1])
dateBoughtSaved.append(data.Close.index[1])

# use = WaveletTransformation(data[0:(data.Close.size - 15)])
# use2 = ARIMAMethod(use)
# svrData1 = pd.DataFrame(data={'dates': data.Close.index[0:len(use)], 'data': use, 'predictions': np.zeros(len(use))})
# result = SVRMethod(svrData1, forecast)
# percDif = result / result[0]
# use2Adjusted = use2 * percDif
# sum1 = 0
# sum2 = 0
# sum3 = 0
# for i in range(1, len(result)):
#     dif1 = data.Close.values[-i] - result[-i]
#     dif2 = data.Close.values[-i] - use2.values[-i]
#     dif3 = data.Close.values[-i] - use2Adjusted.values[-i]
#     sum1 += dif1 ** 2
#     sum2 += dif2 ** 2
#     sum3 += dif3 ** 2
# MSE1 = sum1 / len(result)
# MSE2 = sum2 / len(use2.values)
# MSE3 = sum3 / len(use2Adjusted.values)
# plt.plot(data.Close, color='blue', label='Actual')
# # plt.plot(data.Close.index[(data.Close.size - len(result)):data.Close.size], result, color='red', label='Forecast')
# # plt.plot(data.Close.index[(data.Close.size - len(result)):data.Close.size], use2.values, color='red', label='Forecast')
# plt.plot(data.Close.index[(data.Close.size - len(result)):data.Close.size], use2Adjusted, color='red', label='Forecast')
# plt.xlabel('Year-Month')
# plt.ylabel('Stock Value ($)')
# plt.title('Forecasted Stock Value (Combined)')
# plt.legend()
# plt.show()

print("Initial Investment: $" + str(-initialInvestment))

for idx, val in enumerate(data.Close):
    if idx >= 30 and idx < data.Close.size:
        newData = WaveletTransformation(data[0:idx])
        stockPredictedVals = ARIMAMethod(newData)
        svrData = pd.DataFrame(data={'dates': data.Close.index[0:len(newData)], 'data': newData, 'predictions': np.zeros(len(newData))})
        svrResults = SVRMethod(svrData, forecast)
        svrPercentChange = svrResults / svrResults[0]
        adjustedResults = stockPredictedVals * svrPercentChange
        percentChange = (adjustedResults - investedPrice) / investedPrice
        percentChangeWeight = (np.arange(15, 0, -1) * percentChange)
        if (min(percentChangeWeight) == percentChangeWeight[0]) and (min(percentChangeWeight) <= -.8):
            boughtSaved.append(data.Close[idx])
            dateBoughtSaved.append(data.Close.index[idx])
            investedPrice = data.Close.values[idx]
            stockCount = math.floor((cashAfter * .3) / investedPrice)
            overallStockCount += stockCount
            cashAfter -= investedPrice * stockCount
            print("After buying " + str(stockCount) + " stock(s), your money returned is: $" + str(cashAfter) +". You have " + str(overallStockCount) + " stocks remaining.")
        elif (max(percentChangeWeight) == percentChangeWeight[0]) and (max(percentChangeWeight) >= .8) and (overallStockCount > math.floor((cashAfter * .2) / investedPrice)):
            soldSaved.append(data.Close[idx])
            dateSoldSaved.append(data.Close.index[idx])
            investedPrice = data.Close.values[idx]
            stockCount = math.floor((cashAfter * .35) / investedPrice)
            if overallStockCount < stockCount:
                stockCount = overallStockCount
            cashAfter += investedPrice * stockCount
            overallStockCount -= stockCount
            print("After selling " + str(stockCount) + " stock(s), your money returned is: $" + str(cashAfter) + ". You have " +
                  str(overallStockCount) + " stocks remaining")
boughtDF = pd.DataFrame (data={'dates': dateBoughtSaved, 'data': boughtSaved})
soldDF = pd.DataFrame (data={'dates': dateSoldSaved, 'data': soldSaved})
print("In the given time window, your return is: $" + str(cashAfter) + ". This is a " + str(((cashAfter - budget) / -initialInvestment) * 100) +
      "% return on your original investment. You also have " + str(overallStockCount) + " stocks remaining.")
plotOutcome(stockTicker, data, boughtDF, soldDF)

