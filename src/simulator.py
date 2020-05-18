import time

class MarketSimulator:
    def __init__(self, next_data_func):
        self._next_data = next_data_func
        self.start_time = time.time()
        self.timeSteps = 0
        self.orderNum = 0
        self.orderQueue = []
        self.orderBook = {'buy':[], 'sell':[]}

    def _bestBuy(self):
        return self.orderBook['buy'][0][0]

    def _bestSell(self):
        return self.orderBook['sell'][0][0]

    def _findinBook(self, side, price):
        for tick in self.orderBook[side]:
            if price == tick[0]:
                return tick[1]
           
    def _update_orderBook(self, tick):
        if tick['side'] == 'Buy':
            pass

    #order form : order = {'num': 2, 'side': 'buy', 'price': 8394.3, 'size': 50, 'sequence': 3245}
    def _check_order(self, order):
        if order['side'] == 'buy':
            if order['price'] > self._bestBuy():
                return 1
            else:
                return 0
        else:
            if order['price'] < self._bestsell():
                return 1
            else:
                return 0

    def _aggregate_trades(self, bulk_trades):
        agg_trade = {'buy': 0, 'sell': 0}
        for trade in bulk_trades:
            if trade['side'] == 'Buy':
                agg_trade['buy'] += trade['size']
            else:
                agg_trade['sell'] += trade['size']
        return agg_trade
       

    def take_order(self, side, price, size):
        self.orderNum += 1
        if side == 'buy':
            if price > self._bestBuy():
                seq = 0
            else:
                seq = self._findinBook(side, price)
        else:
            if price < self._bestSell():
                seq = 0
            else:
                seq = self._findinBook(side, price)

        self.orderQueue.append({'num': self.orderNum, 'side': side, 'price': price, 'size': size, 'sequence': seq})

    # data form
    # data = {'orderbook': [], 'trades': [], '}
    def next_step(self):
        data = self._next_data()
        self.timesteps += 1
        filledOrders = []
        aggTrades = self._aggregate_trades(data['trade'])
        aggLiquids = self._aggregate_trades(data['liquid'])

        for tick in data['orderBookL2']:
            self._update_orderbook(tick)

        for order in self.orderQueue:
            order_filled = self._check_order(order)
            if order_filled:
                filledOrders.append(order['num'])
                self.orderQueue.remove(order)

        return {'filledOrders': filledOrders, 'orderBook': self.orderBook, 'trades': aggTrades, 'liquidations': aggLiquids}


    def print_report(self):
        current_time = time.time()
        print("Elapsed time: ", current_time - self.start_time)
        print("Timesteps: ", self.timesteps)
