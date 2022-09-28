#!/bin/env python3
from ast import Try
import pandas as pd

def read_file(filename):
    filetype = get_filetype(filename)
    if filetype == "CSV":
<<<<<<< HEAD
        if not separator:
            seperator = ";"   
            """
            try:
                pd.read_csv(filename[:, 0], seperator = ",")
                seperator = ","
            except:
                seperator = ";"
            """
        return pd.read_csv(filename, sep=separator)
=======
        try:
            return pd.read_csv(filename, sep = ",")
        except:
            return pd.read_csv(filename, sep = ";")
>>>>>>> 52673b7 (fixed issues on read_file_test)
    elif filetype == "TSV":
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

<<<<<<< HEAD
    return "UNKNOWN"
=======
    return "UNKNOWN"

#print(read_file("testfiles/helarsprestationer_from_2017.csv"))
>>>>>>> 52673b7 (fixed issues on read_file_test)
