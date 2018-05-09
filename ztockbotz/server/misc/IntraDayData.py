from stockbot.Stock import Stock


class IntraDayData:
    def __init__(self, stockdata = None):
        self.stockdata = stockdata
        self.stocks = []
        try:
            code = stockdata['Meta Data']['2. Digital Currency Code']
            for key, value in stockdata['Time Series (Digital Currency Intraday)'].items():
                datetime = key
                price = value['1a. price (USD)']
                volume = value['2. volume']
                cap = value['3. market cap (USD)']
                stock = Stock(code, datetime, price, volume, cap)
                self.stocks.append(stock)
            self.stocks.reverse()
        except:
            print(stockdata.keys())
            raise ImportError