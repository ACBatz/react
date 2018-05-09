import matplotlib.pyplot as plt
from stockbot.DailyData import DailyData
from stockbot.EMA import EMA
from stockbot.IntraDayData import IntraDayData
from stockbot.StockAPI import StockAPI
from stockbot.Utils import Utils
from stockbot.Wallet import Wallet
from stockbot.WalletManager import WalletManager

api = StockAPI()

prices = api.getDailyPrices('BTC')
daily = DailyData(prices)
dailyData = daily.stocks
prices = api.getIntraDayPrices('BTC')
intradaily = IntraDayData(prices)
intradailyData = intradaily.stocks
plt.plot(list(map(lambda x: x.datetime, dailyData)), list(map(lambda x: x.price, dailyData)), color='blue')
plt.plot(list(map(lambda x: x.datetime, intradailyData)), list(map(lambda x: x.price, intradailyData)), color='orange')

ema = EMA(dailyData)
macd = ema.macd(12, 26)
signal = ema.signal(9, macd)

ema2 = EMA(intradailyData)
macd2 = ema2.macd(12, 26)
signal2 = ema2.signal(9, macd2)

plt.plot(list(map(lambda x: x.datetime, macd)), list(map(lambda x: x.value, macd)), color='red')
plt.plot(list(map(lambda x: x.datetime, signal)), list(map(lambda x: x.value, signal)), color='green')

plt.plot(list(map(lambda x: x.datetime, macd2)), list(map(lambda x: x.value, macd2)), color='orange')
plt.plot(list(map(lambda x: x.datetime, signal2)), list(map(lambda x: x.value, signal2)), color='blue')
plt.grid(True)



delta = len(macd) - len(signal)
wallet = Wallet(1000)
manager = WalletManager(wallet, .995, 1.01)
manager.attempt_buy(dailyData[0])
prev = None
for i in range(0, len(macd) - 1):
    if i >= delta:
        stock = dailyData[26+i-1]
        dif = macd[i].value - signal[i - delta].value
        if not prev is None:
            if prev > 0 and dif <= 0:
                s = manager.attempt_sell(stock)
                if s:
                    plt.plot(stock.datetime, stock.price, marker='o', color='red')
            elif prev < 0 and dif >= 0:
                b = manager.attempt_buy(stock)
                if b:
                    plt.plot(stock.datetime, stock.price, marker='o', color='green')
        prev = dif
print(Utils.seconds_between(dailyData[0].datetime, dailyData[len(dailyData) - 1].datetime) / 60 / 60 / 24)
print(wallet.funds + wallet.coins * dailyData[len(dailyData) - 1].price)
plt.show()