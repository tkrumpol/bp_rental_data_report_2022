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


Take away some user abilities to choose and just create plots for them since
we know there are only 3 choices for bedoom


"""

import os
import matplotlib.pyplot as plt
import pandas as pd
from math import ceil, floor


from utils import (read_data_from_excelfile, plot_median_rent_YoY,
                   format_data)
from RentalData import RentalData
from type_checking import is_list_type


folder_path = os.getcwd() + '/data/Rent_Data_March2022_.xlsx'
data = read_data_from_excelfile(folder_path)
formatted_data = format_data(data)

# testing
cities = ['PITTSBURGH, PA', 'ATLANTA, GA'] # all caps
# cities = ['PITTSBURGH, PA',] # all caps
# cities = 'PITTSBURGH, PA' # all caps

num_bedrooms = ['1']
num_bedrooms = ['1','2', '3']
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

# split_by_city = df.loc[(cities, slice(None)),:]
# split_by_bedroom = df.loc[(slice(None), slice(num_bedrooms)),:]
# split_by_city_and_bedroom = df.loc[(cities, slice(num_bedrooms)),:]


# IDEA
# Use logic to test length of list of cities passed. If its one, then plot
# all bedrooms on one plot. If greater than one, separate out the plots
# but bedroom and city. This condenses the two functions to one. 



def split_by_cities(multiindex_df: pd.DataFrame(), cities: list()
                    ) -> pd.DataFrame():
    '''
    Split a multi indexed df (City, num bedrooms) by cities

    Parameters
    ----------
    multiindex_df : pd.DataFrame
        the dataframe which is indexed by city and number of bedroomms
    cities : list()
        a list of cities to split the dataframe by

    Returns
    -------
    split_df : pd.DataFrame()
        the subset of the mutiindexed df now split by input cities

    '''
    
    split_df = multiindex_df.loc[(cities, slice(None)),:]
    
    return split_df


def split_by_bedroom(multiindex_df: pd.DataFrame(), 
                     num_bedrooms: str()
                     ) -> pd.DataFrame():
    '''
    Split a multi indexed df (City, num bedrooms) by bedroom

    Parameters
    ----------
    multiindex_df : pd.DataFrame
        the dataframe which is indexed by city and number of bedroomms
    cities : list()
        a list of cities to split the dataframe by
    num_bedrooms : str()
        either 1, 2, or 3 bedrooms

    Returns
    -------
    split_df : pd.DataFrame()
        the subset of the mutiindexed df now split by input cities

    ''' 
    
    split_df = multiindex_df.loc[(slice(None), slice(num_bedrooms)),:]
    
    return split_df


def split_by_cities_and_bedroom(multiindex_df: pd.DataFrame(), 
                                cities: list(),
                                num_bedrooms: str()) -> pd.DataFrame():

    '''
    Split a multi indexed df (City, num bedrooms) by cities and bedroom    

    Parameters
    ----------
    multiindex_df : pd.DataFrame
        the dataframe which is indexed by city and number of bedroomms
    cities : list()
        a list of cities to split the dataframe by
    num_bedrooms : str()
        either 1, 2, or 3 bedrooms

    Returns
    -------
    split_df : pd.DataFrame()
        the subset of the mutiindexed df now split by input cities

    '''

    
    split_df = multiindex_df.loc[(cities, slice(num_bedrooms)),:]
    
    return split_df


def bedroom_info_for_given_city(multi: pd.DataFrame(),
                                cities: list,
                                plot: bool) -> pd.DataFrame():
    
    
    cities = is_list_type(cities)
    df_num_bedrooms_for_city = split_by_cities(multiindex_df=multi,
                                               cities=cities)
    
    if plot:
        if len(cities) == 1:
            for row in df_num_bedrooms_for_city.iterrows():
                row[1].plot(label=f'{row[0]} bedroom')
            plt.xlabel('timeline')
            plt.ylabel('Amount($)')
            plt.title('Median rent by bedroom')
            plt.legend()
        
        else:
            # More than one city, create subplots.
            num_figs = len(cities)
            num_cols = num_figs
            num_rows = 1  # ceil(num_figs/num_cols)

            fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, 
                                     figsize=(12, 8))
            fig.suptitle('Median rent by bedroom')
            
            col = 0
        
            for city in cities:
                city_df = df_num_bedrooms_for_city.loc[(city)]
                for row_info in city_df.iterrows():
                    num_bdrms = row_info[0]
                    data = row_info[1]
                    data.plot(ax=axes[col], label=f'{num_bdrms} bedroom')
                axes[col].set_xlabel('timeline')
                axes[col].set_ylabel('Amount($)')
                axes[col].set_title(f'Median rent by bedroom: {city}')
                axes[col].legend()
            
                col += 1 
    
    return df_num_bedrooms_for_city


bedroom_info_for_given_city(multi=df,
                            cities=cities,
                            plot=True)