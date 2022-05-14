#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created April 2022

@author: tom krumpolc

main function to examine bp rental data

pandas 1.3.5


Notes:
    - Cities are in all caps
    - Mapper for index to city might be able to be reused for each df

Idea
- given an input city, return dataframe with information from each sheet
"""

import os
import matplotlib.pyplot as plt

from utils import read_data_from_excelfile, median_rent_YoY


folder_path = os.getcwd() + '/data/Rent_Data_March2022_.xlsx'
data = read_data_from_excelfile(folder_path)

city = ['PITTSBURGH, PA', 'ATLANTA, GA'] # all caps


#=====================================================
# Only for final dataframe
#=====================================================
# df = data['Median Rent_YoY (%)']
# name_of_sheet = df.iloc[0,0]

# df = df.iloc[1:,:] # for median rent dataframe only, no secondary indexing

# # renaming column headers based on row below it
# rename_mapper = dict()
# for col in df.columns:
#     rename_mapper[col] = df[col].iloc[0]
    
# df.rename(columns=rename_mapper, inplace=True)    
# df = df.iloc[1:,:] # resetting index once more. 

# df.set_index('Largest 100 Cities', inplace=True)
# for c in city:    
#     df.loc[c].plot(label=c)
    
# plt.xlabel('date')
# plt.ylabel('percent (%) change')
# plt.title(f'{name_of_sheet}')
# plt.legend()



test = median_rent_YoY(df=data['Median Rent_YoY (%)'], cities=city, plot=True)
