from file_handler import read_file, get_filetype, FilenameException
from filter import *
import pandas as pd

def input_control(user_input, n_options):
    """ Control that user_input is a valid input
    :param user_input: input value from user
    :type user_input: String
    :return: Input value casted as an integer, or None
    :rtype: int or None
    """
    if user_input.isdigit() and 0 < int(user_input) <= n_options:
        return int(user_input)
    else: return None

def start_up_meny():
    """Start up meny for the program

    :return: A path to an existing file
    :rtype: String
    """
    data_dict = {
    "1.": "25_years_of_salgskimmer.csv",
    "2.": "helarsprestationer_from_2017.csv"
    }
    options_dict = {
    "1.": "Own file",
    "2.": "From datafolder"    
    }
    while True:
        for choice in options_dict:
            print(choice, options_dict[choice])
        user_input = input("Do you want to choose your own file or a file from our datafolder\n:")
        user_choice = input_control(user_input, 2)
        if user_choice == 1:
            path = input("Give me your file path\n:")
            try:
                read_file(path)
                return path
            except FilenameException:
                print("Could not find the file you were looking for, please try again!")
        elif user_choice == 2:
            for choice in data_dict:
                print(choice, data_dict[choice])
            user_input = input("Choose a file!\n:")
            user_choice = input_control(user_input, 2)
            if user_choice is not None:
                path = "projectdata/"+ data_dict[(str(user_choice)+".")]
                return path
            else: print("Something went wrong, please try again!")
        else: print("Something went wrong, please try again!")

def convert_to_numeric(val):
    """convert to numeric if decimal == ','

    :param val: value
    :type val: object
    :return: the intended value
    :rtype: float64
    """
    new_val = val.replace(',','.')
    return float(new_val)

def change_dtypes(df):
    for col in df.columns:
        if pd.api.types.is_object_dtype(df[col]):
            try:
                df[col] = df[col].apply(convert_to_numeric)
            except ValueError:
                df[col] = df[col]
    return df

def undo_change_df(df):
    return df.versions[-2]

def undo_all_changes_df(df):
    return df.versions[0]

class File:
  def __init__(self, path):
    self.path = path
    self.type = get_filetype(path)
    self.df = read_file(path)

def app():
    menu_dict = {
    "1.": "Show DataFrame",   
    "2.": "Filter file",
    "3.": "Show file summary", 
    "4.": "Graph data",
    "5.": "Save current dataframe",
    "6.": "End program"
    }
    while True:
        for choice in menu_dict:
            print(choice, menu_dict[choice])
        user_input = input("Please select an option!\n:")
        user_choice = input_control(user_input, 6)

        if user_choice == 1:
            pass
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass            
        elif user_choice == 4:
            pass
        elif user_choice == 5:
            pass
        elif user_choice == 6:
            # Ask if Save df, save graphs
            print("Goodbye!")
            break
        else:
            print("Please select a valid option!\n:")

def main():
    path = start_up_meny() # get file_path
    data = File(path)
    df = data.df
    print(df)


if __name__ == '__main__':
    main()