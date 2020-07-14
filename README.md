![Python package](https://github.com/altctrlmm/stockmarketdata/workflows/Python%20package/badge.svg)

![Upload Python Package](https://github.com/altctrlmm/stockmarketdata/workflows/Upload%20Python%20Package/badge.svg)

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
import sys
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

operation = sys.argv

    #----------------------------------------------------------------------------
    # Download Current OHLCV from Ally for Every Symbol in a Robinhood Watchlist |
    # ----------------------------------------------------------------------------
if operation[1] == 'fast':    
    rh_symbols = dlq.get_watchlist_symbols(rh_email, rh_password, rh_watchlist)
    ally.get_ohlcv_from_ally(ally_consumer_key, ally_secret, ally_oauth_token, ally_oauth_secret, rh_symbols, filePath)

    # ----------------------------------------------------------------------
    # Download Current OHLCV from AlphaVantage for a List of Stock Symbols |
    # ----------------------------------------------------------------------    
elif operation[1] == 'list':
    del operation[0:2]
    dlq.simple_quotes(av_key, filePath, operation)   
    
    # ----------------------------------------------------------------------------------
    # Download historical quotes for all symbols in a Robinhood watchlist to CSV files |
    # ----------------------------------------------------------------------------------    
elif operation[1] == 'full':
    dlq.dlquotes(av_key, filePath, rh_email, rh_password, rh_watchlist)
    

# Example Usage in Command Line: 

# Download Current OHLCV from Ally for Every Symbol in a Robinhood Watchlist (fast)
# python examples.py fast

# Download Current OHLCV from AlphaVantage for One Symbol OR a List of Symbols (fast)
# python examples.py list WMT
# python examples.py list WMT AAPL MSFT TSLA

# Download historical quotes for all symbols in a Robinhood watchlist (Time consuming)
# python examples.py full 
