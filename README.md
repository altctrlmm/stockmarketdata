![Python package](https://github.com/altctrlmm/Robinhood-Watchlist-Stock-History/workflows/Python%20package/badge.svg)

<h1>rhutils</h1>
A Robinhood Utilities package that downloads stock  and account data to CSV files. Requires a free AlphaVantage key.

<h2>Functions:</h2>
<b>Download historical stock quotes</b> to CSV files for the symbols in your Robinhood watchlists.
<br/><br/>
<b>Download current stock quotes</b> to CSV files for a list of symbols you define or for the symbols in your Robinhood watchlists.

<h4>Example of the CSV Files</h4>
date,1. open,2. high,3. low,4. close,5. volume<br/>
2020-01-31,32.2,32.325,31.85,32.03,3968506.0<br/>
2020-01-30,31.74,32.495,31.69,32.45,4338968.0

<h3>Install</h3>
pip install rhutils

<h3>Import</h3>
import rhutils.dl_quotes as dlq

<h3>Add Your Credentials and Choices</h3>
av_key = 'YOUR_FREE_ALPHAVANTAGE_KEY'<br/>
rh_email = 'YOUREMAIL@SITE.COM' # Your email with Robinhood<br/>
rh_password = 'YOUR_ROBINHOOD_PASSWORD'<br/>
rh_watchlist = 'Default'<br/>
filePath = 'C:\\mkt\\stocks\\' # Where you want your new CSV files

<h3>Download Historical Quotes (up to 20 years) for all Symbols in a Robinhood Watchlist</h3>
dlq.dlquotes(av_key, filePath, rh_email, rh_password, rh_watchlist)

<h3>Download Current OHLCV for Every Symbol in a Robinhood Watchlist</h3>
wlsymbols = dlq.get_watchlist_symbols(rh_email, rh_password, rh_watchlist)<br/>
dlq.simple_quotes(av_key, filePath, wlsymbols)

<h3>Download Current OHLCV for One or More Stock Symbols You Define</h3>
symbol_list = ['BA', 'ALLY', 'F', 'MU', 'SPCE', 'T', 'WMT', 'S']<br/>
dlq.simple_quotes(av_key, filePath, symbol_list)
