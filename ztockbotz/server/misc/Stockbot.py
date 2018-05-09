from stockbot.PostgresInterface import PostgresInterface
from stockbot.StockAPI import StockAPI

ticker = 'BTC'
api = StockAPI()
daily_stock_prices = api.getDailyPrices(ticker)
postgres_interface = PostgresInterface(ticker)

