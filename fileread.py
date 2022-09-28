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
