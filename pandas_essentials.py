#Pandas library is useful for Data Processing & Analysis
#The library has two obejects: Panda Data Frame and Pandas Series
#Pandas Data Frame is a two-dimensional tabular data structure with labelled axes(rows and columns)

# Importing the pandas library
import pandas as pd

# Importing the California housing dataset
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

# Printing the type of the dataset
print(type(fetch_california_housing))  # Output: <class 'sklearn.utils.Bunch'>

# Creating a Pandas DataFrame
housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)