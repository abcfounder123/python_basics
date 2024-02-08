"""
# data collection, sequence data type, element, range, index, slicing

# indexing ( +, - )

# step.1 ( first element, last element , range, min, max )

# left (+) ---> if total count is 10, max index = 9  --->  max_index = total_count - 1  ---> last element   ---> x[len(x) - 1]
# right(-) ---> if total count is 10, max index = 10  --->  max_index = total_count     ---> first element  ---> x[-len(x)]

print(x[0]) # first element
print(x[len(x) - 1]) # last element

print(x[-len(x)]) # first element
print(x[-1]) # last element

#  a,  b,  c,  d,  e,  f,  g
# -7, -6, -5, -4, -3, -2, -1,
#  0,  1,  2,  3,  4,  5,  6

# positive index range ---> 0  ---  total - 1
# negative index range ---> 1  ---  total

min_index = -len(x)
max_index = len(x) - 1
print(min_index)
print(max_index)

################################################

# step.2 ( middle element )

x = "abcdefg"
t = len(x)
print(x[t // 2]) # middle element ( total_count = odd number )

x = "abcdefgh"
t = len(x)
# total_count = even number
print(x[t//2]) # middle element ( right )
print(x[t//2 - 1]) # middle element ( left )

################################################

# step.3  ( first 3, last 3 )
# total - easy index

t = len(x)
print(t - 3)  # positive index of last 3
print(x[t - 3])  # last 3


print(-3)  # negative index of last 3
print(x[-3])  #

print(2) # positive index of first 3
print(x[2]) # first 3

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

# left to right ---> positive step
print(x[2:7:1])  #  2,  3,  4,  5,  6
print(x[-6:-1:1])  # -6, -5, -4, -3, -2

# right to left ---> negative step
print(x[6:1:-1])  # 6, 5, 4, 3, 2
print(x[-2:-7:-1])  # -2, -3, -4, -5, -6
# total = 100


x = "abcdefgh" # -8 ---> 7
print(x[:5:]) # first five #  0, 1, 2, 3, 4
print(x[-5:]) # last five # -5, -4, -3, -2, -1


################################################

# step.2 ---> total count = even ( middle (10 elements) )

x = "11111111abcdefgh11111111"
t = 10  # total 10
half = t // 2

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

t = 7  # total 7
half = t // 2

m = len(x) // 2
s = m - half
stop = m + half + 1

middle = x[s:stop]  # middle (3 elements)
print(middle)

################################################

# step.4 ---> total count = even ( middle (10 elements) ) # equation

x = "aaaaaaaaaaabcdefghaaaaaaaaaa"

number_elements = 10

m = len(x) // 2
f = (number_elements // 2)
s = m - f
stop = m + f

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

middle = x[s:stop] # middle (8 elements) # abcdefgh
print(middle)

reverse = middle[::-1]
print(reverse)

################################################

# Right middle index
x = "aaaaaaaaaaabcdefghaaaaaaaaaa"

total = 8
half = (total // 2)

rm = len(x) // 2

s = rm + (half - 1)
stop = rm - (half + 1)

middle = x[s:stop:-1]  # middle (8 elements) # abcdefgh
print(middle)

################################################

# left middle index
x = "aaaaaaaaaaabcdefghaaaaaaaaaa"

total = 8
half = (total // 2)

lm = len(x) // 2 - 1

s = lm + half
stop = lm - half

middle = x[s:stop:-1]  # middle (8 elements) # abcdefgh
print(middle)

################################################
################################################

# Nested if

c1 = 1
c2 = 1
c3 = 0
c4 = 0
c5 = 1
# 0 0 1
if c1:
    if c2:
        if c3:
            if c4:
                if c5:
                    pass
                else:
                    pass
            else:
                if c5:
                    pass
                else:
                    pass
        else:
            if c4:
                if c5:
                    pass
                else:
                    pass
            else:
                print("motor on")
                if c5:
                    pass
                else:
                    pass


    else:
        if c3:
            if c4:
                pass
            else:
                if c5:
                    pass
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
            if c4:
                if c5:
                    pass
                else:
                    pass

    else:
        if c3:
            if c4:
                print('a')
            else:
                pass


        else:
            pass


################################################

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

################################################

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

if not c1 or not c2 or not c3:
    print("At least one is fasle.")

################################################

item_list

No   item     price    stock  exp_date  discount_price   cash back
1.   apple    1        1000   15         0.3              0
2.   note 11  200      10       _        0               10
3.

################################################

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
        "exp_date": 1,
        "stock": 12000}
}

################################################

# 1. access
order = []
order_list = ["apple", "banana", "beer"]
for k in item_list:
    if item_list[k]["item"] in order_list:
        order.append(item_list[k])

print(order)

################################################

# 2. change value
#item_list[1]["price"] = 0.7
for i in item_list:
    if item_list[i]["exp_date"] < 7:
        item_list[i]["price"] *= 0.5

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

################################################

import math
from tkinter import*


root = Tk()
w= IntVar(root)
w2= StringVar(root)


def cal():
    x = w.get()
    ans = math.sqrt(x)
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

################################################

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
"""
