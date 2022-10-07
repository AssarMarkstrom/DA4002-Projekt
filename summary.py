#!/bin/env python3
# # Get summary of file
from menus import input_control, get_user_choice
import pandas as pd

def get_colnames(df):
    """" Get colnames from dataframe

    :param df: DataFrame 
    :type df: DataFrame
    :return: list of colnames
    :rtype: list
    """
    return list(df.columns)

def get_numerical_coltypes(df):
    """Help functions to only get numerical col_types

    :param df: DataFrame
    :type df: DataFrame
    :return: DataFrame
    :rtype: DataFrame
    """
    return df.select_dtypes(include=['int64', 'float64']) 

# Numerical data 
def get_mean(df):
    """ Calculate mean of a numerical columns in df

    :param df: DataFrame 
    :type df: DataFrame
    :return: DataFrame
    :rtype: DataFrame
    """
    colnames_list = get_colnames(get_numerical_coltypes(df))
    mean = df[colnames_list].mean()
    return mean

def get_median(df):
    """ Calculate median of a numerical columns in df

    :param df: DataFrame 
    :type df: DataFrame
    :return: DataFrame
    :rtype: DataFrame
    """
    colnames_list = get_colnames(get_numerical_coltypes(df))
    median = df[colnames_list].median()
    return median

def get_std(df):
    """ Calculate std of a numerical columns in df

    :param df: DataFrame 
    :type df: DataFrame
    :return: DataFrame
    :rtype: DataFrame
    """
    colnames_list = get_colnames(get_numerical_coltypes(df))
    std = df[colnames_list].std()
    return std

def get_min(df):
    """ Calculate min of a numerical columns in df

    :param df: DataFrame 
    :type df: DataFrame
    :return: DataFrame
    :rtype: DataFrame
    """
    colnames_list = get_colnames(get_numerical_coltypes(df))
    min = df[colnames_list].min()
    return min

def get_max(df):
    """ Calculate max of a numerical columns in df

    :param df: DataFrame 
    :type df: DataFrame
    :return: DataFrame
    :rtype: DataFrame
    """
    colnames_list = get_colnames(get_numerical_coltypes(df))
    max = df[colnames_list].max()
    return max

# Discrete data 
def get_unique_values_count(df):
    """count # unique values in cols

    :param df: DataFrame
    :type df: DataFrame
    :return: DataFrame
    :rtype: DataFrame
    """
    colnames_list = get_colnames(df)
    list = []
    for col in colnames_list:
        col_unique_values = len(df.drop_duplicates(subset=col, keep = 'first'))
        list.append(col_unique_values)
    df_unique_count = pd.DataFrame([list], index = ['count'], columns=colnames_list)
    return df_unique_count 

def get_duplicate_values_count(df):
    """ count # duplicated values in cols

    :param df: DataFrame
    :type df: DataFrame
    :return: DataFrame
    :rtype: DataFrame
    """
    colnames_list = get_colnames(df)
    list = []
    for col in colnames_list:
        col_unique_values = len(df[[col]]) - len(df.drop_duplicates(subset=col, keep = 'first'))
        list.append(col_unique_values)
    df_unique_count = pd.DataFrame([list], index = ['count'], columns=colnames_list)
    return df_unique_count 

def summary_app(df, menu_summary):
    while True:
        user_choice = get_user_choice(menu_summary, "Please select an option!\n:")

        if user_choice == 1: # Mean
            return get_mean(df)
        
        elif user_choice == 2: # Median
            return get_median(df)

        elif user_choice == 3: # Std
            return get_std(df)

        elif user_choice == 4: # Min
            return get_min(df)

        elif user_choice == 5: # Max
            return get_max(df)

        elif user_choice == 6: # Unique values
            return get_unique_values_count(df)

        elif user_choice == 7: # Duplicate values
            return get_duplicate_values_count(df)

        elif user_choice == 8: # Return to start
            pass
        else:
            print("Please select a valid option!\n:")
