#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Fonte de dados:https://www.kaggle.com/datasets/benroshan/ecommerce-data?datasetId=615631


# In[12]:


# Import some libraries
import pandas as pd
import numpy as np


# In[17]:


# Used to pandas library to read csv files:
df = pd.read_csv('List of Orders.csv')


# In[14]:


df


# In[15]:


# head method on pandas, used to dataframes, could show us 5 first lines of our dataset.
df.head()


# In[16]:


# On the other hands, tail method on pandas library could show us the last 3 lines on our dataset.
df.tail()


# In[18]:


# Counting how many line and columns on our database with shape method.
df.shape #(lines, columns)


# In[24]:


# Show all columns
df.columns


# In[25]:


df.duplicated()


# In[19]:


# How many duplicate line there are on dataset 
df.duplicated().sum()


# In[20]:


# Show us data about metadata
df.info()


# In[21]:


# How many empty space are there?
df.isna().sum()


# In[22]:


# Summary Statistical
df.describe()


# In[23]:


# Summary Statistical, include categorical variables
df.describe(include = 'all')


# In[ ]:




