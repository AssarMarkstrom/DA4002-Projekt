#!/bin/env python3
"""
Reading and saving files
"""

import pandas as pd

def file_read(file_path):

    filetype = file_path[-4:]

    if filetype == ".csv":
        df = pd.read_csv(file_path)
    elif filetype == ".tsv":
        df = pd.read_csv(file_path,sep='\t')
    elif filetype == ".xls" or file_path[-5:] == ".xlsx":
        df = pd.read_excel(file_path)
    else:
        raise Exception("Invalid file format")

    return df


def detect_NAs(df):
    print(df[df.isna().any(axis=1)])
    

#file_read(".\testfiles\25_years_of_salgskimmer.csv")
pd.show_versions()
