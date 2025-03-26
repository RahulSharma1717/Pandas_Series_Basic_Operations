# Create a new column that holds serial number 1 to last row.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

df = df.copy()
df["Serial_Number"] = df.index + 1
print(df.iloc[:, -5:])


"""Output:
       Payment_Method Order_Status  Ratings            products  Serial_Number
0          Debit Card      Shipped        5      Cycling shorts              1
1         Credit Card   Processing        4          Lenovo Tab              2
2         Credit Card   Processing        2    Sports equipment              3
3              PayPal   Processing        4       Utility knife              4
4                Cash      Shipped        1   Chocolate cookies              5
...               ...          ...      ...                 ...            ...
293906           Cash   Processing        1  Historical fiction         293907
293907           Cash   Processing        5             LG Gram         293908
293908           Cash      Shipped        2               Parka         293909
293909           Cash      Shipped        4            TV stand         293910
293910           Cash      Shipped        2              Clocks         293911

[293911 rows x 5 columns]
"""