import pandas as pd         # tabular data and csvs
import random               # to generate random data
from faker import Faker     # helps genreate fake but realistic data 
import os                   # file system ops

# initialize faker 
fake = Faker()

# make sure the data folder exits
os.makedirs("data", exist_ok=True)

# generate a bunch of fake customers 
num_cus = random.randint(1, 10000) # num of customers, btw 1 and 10000 
cust = [] # stores the list of customers

for x in range(1, num_cus + 1):
    cust.append({
        "customer_id": x,
        "first_name": fake.first_name(),
        "lastt_name": fake.last_name(),
        "region": random.choice(["North", "South", "East", "West"]),
        "signup_date": fake.date_between(start_date='-5y', end_date='-1y') # signup 1-5 years ago
    })

# save to csv file 
pd.DataFrame(cust).to_csv("data/customers.csv", index=False)

# generate fake products 
num_prod = random.randint(1, 500) # num of products, btw 1 and 500
cats = ["Electronics", "Home", "Fashion", "Books", "Sports"] # categories of products
prods = [] # stores list of products

for a in range(1111111, 1111111 + num_prod):
    prods.append({
        "product_id": a,
        "product_name": random.word().capitalize() + random.choice(["Max", "3000", "X", "P2", "+", "Plus", "Remastered"]),
        "category": random.choice(cats),
        "price": random.choice(10, 3500),
    })

# save to csv file 
pd.DataFrame(prods).to_csv("data/products.csv", index=False)

# generate fake orders for the fake customers
num_orders = 500
orders = []

for i in range(1001, 1001 + num_orders):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, num_cus), # link an order to a random customer by customerid
        "order_date": fake.date_between(start_date='-4y', end_date='today') # order placed in last 4 years 
    })

# save to csv file 
pd.DataFrame(orders).to_csv("data/orders.csv", index=False)

# generate order items (keep a reasonable range of items in orders)
