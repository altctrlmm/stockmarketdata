![Python package](https://github.com/altctrlmm/Robinhood-Watchlist-Stock-History/workflows/Python%20package/badge.svg)

<h1> *** STILL TESTING, RECOMMENDED DON'T DOWNLOAD YET *** </h1>

<h1>rhutils</h1>
A Robinhood Utilities package. Currently it can download historical stock quotes to CSV files for the symbols in your Robinhood watchlists. Requires a free AlphaVantage key.

<h2>Quick Start</h2>
<p>pip install rhutils</p>
<p>
Paste this code into a python file. Then update with your credentials:
</p>

<p>
## Download Stock Quote History for Every Symbol in a Robinhood Watchlist
import rhutils.dl_quotes as dlq
</p>
<p>
### Update your credentials and preferences:
av_key='YOUR_ALPHAVANTAGE_KEY'
historical_filePath = "C:\\YOUR\\PATH\\" # where to place the historical csv files.
rh_email = 'YOUR_EMAIL_WITH_ROBINHOOD@MAIL.COM'
rh_password = 'YOUR_ROBINHOOD_PASSWORD'
rh_watchlist = "Default" # The Robinhood watchlist to pull symbols from.
</p>
<p>
### Run this function
dlq.dlquotes( av_key, historical_filePath, rh_email, rh_password, rh_watchlist )
</p>

<h4>Example of the Historical CSV Files</h4>
date,1. open,2. high,3. low,4. close,5. volume<br/>
2020-01-31,32.2,32.325,31.85,32.03,3968506.0<br/>
2020-01-30,31.74,32.495,31.69,32.45,4338968.0
