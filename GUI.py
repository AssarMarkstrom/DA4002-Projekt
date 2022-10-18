import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graphics import scatter_plot, bar_plot, line_plot, histogram_plot

def multi_plot(df, graph_list):
    """ Converts singleplots to multiplot

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param graph_list: List of current graphs
    :type graph_list: list
    """
    window = tk.Toplevel()
    for graph in graph_list:
        single_plot(df, graph.colnames, window, graph.plottype)

def single_plot(df, cols, root, plottype):
    """ Singleplot

    :param df: DataFrame
    :type df: pandas.DataFrame
    :param cols: Selected columns in DataFrame
    :type cols: list
    :param root: current tkinter window
    :type root: tk.Toplevel()
    :param plottype: plottype
    :type plottype: str
    :return: singleplot or errorplot
    :rtype: function call
    """
    if len(cols) == 2:
        if cols[0] not in df.columns or cols[1] not in df.columns:
            error_plot(cols, root, plottype)
            return None
    elif len(cols) == 1:
        if cols[0] not in df.columns:
            error_plot(cols, root, plottype)
            return None
 
    figure_new = plt.figure(figsize=(6,5), dpi=100)
    ax_new = figure_new.add_subplot(111)
    bar_new = FigureCanvasTkAgg(figure_new, root)
    bar_new.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    if plottype == "bar":
        bar_plot(df, cols, ax_new)

    elif plottype == "line":     
        line_plot(df, cols, ax_new)

    elif plottype == "scatter":
        scatter_plot(df, cols, ax_new)

    elif plottype == "histogram":
        histogram_plot(df, cols, ax_new)

def error_plot(cols, root, plottype):
    """ Plot for error message

    :param cols: Selected columns
    :type cols: list
    :param root: current tkinter window
    :type root: tk.Toplevel()
    :param plottype: plottype
    :type plottype: str
    """
    figure_new = plt.figure(figsize=(6,5), dpi=100)
    ax_new = figure_new.add_subplot(111)
    bar_new = FigureCanvasTkAgg(figure_new, root)
    bar_new.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax_new.text(0.1,0.5, ('ERROR for plot: ' + plottype + ', Columns: ' + cols[0] + ", " + cols[1]), style='italic',
    bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
