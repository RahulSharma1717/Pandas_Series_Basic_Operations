# Calculate margin earned by retailers on each bottle.

import numpy as np
import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)

df['margin'] = df['State Bottle Retail'] - df['State Bottle Cost']
print(df[['State Bottle Retail', 'State Bottle Cost', 'margin']])


"""Output:
     State Bottle Retail  State Bottle Cost  margin
0                  17.43              11.62    5.81
1                  29.37              19.58    9.79
2                  17.43              11.62    5.81
3                 148.50              99.00   49.50
4                  17.43              11.62    5.81
..                   ...                ...     ...
914                11.25               7.50    3.75
915                18.74              12.50    6.24
916                22.49              15.00    7.49
917                 4.60               3.07    1.53
918                 5.06               3.37    1.69

[919 rows x 3 columns]
"""