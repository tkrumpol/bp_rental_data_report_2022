#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created April 2022

@author: tom krumpolc

main function to examine bp rental data

pandas 1.3.5 for reading .xlsx files. 


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
