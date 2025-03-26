# Create a new column with random values between 1,1000.

import numpy as np
import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

rows = df.shape[0]
df['random_numbers'] = np.random.randint(1, 1000, rows)
print(df.iloc[:, -5:].head(50))


"""Output:
   Payment_Method Order_Status  Ratings                  products  \
0      Debit Card      Shipped        5            Cycling shorts   
1     Credit Card   Processing        4                Lenovo Tab   
2     Credit Card   Processing        2          Sports equipment   
3          PayPal   Processing        4             Utility knife   
4            Cash      Shipped        1         Chocolate cookies   
5          PayPal      Pending        4                Lenovo Tab   
6            Cash   Processing        1                   QLED TV   
7            Cash   Processing        1               Dress shirt   
8            Cash    Delivered        1            Dark chocolate   
9            Cash    Delivered        4                   Candles   
10    Credit Card      Shipped        2           Screwdriver set   
11    Credit Card      Pending        2                   Science   
12         PayPal    Delivered        1             Bottled water   
13         PayPal    Delivered        4              Fruit snacks   
14           Cash      Shipped        1                V-neck tee   
15    Credit Card      Pending        1                     Drama   
16     Debit Card      Shipped        2            Flavored water   
17           Cash      Shipped        3        Samsung Galaxy Tab   
18    Credit Card      Shipped        1              Orange juice   
19           Cash      Shipped        2                 Bookshelf   
20         PayPal   Processing        2                  Affogato   
21         PayPal   Processing        2                  Business   
22         PayPal   Processing        2                 Self-help   
23         PayPal      Pending        3                      Sink   
24         PayPal   Processing        1               Grape juice   
25     Debit Card      Pending        1                     Stove   
26         PayPal      Shipped        3                  Huawei P   
27    Credit Card      Shipped        1        Amazon Fire Tablet   
28           Cash    Delivered        5                  Curtains   
29           Cash      Pending        3         Pomegranate juice   
30     Debit Card      Pending        3             Running shoes   
31     Debit Card   Processing        3        Political thriller   
32     Debit Card   Processing        5                  Curtains   
33           Cash      Pending        2              Google Pixel   
34    Credit Card      Pending        4          Chocolate mousse   
35         PayPal    Delivered        4                     Vases   
36    Credit Card      Pending        4              Henley shirt   
37           Cash      Pending        4                      Toys   
38         PayPal   Processing        4                  Iced tea   
39    Credit Card      Pending        4             Running shoes   
40         PayPal      Pending        4               Apple juice   
41     Debit Card      Pending        4                     Drama   
42     Debit Card      Shipped        1  Microsoft Surface Laptop   
43         PayPal   Processing        5                      Desk   
44           Cash    Delivered        2             Bodycon dress   
45    Credit Card      Pending        4         Sports headphones   
46           Cash      Pending        5            Pendant lights   
47    Credit Card   Processing        3                    Clocks   
48    Credit Card    Delivered        1                 Comforter   
49    Credit Card      Pending        2                   Peacoat   

    random_numbers  
0              943  
1              180  
2              950  
3              371  
4              640  
5              655  
6              437  
7              337  
8              119  
9              951  
10             819  
11             681  
12             173  
13             218  
14             865  
15             192  
16              76  
17             693  
18             119  
19             306  
20             485  
21              62  
22             871  
23             196  
24             210  
25             133  
26             302  
27             697  
28             978  
29             296  
30               1  
31             815  
32             434  
33             777  
34             297  
35              97  
36             430  
37             169  
38             630  
39             225  
40             107  
41             806  
42             298  
43             622  
44             949  
45              30  
46             826  
47             251  
48             621  
49             615
"""