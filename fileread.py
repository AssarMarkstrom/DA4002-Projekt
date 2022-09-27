#!/bin/env python3
import pandas as pd

def read_file(filename):
    filetype = get_filetype(filename)
    if filetype == "CSV":
        return pd.read_csv(file_path)
    elif filetype == "TSV":
        return pd.read_csv(file_path, sep='\t')
    elif filetype == "XLS" or filetype == "XLSX":
        return pd.read_excel
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
