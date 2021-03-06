# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 09:16:43 2021
Topic: Exploring Dictionaries in Python
@author: Michael Quinlan
"""

'''
input: Melbourne housing dataset from Kaggle
output: modified dataframe based on exercises
'''

import pandas as pd

# identify columns of original data to use in subset
cols = ['Price', 'Landsize', 'Distance', 'Type', 'Regionname'] 
data = pd.read_csv('melb_data.csv', usecols = cols, 
                   dtype = {'Price': 'int'}, # convert price data to integer type
                   na_values = {'Landsize':9999, 'Regionname':'?'}) # set na values
pd.set_option('max_columns', None)
data.head()

# use a dictionary to find aggregate data for 'Distance' type subgroups (h, t, u)
distance = data[['Type', 'Distance']].groupby('Type').agg(
    ['mean', 'median', 'max', 'min'])

# use a dictionary to aggregate values for multiple columns
aggregate = data.groupby('Type').agg(
    {'Distance':'mean', # find mean of distance
     'Price':lambda x: sum(x) / 1_000_000}) # sum price and divide by 1,000,000

# apply a round function to entire dictionary at once
aggregate_round = data.groupby('Type').agg(
    {'Distance':'mean',
     'Price': lambda x: sum(x) / 1_000_000}).round(
    {'Distance': 2, 'Price': 1})

# dictionaries also add value to the replace
# by using nested dictionaries, we can specify the column, the balue to be 
# replaced, and the value to be used as repalcement
data.replace({'Type':{'h':'house'}, 
              'Regionname':{'Northern Metropolitan':'Northern'}
              }).head()