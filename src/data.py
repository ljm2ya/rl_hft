from reader import DataReader

class BitmexData:
    def __init__(self, data_dir, initial_date):
        self.reader = DataReader(data_dir, initial_date)

    def _idtoprice(self, ID, symbolIdx=88, ticksize=0.01):
        price = ((100000000 * symbolIdx) - ID) * ticksize
        return price

    def _zip_orderBookL2(self, bulk_orderBookL2):
    # return form: data [{side: 'sell', price: '8685', size: '11223'}]
        zip_data = []
        for tick in bulk_orderBookL2:
            side = tick['side']
            price = self._idtoprice(tick['id'])
            size = tick['size']
            zip_data.append({'side':side, 'price':price, 'size':size})
        return zip_data

    def _zip_trade(self, bulk_trade):
        zip_data = []
        for trade in bulk_trade:
            side = trade['side']
            price = trade['price']
            size = trade['size']
            zip_data.append({'side':side, 'price':price, 'size':size})
        return zip_data

    def _zip_liquid(self, bulk_liquid):
        zip_data = []
        for trade in bulk_liquid:
            side = trade['side']
            price = trade['price']
            size = trade['size']
            zip_data.append({'side':side, 'price':price, 'size':size})
        return zip_data


    def next_data(self):
        bulk_data = self.reader.next_file()
        data = {'orderBookL2': [], 'trade': [], 'liquid': []}
        for each_data in bulk_data:
            if each_data['table'] == 'orderBookL2':
                data['orderBookL2'].append(self._zip_orderBookL2(each_data['data']))
            elif each_data['trade'] == 'trade':
                data['trade'].append(self._zip_trade(each_data['data']))
            else:
                data['liquid'].append(self._zip_liquid(each_data['data']))

        return data
