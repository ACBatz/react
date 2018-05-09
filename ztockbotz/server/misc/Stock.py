import time
import datetime
import re

class Stock:
    def __init__(self, ticker, _datetime, price, volume, cap):
        self.ticker = ticker
        pattern = re.compile('^([0-9]{4}-[0-9]{2}-[0-9]{2}$)')
        if pattern.match(_datetime):
            self.datetime = time.mktime(datetime.datetime.strptime(_datetime, '%Y-%m-%d').timetuple())
        else:
            self.datetime = time.mktime(datetime.datetime.strptime(_datetime, '%Y-%m-%d %H:%M:%S').timetuple())
        self.price = float(price)
        self.volume = float(volume)
        self.cap = float(cap)
