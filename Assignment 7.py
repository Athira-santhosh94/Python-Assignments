import numpy as np
import pandas as pd

# Exercise 1: Create a numpy array and reshape it to 2x5
array1 = np.arange(1, 11).reshape(2, 5)
print("Exercise 1 Output:")
print(array1)

# Exercise 2: Create a numpy array and extract elements between 5th and 15th index
array2 = np.arange(1, 21)
extracted_elements = array2[5:15]
print("\nExercise 2 Output:")
print(extracted_elements)

# Exercise 3: Create a Pandas series and add a new item
s_series = pd.Series({'apples': 3, 'bananas': 2, 'oranges': 1})
s_series['pears'] = 4
print("\nExercise 3 Output:")
print(s_series)

# Exercise 4: Create a dataframe with 10 rows
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ivy', 'Jack'],
    'age': [25, 32, 40, 29, 35, 28, 45, 30, 27, 50],
    'gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'F', 'M']
}
df = pd.DataFrame(data)
print("\nExercise 4 Output:")
print(df)

# Exercise 5: Add a new column 'occupation'
df['occupation'] = ['Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer']
print("\nExercise 5 Output:")
print(df)

# Exercise 6: Select rows where age is >= 30
df_filtered = df[df['age'] >= 30]
print("\nExercise 6 Output:")
print(df_filtered)

# Exercise 7: Convert dataframe to CSV and read it back
df.to_csv('dataframe.csv', index=False)
df_read = pd.read_csv('dataframe.csv')
print("\nExercise 7 Output:")
print(df_read)
