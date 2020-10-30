# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:48:26 2020

@author: airar
"""

import pandas as pd
from pandas_datareader import data, wb
import datetime
from datetime import date, timedelta

current_date = date.today().isoformat()   
days_before = (date.today()-timedelta(days=30)).isoformat()

start = pd.to_datetime(days_before)
end = pd.to_datetime(current_date)

userStock = input("Enter the Stock you want to predict: ") 
print("Retrieving " + userStock + " data from the past month...") 

monthlyStock = data.DataReader('TSLA', 'yahoo', start , end)

print(monthlyStock)

print("Predicting value for the next date...")
days_after = (date.today()+timedelta(days=1)).isoformat()
