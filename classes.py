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
    """ Creates Graphics object which has attributes colnames(list) and plottype(str)
    """
    def __init__(self, colnames, plottype):
        self.colnames = colnames
        self.plottype = plottype