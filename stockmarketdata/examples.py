import sys
import stockmarketdata.dl_quotes as dlq
import stockmarketdata.ally as ally


# -----------------------------------------
# Update your credentials and preferences |
# -----------------------------------------
av_key = 'YOUR_ALPHAVANTAGE_KEY'

filePath = "C:\\YOUR\\PATH\\"  # where to place the historical csv files.

rh_email = 'YOUR_EMAIL_WITH_ROBINHOOD@MAIL.COM'
rh_password = 'YOUR_ROBINHOOD_PASSWORD'
rh_watchlist = "Default"  # The Robinhood watchlist to pull symbols from.

ally_consumer_key = 'YOUR_ALLY_CONSUMER_KEY'
ally_secret = 'YOUR_ALLY_SECRET'
ally_oauth_token = 'YOUR_ALLY_OAUTH_TOKEN'
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
    
