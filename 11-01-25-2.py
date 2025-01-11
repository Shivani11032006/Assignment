import pandas as pd
data = {
    'Region': ['East', 'West', 'East', 'North', 'South'],
    'Sales': [1200, 800, 1500, 500, 2000],
    'Profit': [300, 200, 400, 100, 800],
    'Quantity': [10, 5, 20, 4, 25],
}
df = pd.DataFrame(data)
df['Profit_Per_Unit'] = df['Profit'] / df['Quantity']
df['High_Sales'] = df['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')
print(df)
