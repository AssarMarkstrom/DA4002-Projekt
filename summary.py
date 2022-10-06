#!/bin/env python3
# # Get summary of file
from file_handler import *
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

# df_1 = read_file("testfiles/testfile_sum.csv")
