# Display address, zipcode, city, state and country column.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df[['Address', 'Zipcode', 'City', 'State', 'Country']])


"""Output:
                             Address  Zipcode        City            State  \
0                  3959 Amanda Burgs    77985    Dortmund           Berlin   
1                 82072 Dawn Centers    99071  Nottingham          England   
2                  4133 Young Canyon    75929     Geelong  New South Wales   
3        8148 Thomas Creek Suite 100    88420    Edmonton          Ontario   
4          5813 Lori Ports Suite 269    48704     Bristol          England   
...                              ...      ...         ...              ...   
293906        389 Todd Path Apt. 159     4567  Townsville  New South Wales   
293907             52809 Mark Forges    16852     Hanover           Berlin   
293908  407 Aaron Crossing Suite 495    88038    Brighton          England   
293909               3204 Baird Port    67608     Halifax          Ontario   
293910           143 Amanda Crescent    25242      Tucson    West Virginia   

          Country  
0         Germany  
1              UK  
2       Australia  
3          Canada  
4              UK  
...           ...  
293906  Australia  
293907    Germany  
293908         UK  
293909     Canada  
293910        USA  

[293911 rows x 5 columns]
"""