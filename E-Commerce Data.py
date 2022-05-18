#Fonte de dados:https://www.kaggle.com/datasets/benroshan/ecommerce-data?datasetId=615631

# Import some libraries
import pandas as pd
import numpy as np

# Used to pandas library to read csv files:
df = pd.read_csv('List of Orders.csv')

#show dataframe
df

# head method on pandas, used to dataframes, could show us 5 first lines of our dataset.
df.head()

# On the other hands, tail method on pandas library could show us the last 3 lines on our dataset.
df.tail()

# Counting how many line and columns on our database with shape method.
df.shape #(lines, columns)

# Show all columns
df.columns

df.duplicated()

# How many duplicate line there are on dataset 
df.duplicated().sum()

# Show us data about metadata
df.info()

# How many empty space are there?
df.isna().sum()

# Summary Statistical
df.describe()

# Summary Statistical, include categorical variables
df.describe(include = 'all')
