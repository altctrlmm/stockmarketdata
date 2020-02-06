![Python package](https://github.com/altctrlmm/Robinhood-Watchlist-Stock-History/workflows/Python%20package/badge.svg)

<h1>rhutils</h1>
A Robinhood Utilities package. Requires a free AlphaVantage key.

<h2>Functions:</h2>
<b>Download historical stock quotes</b> to CSV files for the symbols in your Robinhood watchlists.
<br/><br/>
<b>Download current stock quotes</b> to CSV files for a list of symbols you define.

<h4>Example of the CSV Files</h4>
date,1. open,2. high,3. low,4. close,5. volume<br/>
2020-01-31,32.2,32.325,31.85,32.03,3968506.0<br/>
2020-01-30,31.74,32.495,31.69,32.45,4338968.0

<h2>Install: pip install rhutils</h2>
'''python
import dl_quotes as dlq


<h3>Update your credentials and preferences:</h3>
'''python
av_key = 'YOUR_ALPHAVANTAGE_KEY'<br/>
historical_filePath = 'C:\\YOUR\\PATH\\'<br/>
rh_email = 'YOUR_EMAIL_WITH_ROBINHOOD@MAIL.COM'<br/>
rh_password = 'YOUR_ROBINHOOD_PASSWORD'<br/>
rh_watchlist = "Default"  # The Robinhood watchlist to pull symbols from.


<h3>Download Stock Quote History for Every Symbol in a Robinhood Watchlist</h3>
'''python
dlq.dlquotes( av_key, historical_filePath, rh_email, rh_password, rh_watchlist )


<h3>Download DOHLCV for a List of Stock Symbols</h3>
'''python
symbol_list = ['BA', 'ALLY', 'F', 'MU', 'SPCE', 'T', 'WMT', 'S']<br/>
dlq.simple_quotes(av_key, historical_filePath, symbol_list)
