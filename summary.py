"""
Summary of file
"""

from fileread import *
from column_filter import *

def show_head(df):
    head = df.head()
    print(head)

def show_mean(df):
    mean = df.mean()
    print(mean)

def show_median(df):
    median = df.median()
    print(median)

def show_standard_deviation(df):
    standard_deviation = df.std()
    print(standard_deviation)
"""
df = read_file(".\projectdata\helarsprestationer_from_2017.csv")
colnames = "Total"

show_head(df, colnames)
"""
