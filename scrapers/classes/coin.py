class Coin:
    # contains tick values for Bitcoin market, will be None if no such value exist (success == false)
    tickerDict = None
    # contains info about the currency from https://bittrex.com/api/v1.1/public/getcurrencies
    currencyDict = None
    currency = None
    currencyLong = None

    # initializes the Object
    def __init__(self, currencyDict):
        self.currencyDict = currencyDict


    def update_ticker(self, tickerDict):
        self.tickerDict = tickerDict



    # returns acronym for coin, for example "BTC"
    def get_currency(self):
        return self.currencyDict["Currency"]


    # returns full name for coin, for example "Bitcoin"
    def get_currencyLong(self):
        return self.currencyDict["CurrencyLong"]


    # returns bid value in float form
    def get_bid(self):
        return self.tickerDict["result"]["Bid"]


    # returns ask value in float form
    def get_ask(self):
        return self.tickerDict["result"]["Ask"]


    # returns last value in float form
    def get_last(self):
        return self.tickerDict["result"]["Last"]