from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "5rPU1lo6cL0CXgRGjI01Qisp7LWm9z5TxIDXEcJX"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"v1/latest?apikey={API_KEY}"
    url = BASE_URL + endpoint
    d = get(url).json()

    # data = list(data.items())
    data = dict(d.items())
    # data.sort()

    # currencyName = [c.keys()[0] for c in data.values()]
    # currencyValue = [c.values()[0] for c in data.values()]

    return data


def print_currencies(currencies):
    currencyName = []
    currencyValue = []
    x = 0
    num = 1
    for item in data.values():
        i = item.keys()  # get keys
        j = item.values()  # get values
        for item in i:
            currencyName.append(item)  # put the keys to the currencyName
        for item in j:
            currencyValue.append(item)  # put the values to the currencyValue
    # then we have devide
    # print(currencyName)
    # print(currencyValue)

    for l in currencyName:
        print(f"{num}. {l} : {currencyValue[x]}")
        num += 1
        x += 1


def exchange_rate(currency1, currency2):
    # i do it manually, because has no api key for do that
    pass


# get_currencies()
data = get_currencies()


print_currencies(data)
