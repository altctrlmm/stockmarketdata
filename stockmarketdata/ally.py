import requests
import csv
from requests_oauthlib import OAuth1


def get_ohlcv_from_ally(api_key, secret, oath_token, oath_secret, symbol_list, filePath):

    # login
    auth = OAuth1(api_key, secret, oath_token, oath_secret)

    # symbol string
    symbol_str = ''
    n = 0
    for sym in symbol_list:
        n = n+1
        symbol_str = symbol_str + ',' + sym

    # url
    url = 'https://api.tradeking.com/v1/market/ext/quotes.json?'\
        'symbols='+symbol_str + \
        '&fids=symbol,date,opn,hi,lo,last,vl'

    # api request
    response = requests.get(url, auth=auth).json()

    # parse response
    i = 0
    while i < n:
        symbol = response['response']['quotes']['quote'][i]['symbol']
        date   = response['response']['quotes']['quote'][i]['date']
        opn    = response['response']['quotes']['quote'][i]['opn']
        hi     = response['response']['quotes']['quote'][i]['hi']
        lo     = response['response']['quotes']['quote'][i]['lo']
        last   = response['response']['quotes']['quote'][i]['last']
        vl     = response['response']['quotes']['quote'][i]['vl']

        # put into CSV file
        fileName = filePath + symbol + '.csv'
        print(fileName)
        with open(fileName, mode='w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['date', '1. open', '2. high', '3. low', '4. close', '5. volume'])
            csv_writer.writerow([date, opn, hi, lo, last, vl])
        i = i+1
