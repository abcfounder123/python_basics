

def add(*x):
    ans = 0
    for n in x:
        ans += int(n)
    return ans

"""

29. boolean exercises




c1 = True
c2 = True
c3 = True

# all true---> and
if c1 and c2 and c3:
    print("All are True.")

if not c1 and not c2 and not c3:
    print("all false.")


# at least one true ---> or
if c1 or c2 or c3:
    print("At least one is true.")


if not c1 or not c2 or not c3: print("At least one is fasle.")


# list, if, elif, else, boolean expression( 1 > 2 , True and True ), conditional executions / statement,
conditional expression ( ternary operator )

# order

# must do ---> name, color, size, item count,
# choose one ---> bank card or cash on delivery

# delivery
# must do ---> address confirm, ph No confirm


orders = []
delivery = []

name = input("Item name : ")
color = input("Item color : ")
size = input("Item size : ")
count = input("Item count : ")
bank_card = input("card payment confirm : ")
cash_on_delivery = input("COD confirm : ")

card_or_cod = bank_card if bank_card else cash_on_delivery

order = name and color and size and count and (bank_card or cash_on_delivery)

if order:
    new = [name, color, size, count, card_or_cod]
    orders.append(new)
    print(orders)
    address = input(f"Please confirm address and ph No for {new} : ")
    if address:
        delivery.append([new, address])
        print(delivery)
        print(f"{new} will be send to {address} by delivery partner kerry in one week.")





# c1 > c2
# c3 > c4
# c5 in c6

age = int(input("age = "))
min_age = 18
bank_card = int(input("Bank card: "))
amount = 3000
item = input("item : ")
stock_list = ["beer", "white wine", "orange juice"]
order = age > min_age and bank_card > amount and item in stock_list

if order:
     print("Ok")






30. dict

name                     >>       dict, dictionary
definition               >>       list of keys and values
usage                    >>       {0 : "a", }, dict()
description              >>       1. Access items            --->    d[key]
                                  2. change item value       --->    d[key] = value

                                   3. loop through a dict    --->    d, d.keys(), d.values(), d.items()
                                   4. check if item in list ---> in
                                   5. check if item not in list ---> not in
                                   6. len()

                                   7. Add item ---> d[key] = value

                                   8. add item with index --> insert()
                                   9. remove with value ---> remove()
                                   10.remove with index ---> pop()


                                   11.clear all value ---> clear()
                                   12.remove with del keyword
                                        >>> del d[key]
                                        >>> object
                                   13. copy a list ---> copy()

                                   14. join lists ---> +
                                                  ---> loop and append()
                                                  ---> extend()




item_list

No   item     price    stock  exp_date  discount_price
1.   apple    1      1000     1          0.3
2.   note 11  200      10       _        0
3.


x = ["apple",
     1000,
     10000]

item_list = {
    1: {"item": "apple",
        "price": 1,
        "exp_date": 5,
        "stock": 10000},
    2: {"item": "note 11",
        "price": 200,
        "exp_date": 100,
        "stock": 10},
    3: {"item": "note 12",
        "price": 250,
        "exp_date": 100,
        "stock": 50},
    4: {"item": "banana",
        "price": 0.3,
        "exp_date": 10,
        "stock": 12000}

}

# change item
# print(item_list[1]["exp_date"])
for k in item_list:
    if item_list[k]["exp_date"] < 15:
        item_list[k]["discount_price"] = item_list[k]["price"] * 30 / 100
    else:
        item_list[k]["discount_price"] = 0

print(item_list)

for k in item_list:
    del item_list[k]["discount_price"]

print(item_list)
item_list.clear()
print(item_list)

# order = []

# access
# for value in item_list.values():
#     if "note" in value["item"]: order.append(value)


# print(order)


"""




"""


30. dict

name                     >>       dict, dictionary
definition               >>       list of keys and values
usage                    >>       {0 : "a", }, dict()
description              >>       1. Access items            --->    d[key]
                                  2. change item value       --->    d[key] = value

                                   3. loop through a dict    --->    d, d.keys(), d.values(), d.items()
                                   4. check if item in list ---> in
                                   5. check if item not in list ---> not in
                                   6. len()

                                   7. Add item ---> d[key] = value

                                   8. add item with index --> insert()
                                   9. remove with value ---> remove()
                                   10.remove with index ---> pop()


                                   11.clear all value ---> clear()
                                   12.remove with del keyword
                                        >>> del d[key]
                                        >>> object
                                   13. copy a list ---> copy()

                                   14. join lists ---> +
                                                  ---> loop and append()
                                                  ---> extend()




item_list

No   item     price    stock  exp_date  discount_price   cash back
1.   apple    1        1000   15         0.3
2.   note 11  200      10       _        0
3.





x = ["apple",
     1000,
     10000]

item_list = {
    1: {"item": "apple",
        "price": 1,
        "exp_date": 5,
        "stock": 10000},

    2: {"item": "note 11",
        "price": 200,
        "exp_date": 100,
        "stock": 10},

    3: {"item": "note 12",
        "price": 250,
        "exp_date": 100,
        "stock": 50},

    4: {"item": "banana",
        "price": 0.3,
        "exp_date": 10,
        "stock": 12000}

}

# 4. del
#del item_list[1]["exp_date"]
for i in item_list:
    del item_list[i]["exp_date"]
print(item_list)

item_list.clear()
print(item_list)

#del item_list


# 3. add new item
# item_list[1]["discount_price"] = 0.3

for i in item_list:
    if item_list[i]["exp_date"] <= 10:
        item_list[i]["discount"] = item_list[i]["price"] * 30 / 100
    else:
        item_list[i]["discount"] = 0


    if item_list[i]["price"] >= 200:
        item_list[i]["cash back"] = item_list[i]["price"] * 5 / 100
    else:
        item_list[i]["cash back"] = 0




print(item_list)
"""
"""
# 2. change value
#item_list[1]["price"] = 0.7
for i in item_list:
    if "note" in item_list[i]["item"]:
        item_list[i]["price"] = item_list[i]["price"] * 90 / 100

print(item_list)


#print(item_list[3]["price"])

# 1. access
order = []
for k in item_list.keys():
    if "note" in item_list[k]["item"]:
        order.append(item_list[k])

print(order)

print("note" in "redmi note 11")
"""


















