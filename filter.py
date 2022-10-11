from menus import get_col_name_menu, input_control, get_user_choice

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

    return df.dropna(how = 'all')

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
    df = df[lower_bound:upper_bound+1]
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
    return df

def filter_app(data, menu_filter):

    df = data.get_current()
    col_options = list(df.columns)
    col_name_filter_menu = get_col_name_menu(col_options)
    selected_col_list = []
    user_choice = get_user_choice(menu_filter)

    if user_choice == 1: # keep/remove columns
        while True:
            selected_col = get_user_choice(col_name_filter_menu, "Select column name\n:", check = False)
            if selected_col in df.columns and selected_col not in selected_col_list:
                selected_col_list.append(selected_col)
                col_options.remove(selected_col)
                answer = input_control("Select another column? (yes: 1, no: 2)\n: ", 2)
                print("Selected columns:", selected_col_list)
                if answer == 2:
                    while True:
                        question = "Do you want to keep or remove the selected columns (keep: 1, remove: 2)\n:"
                        answer = input_control(question, 2)
                        if answer == 1:
                            return col_select(df, selected_col_list, keep = True)
                        elif answer == 2:
                            return col_select(df, selected_col_list, keep = False)
            else:
                print("Invalid column name, try again!")

    elif user_choice == 2: # Filter by column value
        while True:
            selected_col = get_user_choice(col_name_filter_menu, "What column do you want to filter on? \n:", check = False)
            if selected_col in df.columns:
                break
            else:
                print("Invalid column name, try again!")
        search_value = input("What string/value do you want to filter by? \n:")
        return value_filter(df, selected_col, search_value)

    elif user_choice == 3: # Filter by column value interval
        col_options = get_numerical_coltypes(df)
        while True:
            selected_col = get_user_choice(col_name_filter_menu, "What column do you want to filter on? \n:", check = False)
            if selected_col in df.columns:
                break
            else:
                print("Invalid column name, try again!")
        while True:
            lower_bound = input("Choose lower bound \n:", )
            try:
                lower_bound = float(lower_bound)
                break
            except ValueError:
                print("Non-numeric input, try again")
        while True:
            upper_bound = input("Choose upper bound \n:", )
            try:
                upper_bound = float(upper_bound)
                interval_filter(df, selected_col, float(lower_bound), upper_bound)
                break
            except ValueError:
                print("Non-numeric input, try again")
            except BadBounds:
                print("Upper bound must be larger than lower bound.")                

        return interval_filter(df, selected_col, lower_bound, upper_bound)

    elif user_choice == 4: # Choose row interval
        while True:
            lower_bound = input("Choose lower bound \n:", )
            try:
                lower_bound = int(lower_bound)
                break
            except ValueError:
                print("Non-numeric input, try again")
        while True:
            upper_bound = input("Choose upper bound \n:", )
            try:
                upper_bound = int(upper_bound)
                row_interval(df, int(lower_bound), upper_bound)
                break
            except ValueError:
                print("Non-numeric input, try again")
            except BadBounds:
                print("Upper bound must be larger than lower bound.")
            except OutOfRange:
                print("Row index out of range.")

        return row_interval(df, lower_bound, upper_bound)

    elif user_choice == 5: # return to start
        pass
    else:
        print("Please select a valid option!\n:")
