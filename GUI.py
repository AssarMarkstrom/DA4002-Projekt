import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def scatter_plot(df, cols):
    colname1=cols[0]
    colname2=cols[1]
    plt.title(colname1 + " vs " + colname2)
    plt.xlabel(colname1)
    plt.ylabel(colname2)
    plt.scatter(df[colname1], df[colname2])
    plt.show()

def histogram_plot(df, cols):
    colname=cols[0]
    plt.title(colname)
    plt.hist(df[colname])
    plt.show()

def bar_plot(df, cols, ax_input):
    colname1=cols[0]
    colname2=cols[1]
    plt.title(colname1 + " vs " + colname2)
    plt.xlabel(colname1)
    plt.ylabel(colname2)
    plt.bar(df[colname1], df[colname2])
    plt.plot(kind='bar', legend=True, ax=ax_input)

def line_plot(df, cols):
    colname1=cols[0]
    colname2=cols[1]
    plt.title(colname1 + " vs " + colname2)
    plt.xlabel(colname1)
    plt.ylabel(colname2)
    plt.plot(df[colname1], df[colname2])
    plt.show()





def multi_plot(df, graph_list):
    window = tk.Toplevel()
    for graph in graph_list:
        single_plot(df, graph.colnames, window, graph.plottype)

def single_plot(df, cols, root, plottype):
    if len(cols) == 2:
        colname2 = cols[1]
        colname1 = cols[0]
        figure_new = plt.figure(figsize=(6,5), dpi=100)
        ax_new = figure_new.add_subplot(111)
        bar_new = FigureCanvasTkAgg(figure_new, root)
        bar_new.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df_new = df[[colname1, colname2]].groupby(colname1).sum()
        #bar_plot(df, cols, ax_new)



        if plottype == "bar":
            bar_plot(df, cols, ax_new)
            # ax_new.set_title('Country Vs. GDP Per Capita')

        elif plottype == "line":     
            df_new.plot(kind='line', legend=True, ax=ax_new)
            ax_new.set_title('Country Vs. GDP Per Capita')

        elif plottype == "scatter":
            df_new.plot(kind='scatter', legend=True, ax=ax_new)
            ax_new.set_title('Country Vs. GDP Per Capita')

        elif plottype == "bar":
            df_new.plot(kind='bar', legend=True, ax=ax_new)
            ax_new.set_title('Country Vs. GDP Per Capita')

    return