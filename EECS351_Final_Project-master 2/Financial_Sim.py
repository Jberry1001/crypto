# EECS 351 Financial Simulator
# James Berry and James Wegeinka
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import PyWavelets as pywt
import self as self
import pmdarima as pm
from yahoo_fin import stock_info as si

# For finding d, p, q
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

# ARIMA Model
from statsmodels.tsa.arima_model import ARIMA
from sklearn.svm import SVR

#-----------------------------------Import_Data---------------------------------------#


#-----------------------------------Data_Analysis-------------------------------------#
si.get_live_price("aapl")


# i = 0;
# j = 0;
# stock_data = pdr.get_data_yahoo(self.ticker, self.start, self.end).
# x = np.array(self.stock_data.iloc[i: i + 11, j])
#
# # Wavelet Decompostion/Recomposition
# # Find T = R + S
# (ca, cd) = pywt.dwt(x, "haar")
# cat = pywt.threshold(ca, np.std(ca), mode="soft")
# cdt = pywt.threshold(cd, np.std(cd), mode="soft")
# tx = pywt.idwt(cat, cdt, "haar")
#
# # ARIMA Model
# # Get R' (reconstructed part) value
#     # Find d (differentiation value needed to be stable)
#     d  = 1
#     # Find p (AR Term using PACF Plot)
#     plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})
#     fig, axes = plt.subplots(1, 2, sharex=True)
#     axes[0].plot(df.value.diff()); axes[0].set_title('1st Differencing')
#     axes[1].set(ylim=(0,5))
#     plot_pacf(df.value.diff().dropna(), ax=axes[1])
#     plt.show()
#
#     # Find q (MA Term using ACF Plot)
#     plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})
#     # Import data
#     df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/austa.csv')
#     fig, axes = plt.subplots(1, 2, sharex=True)
#     axes[0].plot(df.value.diff()); axes[0].set_title('1st Differencing')
#     axes[1].set(ylim=(0,1.2))
#     plot_acf(df.value.diff().dropna(), ax=axes[1])
#     plt.show()
#
#      #Final ARIMA Model
#     model = ARIMA(df.value, order=(1,1,1))
#     model_fit = model.fit(disp=0)
#     print(model_fit.summary())
#
#     # Plot residual errors
#     residuals = pd.DataFrame(model_fit.resid)
#     fig, ax = plt.subplots(1,2)
#     residuals.plot(title="Residuals", ax=ax[0])
#     residuals.plot(kind='kde', title='Density', ax=ax[1])
#     plt.show()

# SVR Model
# Get S' (error part) value


# Forecast Result (T)
# T' = R' + S'


#------------------------------------Classification----------------------------------#

# Threshold

# Hold

# Buy

# Sell

# Profit
