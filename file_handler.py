#!/bin/env python3
import pandas as pd

# made our own exception to detect filenames.
class FilenameException(Exception):
    def __init__(self):
        pass

# Definition read_file checks what filenames it is from get_filetype
# and read it's contents. 
# Examples if the filename is a csv, it will be comma seperated.
# the FilnameException detects files that are unknown. 
def convert_to_numeric(val):
    """convert to numeric if decimal == ','

    :param val: value
    :type val: object
    :return: the intended value
    :rtype: float64
    """
    new_val = val.replace(',','.')
    return float(new_val)

def change_dtypes(df):
    for col in df.columns:
        if pd.api.types.is_object_dtype(df[col]):
            try:
                df[col] = df[col].apply(convert_to_numeric)
            except ValueError:
                df[col] = df[col]
    return df

def read_file(filename):
    filetype = get_filetype(filename)
    if filetype == "CSV":
        try:
            return change_dtypes(pd.read_csv(filename, sep = ","))
        except:
            return change_dtypes(pd.read_csv(filename, sep = ";"))
    elif filetype == "TSV":
        return change_dtypes(pd.read_csv(filename, sep='\t'))
    elif filetype == "XLS" or filetype == "XLSX":
        return change_dtypes(pd.read_excel(filename))
    raise FilenameException()
 
# Definition save_file will save the file based on what type of file it is.
# Example: if it is a CSV, in the unittest it will save a tmp.csv on github. 
# Due to os, it removes the file so th it does notat intefere with other files. 

def save_file(filename, df):
    filetype = get_filetype(filename)
    if filetype == "CSV":
        df.to_csv(filename, encoding='utf-8', index=False)
    elif filetype == "TSV":
        df.to_csv(filename, encoding='utf-8', index=False, sep= "\t")
    elif filetype == "XLS" or filetype == "XLSX":
        df.to_excel(filename, index=False, engine='openpyxl')
    else:
        raise FilenameException()

# Definition get_filetype, gets the filetype and helps the read_file,
# get the type of file that is meant to be read. 

def get_filetype(filename):
    if filename[-4:] == ".csv":
        return "CSV"
    if filename[-4:] == ".tsv":
        return "TSV"
    if filename[-4:] == ".xls":
        return "XLS"
    if filename[-5:] == ".xlsx":
        return "XLSX"
    return "UNKNOWN"
