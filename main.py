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
import pandas as pd


from utils import (read_data_from_excelfile, plot_median_rent_YoY,
                   format_data)
from type_checking import is_list_type


folder_path = os.getcwd() + '/data/Rent_Data_March2022_.xlsx'
data = read_data_from_excelfile(folder_path)
formatted_data = format_data(data)

# testing
city = ['PITTSBURGH, PA', 'ATLANTA, GA'] # all caps
city = ['PITTSBURGH, PA',] # all caps
city = 'PITTSBURGH, PA' # all caps

num_bedrooms = ['1']
num_bedrooms = ['1','2']
num_bedrooms = '1'

#=====================================================
# Working with median rent by bedrooms
# 
# 2 functions
# - input city, return plots for # bedrroms
# - input cities and # br, return plot with those cities and specification
#=====================================================

df = formatted_data['Median Rent by Bedrooms']

# plot pittsburgh one bedroom 
# df.loc[('PITTSBURGH, PA', '1')].plot()

split_by_city = df.loc[(city, slice(None)),:]
split_by_bedroom = df.loc[(slice(None), slice(num_bedrooms)),:]
split_by_city_and_bedroom = df.loc[(city, slice(num_bedrooms)),:]


# IDEA
# Use logic to test length of list of cities passed. If its one, then plot
# all bedrooms on one plot. If greater than one, separate out the plots
# but bedroom and city. This condenses the two functions to one. 

def bedroom_info_for_given_city(multi: pd.DataFrame(),
                                city: list,
                                plot: bool) -> pd.DataFrame():
    
    
    city = is_list_type(city)
    df_num_bedrooms_for_city = multi.loc[(city, slice(None))]
    
    if plot:
        if len(city) == 1:
            for row in df_num_bedrooms_for_city.iterrows():
                row[1].plot(label=f'{row[0]} bedroom')
            plt.xlabel('timeline')
            plt.ylabel('Amount($)')
            plt.title('Median rent by bedroom')
            plt.legend()
        
        else:
            # More than one city, create subplots.
            for each_city in city:
                city_df = df_num_bedrooms_for_city.loc[(each_city)]
                plt.figure()
                for row in city_df.iterrows():
                    row[1].plot(label=f'{row[0]} bedroom')
                plt.xlabel('timeline')
                plt.ylabel('Amount($)')
                plt.title('Median rent by bedroom: {each_city}')
                plt.legend()
            # fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
            # fig.suptitle('Median rent by bedroom')
            
            # BO_model.results_dict['p_estimator'].Z.plot(ax=axes[0,0])
            # axes[0,0].set_title('Unnoised State Profiles - Z')
            
            # BO_model.results_dict['p_estimator'].C.plot(ax=axes[0,1])
            # axes[0,1].set_title('Noised Concentration Profiles - C')
    
    return df_num_bedrooms_for_city


bedroom_info_for_given_city(multi=split_by_bedroom,
                            city=city,
                            plot=True)