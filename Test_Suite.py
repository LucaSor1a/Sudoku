import unittest
from Test_Ingreso import TestIngreso
from Test_Sudoku import TestSudoku
from Test_API import TestAPI


def suite():
    test_suite = unittest.TestSuite()
    # INGRESO
    test_suite.addTest(unittest.makeSuite(TestIngreso))
    # SUDOKU
    test_suite.addTest(unittest.makeSuite(TestSudoku))
    # API
    test_suite.addTest(unittest.makeSuite(TestAPI))
    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)
