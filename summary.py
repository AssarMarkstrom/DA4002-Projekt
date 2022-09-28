"""
Summary of file
"""

from fileread import *

def show_head(df, colnames):
    head = df[[colnames]].head()
    return print(head)

def show_mean(df, colnames):
    mean = df[colnames[0]].mean()
    return print(mean)

def show_median(df, colnames):
    median = df[colnames[0]].median()
    return print(median)

def show_standard_deviation(df, colnames):
    standard_deviation = df[colnames[0]].std()
    return print(standard_deviation)

df = read_file(".\projectdata\helarsprestationer_from_2017.csv")
colnames = "Total"

show_head(df, colnames)
