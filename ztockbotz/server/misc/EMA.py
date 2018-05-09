from stockbot.TimeValue import TimeValue


class EMA:
    def __init__(self, stocks):
        self.stocks = stocks
        self.values = list(map(lambda x: x.price, sorted(stocks, key=lambda x: x.datetime)))

    def ema(self, values, interval):
        if len(values) < interval:
            return sum(list(map(lambda x: float(x), values))) / float(len(values))
        else:
            ema = []
            subarr = values[:interval]
            avg = sum(subarr) / len(subarr)
            ema.append(avg)
            prev = avg
            for x in values[interval:]:
                ema_i = float(x) * 2 / (interval + 1) + prev * (1 - 2 / (interval + 1))
                ema.append(ema_i)
                prev = ema_i
            return ema

    def macd(self, interval_1, interval_2):
        ema_1 = self.ema(self.values, interval_1)
        ema_2 = self.ema(self.values, interval_2)
        macd_arr = []
        delta = interval_2 - interval_1
        for i in range(0, len(ema_1)):
            if i >= delta:
                macd = TimeValue(self.stocks[i + interval_2 - delta - 1].datetime, (ema_1[i] - ema_2[i - delta]))
                macd_arr.append(macd)
        return macd_arr

    def signal(self, interval_s, macd):
        signal_vals = self.ema(list(map(lambda x: x.value,macd)), interval_s)
        signal_arr = []
        for i in range(0, len(signal_vals)):
            signal = TimeValue(self.stocks[len(self.stocks) - len(macd) + interval_s + i - 1].datetime, signal_vals[i])
            signal_arr.append(signal)
        return signal_arr