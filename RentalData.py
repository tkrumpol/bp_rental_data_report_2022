#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:13:50 2022

@author: tommy


Create a class to take in a single or multiple cities and output summary info

10/6
Currently working on all functionality for taking one city and producing a
summary plot. One plot for each excel sheet with info for that single city

"""

import matplotlib.pyplot as plt
import pandas as pd


from utils import (read_data_from_excelfile, plot_median_rent_YoY,
                   format_data)
from type_checking import is_list_type


class RentalData():
    '''
    Class to hold the rental data and its methods after it has been formatted
    by the functions in the utils script
    '''
    
    def __init__(self, data):
        '''
        Initialize rental information
        '''
        
        # Populated from input to class
        self.formatted_data = data  # dict()
        
        # Populated from examining data sheets
        self.property_type = ['house', 'apartment']
        self.number_of_bedrooms = ['1', '2', '3']  
        
        # Populated from the input data. all_cities common to all sheets
        self.all_cities = list(self.formatted_data['Median Rent_YoY (%)'].index)
        self.sheets = list(self.formatted_data.keys())
        
        # Populated from methods in this class
        self.information_for_given_city = dict()
    
    
    def split_by_cities(self,
                        multiindex_df: pd.DataFrame(), 
                        cities: list()
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
    
    
    def summarize_information_for_given_city(self, city: str()):
        '''
        Given a single city, obtain the information from every excel sheet

        Parameters
        ----------
        city : str()
            the city of interest. 

        Returns
        -------
        city_info : dict
            keys are the excel sheet names, values are the formatted_data
            filtered for just that specific city

        '''
        
        
        if isinstance(city, list):
            city = city[0]
        
        if city not in self.all_cities:
            raise Warning(f'''
                          {city} not in top 100 cities. Check spelling.
                          For a list of all cities, use attribute .all_cities
                          ''')
            
        
        city_info = dict()
        for sheet_name, data in self.formatted_data.items():
            if sheet_name == 'Median Rent_YoY (%)':
                city_info[sheet_name] = data.loc[city]
            else:
                df = self.split_by_cities(multiindex_df=data, cities=city)
                city_info[sheet_name] = df
        
        self.information_for_given_city.update({city:city_info})
        
        return city_info
        
    
    def plot_summarized_info_for_given_city(self, city: str()):
        '''
        After summarize_information_for_given_city method has been run for
        an input city, the atttribute self.information_for_given_city[city]
        will be populated with the argument city for this method. 
        
        Take the summarized information and create 6 plots with the
        filted info from each sheet

        Parameters
        ----------
        city : str()
            The city of interest, must be populated already from running
            summarize_information_for_given_city method with same city name.

        Returns
        -------
        None.  produce a plot

        '''
        
        # If a list is passed, only use the first city in the list
        if isinstance(city, list):
            print(f'''
                  Multiple cities: {city} were passed. Only using
                  the first city for plotting {city[0]}
                  ''')
            city = city[0]
        
        city_data = self.information_for_given_city[city]
        
        fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16, 12), sharex=True)
        fig.suptitle(f'Summarized Rental Information for {city}')
        fig.supxlabel('Timeline')
        
        row = 0
        col = 0
        for sheet_name, data in city_data.items():
            # print(f'{sheet_name}: plot position {row, col}')
            if sheet_name == 'Median Rent_YoY (%)':
                data.plot(ax=axes[row,col])
                axes[row,col].set_title(f'{sheet_name}')

            else:
                for info in data.iterrows():
                    info[1].plot(ax=axes[row,col])
                    
                axes[row,col].set_title(f'{sheet_name}')
            
            axes[row,col].legend()
            
            if col == 2:
                col = 0    
                row += 1
            else:
                col += 1
        
        return None 


if __name__ == '__main__':
    
    import os 
    
    folder_path = os.getcwd() + '/data/Rent_Data_March2022_.xlsx'
    data = read_data_from_excelfile(folder_path)
    formatted_data = format_data(data)
    
    cities = ['PITTSBURGH, PA']
    test = RentalData(formatted_data)
    test.summarize_information_for_given_city(cities)
    test.plot_summarized_info_for_given_city(city=cities)
    
    cities = ['PITTSBURGH, PA', 'ATLANTA, GA', 'AUSTIN, TX'] # all caps
    plot_median_rent_YoY(df=formatted_data['Median Rent_YoY (%)'],
                         cities=cities)
