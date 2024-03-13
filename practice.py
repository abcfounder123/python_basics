
# practices for first month

# practice.1  ( indexing, slicing )
# practice.2   --->   format table
# practice.3   --->   Nested if
# practice.4   --->   automatic water motor controller
# practice.5   --->   elif ( exam fail/pass with marks )
# practice.6   --->    boolean exercises
# practice.7   --->   order
# practice.8   --->   beer
# practice.9   --->   palindrome check
# practice.10   --->   2D  data, nested dict
# practice.11   --->   2D  data with rate formula
#                      https://drive.google.com/file/d/1vMWvbMAgvsZhRgmV-29wbvgsaWjL4ZZK/view?usp=drivesdk
# practice.12   --->   Solved Examples Using Sets Formulas
# practice.13   --->   square root / ํF to ํC  ( tkinter GUI )
# practice.14   --->   effect, result


"""

practice.1  ( indexing, slicing )

# data collection, sequence data type, element, range, index, slicing

# indexing ( +, - )

# step.1 ( first element, last element , range, min, max )

# left (+) ---> if total count is 10, max index = 9   --->  max_index = total_count - 1
                                                      --->  last element   ---> x[len(x) - 1]
# right(-) ---> if total count is 10, max index = 10  --->  max_index = total_count
                                                      --->  first element  ---> x[-len(x)]

x = "abcdefg"

print(x[0])  # first element
print(x[len(x) - 1])  # last element

print(len(x) - 1)
print(-len(x))

print(x[-len(x)])  # first element
print(x[-1]) # last element

x = "abcdefg"
#  a,  b,  c,  d,  e,  f,  g
# -7, -6, -5, -4, -3, -2, -1,
#  0,  1,  2,  3,  4,  5,  6

min_index = -len(x)
max_index = len(x) - 1
print(min_index)
print(max_index)
print(x[32])

################################################

# step.2 ( middle element )

x = "qqabcdefgqq"
t = len(x)
print(t // 2)
print(x[t // 2])  # middle element ( total_count = odd number )


x = "abcdefgh"
t = len(x)
# total_count = even number
print(x[t//2])  # middle element ( right )
print(x[t//2 - 1])  # middle element ( left )

################################################

# step.3  ( first 3, last 3 )
# total - easy index

x = "abcdefg"

print(2)  # positive index of first 3
print(x[2])  # first 3


t = len(x)
print(t - 3 ) # positive index of last 3
print(x[t - 3]) # last 3


print(-3) # negative index of last 3
print(x[-3]) #

print(-(t - 2)) # negative index of first 3
print(x[-(t - 2)]) #

################################################

# step.4 ( range )


# range ( x ) --> -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6  ---> -total to total - 1
x = "abcdefg"

# range ( y ) ---> -5 .... 4  ---> -total_cont, ..., total_count - 1
y = "apple"

# range ( total = 1million ) ---> -1m, ... 1m -1


--->  IndexError: string index out of range

################################################
################################################

# slicing [start:stop:step]
# first 5
# last 5

# step.1

# -8, -7, -6, -5, -4, -3, -2, -1,
#  0,  1,  2,  3,  4,  5,  6 ,  7

x = "abcdefgh"

x = "abcdefg"

# left to right ---> positive step
print(x[2:7:1])  # 2,  3,  4,  5
print(x[-6:-1:1])  # -6, -5, -4, -3, -2
print(x[2:-1:1])

# right to left ---> negative step
print(x[6:1:-1])  # 6, 5, 4, 3, 2
print(x[-2:-7:-1])  # -2, -3, -4, -5, -6
# total = 100



x = "abcdefgh"  # -8 ---> 7
print(x[:5:])  # first five #  0, 1, 2, 3, 4,
print(x[-5:])  # last five # -5, -4, -3, -2, -1

################################################

# step.2 ---> total count = even ( middle (10 elements) )

x = "11111111abcdefgh11111111"
t = 10  # total 10
half = t // 2  # 5

rm = len(x) // 2
s = rm - half
stop = rm + half

print(len(x))
print(rm, x[rm])
print(s)
print(stop)

middle = x[s:stop] # middle (10 elements)
print(middle)

################################################

# step.3 ---> total count = odd ( middle (3 elements) )

x = "11111111abcdefg11111111"

t = 11  # total 7
half = t // 2  # 3

m = len(x) // 2
s = m - half
stop = m + half + 1

print(len(x))
print(m, x[m])
print(s)
print(stop)

middle = x[s:stop]  # middle (3 elements)
print(middle)

################################################

# step.4 ---> total count = even ( middle (10 elements) ) # equation

x = "aaaaaaaaaaabcdefghaaaaaaaaaa"


t = 7  # total 7
half = t // 2  # 3

m = len(x) // 2

s = m - half
stop = m + half

middle = x[s:stop] # middle (10 elements)
print(middle)

################################################

# step.5 ---> total count = odd ( middle (11 elements) )  # equation

x = "aaaaaaaaaaaabcdefgaaaaaaaaaaa"

number_elements = 11

m = len(x) // 2
f = (number_elements // 2)
s = m - f
stop = m + f + 1
middle = x[s:stop] # middle (11 elements)
print(middle)

################################################

# step.6 ---> reversed order
x = "aaaaaaaaaaabcdefghaaaaaaaaaa"

total = 8

rm = len(x) // 2
half = (total // 2)

s = rm - half
stop = rm + half

middle = x[s:stop]  # middle (8 elements) # abcdefgh
print(middle)


reverse = middle[::-1]
print(reverse)

#######

# reverse
x = "aaaaaaaaaaabcdefghaaaaaaaaaa"

total = 8
h = total // 2

rm = len(x) // 2

s = rm + h - 1
stop = rm - h - 1

middle = x[s:stop:-1]  # middle (8 elements)
print(middle)

################################################


# step.5 ---> total count = odd ( middle (11 elements) )  # equation

x = "aaaaaabcdefgaaaaa"

number_elements = 7

m = len(x) // 2
f = (number_elements // 2)

s = m - f
stop = m + f + 1
middle = x[s:stop]  # middle (7 elements)
print(middle)


middle = middle[::-1]  # middle (7 elements) # abcdefgh
print(middle)

#######

# reversed
x = "aaaaaabcdefgaaaaa"

number_elements = 11

m = len(x) // 2
f = number_elements // 2

s = m + f
stop = m - f - 1
middle = x[s:stop:-1]  # middle (7 elements)
print(middle)


################################################################################################

practice.2   --->   format table

h1 = "No"
h2 = "Name"
h3 = "age"
x = f"|{h1:^6}|{h2:^30}|{h3:^7}|"
print("-" * 47 )
print(x)
print("-" * 47 )

l = [(1, "Mg Mg", 20),
     (2, "Mg Aung Myint Myat", 30),
     (3, "Mg Mg", 20),
     (4, "Mg Aung Myint Myat", 30),
     (5, "Mg Mg", 20),
     (6, "Mg Aung Myint Myat", 30),
]

for i in l:
    no, name, age = i
    r = f"|{no:^6}|{name:^30}|{age:^7}|"
    print(r)
    print("-" * 47)


-----------------------------------------------
|  No  |             Name             |  age  |
-----------------------------------------------
|  1   |            Mg Mg             |  20   |
-----------------------------------------------
|  2   |      Mg Aung Myint Myat      |  30   |
-----------------------------------------------
|  3   |            Mg Mg             |  20   |
-----------------------------------------------
|  4   |      Mg Aung Myint Myat      |  30   |
-----------------------------------------------
|  5   |            Mg Mg             |  20   |
-----------------------------------------------
|  6   |      Mg Aung Myint Myat      |  30   |
-----------------------------------------------

################################################################################################

practice.3   --->   Nested if

c1 = 1
c2 = 0
c3 = 1
c4 = 0
c5 = 1
# 0 0 1
if c1:
    if c2:
        pass
    else:
        if c3:
            if c4:
                pass
            else:
                if c5:
                    print("abc")
                else:
                    pass
        else:
            if c5:
                pass
            else:
                pass

else:
    if c2:
        if c3:

            if c4:
                pass
            else:
                pass

        else:
            pass
    else:
        if c3:
            if c4:
                pass
            else:
                pass


        else:
            pass


################################################################################################

practice.4   --->   automatic water motor controller

c1 = 1  # water sensor.2  ( low level ) ( True )
c2 = 0  # electric ( true )
c3 = 0  # short circuit ( false )
c4 = 0  # water sensor.1  ( low level ) ( True )

if c1:
    if c2:
        if c3:
            print("message motor error")
        else:
            print("motor --->  water 1")
    else:
        print('generator --> electric')
        if c3:
            print("message motor error")
            print("close generator")

       else:
            print("motor --->  water 2")

################################################################################################

practice.5   --->   elif ( exam fail/pass with marks )

m = int(input("marks = "))

c1 = m == 100
c2 = m >= 80
c3 = m >= 40
c4 = m < 40

if c1: print("very good.")
elif c2: print("good")
elif c3: print("not bad")
elif c4: print("fail")

if c1: print("very good.")
if not c1 and c2: print("good")
if not c1 and not c2 and c3: print("not bad")
if not c1 and not c2 and not c3 and c4: print("fail")

if m == 100: print("very good.")
if 100 > m >= 80: print("good")
if 40 <= m < 80 : print("not bad")
if m < 40: print("fail")

################################################################################################

practice.6   --->    boolean exercises

# step.1 ( accept any ) ( or )

c = input("paid class feee : ")
c2 = input("member : ")
c3 = input("fund : ")

if c or c2 or c3:
    print("access class")

################################################

# step.2 ( accept all ) ( and )

c = input("operator check : ")
c2 = input("Engine check : ")
c3 = input("Rocket check : ")
c4 = input("Weather check : ")

if c and c2 and c3 and c4:
    print("Rocket is ready to lunch.")

################################################

# step.3 ( accept any + accept all ) ( or + and )

c = input("paid class fee : ")
c2 = input("member : ")

c3 = input("fund : ")

if (c or c2) and c3:
    print("access special class")

################################################

# step.4 ( not )


def less_credit(n):
    return n < 11000


def under_age(age):
    return age <= 18


amount = int(input("Credit amount : "))
buyer_age = int(input("age : "))

if less_credit(amount) or under_age(buyer_age):
    print("You can not buy Beer.")

else:
    print("you can buy beer.")


if not less_credit(amount) and not under_age(buyer_age):
    print("You can buy Beer.")

else:
    print("you can not buy beer.")

################################################

# step.5

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

if not c1 or not c2 or not c3:
    print("At least one is fasle.")

################################################################################################

practice.7   --->   order

# and, or
# all ---> name, color, size, item count, payment
# at least one ---> bank card or cash on delivery

# delivery
# must do ---> address confirm, ph No confirm

################################################

orders = []
delivery = []

name = input("Item name : ")
color = input("Item color : ")
size = input("Item size : ")
count = input("Item count : ")

bank_card = input("card payment confirm : ")
cash_on_delivery = input("COD confirm : ")

payment = bank_card if bank_card else cash_on_delivery

order = name and color and size and count and (bank_card or cash_on_delivery)

if order:
    new = [name, color, size, count, payment] # ['shirt', 'blue', 'M', '2', 'COD']
    orders.append(new)
    print(orders)
    address = input(f"Please confirm address and ph No for {new} : ")

    if address:
        delivery.append([new, address]) # [[['shirt', 'blue', 'M', '2', 'COD'], 'Mandalay, no.1 street, 09111111']]
        print(delivery)
        print(f"{new} will be send to {address} by delivery partner kerry in one week.")

################################################################################################

practice.8   --->   beer

# comparison operator, membership operator and boolean operator
# c1 > c2
# c3 > c4
# c5 in c6

min_age = 18
amount = 3000
stock_list = ["beer", "white wine", "Rum"]

age = int(input("age = "))
bank_card = int(input("Bank card: "))
item = input("item : ")

order = age > min_age and bank_card > amount and item in stock_list
print(order)
if order:
     print("Ok")

################################################################################################

practice.9   --->   palindrome check

# step.1

p = "aba"
print(p == p[::-1])

################################################

# step.2

phrase = input("Enter a phrase: ")  # "1a BA1."  ---> 1aBA1  ---> 1aba1
clean_list = []  # ["1", "a", "b", "a", "1"]

for charactor in phrase.lower():
    print(charactor)
    if charactor.isalnum() and charactor != " ":
        clean_list.append(charactor)
        print(clean_list)

palindrome = clean_list == clean_list[::-1]

if palindrome:
    print(f"\"{phrase}\" is a palindrome.")

else:
    print(f"\"{phrase}\" is not a palindrome.")

################################################

# step.3

space = " "
punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''  # +
rm_list = space + punctuations

phrase = input("Enter a phrase: ")  # "a Ba."
clean_list = []

for charactor in phrase.lower():
    if charactor not in rm_list:
        clean_list.append(charactor)

palindrome = clean_list == clean_list[::-1]

if palindrome:
    print(f"\"{phrase}\" is a palindrome.")

else:
    print(f"\"{phrase}\" is not a palindrome.")



Enter a phrase: A man, a plan, a canal, Panama! <enter>
"A man, a plan, a canal, Panama!" is a palindrome.

Enter a phrase: Hello, World! <enter>
"Hello, World!" is not a palindrome.

################################################

# step.4

def palindrome_check(phrase):
    space = " "
    punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    rm_list = space + punctuations

    clean_list = []

    for charactor in phrase.lower():
        if charactor not in rm_list:
            clean_list.append(charactor)

    palindrome = clean_list == clean_list[::-1]

    if palindrome:
        return f"\"{phrase}\" is a palindrome."

    else:
        return f"\"{phrase}\" is not a palindrome."


# test
check_list = {"A man, a plan, a canal, Panama!": "\"A man, a plan, a canal, Panama!\" is a palindrome.",
              "Hello, World!": "\"Hello, World!\" is not a palindrome.",
              "121": "\"121\" is a palindrome.",
              }

for q, ans in check_list.items():
    print(ans == palindrome_check(q))

################################################################################################

practice.10   --->   2D  data, nested dict

x, y = col, row

item_list
No   item     price    stock  exp_date  discount_price   cash back
1.   apple    1        1000   10         0.3               0
2.   note 11  200      10       _        0                 10
3.

################################################

item_list = {
   1: {"item": "apple",
       "price": 1,
       "exp_date": 5,
       "stock": 10000,
       },

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

################################################

# 1. access
order = []
order_list = ["apple", "banana"]
for k in item_list:
   if item_list[k]["item"] in order_list:
       order.append(item_list[k])

print(order)

################################################

# 2. change value
#item_list[1]["price"] = 0.7
for i in item_list:
   if "note" in item_list[i]["item"]:
       item_list[i]["price"] -= item_list[i]["price"] * 10 / 100

print(item_list)
#print(item_list[3]["price"])

################################################

# 2. change value
for i in item_list:
   if item_list[i]['exp_date'] < 11:
       item_list[i]["price"] *= 0.9

print(item_list)

{1: {'item': 'apple', 'price': 0.9, 'exp_date': 5, 'stock': 10000},
 2: {'item': 'note 11', 'price': 200, 'exp_date': 100, 'stock': 10},
 3: {'item': 'note 12', 'price': 250, 'exp_date': 100, 'stock': 50},
 4: {'item': 'banana', 'price': 0.27, 'exp_date': 10, 'stock': 12000}}

################################################

# 3. add new column
# item_list[1]["discount_price"] = 0.3

for i in item_list:
   if item_list[i]["exp_date"] <= 5:
       item_list[i]["discount"] = item_list[i]["price"] * 0.3
   else:
       item_list[i]["discount"] = 0

   if item_list[i]["price"] >= 200:
       item_list[i]["cash back"] = item_list[i]["price"] * 0.05
   else:
       item_list[i]["cash back"] = 0

print(item_list)


{1: {'item': 'apple', 'price': 1, 'exp_date': 5, 'stock': 10000, 'discount': 0.3, 'cash back': 0},
 2: {'item': 'note 11', 'price': 200, 'exp_date': 100, 'stock': 10, 'discount': 0, 'cash back': 10.0},
 3: {'item': 'note 12', 'price': 250, 'exp_date': 100, 'stock': 50, 'discount': 0, 'cash back': 12.5},
 4: {'item': 'banana', 'price': 0.3, 'exp_date': 10, 'stock': 12000, 'discount': 0.09, 'cash back': 0}}

################################################

# 4. del
#del item_list[1]["exp_date"]
for i in item_list:
   del item_list[i]["exp_date"]

print(item_list)

{1: {'item': 'apple', 'price': 1, 'stock': 10000},
 2: {'item': 'note 11', 'price': 200, 'stock': 10},
 3: {'item': 'note 12', 'price': 250, 'stock': 50},
 4: {'item': 'banana', 'price': 0.3, 'stock': 12000}}

#item_list.clear()
#print(item_list)
#del item_list

################################################################################################

practice.11   --->   2D  data with rate formula
https://drive.google.com/file/d/1vMWvbMAgvsZhRgmV-29wbvgsaWjL4ZZK/view?usp=drivesdk

item_list

No   item     price    stock  exp_date  discount_price   cash back
1.   apple    1        1000    5         0.3              0
2.   note 11  200      10       _        0               10
3.

################################################


{1: {}, 
 2: {},
 3: {},
 4: {},
}

item_list = {
    1: {"item": "apple",
        "price": 1,
        "exp_date": 5,
        "stock": 1000,

        },

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
        "exp_date": 6,
        "stock": 1000}
}

################################################

# 1. access
order = []

for k in item_list:
    if item_list[k]["exp_date"] <= 7:
        n = item_list[k]['item']
        order.append(n)

print(order)

################################################

# 2. change value
#item_list[1]["price"] = 0.7

rates = {
    "apple": 100,
    "banana": 200,
    "note 11": 1,
    "note 12": 1,

}

print(1000 / 750)
print(150 * 1.334)
for i in item_list:
    name = item_list[i]["item"]  # "apple"
    date = item_list[i]["exp_date"]  # 5
    total = item_list[i]["stock"]  # 1000
    rate = rates[name]
    if date <= 7 and (rate * date) < total:
        if total / (rate * date) < 1.5:
            item_list[i]["price"] *= 0.8

        if total / (rate * date) >= 1.5:
            item_list[i]["price"] *= 0.6

print(item_list)
#print(item_list[3]["price"])

################################################

# 3. add new item
# item_list[1]["discount_price"] = 0.3

for i in item_list:
    if item_list[i]["exp_date"] <= 7:
        item_list[i]["discount"] = item_list[i]["price"] * 0.3
    else:
        item_list[i]["discount"] = 0

    if item_list[i]["price"] >= 200:
        item_list[i]["cash back"] = item_list[i]["price"] * 0.05
    else:
        item_list[i]["cash back"] = 0

print(item_list)

################################################

# 4. del
#del item_list[1]["exp_date"]
for i in item_list:
    del item_list[i]["exp_date"]
print(item_list)

item_list.clear()
print(item_list)

#del item_list

################################################################################################

practice.12   --->   Solved Examples Using Sets Formulas

Example 1:
In a club, each person plays chess or carom or both.
The number of people who play chess, carom or both are 11, 12 and 3 respectively.
Representing this given information as sets and
using the set formulae,

################################################

mg mg, ma ma, aung aung

chess - mg mg, ma ma, aung aung
c - mg mg, ma ma
cook - ma ma, aung aung
write - mg mg, ma ma, aung aung

s = {'mg mg', 'ma ma', 'aung aung', 'mg mg', 'ma ma', 'ma ma', 'aung aung', 'mg mg', 'ma ma', 'aung aung'}
print(s)

10   -->  -2, -3, -2   -->   3

23 - 3 = 20

################################################

Q1.  total people in club

let p is chess group
let q is carrom group

n(p) = 11
n(q) = 12
n(p ∩ q) = 3

Applying the set formula,
n(P ∪ Q) = n(P) + n(Q) - n(P∩Q) = 11 + 12 - 3 = 20

Answer: total people in club = 20

################################################

# introduction

# let each person has club id No.1 or 2 or 3
# 3 person like both of chess and carom
# let id of 3 person be 1, 5, 7

p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}  # chess
q = {1, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20}  # carom
# print(len(p))
# print(len(q))


x = p.intersection(q)  # (P ∩ Q)

print("id of people who like both = ", end="")
print(x)

print(len(x))  # n(P∩Q) --> len(P & Q)
print()

ans = p.union(q)  # (P ∪ Q)
print("id of total people in club = ", end="")
print(ans)
print(len(ans))   # n(P∪Q) total person  ---> len(P | Q)
print()

################################################


#Q1.  total people in club
#  | ---> union
p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}  # chess
q = {1, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20}  # carom

print("Q1.  number total people in club =", len(p | q))
print("Q1.  names of total people in club =", p | q)


################################################

Q2. who like to play chess only

p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}  # chess
q = {1, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20}  # carom

# number of  who like to play chess only  ---> n(p) - n(P ∩ Q) ---> len(p) - len(p & q)
# &  ---> intersection
print("number of  who like to play chess only  ---> n(p) - n(P ∩ Q) =", len(p) - len(p & q))
print("names of  who like to play chess only  ---> p - (P ∩ Q) =", p - (p & q))

################################################

Q3. who like to play carom only


p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} # chess
q = {1, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20}  # carom

# number of  who like to play carom only  ---> n(p) - n(P ∩ Q) ---> len(p) - len(p & q)
# &  ---> intersection
print("number of  who like to play carom only  ---> n(q) - n(P ∩ Q) =", len(q) - len(p & q))
print("names of  who like to play carom only  ---> q - (P ∩ Q) =", q - (p & q))

################################################

# if you do not want to change group data, you can use frozenset.
p = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11})  # chess
q = frozenset({1, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20})  # carom

# p.update([21, 22, 23])
# number of  who like to play chess only  ---> n(p) - n(P ∩ Q) ---> len(p) - len(p & q)
# &  ---> intersection
print("number of  who like to play chess only  ---> n(p) - n(P ∩ Q) =", len(p) - len(p & q))
print("names of  who like to play chess only  ---> p - (P ∩ Q) =", p - (p & q))

################################################################################################

practice.13   --->   square root / ํF to ํC

import math
from tkinter import*


root = Tk()
w= IntVar(root)
w2= StringVar(root)


def cal():
    x = w.get()
    ans = math.sqrt(x)  #  ํF to ํC formula
    w2.set(ans)
    l.config(text=f"Square root of {x}  = ")


f = Frame(root, borderwidth=40)
f.pack()
Label(f, text="Enter your number : ").pack(side=LEFT)
Entry(f, textvariable=w).pack(side=LEFT)

Button(root, text="Calculate", command=cal).pack()

f2 = Frame(root, borderwidth=40)
f2.pack()
l = Label(f2, text="Square root  =  ")
l.pack(side=LEFT)
Entry(f2, textvariable=w2).pack(side=LEFT)

root.mainloop()

################################################################################################

practice.14   --->   effect, result

# effect
def x(a, b):
    print(a + b)


l = lambda a, b: print(a + b)

x(1, 2)
l(1, 2)

################################################

# side effect
x = {1, 2, 3, 4, 5}
y = {1, 2, 3}

x.difference_update(y)

print(x)

################################################

# result
def x(a, b): # 0001
    return a + b

l = lambda a, b: a + b # 0002

ans = x(1, 2) # 0005
ans2 = l(1, 2) #

print(1, "apple", file=open("a.txt", "w"))

################################################

# effect and result   ---> dict.pop()

################################################################################################
"""
