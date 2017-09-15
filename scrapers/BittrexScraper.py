#!/usr/bin/python
import time
from threading import Thread
from scrapers.JSONscraper import fetch_data
from scrapers.classes.coin import Coin
import queue
# https://www.bittrex.com/Home/Api Bittrex API page


# creates a Coin object for each type of currency from https://bittrex.com/api/v1.1/public/getcurrencies
def initialize_coins():
    start_time = time.time()
    currency_list = get_currencies()
    coins = []
    for dictionary in currency_list: # dictionary is currency info for a specific coin
        newCoin = Coin(dictionary)
        coins.append(newCoin)
    update_all_tickers(coins)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    return coins


# gets the info on all currencies, returns a list that contains dictionaries with information about each dictionary
def get_currencies():
    currency_catalog = fetch_data("https://bittrex.com/api/v1.1/public/getcurrencies")
    return currency_catalog["result"]


# gets tick info for specific market and specific currency, returns dictionary, link parameter given by ?market=market-currency
def get_ticker(currency,market):
    seq = ("https://bittrex.com/api/v1.1/public/getticker?market=", market, "-", currency) # sequence of strings that will be put together to create the URL for the API
    ticker_catalog = fetch_data("".join(seq)) #puts the seq strings together
    return ticker_catalog

# input is list containing Coin objects. Created t threads to quicker get all the ticker data from the API, and splits the
# list of coins into t lists of approximate size len(coins) // t
def update_all_tickers(coins):
    threads = []
    t=20 # amount of threads
    length = len(coins) // t #length of each partition
    for i in range(t):
        if i == t:
            length2 = 0
        else:
            length2 =  length*(i+1)
        t = Thread(target=update_ticker_partition, args=[coins[length*i:length2]]) #creates new thread
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join() #waits for thread to finish

def update_ticker_partition(coins): # allows threads to do their work. input is one of the smaller#  lists from update_all_tickers
    for coin in coins:
        update_ticker(coin)



# updates ticker for a coin from coin.
def update_ticker(coin):
    print("tick")
    ticker = get_ticker(coin.get_currency(), "BTC")
    if ticker["success"] is True:
        coin.update_ticker(ticker)
    else:
        coin.update_ticker(None)

print(initialize_coins())