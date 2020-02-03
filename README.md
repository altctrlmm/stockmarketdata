![Python package](https://github.com/altctrlmm/Robinhood-Watchlist-Stock-History/workflows/Python%20package/badge.svg)

# Robinhood-Watchlist-Stock-History
Download historical stock quotes to CSV files for the symbols in your default Robinhood watchlist.

# Example of the CSV Files
date,1. open,2. high,3. low,4. close,5. volume<br/>
2020-01-31,32.2,32.325,31.85,32.03,3968506.0<br/>
2020-01-30,31.74,32.495,31.69,32.45,4338968.0 

# Quick Start
1. Run:<br/>
$ pip install -r requirements.txt

2. Open preferences.txt

3. Update:<br/>
A. Your free AlphaVantage API key<br/>
B. Your path for the csv files.<br/>
C. Your Robinhood email<br/>
D. Your Robinhood password

4. Rename preferences.txt to preferences.py

5. Open example_codes.py and run it.

# Big Thanks
Big thank you to Robinhood for being the no-commission pioneer and also making an API available for free; 
also a big thanks to JMFernandes at <a href="https://github.com/jmfernandes/robin_stocks">https://github.com/jmfernandes/robin_stocks</a> for creating a python code for the Robinhood API. 