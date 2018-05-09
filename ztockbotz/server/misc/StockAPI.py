import requests


class StockAPI:
    def __init__(self):
        self.api_key = "&apikey=4RJOGGUOE38RD4US"
        self.api_market = "&market=USD"
        self.api_url = "https://www.alphavantage.co/query?"

    def getDailyPrices(self, symbol):
        req = requests.get(self.api_url + "function=DIGITAL_CURRENCY_DAILY" + "&symbol=" + symbol + self.api_market + self.api_key)
        return req.json()

    def getIntraDayPrices(self, symbol):
        req = requests.get(self.api_url + "function=DIGITAL_CURRENCY_INTRADAY" + "&symbol=" + symbol + self.api_market + self.api_key)
        return req.json()

    def getDailyStockPrices(self, symbol):
        req = requests.get(self.api_url + "function=TIME_SERIES_DAILY" + "&symbol=" + symbol + self.api_market + self.api_key)
        return req.json()