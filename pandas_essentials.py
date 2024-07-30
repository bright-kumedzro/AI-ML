#Pandas library is useful for Data Processing & Analysis
#The library has two obejects: Panda Data Frame and Pandas Series
#Pandas Data Frame is a two-dimensional tabular data structure with labelled axes(rows and columns)

# Importing the pandas library
import pandas as pd
import os

# Importing the California housing dataset
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

# Printing the type of the dataset
type(fetch_california_housing)  # Output: <class 'sklearn.utils.Bunch'>

# Creating a Pandas DataFrame
housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
print(housing_df.head())
print(housing_df.shape)


#Importing the data from a csv file to a pandas DataFrame
print(os.path.exists("oritweets.csv"))
oritweets_df = pd.read_csv("oritweets.csv")
print(oritweets_df)

housing_df.to_csv('housing_data.csv')