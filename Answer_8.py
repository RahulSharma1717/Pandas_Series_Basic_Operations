# Find out the birth year of the customers.

import pandas as pd

df = pd.read_csv('retail_data.csv')
df['birth_year'] = df['Year'] - df['Age']
print(df[['Year', 'Age', 'birth_year']])


"""Output:
        Year  Age  birth_year
0       2023   21        2002
1       2023   19        2004
2       2023   48        1975
3       2023   56        1967
4       2024   22        2002
...      ...  ...         ...
293906  2024   31        1993
293907  2023   35        1988
293908  2024   41        1983
293909  2023   41        1982
293910  2024   28        1996

[293911 rows x 3 columns]
"""