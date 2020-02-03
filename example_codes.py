# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:03:05 2020

@author: micah
"""

# Collect preferences and credentials
import preferences
email = preferences.rh_email
password = preferences.rh_password
path_for_files = preferences.my_filePath
avkey = preferences.av_key

# Run the script
import dl_quotes
dl_quotes.dlquotes(email, password, path_for_files, avkey)

