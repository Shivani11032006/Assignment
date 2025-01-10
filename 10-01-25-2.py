#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B'],
    'Sales': [100, 200, 150, 130, 170, 190, 120, 180],
    'Quantity': [10, 20, 15, 13, 17, 19, 12, 18],
    'Profit': [30, 60, 45, 39, 51, 57, 36, 54]
}
df = pd.DataFrame(data)
total_sales_by_region = df.groupby('Region')['Sales'].sum()
most_sold_product = df.groupby('Product')['Quantity'].sum().idxmax()
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
average_profit_margin_by_product = df.groupby('Product')['Profit_Margin'].mean()
print("Total Sales by Region:")
print(total_sales_by_region)
print("\nMost Sold Product (Based on Quantity):")
print(most_sold_product)
print("\nAverage Profit Margin by Product:")
print(average_profit_margin_by_product)


# In[ ]:




