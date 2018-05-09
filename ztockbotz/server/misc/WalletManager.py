from stockbot.Transaction import Transaction


class WalletManager:
    def __init__(self, wallet, buy_limiter, sell_limiter):
        self.wallet = wallet
        self.buys = []
        self.sells = []
        self.history = []
        self.buy_limiter = buy_limiter
        self.sell_limiter = sell_limiter

    def add_buy(self, buy):
        self.buys.append(buy)
        self.wallet.funds -= buy.price * buy.amount
        self.wallet.coins += buy.amount
        self.history.append(buy)

    def add_sell(self, sell):
        self.sells.append(sell)
        self.wallet.funds += sell.price * sell.amount
        self.wallet.coins -= sell.amount
        self.history.append(sell)

    def get_buys_below(self, price):
        return list(filter(lambda tx: tx.price < price, self.buys))

    def remove_buy(self, buy):
        self.buys.remove(buy)

    def attempt_buy(self, stock):
        if self.wallet.funds > 0:
            amount = self.wallet.funds / stock.price
            tx = Transaction(stock.datetime, 'BUY', stock.price, amount * self.buy_limiter)
            self.add_buy(tx)
            return True
        else:
            return False

    def attempt_sell(self, stock):
        if self.wallet.coins > 0:
            buys = self.get_buys_below(stock.price * self.sell_limiter)
            if len(buys) > 0:
                coins = sum(list(map(lambda x: x.amount, buys)))
                tx = Transaction(stock.datetime, "SELL", stock.price, coins)
                self.add_sell(tx)
                for buy in buys:
                    self.remove_buy(buy)
                return True
        return False
