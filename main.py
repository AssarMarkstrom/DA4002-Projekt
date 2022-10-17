from ast import Global
from menus import get_menu_files,get_menu_files_options, get_menu_main, input_control
from menus import  get_menu_filter, get_menu_summary, get_menu_graphics, get_user_choice
from file_handler import FilenameException, read_file, save_file, save_app
from filter_handler import filter_app
from summary import summary_app
from graphics import graphics_app
from classes import File
from GUI import multi_plot
import tkinter as tk

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
        user_choice = get_user_choice(menu_files_options, "Do you want to choose your own file or a file from our datafolder\n:")
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
    :type data: Object (File)
    :param menu_main: Menu for the main application
    :type menu_main: dict
    """
    graph_list = []
    while True:
        user_choice = get_user_choice(menu_main)

        if user_choice == 1: # Show dataframe
            print(data.get_current().head())
            
        elif user_choice == 2: # Go to filter menu
            if data.get_current().empty:
                print("Can't filter on empty dataframe!")
            filter_ = filter_app(data, get_menu_filter())
            data.versions.append(filter_)
            if len(graph_list) != 0  and filter_ is not None: 
                multi_plot(data.get_current(), graph_list)
        
        elif user_choice == 3: # File summary
            sum_return = summary_app(data.get_current(), get_menu_summary())
            if sum_return is not None:
                print(sum_return)

        elif user_choice == 4: # Graph data
            if len(data.get_current().columns) >= 2:            
                graph_ = graphics_app(data.get_current(), get_menu_graphics()) # Saves new graph object
                if graph_ is not None:
                    graph_list.append(graph_) # New graph object added to graph_list
                    multi_plot(data.get_current(), graph_list) # Plot all current graphs

        elif user_choice == 5: # Delete last graph
            if len(graph_list) == 0:
                print("No graphs found!")
            else:
                graph_list.pop(-1)
                if len(graph_list) != 0:
                    multi_plot(data.get_current(), graph_list)
                else:
                    print("That was your last graph!")

        elif user_choice == 6: # Save file
            save_app(data)

        elif user_choice == 7: # Undo chage
            if len(data.versions) != 1:
                data.versions.pop(-1) # Removes latest dataframe from versions list 

        elif user_choice == 8: # Undo all changes
            data.versions = [data.df]

        elif user_choice == 9: # Quit
            answer = input_control("Do you want to save your current dataframe before exiting? (yes: 1, no: 2)\n: ", 2)
            if answer == 1:
                save_app(data)
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
        root.destroy()
        quit()
    root.mainloop()

if __name__ == '__main__':
    main()
