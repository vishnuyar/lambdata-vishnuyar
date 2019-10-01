"""
Function to report
the number of nulls is each column of the dataframe along with the % of Null values wrt to No of rows. 
"""

import pandas as pd
import numpy as np

def nullinfo(df):
	no_of_rows = df.shape[0]  #Get number of rows in the Dataframe
	no_of_nulls = df.isnull().sum() #Get a dataframe containing number of nulls in each columns
	null_notify = pd.DataFrame(no_of_nulls).reset_index() # Creating a Dataframe with Null values information
	null_notify.columns = ['Column Name','No of Nulls'] #Naming the columns of the DataFrame
	null_notify['Nulls percent']=np.round(null_notify['No of Nulls']/no_of_rows,2)#using round function to have only 2 decimal points
#returing the Dataframe
	return null_notify