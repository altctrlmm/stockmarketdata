import all_rh_csv.dl_quotes as dlq


# Update your credentials and preferences:
av_key = 'YOUR_ALPHAVANTAGE_KEY'
filePath = "C:\\YOUR\\PATH\\"  # where to place the historical csv files.
rh_email = 'YOUR_EMAIL_WITH_ROBINHOOD@MAIL.COM'
rh_password = 'YOUR_ROBINHOOD_PASSWORD'
rh_watchlist = "Default"  # The Robinhood watchlist to pull symbols from.


# ------------------------------------------------------------------------
# Download Stock Quote History for Every Symbol in a Robinhood Watchlist |
# ------------------------------------------------------------------------
dlq.dlquotes(av_key, filePath, rh_email, rh_password, rh_watchlist)


# ----------------------------------------------------------
# Download OHLCV for Every Symbol in a Robinhood Watchlist |
# ----------------------------------------------------------
wlsymbols = dlq.get_watchlist_symbols(rh_email, rh_password, rh_watchlist)
dlq.simple_quotes(av_key, filePath, wlsymbols)


# ---------------------------------------------
# Download DOHLCV for a List of Stock Symbols |
# ---------------------------------------------
symbol_list = ['BA', 'ALLY', 'F', 'MU', 'SPCE', 'T', 'WMT', 'S']
dlq.simple_quotes(av_key, filePath, symbol_list)
