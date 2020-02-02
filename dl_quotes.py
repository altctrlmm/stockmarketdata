# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 09:35:12 2019

@author: micah
"""
from datetime import datetime
import sys
import requests
import robin_stocks as r
import time
from alpha_vantage.timeseries import TimeSeries
import preferences
ts = preferences.ts
email = preferences.email
password = preferences.password
filePath = preferences.filePath

start_time = datetime.now()
processed_count = 0
failed_symbols = []

def minute_passed(oldepoch):
    return time.time() - oldepoch >= 60

try:
    login = r.login(email,password)
    watchlist = r.get_watchlist_by_name(name='Default', info=None)
    watchlistDict = {}
    for item in watchlist:
        url = item['instrument']
        r = requests.get(url)
        data_json = r.json()
        #print(str(data_json))  # print this to see more available symbol info.
        watchlistDict[data_json['symbol']] = data_json['simple_name']
except Exception as e:
    sys.exit(e)

oldepoch = time.time()
print("Total number of symbols to update: ",len(watchlistDict))
total_symbols = len(watchlistDict)
symbols_remaining = total_symbols
processed_count_continuous = 0


# --------------------------------------------------
# How to re-run script with only the failed symbols:
# --------------------------------------------------
"""

*** For these instructions, please note the uppercase letters at the end 
of the next several lines. ***

Sometimes, some symbols fail to download. When this occurs, you will be
provided a convenient list of the failed symbols, like the list on line A.
1. Copy/paste that list onto line A. 
2. Uncomment lines A, B, C, and D.
3. Comment-out line E.
"""                                                                # LINES
#                                                                  ________
#failedSymbolList = ['TRU', 'BRK.B', 'CSCO', 'CHKP', 'ELY', 'LGND']  # A
#name="failed symbols run only"                                      # B
#symbols_remaining = len(failedSymbolList)                           # C
#for _symbol in failedSymbolList:                                    # D
# ---------------------------------------
for _symbol, name in watchlistDict.items():                          # E
    try:      
        rate_limit_begin_time = time.time()
        processed_count = processed_count+1     
        processed_count_continuous = processed_count_continuous+1
        print(_symbol,": ",name)
        data, meta = ts.get_daily(_symbol,outputsize='full')
        fileName = _symbol + ".csv" 
        fh = open(filePath + fileName, "w") 
        fh.write( data.to_csv() )  
        fh.close() 
        symbols_remaining = symbols_remaining-1
        # Adjustments for AlphaVantage's Rate Limit, 5 symbols per minute
        if minute_passed(oldepoch) or processed_count==5:
            rate_limit_end_time = time.time()
            time_passed = rate_limit_end_time - rate_limit_begin_time
            pause_time = 60 - time_passed
            processed_count=0
            print("*** Pausing for ",pause_time," seconds.")
            print("*** ",symbols_remaining," symbols remain.")
            time_passed = datetime.now() - start_time
            print("*** This download has been running for ",time_passed)
            download_rate = time_passed / processed_count_continuous     
            estimated_time_remaining = symbols_remaining * download_rate
            print("*** Estimated time remaining: ",estimated_time_remaining)
            est_end_time = datetime.now() + estimated_time_remaining
            print("*** Estimated end time: ",est_end_time)
            time.sleep(pause_time)
            oldepoch = time.time()                
    except Exception as e:        
        print("Error on "+_symbol+": ",e)
        failed_symbols.append(_symbol)

end_time = datetime.now()
print("**************************")
print("")
print("Done! Time Elapsed: "+ str(end_time - start_time) )
if len(failed_symbols) > 0:
    print("Failed symbols: "+str(failed_symbols))
else: 
    print("There were no failed symbols.")
print("Completed at ",end_time)