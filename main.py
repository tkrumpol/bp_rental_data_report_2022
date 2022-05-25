#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created April 2022

@author: tom krumpolc

main function to examine bp rental data

pandas 1.3.5 for reading .xlsx files. 

Multiindexing Article:
    https://towardsdatascience.com/how-to-use-multiindex-in-pandas-to-level-up-your-analysis-aeac7f451fce

Notes:
    - Cities are in all caps
    - Mapper for index to city might be able to be reused for each df
       -- If turned into class then make this common attribute

Idea
- given an input city, return dataframe with information from each sheet

Sheet Names
- 'Median Rent & Number of Listing' 
- 'Median Rent_YoY (%)'
- 'Median Rent by Bedrooms'
- 'Median Rent by Bedrooms YoY(%)' 
- 'Median Rent by Type'
- 'Median Rent by Type YoY(%)'

[ ] df = data['Median Rent & Number of Listing' ]
[x] df = data['Median Rent_YoY (%)']
[\] df = data['Median Rent by Bedrooms']
[ ] df = data['Median Rent by Bedrooms YoY(%)' ]
[ ] df = data['Median Rent by Type']
[ ] df = data['Median Rent by Type YoY(%)']

"""

import os
import matplotlib.pyplot as plt

from utils import (read_data_from_excelfile, median_rent_YoY,
                   common_df_reformatting)


folder_path = os.getcwd() + '/data/Rent_Data_March2022_.xlsx'
data = read_data_from_excelfile(folder_path)


city = ['PITTSBURGH, PA', 'ATLANTA, GA'] # all caps


#=====================================================
# Working with median rent by bedrooms
# 
# 2 functions
# - input city, return plots for # bedrroms
# - input cities and # br, return plot with those cities and specification
#=====================================================

df = data['Median Rent by Bedrooms']

name_of_sheet = df.iloc[0,0]
common_df_reformatting(df)

df.fillna(method='ffill', inplace=True)  # forward fill city names for multiindexing

# creating multiindexing with city, #bedrooms. df already sorted but sort_index()
# at the end is best practice for efficient lookup 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html 
multi = df.set_index(['Largest 100 Cities', 'Number of Bedrooms']).sort_index()

# plot pittsburgh one bedroom 
# multi.loc[('PITTSBURGH, PA', '1')].plot()


# multi.loc[('PITTSBURGH, PA', slice(None))]

#                     2017-01-01  ...  2022-02-01
# Number of Bedrooms              ...            
# 1                        935.0  ...      1425.0
# 2                       1150.0  ...      1575.0
# 3                       1300.0  ...      1595.0

# [3 rows x 62 columns]








