import pandas as pd
from scipy.stats import chi2_contingency

class ContingencyChiSquare:
    """
    Helper class for generating contingency table and chi square statistics
    """
   

        # Defining the initation fo the class
    def __init__(self):
        pass


    # Defining the function for creating contigency table
    def get_contingency_table(self,column1, column2):
        self.contingeny_table = pd.crosstab(index= column1, columns= column2)
        return self.contingeny_table

    #Definig function for getting chi square test
    def get_chi_square_stats(self,column1,column2):
        self.contingeny_table = self.get_contingency_table(column1,column2)
        self.chi_results = chi2_contingency(self.contingeny_table.values)
        return self.chi_results

