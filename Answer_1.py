# Load the data and access name series.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df['Name'])


"""Output:
0         Michelle Harrington
1                 Kelsey Hill
2                Scott Jensen
3               Joseph Miller
4               Debra Coleman
                 ...         
293906           Meagan Ellis
293907            Mathew Beck
293908             Daniel Lee
293909         Patrick Wilson
293910         Dustin Merritt
Name: Name, Length: 293911, dtype: object
"""