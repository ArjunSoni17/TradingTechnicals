import alpaca_trade_api as tradeapi
from pprint import pprint
import pandas as pd
from datetime import date
import numpy as np



api = tradeapi.REST(
    key_id='xxxxxxxx',
    secret_key='xxxxxxx',
    base_url='xxxxx'
)
# api.list_positions()

# Get the last 100 of our closed orders
closed_orders = api.list_orders(
    status='filled',
    limit=1000,
    #nested=True  # show nested multi-leg orders
)


sell=[]
buy=[]
stock=[]

# Get only the closed orders for a particular stock
closed_aapl_orders = [o for o in closed_orders ]
print(len(closed_orders))

symbol1 = input("enter the symbol:").upper()
currentdate = input("Please enter todays date in the format yyyy-mm-dd: ")
year,month,day = currentdate.split('-')
today = date(int(year),int(month),int(day))

for item in closed_aapl_orders:
    if item.symbol == symbol1 or symbol1=="":
        
        if today == item.created_at.date() :

            if item.status== "filled" and item.side=="buy"  :
                buy_side= item.created_at.date(),item.symbol,item.side,item.filled_avg_price,item.qty,item.limit_price,item.status
                buy.append(buy_side)
                stock1=item.symbol
                stock.append(stock1)
            if item.status=="filled" and item.side=="sell":
                sell_side= item.created_at.date(),item.symbol,item.side,item.filled_avg_price,item.qty,item.limit_price,item.status
                sell.append(sell_side)
                

buydf = pd.DataFrame(buy,columns =['Created_at', 'symbol', 'side','filled_avg_price','qty','limit_price','status']) 
print(buydf)
print()

print()
selldf= pd.DataFrame(sell,columns =['Created_at', 'symbol', 'side','filled_avg_price','qty','limit_price','status']) 
print(selldf)
