"""
Filtering dataframe based on columns
"""
#!/bin/env python3
import fileread

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
    # if not is_numeric_dtype(df[colname]):
    #     return "Non-numeric column selectec"
    df = df.where((df[colname] >= lower_bound) & (df[colname] <= upper_bound))
    return df.dropna()
    

# print(interval_filter(df, "Kalenderår", 2019, 2020))


