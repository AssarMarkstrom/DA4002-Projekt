#!/bin/env python3
import pandas as pd

# out own excpetion.
class FilenameException(Exception):
    def __init__(self):
        pass

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
    raise FilenameException()
 
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
