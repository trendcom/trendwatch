#!/usr/bin/python
import time
from classes.coin import Coin
import queue
import aiohttp
import asyncio
# https://www.bittrex.com/Home/Api Bittrex API page

#input is url you want to get json dat from, returns the data
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return data

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print ('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts))
        return result

    return timed

# creates a Coin object for each type of currency from https://bittrex.com/api/v1.1/public/getcurrencies
#@timeit
async def initialize_coins():
    currency_list = await get_currencies()
    coins = []
    for dictionary in currency_list: # dictionary is currency info for a specific coin
        newCoin = Coin(dictionary)
        coins.append(newCoin)
    await update_all_tickers(coins)
    return coins


# gets the info on all currencies, returns a list that contains dictionaries with information about each dictionary
async def get_currencies():
    currency_catalog = await fetch_data("https://bittrex.com/api/v1.1/public/getcurrencies")
    return currency_catalog["result"]


# gets tick info for specific market and specific currency, returns dictionary, link parameter given by ?market=market-currency
async def get_ticker(currency,market):
    seq = ("https://bittrex.com/api/v1.1/public/getticker?market=", market, "-", currency) # sequence of strings that will be put together to create the URL for the API
    ticker_catalog = await fetch_data("".join(seq)) #puts the seq strings together
    return ticker_catalog


# input is list containing Coin objects.
async def update_all_tickers(coins):
    await asyncio.gather(
        *(update_ticker(coin) for coin in coins)
        )


# updates ticker for a Coin object.
async def update_ticker(coin):
    ticker = await get_ticker(coin.get_currency(), "BTC")
    if ticker["success"] is True:
        coin.update_ticker(ticker)
    else:
        coin.update_ticker(None)

coinList = []
loop = asyncio.get_event_loop()
#asyncio.ensure_future(initialize_coins())
<<<<<<< Updated upstream
list = loop.run_until_complete(asyncio.gather(initialize_coins()))
list = list[0]
=======
<<<<<<< HEAD
dicto = loop.run_until_complete(asyncio.gather(initialize_coins()))
dicto = list[0]
print(dict["BTC"].getCurrency())
>>>>>>> Stashed changes
#for coin in list:
    #print(coin.get_currency())
=======
list = loop.run_until_complete(asyncio.gather(initialize_coins()))
list = list[0]
# for coin in list:
#    print(coin.get_currency())
>>>>>>> develop



