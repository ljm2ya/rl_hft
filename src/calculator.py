#!/usr/bin/env python3
import pprint

'''
def _compress_orderbook(orderbook, depth):
    # orderbook range is dollor
    midprice = _analize_orderbook(orderbook)['midprice']
    compressed_orderbook = {'T': orderbook['T'], 'asks':[], 'bids':[]}
    for order in orderbook['asks']:
        price = float(order[0])
        if price <= (midprice + depth):
            compressed_orderbook['asks'].append(order)
    for order in orderbook['bids']:
        price = float(order[0])
        if price >= (midprice - depth):
            compressed_orderbook['bids'].append(order)
    return compressed_orderbook
'''

def _get_book_price_list(orderbook):
    list = {'asks': [], 'bids': []}
    for order in orderbook['asks']:
        list['asks'].append(float(order[0]))
    for order in orderbook['bids']:
        list['bids'].append(float(order[0]))
    return list

def _compare_orderbook(new_obook, old_obook):
    _orderbook_price_list = _get_book_price_list(old_obook)
    interval = new_obook['T'] - old_obook['T']
    net_orderbook = {'interval':interval, 'asks':[], 'bids':[]}
    for order in new_obook['asks']:
        price = float(order[0])
        count = float(order[1])
        try:
            index = _orderbook_price_list['asks'].index(price)
        except ValueError:
            # ask order was not in old ask order
            # all flow is net flow
            netflow = count
        else:
            # ask order was in old ask order.
            # so flow = new - old
            netflow = count - float(old_obook['asks'][index][1])
        net_orderbook['asks'].append([price, netflow])

    for order in new_obook['bids']:
        price = float(order[0])
        count = float(order[1])
        try:
            index = _orderbook_price_list['bids'].index(price)
        except ValueError:
            # ask order was not in old ask order
            # all flow is net flow
            netflow = count
        else:
            # ask order was in old ask order.
            # so flow = new - old
            netflow = count - float(old_obook['bids'][index][1])
        net_orderbook['bids'].append([price, netflow])

    return net_orderbook

def calc_DOBI(new_obook, old_obook, recent_trades):
    netAsk = 0
    netBid = 0
    for trade in recent_trades:
        trade_time = trade['time']
        price = float(trade['price'])
        qty = float(trade['qty'])
        old_obook_time = old_obook['T']
        new_obook_time = new_obook['T']
        minAsk = float(new_obook['asks'][0][0])
        maxBid = float(new_obook['bids'][0][0])
        if trade_time > old_obook_time and trade_time < new_obook_time:
            # trade is happened between new,old book
            if trade['isBuyerMaker']:# was ask order
                if price < minAsk:
                    netAsk -= qty
            else: # was bid order
                if price > maxBid:
                    netBid -= qty

    net_orderbook = _compare_orderbook(new_obook, old_obook)
    for order in net_orderbook['asks']:
        netAsk += order[1]
    for order in net_orderbook['bids']:
        netBid += order[1]

    return {'netAsk': netAsk, 'netBid': netBid}
