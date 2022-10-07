"""
Filtering dataframe based on columns
"""

class BadBounds(Exception):
    def __init__(self):
        pass

class OutOfRange(Exception):
    def __init__(self):
        pass


def get_numerical_coltypes(df):
    """Help functions to only get numerical col_types

    :param df: DataFrame
    :type df: DataFrame
    :return: DataFrame
    :rtype: DataFrame
    """
    return df.select_dtypes(include=['int64', 'float64']) 

def col_select(df, col_names, keep = True):
    """
    input:
        df: pandas dataframe
        col_names: list of strings
        Boolean keep: if true df with col_names are returned,
                        else df with col_names removed
    Returns: pandas dataframe
    """
    if keep:
        cols = []
        for col in df.columns:
            if col not in col_names:
                cols.append(col)
        df = df.drop(cols, axis=1)
    else:
        df = df.drop(col_names, axis=1)

    return df


def interval_filter(df, colname, lower_bound, upper_bound):
    """
    Input:
        df: pandas dataframe
        colname: column in df (string)
        lower_bound/upper_bound: Interval which df is filtered on
    Output: Filtered dataframe containing anly rows with values between lower and upper bound
    """
    coltype = df[colname].dtypes
    if lower_bound < 0 or upper_bound < lower_bound:
        raise BadBounds
    if colname not in get_numerical_coltypes(df):  # Check that column is numeric
        raise Exception("Non-numeric column select")
    df = df.where((df[colname] >= lower_bound) & (df[colname] <= upper_bound))
    df[colname] = df[colname].astype(coltype)

    return df.dropna(how='all')


def row_interval(df, lower_bound, upper_bound):
    """
    Input:
        df: pandas dataframe
        lower_bound/upper_bound: Desired row-interval
    Output: Dataframe containing only rows in the given interval 
    """
    if lower_bound < 0 or upper_bound < lower_bound:
        raise BadBounds
    if len(df) < upper_bound:
        raise OutOfRange
    df = df[lower_bound-1:upper_bound]
    return df 


def value_filter(df, colname, value):
    """
    Input:
        df: pandas dataframe
        colname: Name of a column in df (string)
        value:
    Output: Dataframe containing rows which have value in them 
    """
    value = str(value)
    coltype = df[colname].dtypes  # Store column's original datatype
    df[colname] = df[colname].astype(str) # Change column to string
    df = df.where(df[colname].str.contains(value))
    df = df.dropna(how='all')
    df[colname] = df[colname].astype(coltype)

    if len(df) == 0:
        print("Value not found in dataframe")
    return df
