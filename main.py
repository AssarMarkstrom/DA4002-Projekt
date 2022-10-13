from queue import Empty
from menus import get_menu_files,get_menu_files_options, get_menu_main
from menus import  get_menu_filter, get_menu_summary, get_menu_graphics, get_user_choice
from file_handler import read_file, FilenameException, get_filetype, save_file
from filter import filter_app
from summary import summary_app
from graphics import graphics_app
from classes import File
from GUI import multi_plot
import tkinter as tk
from sys import *
def start_up_meny(menu_files_options, menu_files):
    """ A menu for selecting a file to start with

    :param menu_files_options: A menu for choosing between a local file and projectdata.
    :type menu_files_options: dict
    :param menu_files: A menu for selecting a specific file based on previous choice.
    :type menu_files: dict
    :return: Path to the chosen file
    :rtype: String
    """
    while True:
        user_choice = get_user_choice(menu_files_options,
        "Do you want to choose your own file or a file from our datafolder\n:")
        if user_choice == 1:
            path = input("Give me your file path\n:")
            try:
                read_file(path)
                return path
            except FilenameException:
                print("Could not find the file you were looking for, please try again!")
        elif user_choice == 2:
            user_choice = get_user_choice(menu_files,"Choose a file!\n:") 
            if user_choice is not None:
                path = "projectdata/"+ menu_files[(str(user_choice)+".")]
                return path
            else: print("Something went wrong, please try again!")
        else: print("Something went wrong, please try again!")

def app(data, menu_main):
    """ Main menu for the program

    :param data: Object created from class File
    :type data: Object
    :param menu_main: Menu for the main application
    :type menu_main: dict
    """
    graph_list = []
    while True:
        user_choice = get_user_choice(menu_main)

        if user_choice == 1: # Show dataframe
            print(data.get_current().head())
            
        elif user_choice == 2: # Go to filter menu
            filter_ = filter_app(data, get_menu_filter())
            if graph_list is not Empty and filter_ is not None:
                data.versions.append(filter_)
                multi_plot(data.get_current(), graph_list)
        elif user_choice == 3: # File summary
            sum_return = summary_app(data.get_current(), get_menu_summary())
            if sum_return is not None:
                print(sum_return)

        elif user_choice == 4:
            graph_list.append(graphics_app(data.get_current(), get_menu_graphics(), graph_list))

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
            return "Exit"
        else:
            print("Please select a valid option!\n:")

def main():
    """Main()
"""
    root= tk.Tk()
    root.withdraw()
    path = start_up_meny(get_menu_files_options(), get_menu_files()) # get file_path
    data = File(path)
    application = app(data, get_menu_main())
    if application == "Exit":
        quit()
    root.mainloop()

if __name__ == '__main__':
    main()
