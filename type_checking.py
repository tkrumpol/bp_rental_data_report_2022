#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jun 1 2022

@author: tommy
"""


def is_list_type(obj) -> list():
    '''
    Test whether the object is a list. If it is a single string, such as 
    'PITTSBURGH, PA', then return it with a message as a [list].
    If it is not a string or a list, raise a type error

    Parameters
    ----------
    obj : either a string or list
        python object to test if the object is a list

    Raises
    ------
    TypeError
        if not a string or list, raise an error that this should be a list.

    Returns
    -------
    obj : list
        the same object back if input type was list. if input obj was a str,
        then return [str]

    '''
    
    if isinstance(obj, str):
        obj = [obj]
        print(f'''
              Input should be a list. Single object was detected as
              type str() was converted to list(str()) i.e. {obj}
              ''')
    elif isinstance(obj, list):
        pass
    else:
        raise TypeError("Must be a list. e.x. ['PITTSBURGH, PA'] or ['1']")
        
    return obj
        
     
 