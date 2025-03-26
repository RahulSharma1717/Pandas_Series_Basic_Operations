# Create a column for total sales.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

df['total_sales'] = df['Total_Purchases'] * df['Amount']
print(df.iloc[:, -13:])


"""Output:
        Total_Purchases      Amount  Total_Amount Product_Category  \
0                     3  108.028757    324.086270         Clothing   
1                     2  403.353907    806.707815      Electronics   
2                     3  354.477600   1063.432799            Books   
3                     7  352.407717   2466.854021       Home Decor   
4                     2  124.276524    248.553049          Grocery   
...                 ...         ...           ...              ...   
293906                5  194.792597    973.962984            Books   
293907                1  285.137301    285.137301      Electronics   
293908                3   60.701761    182.105285         Clothing   
293909                1  120.834784    120.834784       Home Decor   
293910                7  340.319059   2382.233417       Home Decor   

        Product_Brand Product_Type   Feedback Shipping_Method Payment_Method  \
0                Nike       Shorts  Excellent        Same-Day     Debit Card   
1             Samsung       Tablet  Excellent        Standard    Credit Card   
2       Penguin Books   Children's    Average        Same-Day    Credit Card   
3          Home Depot        Tools  Excellent        Standard         PayPal   
4              Nestle    Chocolate        Bad        Standard           Cash   
...               ...          ...        ...             ...            ...   
293906  Penguin Books      Fiction        Bad        Same-Day           Cash   
293907          Apple       Laptop  Excellent        Same-Day           Cash   
293908         Adidas       Jacket    Average         Express           Cash   
293909           IKEA    Furniture       Good        Standard           Cash   
293910     Home Depot  Decorations    Average        Same-Day           Cash   

       Order_Status  Ratings            products  total_sales  
0           Shipped        5      Cycling shorts   324.086270  
1        Processing        4          Lenovo Tab   806.707815  
2        Processing        2    Sports equipment  1063.432799  
3        Processing        4       Utility knife  2466.854021  
4           Shipped        1   Chocolate cookies   248.553049  
...             ...      ...                 ...          ...  
293906   Processing        1  Historical fiction   973.962985  
293907   Processing        5             LG Gram   285.137301  
293908      Shipped        2               Parka   182.105284  
293909      Shipped        4            TV stand   120.834784  
293910      Shipped        2              Clocks  2382.233416  

[293911 rows x 13 columns]
"""