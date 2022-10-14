def get_user_choice(menu, question = "Please select an option!\n:", check = True):
    n_options = len(menu)
    for choice in menu:
        print(choice, menu[choice])
    if check is False:
        return input(question)

    return input_control(question, n_options)

def input_control(question, n_options):
    """ Asks a question and control that the answer is a valid input

    :param question: A question from program->user
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
    menu_files = {
            "1.": "25_years_of_salgskimmer.csv",
            "2.": "helarsprestationer_from_2017.csv"
    }
    return menu_files
    
def get_menu_files_options():
    menu_files_options = {
        "1.": "Own file",
        "2.": "From datafolder"    
    }
    return menu_files_options
    
def get_menu_main():
    menu_main = {
        "1.": "Show DataFrame",   
        "2.": "Filter file",
        "3.": "Show file summary", 
        "4.": "Graph data",
        "5.": "Delete last graph",
        "6.": "Save current dataframe",
        "7.": "Undo previous changes",
        "8.": "Undo all changes",
        "9.": "End program"
    }
    return menu_main

def get_menu_filter():
    menu_filter = {
        "1.": "Remove or keeps column/s by name", 
        "2.": "Filter by column value",
        "3.": "Filter by column value interval",
        "4.": "Choose row interval",
        "5.": "Return to start menu"
    }
    return menu_filter

def get_menu_summary():
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
    menu_graphics = {
        "1.": "Scatterplot", 
        "2.": "Line plot",
        "3.": "Barchart",
        "4.": "Histogram",
        "5.": "Return to start menu"
    }
    return menu_graphics

def get_col_name_menu(col_list):
    col_name_menu = {v: k for v, k in enumerate(col_list)}
    return col_name_menu