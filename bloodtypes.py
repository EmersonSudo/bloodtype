#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:39:51 2022

@author: emerson
"""

#%% Packages

import pandas as pd

#%% dataset

blood = pd.read_csv("bloodtypes.csv")

#%% exploration

#pandas row and col length
blood.shape

blood.head(10)
blood.tail(10)

#check col types
blood.dtypes

#%% data transformation

#changing first col name
blood = blood.rename(columns={'Unnamed: 0' : 'ID'})

#transforming population column
blood['Population'] = blood['Population'].apply(lambda x : x.replace(',', ''))
blood['Population'] = blood['Population'].astype(int)
blood['Population'].dtype

# Blood groups transformation (dropping '%' and transforming into numeric)
blood.iloc[:, 3:11] = blood.iloc[:, 3:11].applymap(lambda x : x.replace('%', ''))
blood.iloc[:, 3:11] = blood.iloc[:, 3:11].apply(pd.to_numeric)
