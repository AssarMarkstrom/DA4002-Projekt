#!/bin/env python3
import unittest
from file_handler import *
from summary import *

class TestSummary(unittest.TestCase):
    def setUp(self):
        self.testfile_sum =  "testfiles/testfile_sum.csv"
        self.df = read_file(self.testfile_sum)
    
    def test_get_colnames(self):
        self.assertEqual(get_colnames(self.df), list(self.df.head(1)))

    def test_get_unique_values_count(self):
        unique_list = []
        for col in self.df.columns:
            for item in self.df[col]:
                if item not in unique_list:
                    unique_list.append(item)
        
            self.assertEqual(get_unique_values_count(self.df)._get_value('count', col)
            ,len(unique_list))
            unique_list.clear()
        




   
