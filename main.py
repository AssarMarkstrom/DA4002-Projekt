from file_handler import read_file, FilenameException, get_filetype, save_file
from menus import get_col_name_menu, get_menu_files, get_menu_files_options, get_menu_main, get_menu_filter, get_menu_summary
from filter import col_select, value_filter, interval_filter, row_interval, BadBounds, OutOfRange, get_numerical_coltypes
from summary import get_max, get_mean, get_median, get_std, get_min, get_max, get_duplicate_values_count, get_unique_values_count
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

def start_up_meny(menu_files_options, menu_files):
    """Start up meny for the program

    :return: A path to an existing file
    :rtype: String
    """
    while True:
        for choice in menu_files_options:
            print(choice, menu_files_options[choice])
        user_input = input("Do you want to choose your own file or a file from our datafolder\n:")
        user_choice = input_control(user_input, len(menu_files_options))
        if user_choice == 1:
            path = input("Give me your file path\n:")
            try:
                read_file(path)
                return path
            except FilenameException:
                print("Could not find the file you were looking for, please try again!")
        elif user_choice == 2:
            for choice in menu_files:
                print(choice, menu_files[choice])
            user_input = input("Choose a file!\n:")
            user_choice = input_control(user_input, len(menu_files))
            if user_choice is not None:
                path = "projectdata/"+ menu_files[(str(user_choice)+".")]
                return path
            else: print("Something went wrong, please try again!")
        else: print("Something went wrong, please try again!")

class File:
    def __init__(self, path):
        self.path = path
        self.type = get_filetype(path)
        self.df = read_file(path)
        self.versions = [self.df]
        
def filter_app(data, menu_filter):
    df = data.versions[-1]
    for choice in menu_filter:
        print(choice, menu_filter[choice])
    user_input = input("Please select an option!\n:")
    user_choice = input_control(user_input, len(menu_filter))
    col_options = list(df.columns)
    if user_choice == 1: # remove columns
        selected_col_list = []
        while True:
            col_name_filter_menu =  get_col_name_menu(col_options)
            for choice in col_name_filter_menu:
                print(choice, col_name_filter_menu[choice])
            print("Selected columns:", selected_col_list)
            selected_col = input("Select column name\n:")
            if selected_col in df.columns and selected_col not in selected_col_list:
                selected_col_list.append(selected_col)
                col_options.remove(selected_col)
                user_answer = input("Select another column? (yes: 1, no: 2)\n: ", )
                answer = input_control(user_answer, 2)
                if answer == 2:
                    while True:
                        keep = bool
                        print("Selected columns:", selected_col_list)
                        user_answer = input("Do you want to keep or remove the selected columns"+
                        "(keep: 1, remove: 2)\n: ", )

                        answer = input_control(user_answer, 2)
                        if answer == 1:
                            keep = True
                            return col_select(df, selected_col_list, keep)
                        elif answer == 2:
                            keep = False
                            return col_select(df, selected_col_list, keep)
            else:
                print("Invalid column name, try again!")

    elif user_choice == 2: # Filter by column value
        while True:
            col_name_filter_menu =  get_col_name_menu(col_options)
            for choice in col_name_filter_menu:
                print(choice, col_name_filter_menu[choice])
            selected_col = input("What column do you want to filter on? \n:", )

            if selected_col in df.columns:
                break
            else:
                print("Invalid column name, try again!")

        search_value = input("What string/value do you want to filter by? \n:", )
        return value_filter(df, selected_col, search_value)

    elif user_choice == 3: # Filter by column value interval
        col_options = get_numerical_coltypes(df)
        while True:
            col_name_filter_menu =  get_col_name_menu(col_options)
            for choice in col_name_filter_menu:
                print(choice, col_name_filter_menu[choice])
            selected_col = input("What column do you want to filter on? \n:", )

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

def summary_app(df, menu_summary):
    while True:
        for choice in menu_summary:
            print(choice, menu_summary[choice])
        user_input = input("Please select an option!\n:")
        user_choice = input_control(user_input, len(menu_summary))

        if user_choice == 1: # Mean
            return get_mean(df)
        
        elif user_choice == 2: # Median
            return get_median(df)

        elif user_choice == 3: # Std
            return get_std(df)

        elif user_choice == 4: # Min
            return get_min(df)

        elif user_choice == 5: # Max
            return get_max(df)

        elif user_choice == 6: # Unique values
            return get_unique_values_count(df)

        elif user_choice == 7: # Duplicate values
            return get_duplicate_values_count(df)

        elif user_choice == 8: # Return to start
            pass
        else:
            print("Please select a valid option!\n:")

def app(data, menu_main):
    while True:
        for choice in menu_main:
            print(choice, menu_main[choice])
        user_input = input("Please select an option!\n:")
        user_choice = input_control(user_input, len(menu_main))

        if user_choice == 1: # Show dataframe
            print((data.versions[-1]).head())
            
        elif user_choice == 2: # Go to filter menu
            data.versions.append(filter_app(data, get_menu_filter()))

        elif user_choice == 3: # File summary
            print(summary_app(data.versions[-1], get_menu_summary()))

        elif user_choice == 4:
            # Graph menu
            pass

        elif user_choice == 5:
            file_name = input("Chose filename\n: ")
            file_type = input("Chose filentype\n: ")
            while file_type not in ["csv" , "xlsx", "tsv", "xls"]:
                print("Invalid filetype, try again, csv, tsv, xls or xlsx")
                file_type = input("Chose filentype\n: ")
            my_file = file_name + "." + file_type
            save_file(my_file, data.versions[-1])
        elif user_choice == 6: # Undo chage
            if len(data.versions) != 1:
                data.versions.pop(-1)

        elif user_choice == 7: # Undo all changes
            data.versions = [data.df]

        elif user_choice == 8: # Quit
            # Ask if Save df, save graphs
            print("Goodbye!")
            break
        else:
            print("Please select a valid option!\n:")

def main():
    path = start_up_meny(get_menu_files_options(), get_menu_files()) # get file_path
    data = File(path)
    app(data, get_menu_main())


if __name__ == '__main__':
    main()
