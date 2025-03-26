# Update the address column and add the city name along with the address.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

df['New_Address'] = df['Address'] + ' ' + df['City']
print(df[['Address', 'City', 'New_Address']])


"""Output:
                             Address        City  \
0                  3959 Amanda Burgs    Dortmund   
1                 82072 Dawn Centers  Nottingham   
2                  4133 Young Canyon     Geelong   
3        8148 Thomas Creek Suite 100    Edmonton   
4          5813 Lori Ports Suite 269     Bristol   
...                              ...         ...   
293906        389 Todd Path Apt. 159  Townsville   
293907             52809 Mark Forges     Hanover   
293908  407 Aaron Crossing Suite 495    Brighton   
293909               3204 Baird Port     Halifax   
293910           143 Amanda Crescent      Tucson   

                                  New_Address  
0                  3959 Amanda Burgs Dortmund  
1               82072 Dawn Centers Nottingham  
2                   4133 Young Canyon Geelong  
3        8148 Thomas Creek Suite 100 Edmonton  
4           5813 Lori Ports Suite 269 Bristol  
...                                       ...  
293906      389 Todd Path Apt. 159 Townsville  
293907              52809 Mark Forges Hanover  
293908  407 Aaron Crossing Suite 495 Brighton  
293909                3204 Baird Port Halifax  
293910             143 Amanda Crescent Tucson  

[293911 rows x 3 columns]
"""