import unittest
import pandas as pd
import numpy as np

import chisquare


class ChisquareHelperTest(unittest.TestCase):
    """Testing the contingency chisquare class"""
    a = np.array(["foo", "foo", "foo", "foo", "bar", "bar","bar", "bar", "foo", "foo", "foo"], dtype=object)
    b = np.array(["one", "one", "one", "two", "one", "one","one", "two", "two", "two", "one"], dtype=object)
    myframe = pd.DataFrame({'a':a,'b':b})
    

    def test_contingency_table(self):
        """ Testing contingency table generation """
        cc = chisquare.ContingencyChiSquare()
        con_table = cc.get_contingency_table(self.myframe['a'], self.myframe['b'])
        self.assertEqual(con_table.shape,(2,2))


if __name__ == "__main__":
    unittest.main()