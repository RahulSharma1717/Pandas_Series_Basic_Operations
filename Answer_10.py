# Load the data and display all the invoice numbers.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
# pd.set_option('display.max_rows', None)

print(df['Invoice/Item Number'])


"""Output:
0      S28865700001
1      S29339300091
2      S28866900001
3      S29134300126
4      S29282800048
           ...     
914    S26164400020
915    S19675100022
916    S12278000057
917    S05694100030
918    S23309100006
Name: Invoice/Item Number, Length: 919, dtype: object
"""