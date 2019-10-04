import pandas as pd
import numpy as np
import unittest

import nullinfo as ni

class TestNullInfo(unittest.TestCase):
    """Class for testing Nullinfo """
    a = np.array([23, 5,11,np.nan,24,np.nan,np.nan,np.nan ])
    b = np.array(["one", None, "twoone", None, "one", "one","two", "two"], dtype=object)
    myframe = pd.DataFrame({'numbers':a,'cardinals':b})

    def test_nullinfo(self):
        self.null_frame = ni.nullinfo(self.myframe)
        self.assertListEqual(list(self.null_frame.values),list(np.array([['numbers',4,0.5],['cardinals',2,0.25]])))
if __name__ == "__main__":
    unittest.main()