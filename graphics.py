from menus import get_col_name_menu, get_user_choice
from classes import Graphics
import matplotlib.pyplot as plt

def scatter_plot(df, cols, ax_input):
    """ Scatterplot

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param cols: columns for DataFrame
    :type cols: list
    :param ax_input: figure
    :type ax_input: plt.figure
    """
    colname1=cols[0]
    colname2=cols[1]
    plt.title(colname2 + " vs " + colname1)
    plt.xlabel(colname1)
    plt.ylabel(colname2)
    plt.scatter(df[colname1], df[colname2])
    plt.plot(kind='scatter', legend=True, ax=ax_input)

def histogram_plot(df, cols, ax_input):
    """ Histogramplot

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param cols: column for DataFrame
    :type cols: list
    :param ax_input: figure
    :type ax_input: plt.figure
    """
    colname=cols[0]
    plt.title(colname)
    plt.hist(df[colname])
    plt.plot(kind='histogram', legend=True, ax=ax_input)

def bar_plot(df, cols, ax_input):
    """ Barplot

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param cols: columns for DataFrame
    :type cols: list
    :param ax_input: figure
    :type ax_input: plt.figure
    """
    colname1=cols[0]
    colname2=cols[1]
    plt.title(colname2 + " vs " + colname1)
    plt.xlabel(colname1)
    plt.ylabel(colname2)
    plt.bar(df[colname1], df[colname2])
    plt.plot(kind='bar', legend=True, ax=ax_input)

def line_plot(df, cols, ax_input):
    """ Lineplot

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param cols: columns for DataFrame
    :type cols: list
    :param ax_input: figure
    :type ax_input: plt.figure
    """
    colname1=cols[0]
    colname2=cols[1]
    plt.title(colname2 + " vs " + colname1)
    plt.xlabel(colname1)
    plt.ylabel(colname2)
    plt.plot(df[colname1], df[colname2])
    plt.plot(kind='line', legend=True, ax=ax_input)

def graphics_app(df, menu_graph):
    """ Graphics meny for the program 

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param menu_graph: Menu options for filter
    :type menu_graph: dict
    :return: DataFrame
    :rtype: pandas.DataFrame
    """

    user_choice = get_user_choice(menu_graph)
    col_options = list(df.columns)

    if user_choice == 5: # Return to start
        return None

    selected_col_list = []
    col_name_menu =  get_col_name_menu(col_options)
    while True:
        
        for choice in col_name_menu:
            print(choice, col_name_menu[choice])
        selected_col = input("Select x-variable\n:")

        if selected_col in df.columns and selected_col not in selected_col_list:
            selected_col_list.append(selected_col)
            col_options.remove(selected_col)
            if user_choice == 4: # Histogram
                return Graphics(selected_col_list, "histogram")
            break

    while True:
        for choice in col_name_menu:
            print(choice, col_name_menu[choice])
        selected_col = input("Select y-variable\n:")

        if selected_col in df.columns and selected_col not in selected_col_list:
            selected_col_list.append(selected_col)
            break

    if user_choice == 1: # Scatter plot
        return Graphics(selected_col_list, "scatter")

    elif user_choice == 2: # Line plot
        return Graphics(selected_col_list, "line")

    elif user_choice == 3: # Bar chart
        return Graphics(selected_col_list, "bar")
