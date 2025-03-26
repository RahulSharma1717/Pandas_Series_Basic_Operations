# Create a new column with 100 stored in it as value.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
df['new_column'] = 100
print(df.iloc[:, -5:])


"""Output:
       Payment_Method Order_Status  Ratings            products  new_column
0          Debit Card      Shipped        5      Cycling shorts         100
1         Credit Card   Processing        4          Lenovo Tab         100
2         Credit Card   Processing        2    Sports equipment         100
3              PayPal   Processing        4       Utility knife         100
4                Cash      Shipped        1   Chocolate cookies         100
...               ...          ...      ...                 ...         ...
293906           Cash   Processing        1  Historical fiction         100
293907           Cash   Processing        5             LG Gram         100
293908           Cash      Shipped        2               Parka         100
293909           Cash      Shipped        4            TV stand         100
293910           Cash      Shipped        2              Clocks         100

[293911 rows x 5 columns]
"""