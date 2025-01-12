import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 22, 28, 35],
    'Salary': [50000, 60000, 45000, 55000, 70000]
}
df = pd.DataFrame(data)
print("First 2 rows of the DataFrame:")
print(df.head(2))
df['Bonus'] = df['Salary'] * 0.10
average_salary = df['Salary'].mean()
print("\nAverage Salary of Employees:", average_salary)
older_than_25 = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(older_than_25)
