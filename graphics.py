
from file_reader import file_read
from fileread import read_file
import matplotlib.pyplot as plt

def scatter_plot(df, colname1, colname2):
    plt.scatter(df[colname1], df[colname2])
    plt.show()


df=file_read(".\\projectdata\\helarsprestationer_from_2017.csv")

df

#scatter_plot()