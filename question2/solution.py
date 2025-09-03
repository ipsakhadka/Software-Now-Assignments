# Importing libraries
import os 
from glob import glob
import pandas as pd
import numpy as np


# Now, we will create a function to combine all csv files and create a dataframe

def load_data(path):
    csv_files= glob(os.path.join(path,"*.csv"))

    data=[]

    for file_path in csv_files:
        df=pd.read_csv(file_path)
        data.append(df)

    df_combined=pd.concat(data,ignore_index=True)
    return df_combined



'''
Testing if dataframe is created 

df=load_data("question2_data")

print(df.shape)
print(df.head())

'''