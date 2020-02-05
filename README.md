![Python package](https://github.com/altctrlmm/Robinhood-Watchlist-Stock-History/workflows/Python%20package/badge.svg)

<h1>rhutils</h1>
A Robinhood Utilities package. Currently it can download historical stock quotes to CSV files for the symbols in your Robinhood watchlists. Requires a free AlphaVantage key.

<h4>Example of the Historical CSV Files</h4>
date,1. open,2. high,3. low,4. close,5. volume<br/>
2020-01-31,32.2,32.325,31.85,32.03,3968506.0<br/>
2020-01-30,31.74,32.495,31.69,32.45,4338968.0

<h2>Quick Start</h2>
<b>1. Install: </b>pip install rhutils

<b>2. Paste the code below into a python file. Then update it with your credentials:</b>

<h3>Download Stock Quote History for Every Symbol in a Robinhood Watchlist</h3>
import rhutils.dl_quotes as dlq

<h4>Update your credentials and preferences:</h3>
av_key='YOUR_ALPHAVANTAGE_KEY'<br/>
historical_filePath = "C:\\YOUR\\PATH\\"<br/>
rh_email = 'YOUR_EMAIL_WITH_ROBINHOOD@MAIL.COM'<br/>
rh_password = 'YOUR_ROBINHOOD_PASSWORD'<br/>
rh_watchlist = 'Default'

<h4>Run this function</h3>
dlq.dlquotes( av_key, historical_filePath, rh_email, rh_password, rh_watchlist )
