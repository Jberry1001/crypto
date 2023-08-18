import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib  import animation
from numpy import random
import numpy as np
import math
import datetime

def plotOutcome(stockTicker, realData, boughtPoints, soldPoints):
    plt.plot(realData.Close, label = stockTicker + ' Ticker')
    plt.scatter(boughtPoints.dates, boughtPoints.data, marker = "^", color = "red", label = "Stock Bought")
    plt.scatter(soldPoints.dates, soldPoints.data, marker=",", color="green", label="Stock Sold")
    plt.title('Stock Price + Decisions Made (189.9% Return)')
    plt.xlabel('Date/Month')
    plt.ylabel('Stock Price ($)')
    plt.legend()
    plt.show()