import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pywt
import warnings

def WaveletTransformation(stockData):
    wavelet = pywt.Wavelet('sym5')
    coeffs = pywt.wavedec(stockData.Close.values, wavelet, level=6)
    denoisedSignal = pywt.waverec(coeffs[:-2] + [None] * 2, wavelet)
    # plt.plot(stockData.Close.index, stockData.Close.values, label = 'Original Stock Value')
    # plt.plot(stockData.Close.index, denoisedSignal[1:stockData.Close.size + 1], label = 'Denoised Signal')
    # plt.xlabel("Year-Month")
    # plt.ylabel("Stock Price ($)")
    # plt.legend()
    # plt.title("Stock Price Denoised with Wavelet Transforms (Stock = AAPL)")
    # plt.show()
    return denoisedSignal[0:len(stockData.Close.values)]