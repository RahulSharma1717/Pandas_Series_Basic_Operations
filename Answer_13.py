# Create a new column Liquor Type with random values among (whiskey, rum, vodka).
# Store columns like category, category name, item description, and beverage type in a variable and display all values.

import numpy as np
import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)

liquor_type = ['whiskey', 'rum', 'vodka']
df['Liquor Type'] = np.random.choice(liquor_type, size=len(df))

selected_columns = ['Category', 'Category Name', 'Item Description', 'Liquor Type']
print(df[selected_columns])


"""Output:
     Category                   Category Name              Item Description  \
0     1701100  DECANTERS & SPECIALTY PACKAGES  Forbidden Secret Coffee Pack   
1     1701100  DECANTERS & SPECIALTY PACKAGES   Laphroaig w/ Whiskey Stones   
2     1701100  DECANTERS & SPECIALTY PACKAGES  Forbidden Secret Coffee Pack   
3     1081200                  CREAM LIQUEURS           Rumchata "GoChatas"   
4     1701100  DECANTERS & SPECIALTY PACKAGES  Forbidden Secret Coffee Pack   
..        ...                             ...                           ...   
914   1031200                  VODKA FLAVORED         Uv Red (cherry) Vodka   
915   1042100               IMPORTED DRY GINS         Tanqueray Rangpur Gin   
916   1032200           IMPORTED VODKA - MISC  Absolut Citron (lemon Vodka)   
917   1012100               CANADIAN WHISKIES                  Black Velvet   
918   1031080                  VODKA 80 PROOF        Five O'clock PET Vodka   

    Liquor Type  
0           rum  
1         vodka  
2           rum  
3         vodka  
4       whiskey  
..          ...  
914     whiskey  
915       vodka  
916       vodka  
917     whiskey  
918         rum  

[919 rows x 4 columns]
"""