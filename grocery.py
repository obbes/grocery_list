# This program creates a grocery list defined as a dict
# each item on the grocery list is an embedded dict defined by
# the last purchase date, 
# the number of days since last purchase
#   ^this may be redundant
# and the amount of the item purchased
#
#The goal of the program is to take and update a grocery list
#to generate a grocery list for a user based on previous purchases
from datetime import datetime

#the grocery list dict
grocery_list ={

#Test case example of an embedded dict
# #'apples': {    'last_buy': datetime(2020,1,1),    'days': 0,    'amount': 4}
'apples': {    'last_buy': datetime(2020,1,1),    'days': 0,    'amount': 4}
}

#method checks when the item was last purchased
def last_bought(item):
    return item['last_buy']
#method returns days 
def days_since_purchase(item):
    return item['days']

#method adds or updates an item in grocery_list

def add_item(item, amount):
    grocery_list[item] = {
        'last_buy': datetime.now(),
        'days': 0,
        'amount': amount
        
    }
def purchase_item(item, amount):
    now = datetime.now()
    if item in grocery_list.keys():
        grocery_list[item]['days'] = now - grocery_list[item]['last_buy']
        grocery_list[item]['last_buy'] = now
        grocery_list[item]['amount_lasted'] = [grocery_list[item]['amount'], grocery_list[item]['days']]
        grocery_list[item]['amount'] = amount
    else:
        add_item(item, amount)
    return grocery_list

print(purchase_item('bananas', 2))
purchase_item('apples', 5)

print(grocery_list)