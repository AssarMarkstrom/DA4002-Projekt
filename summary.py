#!/bin/env python3
# # Get summary of file
from menus import get_user_choice
import pandas as pd

def get_colnames(df):
    """" Get colnames from dataframe

    :param df: DataFrame 
    :type df: pandas.DataFrame
    :return: list of colnames
    :rtype: list
    """
    return list(df.columns)

def get_numerical_coltypes(df):
    """ Remove columns in dataset that are not numerical

    :param df: DataFrame
    :type df: pandas.DataFrame
    :return: DataFrame with numerical columns
    :rtype: pandas.DataFrame
    """
    return df.select_dtypes(include=['int64', 'float64']) 

# Numerical data 
def get_mean(df):
    """ Calculate mean of a numerical columns in dataframe

    :param df: DataFrame 
    :type df: pandas.DataFrame
    :return: DataFrame with mean-value for each column
    :rtype: pandas.DataFrame
    """
    colnames_list = get_colnames(get_numerical_coltypes(df))
    mean = df[colnames_list].mean()
    return mean

def get_median(df):
    """ Calculate median of a numerical columns in dataframe

    :param df: DataFrame 
    :type df: pandas.DataFrame
    :return: DataFrame with median-value for each column
    :rtype: pandas.DataFrame
    """
    colnames_list = get_colnames(get_numerical_coltypes(df))
    median = df[colnames_list].median()
    return median

def get_std(df):
    """ Calculate the standard deviation of a numerical columns in dataframe

    :param df: DataFrame 
    :type df: pandas.DataFrame
    :return: DataFrame with std-value for each column
    :rtype: pandas.DataFrame
    """
    colnames_list = get_colnames(get_numerical_coltypes(df))
    std = df[colnames_list].std()
    return std

def get_min(df):
    """ Calculate min-value of a numerical columns in dataframe

    :param df: DataFrame 
    :type df: pandas.DataFrame
    :return: DataFrame with min-value for each column
    :rtype: pandas.DataFrame
    """
    colnames_list = get_colnames(get_numerical_coltypes(df))
    min = df[colnames_list].min()
    return min

def get_max(df):
    """ Calculate max-value of a numerical columns in dataframe

    :param df: DataFrame 
    :type df: pandas.DataFrame
    :return: DataFrame with max-value for each column
    :rtype: pandas.DataFrame
    """
    colnames_list = get_colnames(get_numerical_coltypes(df))
    max = df[colnames_list].max()
    return max

# Discrete data 
def get_unique_values_count(df):
    """ Count # unique values in columns

    :param df: DataFrame
    :type df: pandas.DataFrame
    :return: DataFrame with # unique values for each column
    :rtype: pandas.DataFrame
    """
    
    list = []
    for col in get_colnames(df):
        col_unique_values = len(df.drop_duplicates(subset=col, keep = 'first'))
        list.append(col_unique_values)
    df_unique_count = pd.DataFrame([list], index = ['count'], columns=get_colnames(df))
    return df_unique_count 

def summary_app(df, menu_summary):
    """ Summary app (menu)

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param menu_summary: Menu
    :type menu_summary: _type_
    :return: _description_
    :rtype: _type_
    """
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

        elif user_choice == 7: # Return to start
            return
        else:
            print("Please select a valid option!\n:")
