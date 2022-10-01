#!/bin/env python3
import pandas as pd

def read_file(filename):
    filetype = get_filetype(filename)
    if filetype == "CSV":
        try:
            return pd.read_csv(filename, sep = ",")
        except:
            return pd.read_csv(filename, sep = ";")
    elif filetype == "TSV":
        return pd.read_csv(filename, sep='\t')
    elif filetype == "XLS" or filetype == "XLSX":
        return pd.read_excel(filename)
    return None
 
def save_file(filename):
    df = pd.Dataframe[filename]
    df._to_csv('filename', encoding='utf-8', index=False)

def check_content(filename)
    # checks max rows, which the files has 600 something..
    pd.set_option('max_info_columns', 600)
    df.info()
    # check types
    df.dtypes
    for i, v in enumerate(df.columns)
    print (i,v)




get_filetype(filename):
    if filename[-4:] == ".csv":
        return "CSV"
    if filename[-4:] == ".tsv":
        return "TSV"
    if filename[-4:] == ".xls":
        return "XLS"
    if filename[-5:] == ".xlsx":
        return "XLSX"
    return "UNKNOWN"
