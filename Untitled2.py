#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# Load the dataset
sales_data = pd.read_csv("C://Users//shiva//Downloads//Day_7_sales_data.csv")

# Display the first 5 rows of the dataset
print(sales_data.head())

# Display basic statistics for numerical columns
print(sales_data.describe())


# In[ ]:




