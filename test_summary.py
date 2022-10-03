#!/bin/env python3
import unittest
from fileread import *
from summary import *
import pandas as pd

class TestSummary(unittest.TestCase):
    def setUp(self):
        self.testfile_sum =  "testfiles/testfile_sum.csv"
        self.df = read_file(self.testfile_sum)
    
    def test_get_colnames(self):
        self.assertEqual(get_colnames(self.df), list(self.df.head(1)))
    
    #def test_get_numerical_coltypes(self):
        #self.assertTrue()

    def test_get_head(self):
        self.assertLessEqual(len(get_head(self.df)),5)

   
