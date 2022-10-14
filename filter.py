from menus import get_col_name_menu, input_control, get_user_choice

class BadBounds(Exception):
    """Class to create our own exception to detect invalid bounds

    :param Exception: Specific exception
    :type Exception: Exception
    """
    def __init__(self):
        pass
class OutOfRange(Exception):
    """ Class to create our own exception to detect out of range row numbers

    :param Exception: Specific exception
    :type Exception: Exception
    """
    def __init__(self):
        pass

def get_numerical_coltypes(df):
    """ Help function to only get numerical dtypes for columns

    :param df: DataFrame
    :type df: pandas.DataFrame
    :return: DataFrame
    :rtype: pandas.DataFrame
    """
    return df.select_dtypes(include=['int64', 'float64']) 

def col_select(df, col_names, keep = True):
    """ Select columns to keep/remove from dataframe

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param col_names: Name of columns in dataframe
    :type col_names: list
    :param keep: Removes columns if False, defaults to True
    :type keep: bool, optional
    :return: DataFrame
    :rtype: pandas.DataFrame
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
    """  Keep rows of dataframe with values in selected column between lower and upper bound

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param colname: Name of numeric column in DataFrame
    :type colname: str
    :param lower_bound: Lower bound of search interval
    :type lower_bound: float64
    :param upper_bound: Upper bound of search interval
    :type upper_bound: float64
    :raises BadBounds: Exception for invalid interval
    :raises Exception: Exception non numeric
    :return: Dataframe
    :rtype: pandas.DataFrame
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
    """ Keep rows of dataframe in interval lower_bound, upper_bound

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param lower_bound: Lower bound of wanted row number
    :type lower_bound: int
    :param upper_bound: Upper bound of wanted row number
    :type upper_bound: int
    :raises BadBounds: Exception for invalid bounds
    :raises OutOfRange: Exception for out of range row numbers
    :return: DataFrame
    :rtype: pandas.DataFrame
    """
    if lower_bound < 0 or upper_bound < lower_bound:
        raise BadBounds
    if len(df) < upper_bound:
        raise OutOfRange
    df = df[lower_bound:upper_bound+1]
    return df 

def value_filter(df, colname, value):
    """ Keep rows of dataframe where input value is found in chosen column

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param colname: Name of column in dataframe
    :type colname: str
    :param value: Pattern to filter by
    :type value: any
    :return: DataFrame
    :rtype: pandas.DataFrame
    """
    value = str(value)
    coltype = df[colname].dtypes  # Store column's original datatype
    df[colname] = df[colname].astype(str) # Change column to string
    df = df.where(df[colname].str.contains(value, case = False))
    df = df.dropna(how='all')
    df[colname] = df[colname].astype(coltype)
    return df

def filter_app(data, menu_filter):
    """ Filter menu for the program
    
    :param data: Object created from class File
    :type data: File object
    :param menu_filter: Menu options for filter
    :type menu_filter: dict
    :return: DataFrame
    :rtype: pandas.DataFrame
    """
    df = data.get_current()
    col_options = list(df.columns)
    selected_col_list = []
    user_choice = get_user_choice(menu_filter)

    if user_choice == 1: # keep/remove columns
        while True:
            selected_col = get_user_choice(get_col_name_menu(col_options), "Select column name\n:", check = False)
            if selected_col in df.columns and selected_col not in selected_col_list:
                selected_col_list.append(selected_col)
                col_options.remove(selected_col)
                if len(col_options) > 0:
                    answer = input_control("Select another column? (yes: 1, no: 2)\n: ", 2)
                    if answer == 1:
                        print("Selected columns:", selected_col_list)
                        continue
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
            selected_col = get_user_choice(get_col_name_menu(col_options), "What column do you want to filter on? \n:", check = False)
            if selected_col in df.columns:
                break
            else:
                print("Invalid column name, try again!")
        search_value = input("What string/value do you want to filter by? \n:")
        return value_filter(df, selected_col, search_value)

    elif user_choice == 3: # Filter by column value interval
        col_options = get_numerical_coltypes(df)
        while True:
            selected_col = get_user_choice(get_col_name_menu(col_options), "What column do you want to filter on? \n:", check = False)
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
