from numpy import single
import file_handler
import graphics 
import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
import time
import threading
# import random as randint

from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


#df=file_handler.read_file(".\\testfiles\\testfile.csv")



# def single_plot(df, cols, root):

#     colname1=cols[0]
#     colname2=cols[1]
#     figure_new = plt.Figure(figsize=(6,5), dpi=100)
#     ax_new = figure_new.add_subplot(111)
#     bar_new = FigureCanvasTkAgg(figure_new, root)
#     bar_new.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
#     df_new = df[[colname1,colname2]].groupby(colname2).sum()

#     df_new.plot(kind='bar', legend=True, ax=ax_new)
#     ax_new.set_title('Country Vs. GDP Per Capita')


def single_plot(df, cols, root):

    colname1=cols[0]
    colname2=cols[1]
    figure_new = plt.Figure(figsize=(6,5), dpi=100)
    ax_new = figure_new.add_subplot(111)
    bar_new = FigureCanvasTkAgg(figure_new, root)
    bar_new.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df_new = df[[colname1,colname2]].groupby(colname2).sum()

    df_new.plot(kind='bar', legend=True, ax=ax_new)
    ax_new.set_title('Country Vs. GDP Per Capita')



def multi_plot(df, graph_list):

    # single_plot(df, graph1.columns)

    root= tk.Tk() 

    for graph in graph_list:
        single_plot(df, graph.colnames, root)

    root.mainloop()


#def animate(df, cols):