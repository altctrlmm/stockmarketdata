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


# ----------------------------------------------------------------------------
# Download Current OHLCV from Ally for Every Symbol in a Robinhood Watchlist |
# ----------------------------------------------------------------------------
rh_symbols = dlq.get_watchlist_symbols(rh_email, rh_password, rh_watchlist)
ally.get_ohlcv_from_ally(ally_consumer_key, ally_secret, ally_oauth_token,
    ally_oauth_secret, rh_symbols, filePath)


# --------------------------------------------------------------
# Download Current OHLCV from Ally for a List of Stock Symbols |
# --------------------------------------------------------------
ally_symbols = ['WORK', 'SPCE', 'BILI']
ally.get_ohlcv_from_ally(ally_consumer_key, ally_secret, ally_oauth_token,
    ally_oauth_secret, ally_symbols, filePath)


# ----------------------------------------------------------------------------------
# Download historical quotes for all symbols in a Robinhood watchlist to CSV files |
# ----------------------------------------------------------------------------------
dlq.dlquotes(av_key, filePath, rh_email, rh_password, rh_watchlist)


# ------------------------------------------------------------------------------------
# Download Current OHLCV from AlphaVantage for Every Symbol in a Robinhood Watchlist |
# ------------------------------------------------------------------------------------
wlsymbols = dlq.get_watchlist_symbols(rh_email, rh_password, rh_watchlist)
dlq.simple_quotes(av_key, filePath, wlsymbols)


# ----------------------------------------------------------------------
# Download Current OHLCV from AlphaVantage for a List of Stock Symbols |
# ----------------------------------------------------------------------
symbol_list = ['BA', 'ALLY', 'F', 'MU', 'SPCE', 'T', 'WMT', 'S']
dlq.simple_quotes(av_key, filePath, symbol_list)
