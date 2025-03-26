# Display all the columns that are related to products.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df[['products', 'Product_Category', 'Product_Brand', 'Product_Type']].head(50))


"""Output:
                    products Product_Category      Product_Brand Product_Type
0             Cycling shorts         Clothing               Nike       Shorts
1                 Lenovo Tab      Electronics            Samsung       Tablet
2           Sports equipment            Books      Penguin Books   Children's
3              Utility knife       Home Decor         Home Depot        Tools
4          Chocolate cookies          Grocery             Nestle    Chocolate
5                 Lenovo Tab      Electronics              Apple       Tablet
6                    QLED TV      Electronics            Samsung   Television
7                Dress shirt         Clothing               Zara        Shirt
8             Dark chocolate          Grocery             Nestle    Chocolate
9                    Candles       Home Decor         Home Depot  Decorations
10           Screwdriver set       Home Decor         Home Depot        Tools
11                   Science            Books       Random House  Non-Fiction
12             Bottled water          Grocery          Coca-Cola        Water
13              Fruit snacks          Grocery             Nestle       Snacks
14                V-neck tee         Clothing             Adidas      T-shirt
15                     Drama            Books       Random House   Literature
16            Flavored water          Grocery              Pepsi        Water
17        Samsung Galaxy Tab      Electronics              Apple       Tablet
18              Orange juice          Grocery          Coca-Cola        Juice
19                 Bookshelf       Home Decor               IKEA    Furniture
20                  Affogato          Grocery             Nestle       Coffee
21                  Business            Books      HarperCollins  Non-Fiction
22                 Self-help            Books      Penguin Books  Non-Fiction
23                      Sink       Home Decor  Bed Bath & Beyond     Bathroom
24               Grape juice          Grocery          Coca-Cola        Juice
25                     Stove       Home Decor  Bed Bath & Beyond      Kitchen
26                  Huawei P      Electronics            Samsung   Smartphone
27        Amazon Fire Tablet      Electronics              Apple       Tablet
28                  Curtains       Home Decor         Home Depot  Decorations
29         Pomegranate juice          Grocery          Coca-Cola        Juice
30             Running shoes         Clothing             Adidas        Shoes
31        Political thriller            Books      HarperCollins     Thriller
32                  Curtains       Home Decor               IKEA  Decorations
33              Google Pixel      Electronics            Samsung   Smartphone
34          Chocolate mousse          Grocery             Nestle    Chocolate
35                     Vases       Home Decor               IKEA  Decorations
36              Henley shirt         Clothing               Zara        Shirt
37                      Toys            Books      Penguin Books   Children's
38                  Iced tea          Grocery              Pepsi   Soft Drink
39             Running shoes         Clothing             Adidas        Shoes
40               Apple juice          Grocery          Coca-Cola        Juice
41                     Drama            Books       Random House   Literature
42  Microsoft Surface Laptop      Electronics              Apple       Laptop
43                      Desk       Home Decor               IKEA    Furniture
44             Bodycon dress         Clothing               Zara        Dress
45         Sports headphones      Electronics               Sony   Headphones
46            Pendant lights       Home Decor               IKEA     Lighting
47                    Clocks       Home Decor         Home Depot  Decorations
48                 Comforter       Home Decor  Bed Bath & Beyond      Bedding
49                   Peacoat         Clothing             Adidas       Jacket
"""