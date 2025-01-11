import pandas as pd

# Sample data
data = {
    'Region': ['East', 'West', 'East', 'North', 'South'],
    'Sales': [1200, 800, 1500, 500, 2000],
}

# Create a DataFrame
df = pd.DataFrame(data)

# 1. Extract all rows where sales are greater than 1000
sales_above_1000 = df[df['Sales'] > 1000]
print("Sales > 1000:")
print(sales_above_1000)

# 2. Find all sales records for a specific region (e.g., "East")
region_east_sales = df[df['Region'] == 'East']
print("\nSales for Region 'East':")
print(region_east_sales)
