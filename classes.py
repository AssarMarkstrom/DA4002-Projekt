from file_handler import get_filetype, read_file

class File:
    """ Creates File object which stores given file as Dataframe.
    And has attributes type(filetype), df(DataFrame) and versions(list of dataframes)
    """
    def __init__(self, path):
        self.type = get_filetype(path)
        self.df = read_file(path)
        self.versions = [self.df]
    
    def get_current(self):
        current = self.versions[-1]
        return current

class Graphics():
    def __init__(self, colnames, plottype):
        self.colnames = colnames
        self.plottype = plottype


"""
path = "projectdata/helarsprestationer_from_2017.csv"
testfile = File(path)
# print(testfile.current)
graph_obj = Graphics(["Kod", "Män"], "scatter", path)
print(graph_obj.current)
"""