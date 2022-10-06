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
        "5.": "Save current dataframe",
        "6.": "End program"
    }
    return menu_main
def get_menu_filter():
    menu_filter = {
        "1.": "Filter by column name",   
        "2.": "Filter by column value",
        "3.": "Filter by column value interval",
        "4.": "Choose row interval"
        }
    return menu_filter