# Create a new column Beverage Type with values 'LIQUOR'.
# Store columns like category, category name, item description, and beverage type in a variable and display all values.

import pandas as pd

df = pd.read_csv('sample_iowa_liquor_sales.csv')
pd.set_option('display.max_columns', None)

df['Beverage Type'] = 'LIQUOR'
variable_df = df[['Category', 'Category Name', 'Item Description', 'Beverage Type']]
print(variable_df)


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

    Beverage Type  
0          LIQUOR  
1          LIQUOR  
2          LIQUOR  
3          LIQUOR  
4          LIQUOR  
..            ...  
914        LIQUOR  
915        LIQUOR  
916        LIQUOR  
917        LIQUOR  
918        LIQUOR  

[919 rows x 4 columns]
"""