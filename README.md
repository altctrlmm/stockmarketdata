![Python package](https://github.com/altctrlmm/Robinhood-Watchlist-Stock-History/workflows/Python%20package/badge.svg)

<h1>rhutils</h1>
A Robinhood Utilities package. Currently it can download historical stock quotes to CSV files for the symbols in your Robinhood watchlists. Requires a free AlphaVantage key.

<h2>Quick Start</h2>
<ol>
<li>pip install rhutils</li>
<li>In your python <b>~/site-packages/rhutils/</b> open preferences.txt and update:</li>
<ul>
<li>Your free AlphaVantage API key</li>
<li>Your path for the historical csv files.<br/>
<li>Your Robinhood email<br/>
<li>Your Robinhood password
</ul>
<li>Rename preferences.txt to preferences.py</li>
<li>Create a new python file and insert code:</li>
</ol>

<h3>TO DOWNLOAD STOCK HISTORY FOR ANY ROBINHOOD WATCHLIST:</h3>
import rhutils.dl_quotes as dlq<br/>
dlq.dlquotes('Default') # or the name of any watchlist in your account

<h4>Example of the Historical CSV Files</h4>
date,1. open,2. high,3. low,4. close,5. volume<br/>
2020-01-31,32.2,32.325,31.85,32.03,3968506.0<br/>
2020-01-30,31.74,32.495,31.69,32.45,4338968.0 

<h3>Big Thanks</h3>
Big thank you to Robinhood for being the no-commission pioneer and also making an API available for free; 
also a big thanks to JMFernandes at <a href="https://github.com/jmfernandes/robin_stocks">https://github.com/jmfernandes/robin_stocks</a> for creating a python code for the Robinhood API. 
A version of robin_stocks is distributed with this package.