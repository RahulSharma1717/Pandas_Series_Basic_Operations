# Update the values of the column Volume Sold (Liters) into ml.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)

df['Volume Sold (ml)'] = df['Volume Sold (Liters)'] * 1000
print(df.iloc[:, -3:])


"""Output:
     Volume Sold (Liters)  Volume Sold (Gallons)  Volume Sold (ml)
0                     9.0                   2.38            9000.0
1                     3.0                   0.79            3000.0
2                     1.5                   0.40            1500.0
3                     6.0                   1.59            6000.0
4                     9.0                   2.38            9000.0
..                    ...                    ...               ...
914                  12.0                   3.17           12000.0
915                   1.5                   0.40            1500.0
916                  60.0                  15.85           60000.0
917                  18.0                   4.76           18000.0
918                   9.0                   2.38            9000.0

[919 rows x 3 columns]
"""