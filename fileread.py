#!/bin/env python3
import pandas as pd

#Convert TSV file to CSV..
#with open("filename.tsv") as file:
#    # Passing tsv.file to reader(), and with tab delimiter
#    tsv_file = csv.reader(file, delimiter="\t")
#
#    for line in tsv_file:
#        print(line)

# Using split? data = []
# for line in f:
# l=line.split('\n'). reads line by line
#  data.append(l). splits data and stores lists.
# for i in data: print (i)

def load_file(filepath):
    data = []
    col = []
     #checkcol = false, should this be here?
    with open(filepath) as f:
        for val in f.readlines():
            val = val.replace("\n")
            val = val.split(',')
            # something to check stored data, maybe use checkcol?
            # if checkcol is false: col = val, checkcol = true.

def id_file(filename):
    if filename[-4:] == ".csv":
        return "CSV"
    if filename[-4:] == ".tsv":
        return "TSV"
    if filename[-4:] == ".xls":
        return "XLS"
    if filename[-5:] == ".xlsx":
        return "XLSX"

    return "UNKNOWN"
