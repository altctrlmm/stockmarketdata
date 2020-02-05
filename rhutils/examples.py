# -*- coding: utf-8 -*-

# Download Stock Quote History for Every Symbol in a Robinhood Watchlist
import rhutils.dl_quotes as dlq

# Update your credentials and preferences:
av_key='YOUR_ALPHAVANTAGE_KEY'
historical_filePath = "C:\\YOUR\\PATH\\" # where to place the historical csv files.
rh_email = 'YOUR_EMAIL_WITH_ROBINHOOD@MAIL.COM'
rh_password = 'YOUR_ROBINHOOD_PASSWORD'
rh_watchlist = "Default" # The Robinhood watchlist to pull symbols from.

# Run this function 
dlq.dlquotes( av_key, historical_filePath, rh_email, rh_password, rh_watchlist )
