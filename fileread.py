import pandas as pd

#Convert TSV file to CSV..
with open("filename.tsv") as file:
    # Passing tsv.file to reader(), and with tab delimiter
    tsv_file = csv.reader(file, delimiter="\n")

    for line in tsv_file:
        print(line)

# Using split? data = []
# for line in f:
# l=line.split('\n'). reads line by line
#  data.append(l). splits data and stores lists.
# for i in data: print (i)

def load_file(filepath):
    data = []
    col = []
     #checkcol = false, should this be here?
    with open(filepath) as f:
        for val in f.readlines():
            val = val.replace("\n")
            val = val.split(',')
            # something to check stored data, maybe use checkcol?
            # if checkcol is false: col = val, checkcol = true.
