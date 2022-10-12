def get_user_choice(menu, question = "Please select an option!\n:", check = True):
    """ Convert user input to an answer in desired format

    :param menu: A menu with answer options 
    :type menu: dict
    :param question: A question, defaults to "Please select an option!\n:"
    :type question: str, optional
    :param check: if user input is to be converted to numeric, defaults to True
    :type check: bool, optional
    :return: The input as a valid str/int depending on bool check
    :rtype: str or int
    """
    n_options = len(menu)
    for choice in menu:
        print(choice, menu[choice])
    if check is False:
        return input(question)

    return input_control(question, n_options)

def input_control(question, n_options):
    """ Asks a question and control that the answer is a valid input

    :param question: A question from program to user
    :type question: String
    :param n_options: Number of valid answers 
    :type n_options: int
    :return: The selected answer as int and if it's not valid return None
    :rtype: int or None
    """
    
    user_input = input(question)
    if user_input.isdigit() and 0 < int(user_input) <= n_options:
        return int(user_input)
    else:
        return None

def get_menu_files():
    """ Projectdata listed as a dictionary

    :return: The menu for projectdata
    :rtype: dict
    """
    menu_files = {
            "1.": "25_years_of_salgskimmer.csv",
            "2.": "helarsprestationer_from_2017.csv"
    }
    return menu_files
    
def get_menu_files_options():
    """ A menu for questions to get a specific file

    :return: The menu for the file options
    :rtype: dict
    """
    menu_files_options = {
        "1.": "Own file",
        "2.": "From datafolder"    
    }
    return menu_files_options
    
def get_menu_main():
    """ A menu for the main app

    :return: The main menu for the program
    :rtype: dict
    """
    menu_main = {
        "1.": "Show DataFrame",   
        "2.": "Filter file",
        "3.": "Show file summary", 
        "4.": "Graph data",
        "5.": "Save current dataframe",
        "6.": "Undo previous changes",
        "7.": "Undo all changes",
        "8.": "End program"
    }
    return menu_main

def get_menu_filter():
    """ A menu for the filter app

    :return: The filter menu for the program
    :rtype: dict
    """
    menu_filter = {
        "1.": "Remove or keeps column/s by name", 
        "2.": "Filter by column value",
        "3.": "Filter by column value interval",
        "4.": "Choose row interval",
        "5.": "Return to start menu"
    }
    return menu_filter

def get_menu_summary():
    """ A menu for the summary app

    :return: The summary menu for the program
    :rtype: dict
    """
    menu_summary = {
        "1.": "Show mean", 
        "2.": "Show median",
        "3.": "Show std",
        "4.": "Show min",
        "5.": "Show max",
        "6.": "Count # unique values",
        "7.": "Return to start menu"
    }
    return menu_summary

def get_menu_graphics():
    """ A menu for the graphics app

    :return: The graphics menu for the program
    :rtype: dict
    """
    menu_graphics = {
        "1.": "Scatterplot", 
        "2.": "Line plot",
        "3.": "Barchart",
        "4.": "Histogram",
        "5.": "Return to start menu"
    }
    return menu_graphics

def get_col_name_menu(col_list):
    """ A menu for the existing columns in the DataFrame

    :param col_list: columns in current DataFrame
    :type col_list: list
    :return: columns listed in a dictionary
    :rtype: dict
    """
    col_name_menu = {v: k for v, k in enumerate(col_list)}
    return col_name_menu