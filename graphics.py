
# from file_reader import file_read
import fileread 
#from fileread import read_file
import matplotlib.pyplot as plt

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


def bar_plot(df, cols):
    colname1=cols[0]
    colname2=cols[1]
    plt.title(colname1 + " vs " + colname2)
    plt.xlabel(colname1)
    plt.ylabel(colname2)
    plt.bar(df[colname1], df[colname2])
    plt.show()

def line_plot(df, cols):
    colname1=cols[0]
    colname2=cols[1]
    plt.title(colname1 + " vs " + colname2)
    plt.xlabel(colname1)
    plt.ylabel(colname2)
    plt.plot(df[colname1], df[colname2])
    plt.show()




df=fileread.read_file(".\\projectdata\\helarsprestationer_from_2017.csv")

print(df) 


#scatter_plot(df, ["Kalenderår","Total"])
#histogram_plot(df, ["Kalenderår","Total"])
#bar_plot(df, ["Kalenderår","Total"])
line_plot(df, ["Kalenderår","Total"])


#o=["Kalendår","Kod"]

#print(o[1])



