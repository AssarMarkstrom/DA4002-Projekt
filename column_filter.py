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


# df = fileread.read_file(".\projectdata\helarsprestationer_from_2017.csv")
