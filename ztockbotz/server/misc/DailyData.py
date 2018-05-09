from stockbot.Stock import Stock


class DailyData:
    def __init__(self, stockdata = None):
        self.stockdata = stockdata
        self.stocks = []
        code = stockdata['Meta Data']['2. Digital Currency Code']
        for key, value in stockdata['Time Series (Digital Currency Daily)'].items():
            datetime = key
            price = value['4a. close (USD)']
            volume = value['5. volume']
            cap = value['6. market cap (USD)']
            stock = Stock(code, datetime, price, volume, cap)
            self.stocks.append(stock)
        self.stocks.reverse()