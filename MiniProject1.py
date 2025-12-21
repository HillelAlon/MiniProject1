"""Import the libraries and the dataset."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('laptop_price - dataset.csv')
print(df)
print(df.info())

'''Plot the price of all the laptops'''
sns.histplot(df['Price (Euro)'], kde=True, )


'''Which company has on average the most expensive laptop? 
What is the average laptop price for each company?'''



'''Find the different types of Operating systems present in the data - under the column name "OpSys".
Please note - there are operating systems that are the same systems and
just written differently in the column - please fix them to be uniform.'''



'''Plot for each of the operating system types the distribution of the prices,
so that the number of plots equals to the number of unique operating systems.'''



'''What is the relationship between RAM and computer price?
add an adequate plot to support your findings. <<< check data for outliers,
what would be considered as an outlier? How will you detect it ? >>>'''



'''Create a new column for the dataframe called "Storage type" that
extracts the storage type from the column "Memory".
For example, in the first row in the column "Memory" it states "128GB SSD",
the new column will have just "SSD" in its first row.'''
