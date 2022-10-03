# import unittest
# import fileread
# import column_filter


# class FilterTestCase(unittest.TestCase):

#     def SetUp(self):

#         self.test_df =  fileread.read_file("testfiles/testfile.csv")
#         self.colnames = list(self.test_df.columns)
#         self.ncol = len(self.colnames)
#         self.nrow = len(self.test_df)
        
#     def test_col_select(self):

#         for col in self.test_df:
#             df_keep = column_filter.col_select(self.test_df, col, keep = True)
#             self.assertEqual(
#                 df_keep.columns, col)
#             self.assertEqual(
#                 df_keep.shape, (self.nrow, 1))
#             # Test keep = False
#             df_remove = column_filter.col_select(self.test_df, col, keep = False)
#             self.assertEqual(df_remove.columns, self.colnames.remove(col))
#             self.assertEqual(df_remove.shape, (self.nrow, self.ncol-1))

    
#     def test_interval_filter(self):

#         for col in self.test_df:
#             df_keep = column_filter.col_select(self.test_df, col, keep = True)
#             self.assertEqual(
#                 df_keep.columns, col)
#             self.assertEqual(
#                 df_keep.shape, (self.nrow, 1))
#             # Test keep = False
#             df_remove = column_filter.col_select(self.test_df, col, keep = False)
#             self.assertEqual(df_remove.columns, self.colnames.remove(col))
#             self.assertEqual(df_remove.shape, (self.nrow, self.ncol-1))
        
#         # for col in list(combinations(self.colnames, 2)):
#         #     df_keep = column_filter.col_select(self.test_df, col, keep = True)
#         #     self.assertEqual(
#         #         df_keep.columns, col)
#         #     self.assertEqual(
#         #         df_keep.shape, (self.nrow, 2))
#         #     # Test keep = False
#         #     df_remove = column_filter.col_select(self.test_df, col, keep = False)
#         #     self.assertEqual(df_remove.columns, self.colnames.remove(col))
#         #     self.assertEqual(df_remove.shape, (self.nrow, self.ncol-2))

# if __name__ == '__main__':
#     unittest.main()
