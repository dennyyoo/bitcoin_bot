import robin_stocks as r
import numpy as np
import tulipy as ti
import cryptocompare
import time
#login info
login = r.login('username', "password")

#gets bitcoin price
def btc_price():
    price = cryptocompare.get_price('BTC', curr='USD', full= False)['BTC']['USD']
    return price

lst = [0]*11


while True:
    lst.append(btc_price())
    del lst[0]
    print(lst)
    arr = np.asarray(lst)
    rssi = ti.rsi(arr, period = 5)
    print(rssi[4])
    time.sleep(300)
    if rssi[4] >70:
        r.order_sell_crypto_by_price('BTC', 100)
        #can change number for how much you want to buy
    elif rssi[4] < 40:
        r.order_buy_crypto_by_price('BTC', 100)
        #same thing as above but how much you want to sell