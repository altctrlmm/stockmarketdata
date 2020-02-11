<h1>stockmarketdata</h1>
Download current and historical stock quotes while connecting to your Ally or Robinhood account.

<h2>Working Functions:</h2>
<b>Download historical stock quotes</b> to CSV files from AlphaVantage (slow) OR Ally (fast!) for the symbols in your Robinhood watchlists.
<br/><br/>
<b>Download current stock quotes</b> to CSV files from AlphaVantage (slow) OR Ally (fast!) for a list of symbols you define or for the symbols in your Robinhood watchlists (Ally watchlists coming soon!).

<h4>Example of the CSV Files</h4>
date,1. open,2. high,3. low,4. close,5. volume<br/>
2020-01-31,32.2,32.325,31.85,32.03,3968506.0<br/>
2020-01-30,31.74,32.495,31.69,32.45,4338968.0

<h3>Install</h3>
pip install stockmarketdata

<h3>Import</h3>
import stockmarketdata.dl_quotes as dlq<br/>
import stockmarketdata.ally as ally

<h3>Add Your Credentials and Choices</h3>
av_key = 'YOUR_ALPHAVANTAGE_KEY'
<br/><br/>
filePath = "C:\\YOUR\\PATH\\"  # where to place the CSV files.
<br/><br/>
rh_email = 'YOUR_EMAIL_WITH_ROBINHOOD@MAIL.COM'<br/>
rh_password = 'YOUR_ROBINHOOD_PASSWORD'<br/>
rh_watchlist = "Default"  # The Robinhood watchlist to pull symbols from.
<br/><br/>
ally_consumer_key = 'YOUR_ALLY_CONSUMER_KEY'<br/>
ally_secret = 'YOUR_ALLY_SECRET'<br/>
ally_oauth_token = 'YOUR_ALLY_OAUTH_TOKEN'<br/>
ally_oauth_secret = 'YOUR_ALLY_OAUTH_SECRET'

<h3>Download Current OHLCV from Ally for Every Symbol in a Robinhood Watchlist (Fast)</h3>
rh_symbols = dlq.get_watchlist_symbols(rh_email, rh_password, rh_watchlist)<br/>
ally.get_ohlcv_from_ally(ally_consumer_key, ally_secret, ally_oauth_token, ally_oauth_secret, rh_symbols, filePath)

<h3>Download Current OHLCV from Ally for a List of Stock Symbols (Fast)</h3>
ally_symbols = ['WORK', 'SPCE', 'BILI']<br/>
ally.get_ohlcv_from_ally(ally_consumer_key, ally_secret, ally_oauth_token, ally_oauth_secret, ally_symbols, filePath)

<h3>Download Historical Quotes (up to 20 years) from AlphaVantage for all Symbols in a Robinhood Watchlist (Slow but currently don't have an alternative for historical)</h3>
dlq.dlquotes(av_key, filePath, rh_email, rh_password, rh_watchlist)

<h3>Download Current OHLCV from AlphaVantage for Every Symbol in a Robinhood Watchlist (Slow)</h3>
wlsymbols = dlq.get_watchlist_symbols(rh_email, rh_password, rh_watchlist)<br/>
dlq.simple_quotes(av_key, filePath, wlsymbols)

<h3>Download Current OHLCV from AlphaVantage for One or More Stock Symbols You Define (Slow)</h3>
symbol_list = ['BA', 'ALLY', 'F', 'MU', 'SPCE', 'T', 'WMT', 'S']<br/>
dlq.simple_quotes(av_key, filePath, symbol_list)
