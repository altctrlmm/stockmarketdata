![Python package](https://github.com/altctrlmm/Robinhood-Watchlist-Stock-History/workflows/Python%20package/badge.svg)

# rhutils
A Robinhood Utilities package. Currently it can download historical stock quotes to CSV files for the symbols in your default Robinhood watchlist. Requires a free AlphaVantage key.

## Download Historical Stock Quotes
### Example of the CSV Files
date,1. open,2. high,3. low,4. close,5. volume<br/>
2020-01-31,32.2,32.325,31.85,32.03,3968506.0<br/>
2020-01-30,31.74,32.495,31.69,32.45,4338968.0 

# Quick Start
1. Run:<br/>
$ pip install rhutils

2. Open preferences.txt and update:<br/>
A. Your free AlphaVantage API key<br/>
B. Your path for the csv files.<br/>
C. Your Robinhood email<br/>
D. Your Robinhood password

3. Rename preferences.txt to preferences.py

4. Open example_codes.py for an example.

## Big Thanks
Big thank you to Robinhood for being the no-commission pioneer and also making an API available for free; 
also a big thanks to JMFernandes at <a href="https://github.com/jmfernandes/robin_stocks">https://github.com/jmfernandes/robin_stocks</a> for creating a python code for the Robinhood API. 