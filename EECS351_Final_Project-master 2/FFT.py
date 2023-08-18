from pandas_datareader import data
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.fftpack

def FFTMethod(stockData):
    if 1:
        sum = 0;

        data = yf.download('AAPL', '2010-01-01', '2012-04-30')
        daysPredict = 30
        harmonics = 5;
        dataRange = np.arange(0, stockData.Close.size)
        polyFit = np.polyfit(dataRange, stockData.Close.values, 1)
        dataNoTrend = stockData.Close.values - polyFit[0] * dataRange
        dataFFT = np.fft.fft(dataNoTrend)
        freq = np.fft.fftfreq(stockData.Close.size)
        indices = range(stockData.Close.size)
        indices = list(range(stockData.Close.size))

        dataRange = np.arange(0, stockData.Close.size + daysPredict)
        restoredData = np.zeros(dataRange.size)
        for i in indices[:1 + harmonics * 2]:
            amplitude = np.absolute(dataFFT[i]) / stockData.Close.size
            phase = np.angle(dataFFT[i])
            restoredData += amplitude * np.cos(2 * np.pi * freq[i] * dataRange + phase)
        finalVals = restoredData + polyFit[0] * dataRange

        for i in range(0, len(stockData.Close.values)):
            dif = stockData.Close.values[i] - finalVals[i]
            sum += dif**2
        MSE = sum / len(stockData.Close.values)
        print(MSE)

        plt.plot(data.index.values, data.Close.values, 'b', label='Original Stock Price')
        plt.plot(data.index[0:(data.index.size - 30)], finalVals[0:(finalVals.size - 30)], 'r', label = 'Denoised')
        plt.plot(data.index[(data.index.size - 29):data.index.size], finalVals[(finalVals.size - 29):finalVals.size], 'g', label = 'Forecast', linewidth = 3)
        plt.xlabel("Year-Month")
        plt.ylabel("Stock Value ($)")
        plt.title("Stock Price Denoised + Extrapolated with FFT (Harmonic = 5, Stock = AAPL)")
        plt.legend()
        plt.show()

    # regDelta = 0
    #
    # stockDataFFT = np.fft.fft(stockData.values)
    # thetaFFT = np.arctan(stockDataFFT.imag / stockDataFFT.real)
    # amplitudeFFT = (np.sqrt(stockDataFFT.real**2 + stockDataFFT.imag**2) / (len(stockData) / 2))
    # frequencyFFT = np.fft.fftfreq(stockDataFFT.size, d=1)
    # frequencyFFT = frequencyFFT.reshape(amplitudeFFT.shape[0], amplitudeFFT.shape[1])
    # plt.figure(figsize=(15, 5))
    # plt.axvline(x=0, ymin=0, ymax=100000, linewidth=1, color='r')
    # plt.plot(frequencyFFT, amplitudeFFT, '.')
    # plt.show()
    #
    #
    # dominantAmplitudeVerifyFFT = amplitudeFFT > (3 * np.std(amplitudeFFT) + np.std(amplitudeFFT))
    # dominantFrequencyVerifyFFT = frequencyFFT > 0
    #
    # dominantAmplitudeFFT = amplitudeFFT[np.logical_and(dominantAmplitudeVerifyFFT, dominantFrequencyVerifyFFT)]
    # dominantFrequencyFFT = frequencyFFT[np.logical_and(dominantAmplitudeVerifyFFT, dominantFrequencyVerifyFFT)]
    # dominantThetaFFT = thetaFFT[np.logical_and(dominantAmplitudeVerifyFFT, dominantFrequencyVerifyFFT)]
    #
    # for i in range(len(dominantThetaFFT)):
    #     shift = dominantThetaFFT[i]
    #     regDelta += dominantAmplitudeFFT[i] * np.cos(i * np.array(range(len(stockDataFFT))) + shift)
    #
    # reg = stockData.Close[0] + np.cumsum(regDelta)
    #
    # plt.figure(figsize=(15,5))
    # plotData = stockData.Close.values
    # plt.plot(plotData)
    # plt.plot(reg)
    # #plt.show()