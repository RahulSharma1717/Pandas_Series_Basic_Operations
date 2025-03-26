# Display the details and address with zipcode of all the stores.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)
print(df[['Store Number', 'Store Name', 'Address', 'City', 'Zip Code']])


"""Output:
     Store Number                         Store Name                  Address  \
0            2538    Hy-Vee Food Store #3 / Waterloo         1422 FLAMMANG DR   
1            2662  Hy-Vee Wine & Spirits / Muscatine    522 MULBERRY, SUITE A   
2            3650         Spirits, Stogies and Stuff       118 South Main St.   
3            3723                 J D Spirits Liquor             1023  9TH ST   
4            2642    Hy-Vee Wine and Spirits / Pella          512 E OSKALOOSA   
..            ...                                ...                      ...   
914          3944          Sam's Club 4973 / Dubuque           4400 ASBURY RD   
915          4008               Sioux Valley Spirits            116 E MAIN ST   
916          3385     Sam's Club 8162 / Cedar Rapids  2605 BLAIRS FERRY RD NE   
917          2487               Anamosa Family Foods            402 EAST MAIN   
918          4559                Osage Payless Foods            633, CHASE ST   

             City Zip Code  
0        WATERLOO    50702  
1       MUSCATINE    52761  
2        HOLSTEIN    51025  
3           ONAWA    51040  
4           PELLA    50219  
..            ...      ...  
914       DUBUQUE    52002  
915        ANTHON    51004  
916  CEDAR RAPIDS    52402  
917       ANAMOSA    52205  
918         OSAGE    50461  

[919 rows x 5 columns]
"""