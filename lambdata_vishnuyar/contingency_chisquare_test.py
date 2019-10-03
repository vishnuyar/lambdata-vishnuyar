import unittest
from . contingency_chisquare import ContingencyChiSquare
import pandas as pd
import numpy as np


class ChisquareHelperTest(unittest.TestCase):
    """Testing the contingency chisquare class"""
    a = np.array(["foo", "foo", "foo", "foo", "bar", "bar","bar", "bar", "foo", "foo", "foo"], dtype=object)
    b = np.array(["one", "one", "one", "two", "one", "one","one", "two", "two", "two", "one"], dtype=object)
    myframe = pd.DataFrame({'a':a,'b':b})
    

    def contingency_table_test(self):
        """ Testing contingency table generation """
        self.cc = ContingencyChiSquare()
        self.con_table = self.cc.contingeny_table(self.myframe['a'], self.myframe['b'])
        self.assertEqual(5,3)


if __name__ == "__main__":
    unittest.main()