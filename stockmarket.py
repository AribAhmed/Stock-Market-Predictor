# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:48:26 2020

@author: airar
"""

import pandas as pd
from pandas_datareader import data, wb
import datetime

start = pd.to_datetime('2020-10-01')
end = pd.to_datetime('today')

tesla_df = data.DataReader('TSLA', 'yahoo', start , end)
tesla_df

print(tesla_df)