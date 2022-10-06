from file_handler import read_file, FilenameException, get_filetype, save_file
from filter import *
from menus import *
import pandas as pd
from menus import *

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

def start_up_meny(menu_files, menu_files_options):
    """Start up meny for the program

    :return: A path to an existing file
    :rtype: String
    """
    while True:
        for choice in menu_files:
            print(choice, menu_files[choice])
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
            for choice in menu_files_options:
                print(choice, menu_files_options[choice])
            user_input = input("Choose a file!\n:")
            user_choice = input_control(user_input, 2)
            if user_choice is not None:
                path = "projectdata/"+ menu_files_options[(str(user_choice)+".")]
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

def undo_change_df(data):
    return data.versions[-2]

def undo_all_changes_df(data):
    return data.versions[0]

class File:
  def __init__(self, path):
    self.path = path
    self.type = get_filetype(path)
    self.df = read_file(path)
    self.versions = [self.df]

def app(df, menu_main, menu_filter):
    
    while True:
        for choice in menu_main:
            print(choice, menu_main[choice])
        user_input = input("Please select an option!\n:")
        user_choice = input_control(user_input, 6)

        if user_choice == 1:
            print(df.head())
        elif user_choice == 2:
            # Filter menu
            pass
        elif user_choice == 3:
            pass            
        elif user_choice == 4:
            # Graph menu
            pass
        elif user_choice == 5:
            break
            file_name = input("Chose filename\n: ")
            file_type = input("Chose filentype\n: ")
            while file_type not in ["csv" , "xlsx", "tsv", "xls"]:
                print("Invalid filetype, try again, csv, tsv, xls or xlsx")
                file_type = input("Chose filentype\n: ")            
            my_file = file_name + "." + file_type
            save_file(my_file, df)
        elif user_choice == 6:
            # Ask if Save df, save graphs
            print("Goodbye!")
            break
        else:
            print("Please select a valid option!\n:")

def main():
    path = start_up_meny(get_menu_files(), get_menu_files_options()) # get file_path
    data = File(path)
    app(data.versions[-1], get_menu_main(), get_menu_filter())
    


if __name__ == '__main__':
    main()
