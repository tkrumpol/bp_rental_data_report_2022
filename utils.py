#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:07:05 2022

@author: tommy
"""

import pandas as pd  # must be recent pandas version to read xlsx file
import matplotlib.pyplot as plt


def read_data_from_excelfile(path: str) -> dict:
    '''
    Read in an excel file with multiple sheets to a dictionary where the 
    key is the sheet name and value is the pandas dataframe of that sheets 
    data
    
    Parameters
    ----------
    path : str
            location of the Excel file
    
    Returns
    -------
    df_dict : dict
            return a dictionary of pandas dataframes where the keys are the 
            sheetnames from the excel file    
    
    '''
    
    xlsx = pd.ExcelFile(path)
    
    df_dict = dict()
    for sheet in xlsx.sheet_names:
        df_dict[sheet] = pd.read_excel(xlsx, sheet, index_col=False)
    
    return df_dict


def uppercase_cities(cities: list) -> list:
    '''
    Helper function to capitalize all cities in the input list.
    
    Parameters
    ----------
    cities : list
            list of cities input by the user
    
    Returns
    -------
    cities : list
            the same list is returned but each element has the .upper()
            method applied to it
    
    '''
    
    return [city.upper() for city in cities]


def common_df_reformatting(df: pd.DataFrame()) -> pd.DataFrame():
    '''
    Perform the same reformatting to every sheet in the excel file.
    They all follow the same formatting. 
    
    Parameters
    ----------
    df: pd.DataFrame()
            dataframe corresponding to one of the excel sheets from the
            input data
    
    Returns
    -------
    df: pd.DataFrame()
            the same dataframe with formatting applied
    
    '''
    
    df.drop(0, inplace=True) # for median rent dataframe only, no secondary indexing

    # renaming column headers based on row below it
    rename_mapper = dict()
    for col in df.columns:
        rename_mapper[col] = df[col].iloc[0]
        
    df.rename(columns=rename_mapper, inplace=True)    
    df.drop(1, inplace=True) # resetting index once more. 
    
    return df


def median_rent_YoY(df: pd.DataFrame(), 
             cities: list,
             plot: bool) -> pd.DataFrame():
    '''
    Finction to take the last sheet, median rent YoY and organize and plot
    some of the data/cities if specified. Could be pslit up into multiple
    functions. One to split one to plot. 
    
    Parameters
    ----------
    df : pd.DataFrame
            the median rent YoY dataframe
    
    cities : list
            list of cities to plot the data from. 
    
    plot : bool
            plot the data for the specified cities or not 
    
    Returns
    -------
    df : pd.DataFrame
            The same dataframe but organized. Need to write more detail 
            on this
    
    '''
    
    cities = uppercase_cities(cities)  # all cities in list uppercased
    name_of_sheet = df.iloc[0,0]  # 'Median Rent_YoY (%)'
    common_df_reformatting(df)  # perform data reformatting. Done 'inplace'
    df.set_index('Largest 100 Cities', inplace=True)  # sheet specific
    
    if plot:
        for city in cities:    
            df.loc[city].plot(label=city)
            
        plt.xlabel('date')
        plt.ylabel('percent (%) change')
        plt.title(f'{name_of_sheet}')
        plt.legend()

    
    return df


if __name__ == '__main__':
    import os
    
    folder_path = os.getcwd() + '/data/Rent_Data_March2022_.xlsx'
    data = read_data_from_excelfile(folder_path)
    city = ['PITTSBURGH, PA', 'ATLANTA, GA'] # all caps
    
    median_rent_YoY(df=data['Median Rent_YoY (%)'], cities=city, plot=True)




