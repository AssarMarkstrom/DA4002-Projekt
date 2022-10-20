#!/bin/env python3
import pandas as pd

class FilenameException(Exception):
    """ Class to create our own exception to detect filenames.

    :param Exception: Specific Exception
    :type Exception: Exception
    """
    def __init__(self):
        pass

def convert_to_numeric(val):
    """ Convert to numeric if decimal seperator is, instead of .

    :param val: row-value
    :type val: pandas.object
    :return: converted row-value
    :rtype: float64
    """
    new_val = val.replace(',','.')
    return float(new_val)

def change_dtypes(df):
    """ If pandas auto-detected object dtype try to convert to numeric 

    :param df: DataFrame
    :type df: pandas.DataFrame
    :return: Dataframe with changed dtypes
    :rtype: pandas.DataFrame
    """
    for col in df.columns:
        if pd.api.types.is_object_dtype(df[col]):
            try:
                df[col] = df[col].apply(convert_to_numeric)
            except ValueError:
                df[col] = df[col]
    return df

def read_file(filename):
    """ Checks what filenames it is from get_filetype() and read it's contents. 
    Ex: If the filename is a csv, it will be comma seperated.
    The FilnameException detects files that are unknown. 
    Reads file using pandas

    :param filename: filename
    :type filename: str
    :raises FilenameException: if filetype can not be interpreted
    :return: DataFrame
    :rtype: pandas.DataFrame
    """
    filetype = get_filetype(filename)
    if filetype == "CSV":
        try:
            return pd.read_csv(filename, sep = ",")
        except:
            return change_dtypes(pd.read_csv(filename, sep = ";"))
    elif filetype == "TSV":
        return change_dtypes(pd.read_csv(filename, sep='\t'))
    elif filetype == "XLS" or filetype == "XLSX":
        return change_dtypes(pd.read_excel(filename))
    raise FilenameException()
 
def save_file(filename, df):
    """ Save the file based on what type of file it is.
    Example: if it is a CSV, in the unittest it will save a tmp.csv on github. 
    Due to os, it removes the file so th it does not intefere with other files. 

    :param filename: filename
    :type filename: str
    :param df: DataFrame
    :type df: pandas.DataFrame
    """
    
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
    """ Gets the filetype and helps the read_file 
    chose the correct type of the file. 

    :param filename: filename   
    :type filename: str
    :return: filetype
    :rtype: str
    """
    if filename[-4:] == ".csv":
        return "CSV"
    if filename[-4:] == ".tsv":
        return "TSV"
    if filename[-4:] == ".xls":
        return "XLS"
    if filename[-5:] == ".xlsx":
        return "XLSX"
    return "UNKNOWN"
    
def save_app(data):
    """ Saves file locally on user's computer

    :param data: Object created from class File
    :type data: Object
    """
    file_name = input("Chose filename\n: ")
    file_type = input("Chose filetype\n: ")
    while file_type not in ["csv" , "xlsx", "tsv", "xls"]: # If user's file type not recognised 
        print("Invalid filetype, try again, csv, tsv, xls or xlsx")
        file_type = input("Chose filentype\n: ")
    my_file = file_name + "." + file_type # Create valid file name
    save_file(my_file, data.get_current()) # Save file