
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


df=fileread.read_file(".\\projectdata\\helarsprestationer_from_2017.csv")

print(df) 


scatter_plot(df, ["Kalenderår","Total"])


#o=["Kalendår","Kod"]

#print(o[1])



