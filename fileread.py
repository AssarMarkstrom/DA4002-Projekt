#!/bin/env python3
import pandas as pd

def read_file(filename, separator=None):
    filetype = get_filetype(filename)
    if filetype == "CSV":
        if not separator:
            separator = ","
        return pd.read_csv(filename, sep=separator)
    elif filetype == "TSV":
        if not separator:
            separator = "\t"
        return pd.read_csv(filename, sep='\t')
    elif filetype == "XLS" or filetype == "XLSX":
        return None
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
