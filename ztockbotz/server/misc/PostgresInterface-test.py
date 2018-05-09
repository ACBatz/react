from stockbot.IntraDayData import IntraDayData
from stockbot.PostgresInterface import PostgresInterface
from stockbot.StockAPI import StockAPI

api = StockAPI()
intra_day_prices = api.getIntraDayPrices('XRP')
data = IntraDayData(intra_day_prices)
assert len(data.stocks) > 0
pi = PostgresInterface('XRP')
for stock in data.stocks:
    pi.insert(stock)
select = pi.select('XRP')
assert len(select['records']) == len(data.stocks)
data2 = IntraDayData(select)