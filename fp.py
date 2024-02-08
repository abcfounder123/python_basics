
"""

1. introduction
2. Objects, variables, and functions as objects.
3. Immutable objects.
4. Recursion.
5. Closures.
6. Iterators.
7. Transforming and reducing iterables.
8. Comprehensions.
9. Generators.
10. Partial application and currying.
11. Functors and monads.
12. itertools, functools and other useful libraries.

Introduction
1.1 Programming paradigms
1.2 What is functional programming?
1.3 Characteristics of functional programming
1.4 Advantages of functional programming
1.5 Disadvantages of functional programming

2 Functions as objects
2.1 Objects and variables in Python
2.2 Storing functions
2.3 Aliases
2.3.1 Redefining a function
2.4 Functions as parameters
2.4.1 The sorted function
2.5 Lambda functions
2.6 Functions as return values (partial)
2.7 Function versions of standard operators
2.8 Summary – sources of function objects

3 Mutability
3.1 Mutability in Python
3.2 Numbers are immutable
3.3 The problem with mutable objects
3.3.1 Defensive copying
3.4 Immutability is the answer
3.5 Changing immutable objects
3.5.1 Using slices
3.5.2 Using list comprehensions
3.5.3 Using a loop
3.5.4 Converting the data to a list
3.6 The problem with immutable objects
3.7 Immutability is shallow
3.8 Summary


4.1 Factorials
4.2 Recursion limits
4.3 Tail recursion
4.4 Inefficient recursion – Fibonacci numbers
4.5 Memoization
4.5.1 functools lru_cache
4.6 Flattening lists
4.6.1 A less recursive solution
4.7 Summary

"""

"""
1.1 Programming paradigms
1. Imperative paradigm ( structure, procedural, oop )

students = pd.read_excel("students.xlsh")
fail = []
for student in students:
    if int(student["mark"]) < 40:
        fail.append(student)
        

2. Declarative paradigm ( SQL )
select all from students where marks < 40

#################################################

1. Procedural programming ( if, loops, fun )
2. Object oriented programming (OOP) 
3. Functional programming (FP) 

paradigm

1.2 What is functional programming?

x = 0
x = int(0)
function zero

--> f
--> calculate C
--> C

#################################################

1.3 Characteristics of functional programming

1. FP avoids side effects. ( set.difference() ) ( difference_update )
( FP prefers pure functions. )


s = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}

s.difference_update(s2)

print(s)
print(s2)

မူရင်းတန်ဖိုးကို သွားပြင်တာမျိုးဆိုရင် pure မဟုတ်
မူရင်း data ကို မထိခိုက်တာမျိုး
# only return , not effect

s1 = {1, 2, 3, 4}
s2 = {1, 2, 5, 6}
a = s1.difference(s2)

s1 = {1, 2, 3, 4}
s2 = {1, 2, 5, 6}
s1.difference_update(s2)
print(s1)
print(s2)

#################################################

2. Functions are first class objects. 
a function is 
> an object that can be stored in a variable
> passed as an argument to a function
> returned as the result of a function.

#################################################

x = print  #  a function is an object that can be stored in a variable
x(1, 2, "apple", sep=" ----> " )
print(1)

#################################################

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def adpator(f, f2, *args):
    return f(*args), f2(*args)

ans = adpator(mul, add, 4, 2) # a function is passed as an argument to a function
print(ans)

#################################################

def add(x, y):
    return x + y

x = add

print(x(1, 2))
print(add(1, 2))

#################################################

# 0001 ---> first fun ( f )

# 0002 ---> second fun ( add, y )

def f():
    def add(x, y):
        return x + y
    return add  #  a function is returned as the result of a function.

y = f() # 0002


print(y(1, 2))

print(f()(1, 2))

#################################################

3. FP prefers immutable objects. 
function တွေဟာ pure ဖြစ်ဖို့ immutable objects ပဲ သုံးမှအဆင်ပြေနိုင်

#################################################

4. FP prefers iterators over lists. 
တစ်ကြိမ်မှ တစ်ခုသာဖတ်
An iterator is an object that provided access to a collection of data. 
An iterator can only read data one element at a time, it has no ability to change the data. 

#################################################

5. FP favours lazy evaluation. 
လိုမှတွက်
memory သက်သာ / မြန်မြန်ဆန်ဆန် output ထွက်
An iterator will often choose to calculate new values only as they are needed – this is called lazy evaluation.
It often reduces the amount of memory used and allows the program to start creating output with less initial delay.

#################################################

6. FP avoids loops and if statements.

( map )
( filter )

#################################################

# loop   --->  map

def squar(n):
    return n ** 2

l = [2,  3, 4, 5, 6, 7, 8, 9, 10]
s = []
for i in l:
    a = squar(i)
    s.append(a)

print(s)

sq = map(squar, l)

print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))

#################################################

# loop, if   --->  filter
def is_even(n):
    #print(f"is_even({n})")
    return n % 2 == 0

l = [1, 2,  3, 4, 5, 6, 7, 8, 9, 10]

a = []
for i in l:
    if is_even(i):
        a.append(i)

print(a)
#print(a[0])


e = filter(is_even, l)

print(next(e))
print(next(e))

#################################################

# loop ,  if   ---> map, filter

def squar(n):
    print(f"sq({n})")
    return n ** 2

def is_even(n):
    print(f"is_even({n})")
    return n % 2 == 0

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ans = []
for i in l:
    if is_even(i):
        ans.append(squar(i))

print(ans)

f = filter(is_even, l)

ans2 = map(squar, f)

print(next(ans2))

#################################################

ans3 = map(squar, filter(is_even, l))
print(next(ans3))

#################################################

7. FP often uses recursion to avoid loops. 
Recursion is a useful alternative to looping for certain algorithms.

#################################################

8. FP uses higher order functions to define new functions. 

procedural programming မှာ function တွေဟာ အသေဖြစ်

In functional programming we tend to use higher order functions 
that modify or combine existing functions to create new functions.
fp မှာ အရှင်
higher order function 
ရှိပြီးသား function ကို ပြင်တာမျိုး ပေါင်းစပ်တာမျိုးလုပ်ပြီး function အသစ်ဖန်တီးတာ

#################################################

1.4 Advantages of functional programming

1. FP often creates less code.
ပိုမြင့်တဲ့အတွက် တစ်ကြောင်းချင်းစီက အကျိုးသက်ရောက်မှုဖြစ်စေ လို့ နည်းနည်းပဲရေးရန်လိုအပ်။

#################################################

2. Intent of the code is clearer. 
loop ပတ်တာ 
if else ဆုံးဖြတ်တာ မပါလို့ ပိုပြီး မျက်စိရှင်း

#################################################

3. There are often fewer bugs. 
Using standard functions that are well tested, 
instead of ad hoc loops that might contain bugs is generally more reliable.
ad hoc = for this ( specific function + loop )
# ဆယ်ကြိမ်အတိအကျလုပ်ပါ။
for i in range(10):
    print() 

#################################################

4. Code is potentially စွမ်းရည် mathematically provable. 
မူလ function တွေမှန်ရင် higher order function နဲ့ ပေါင်းစပ်ရင်လည်း မှန်နေမည်လို့ သက်သေပြနိုင်။

#################################################

5. Multiprocessing can be applied easily. 
pure function ဖြစ်လို့ အလုပ်များစွာပြိုင်တူလုပ်နိုင်

################################################

1.5 Disadvantages of functional programming

1. Not all functions can be pure. 
pp , fp ရောရေးမှ ရနိုင်တာမျိုးဖြစ်နိုင်
( impure function တွေနေရာမှာ oop နဲ့ အစားထိုးနိုင် )

2. FP has a learning curve. 
လေ့လာရခက်ခဲ

3. FP can be inefficient. 
တစ်ချို့အပိုင်းတွေမှာအားနည်း။
ဥပမာ။  ။ python မှာ recursion ကို အခါတစ်ထောင်ထပ်ပိုလုပ်ခွင့်မပြုတာမျိုးပေါ့။

################################################

2. Objects, variables, and functions as objects.

2.1 Objects and variables in Python

x = "apple" # 0001
y = "banana" # 0002

"apple" and "banana" are object in computer memory.
x and y are pointer of their locations.

#################################################

x = y # 0002

The previous 'apple' string is still in memory, but you can no longer access it in any way. 

ပြန်မသုံးတော့ရင် ဖျက်ပစ်မည်။
garbage collection သင်ခန်းစာလုပ်ရန်

Python will eventually free up the memory it occupies, so it can be used for something else.

#################################################

x = int(1) # 36
y = int(2) # 68

print(f"x = {x}   --->   ", end="")
print(id(x))
print(f"y = {y}   --->   ", end="")
print(id(y))

y = x # 36
print(f"y = {y}   --->   ", end="")
print(id(y))

x = 2 # 68
print(f"x = {x}   --->   ", end="")
print(id(x))

y += 1 # 68
print(f"y = {y}   --->   ", end="")
print(id(y))

x -= 1
print(f"x = {x}   --->   ", end="")
print(id(x))

y -= 1
print(f"y = {y}   --->   ", end="")
print(id(y))


def x(x):
    return x + 1
    
def y(x):
    return x + 2

x = lambda x: x + 1 # 40
y = lambda x: x + 2 # 80

a = x
a = x(10)

print(f"x = {x}   --->   ")
print(id(x))

print(f"y = {y}   --->   ")
print(id(x))
y = x # 40
print(f"y = {y}   --->   ")


x = 2 # 68
print(f"x = {x}   --->   ", end="")
print(id(x))


#################################################

x = 1   --->   533320665392
y = 2   --->   533320665424
y = 1   --->   533320665392
x = 2   --->   533320665424
y = 2   --->   533320665424
x = 1   --->   533320665392
y = 1   --->   533320665392

#################################################

class int:
    def __add__(self, other):
1 + 1

#################################################

2.2 Storing functions

x = 1
add_one = fun obj
add_one = lambda p1:p1 + 1

def add_one(p1): # 40
    return p1 + 1 #


x = int(1) # 1 ---> b8


def add_one(p1): # 40
    return p1 + 1 # 2 --> d8


y = add_one(1) # 2 --> d8

print(f"x = {x}   --->   ", end="")
print(hex(id(x)))

print(f"y = {y}   --->   ", end="")
print(hex(id(y)))

print(f"add_one = {add_one}   --->   ", end="")
print(hex(id(add_one)))

print(type(x))
print(type(y))
print(type(add_one))

x = add_one

print(f"x = {x}   --->   ", end="")
print(hex(id(x)))

#################################################

x = 1   --->   514389784880
y = 2   --->   514389784912
add_one = <function add_one at 0x773f76b310>   --->   0x773f76b310
<class 'int'>
<class 'int'>
<class 'function'>

#################################################

1 , 2 and function are objects in our computer memory.

x, y and add_one are pointers of their locations.

They also known as variables, label and identifiers.

#################################################

2. 3. Aliases

Aliasing is when two different variables reference the same object in Python.

x = (10, 20, 30) # 0001
y = x # 0001
print(x[0]) # 10
print(y[0]) # 10
print(id(x))
print(id(y))

same data with two names x and y.

When we set y  = x, 
we are actually copying the reference into the variable y. 
We don’t create a copy of the actual tuple itself. 

There is only one tuple, but both y and x point to it, 
so we call then aliases – different names for the same data.

When we then print x[0] and y[0], they
both refer to element index 0 in the original tuple.

# add_one and ao point same fun object
def add_one(p1):
    return p1 + 1

ao = add_one

y = ao(1)
print(y)

# pr and print point same fun object
pr = print
pr('This is an alias')

#####################

2. 3. 1. Redefining a function ( မလုပ်ရ )

Since functions are essentially variables that happen to hold function objects, 
you can reassign them at any time:

a = 1
a = 2

def a():
    print(1)

def a():
    print(2)
    
    
############

# direct use

# logical error ဖြစ်ဖို့ ဦးတည်

def a(): # f1
    print(1)
    
def b(): # # f2
    a()

b() # 1

def a(): # # f3
    print(2)

b() # 2

a = 1
b() # 3

#####################

2. 4.Functions as parameters ( indirect use )

def inch_cm(x):
    return x * 2.54

def convert(x):
    y = inch_cm(x)
    print(x, '=>', y)

convert(3) # 3 => 7.62

#inch_cm = 3
convert(4)


###########

def cm_inch(x):
    return x / 2.54

def convert(x):
    y = cm_inch(x)
    print(x, '=>', y)

convert(7.62)


###########

# function as parameter


def inch_cm(x):
    return x * 2.54
    
def cm_inch(x):
    return x / 2.54

def convert(f, x):
    y = f(x)
    print(x, '=>', y)


convert(inch_cm, 3)
convert(cm_inch, 7.62)

ic = inch_cm
inch_cm = 1

convert(ic, 3)

###########

# C° to F°

def c_f(x):
    return x * 1.8 + 32
    
def f_c(x):
    return ( x - 32 ) / 1.8
    
def convert(f, x):
    y = f(x)
    print(x, '=>', y)

convert(c_f, 100)
convert(f_c, 212)        

#####################

#####################

2.4.1 The sorted function ( example of fun as parameter )

# sorts the numbers in increasing order
p = [3, 7, 2, 6, 1]
q = sorted(p)
print(q) # [1, 2, 3, 6, 7]


# sorts the alphabets in increasing order
p = ['red', 'green', 'blue', 'yellow', 'cyan', 'apple', "Banana", "Apple", "banana", "Orange"]
q = sorted(p)
print(q) # ['blue', 'cyan', 'green', 'red', 'yellow']

#The key parameter accepts a function object as a value. 
#The function is applied to each element is the list,
# and the list is sorted based on the return value.

# sorts the words with their length
p = ['red', 'green', 'blue', 'yellow', 'cyan']
q = sorted(p, key=len)
print(q) # ['red', 'blue', 'cyan', 'green', 'yellow']


# sorts by area ( width * height)
def area(x):
    return x[0] * x[1]
    
area = lambda x: x[0] * x[1]
    
p = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)]
q = sorted(p, key=area)

print(q) # [(2, 2), (1, 7), (4, 2), (3, 3), (5, 2)]

################################################

2.5 Lambda functions ( lambda fun as parameter )

p = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)]
q = sorted(p, key=lambda x: x[0] * x[1])
print(q)

#This code creates a temporary, anonymous function object and passes it into the sorted function. 
#The sorted function uses it to perform the sort. 

#- - - >   And then it’s gone, just like any other temporary object.

################################################

lambda exercises

# lambda is the same function obj like other function

#####################

# result function
area = lambda x: x[0] * x[1]

def area(x):
    return x[0] * x[1]

#####################

# fun with no parameter
def f():
     return 1
     
f = lambda : 1 # No arguments

#####################

# effect fun
l = lambda x: print(f"l Area of {x} = {x[0] * x[1]}")

def area(x):
    print(f"F Area of {x} = {x[0] * x[1]}")

l((50, 100))
area((50, 100))

#####################

# fun with parameter
def f(x, y):
    return x + y

lambda x, y: x + y

#####################

# fun with special parameters
def f1(a, b, c, d, /):
    return a + b + c + d

f2 = lambda a, b, c, d, /: a + b + c + d

f1(1, 2, 3, 4)

################################################

1.  Lambdas can only contain a single Python expression. 
If your function cannot be expressed in one line, you can’t use a lambda.

2. Generally, it is best to use them only for short and simple code, 
where the behaviour of the function is obvious  သိသာ ထင်ရှား by looking at it. 
ကြည့်ရုံနဲ့နားလည်နိုင်မယ့် လုပ်ဆောင်ချက်ဆိုရင် lambda သုံး

If the behaviour is complicated ရှုတ်ထွေး, 
it is usually best to define a normal function so you can give it a meaningful name 
and add comments.
ရှုတ်ထွေးနေရင် ပုံမှန် function ဖန်တီးပြီး သင့်တော်မယ့်အမည်နဲ့ ရှင်းလင်းချက်ရေးရမည်။

3. Since a lambda expression will usually be used as part of a longer line of code, 
make sure that overall the code is still readable.
If a function call uses several lambda expressions, 
it might be difficult to see what is going on.
function တွေထဲ lambda expression အများကြီး သုံးထားရင် ရှုတ်ထွေးသွားပြီးဖတ်ရခက်နိုင်။

4. If the same function is used in several places, 
it is usually better to define a normal function, rather than repeating the lambda.
ထပ်တလဲလဲ သုံးနေရမယ်ဆိုရင်လည်း ပုံမှန် function သာသုံးပါ။

################################################

2.6 Functions as return values

################################################

2.7 Function versions of standard operators
# can be use as the key argument for the sorted function.

from operator import add

def myadd(n1, n2):
    return n1 + n2

x = 1
y = 2
print(x + y) # 1. standard operators
print(x.__add__(y)) # 2. OOP
print(myadd(x, y)) # 3. custom function
print(add(x, y)) # 4. external function

################################################

# def, lambda အစား ရှိပြီးသား function  ‌ေတွသံုးနိုင်
import operator
x = operator.add(a, b) # Equivalent to x = a + b
x = operator.truediv(a, b) # Equivalent to x = a / b
x = operator.floordiv(a, b) # Equivalent to x = a // b

operator.lt(a, b) # a < b
operator.eq(a, b) # a == b
operator.not(a) # not a
operator.neg(a) # -a

################################################

from operator import getitem, setitem, delitem, itemgetter

s = ["APPLE", 2, 3]

i = 0
print(s[i])
print(getitem(s, i))

x = "apple"
# s[0] = x
setitem(s, i, x)  
print(s)

# del s[i]
delitem(s, i) 
print(s)

################################################

def f1(x):
    return x[0]

f2 = lambda x: x[0]

f3 = itemgetter(0)

def myitemgetter(i):
    def f(x):
        return x[i]
    return f

f4 = myitemgetter(0)

print(f1(s))
print(f2(s))
print(f3(s))
print(f4(s))

################################################

def myitemgetter2(i):
    return lambda x: x[i]

f4 = myitemgetter2(0)
print(f4(s))

print(s[0])
print(myitemgetter2(0)(s))

################################################

from operator import itemgetter

def myitemgetter2(i):
    return lambda x: x[i]

# sorts the words with their index
p = ['red', 'green', 'blue', 'yellowb', 'cyana']

q = sorted(p, key=itemgetter(-1)) # lambda x: x[-1]
print(q) # ['cyana', 'yellowb', 'red', 'blue', 'green']

q = sorted(p, key=myitemgetter2(-1)) # lambda x: x[-1]
print(q) # ['cyana', 'yellowb', 'red', 'blue', 'green']


################################################

# add(3, n)

def add3(n):
    return n + 3

def add4(n):
    return n + 4

def add5(n):
    return n + 5

#print(add3(20))

def all1(n2):
    def add(n):
        return n + n2
    return add

def all(n2):
    return lambda n: n + n2

ad3 = all(n2=3) # closure --> close # lambda n: n + n2  <--- n2 = 3
ad4 = all(4)
ad5 = all(5)
print(all(5)(10))
print(all1(1)(2))

################################################

from functools import partial
from operator import add, mul, sub

# add(3, 2)
f = partial(add, 3) #  f = lambda x: 3 + x # add(3)
x = f(10) # Equivalent to x = 3 + 7
print(x)

f = partial(mul, 3) #  f = lambda x: 3 * x
x = f(10) # Equivalent to x = 3 + 7
print(x)

f = partial(sub, 3) #  f = lambda x: 3 - x
x = f(10) # Equivalent to x = 3 + 7
print(x)

def mpartial(f, n):
    def c(x): # f --> add , n = 3
        return f(n, x) # add(3, 10)
    return c

f = mpartial(add, 3) #  f = lambda x: 3 + x
print(f(10))

f = mpartial(mul, 3) #  f = lambda x: 3 * x #
x = f(10) # Equivalent to  3 * 10 # mul(3, 10)
print(x)

f = mpartial(sub, 3) #  f = lambda x: 3 - x
x = f(10) # Equivalent to 3 - 10 # sub(3, 10)
print(x)

################################################

def mpartial(f, n):
    return lambda x: f(n, x)

################################################

import operator

k = [2, 4, 6, 8]
# get index 2
f = operator.itemgetter(2)
x = f(k) # x = 6


f_1 = operator.itemgetter(0)
x = f_1(k) # x = 6
print(x)

#itemgetter(2) returns a function that will get element number 2 from a list. 

################################################

# functional programming 
# 2.6 Functions as return values

# example usage in partial
# 1. normal
# 2. lambda
# 3. partial
# 4. our partial
# 5. test

def add(x, y):
    return x + y

p = add(1)# partial

def add(y):
    return 1 + y

p(2)

z = ax**2 + 2ab - y**2 + c

def eq(a, b, c, x, y):
    return a*x**2 + 2*a*b - y**2 + c
    
#####################

# 1. normal 
def add(x):
    def f(y):
        return x + y
    return f


#def add_5(x):
#    return x + 5
add_5 = add(5) #  ( memory address of fun ) ( local x = 5 )

print(add_5(1))

#def add_10(x):
#    return x + 10
add_10 = add(10) #  ( memory address of fun ) ( local x = 10 )
print(add_10(1))

print(add(5)(1))
print(add(10)(1))


#####################

# 2. lambda

def add(x):
    return lambda y: x + y

#def add_5(y):
#    return 5 + y
add_5 = add(5) # lambda y: 5 + y
print(add_5(1))

add_10 = add(10) # lambda y: 10 + y
print(add_10(1))

print(add(5)(1))
print(add(10)(1))

#####################

# add 

print(1 + 2)

import operator
print(operator.add(1, 2))

def add(n1, n2):
    return n1 + n2

print(add(1, 2))

#####################

# 3. partial
from functools import partial
import operator

# lambda y: 5 + y
# lambda y: operator.add(5, y)
add_5p = partial(operator.add, 5)
print(add_5p(1))

# lambda y: 10 + y
# lambda y: operator.add(10, y))
add_10p = partial(operator.add, 10)
print(add_10p(1))

def add(n1, n2):
    return n1 + n2

add_5p = partial(add, 5)
print(add_5p(1))

add_10p = partial(add, 10)
print(add_10p(1))

#####################

import operator

# 4. our partial
def p(f, n):
    return lambda x: f(x, n)

def p2(f, n):
    return lambda x: f(n, x)


def add(n1, n2):
    return n1 / n2

add_10op = p(add, 100) # n1 / 100
print("t", add_10op(4))

add_10op = p2(add, 100) # 100 /n2
print("t", add_10op(4))


# lambda x: x + 5
# lambda x: operator.add(x, 5)      
add_5op = p(operator.add, 5)
print(add_5op(1)) #  add(1, 5)

# lambda x: x + 10
# lambda x: operator.add(x, 10)
add_10op = p(operator.add, 10) 
print(add_10op(1))


# 5. test our p
# lambda x: x / 5
# lambda x: operator.truediv(x, 5)
div_5 = p(operator.truediv, 5)
print(div_5(100)) # 100 / 5 

# lambda x: x * 5
# lambda x: operator.mul(x, 5)
mul_5 = p(operator.mul, 5)
print(mul_5(20)) # 20 * 5


################################################
################################################


import operator

def p(f, n):
    return lambda x: f(x, n)

# lambda x: x > 18
# lambda x: operator.gt(x, 18)
drinking_permit = p(operator.gt, 18)

pn = lambda gender: 'he' if gender == 'M' else 'she'

name = "Mg Mg" # input("Name : ")
age = 20 # int(input("Age : "))
gender = "M" # input("Gender ( female or male ) F/M : ")
if drinking_permit(age):
    print(f"{name} can drink beer because {pn(gender)} is {age} years old. ")
else:
    print(f"{name} can not drink beer because {pn(gender)} is {age} years old. ")


#####################

name = "Ma Ma" # input("Name : ")
age = 18 # int(input("Age : "))
gender = "F" # input("Gender ( female or male ) F/M : ")

if drinking_permit(age):
    print(f"{name} can drink beer because {pn(gender)} is {age} years old. ")
else:
    print(f"{name} can not drink beer because {pn(gender)} is {age} years old. ")

#####################

# function as return value example

# alcohol permit function by country
import operator

# 4. our partial
def p(f, n):
    return lambda x: f(x, n)

pn = lambda gender: 'he' if gender == 'M' else 'she'

country_limit = {"Japan" : 20, "UK" : 18, "Germany" : 16}

name = input("Name : ")
age = int(input("Age : "))
gender = input("Gender ( female or male ) F/M : ")
country = input("Enter your country : ")

'''
# procedural way
if country == "UK":
    if age > country_limit[country]:
        print(f"{name} can drink beer because {pn(gender)} is {age} years old. ")
    else:
        print(f"{name} can not drink beer because {pn(gender)} is {age} years old. ")

elif country == "Japan":
    if age > country_limit[country]:
        print(f"{name} can drink beer because {pn(gender)} is {age} years old. ")
    else:
        print(f"{name} can not drink beer because {pn(gender)} is {age} years old. ")

elif country == "Germany":
    if age > country_limit[country]:
        print(f"{name} can drink beer because {pn(gender)} is {age} years old. ")
    else:
        print(f"{name} can not drink beer because {pn(gender)} is {age} years old. ")
'''


# partial style
# possible function result

# if Japan , lambda x: x > 20
# if Japan, lambda x: operator.gt(x, 20)

# if UK , lambda x: x > 18
# if UK, lambda x: operator.gt(x, 18)

# if Germany , lambda x: x > 16
# if Germany, lambda x: operator.gt(x, 16)

drinking_permit = p(operator.gt, country_limit[country])

if drinking_permit(age):
    print(f"{name} can drink beer because {pn(gender)} is {age} years old. ({country})")
else:
    print(f"{name} can not drink beer because {pn(gender)} is {age} years old. ({country})")


#####################

2.8 Summary – sources of function objects

1. Built in functions, such as len, min, abs etc. 
note --->
len(s) calls the len function to find the length of s, 
but len on its own gives the actual function object.

2. module, package ( built-in, external )
The operator module contains function versions of most Python operators, 
for example add is the function equivalent of +.

3. Lambda expressions can be used to create simple, unnamed functions.

4. create new functions by the standard way. ( using def )

5. Composition can be used to create a new function by combining two or more existing 
functions that call each other, for example f(g(x)).

6. Partial application can be used to create a new function based on an existing function 
with some of its parameters already applied.

7. Currying is an alternative way to achieve similar results to partial application.
# multiple argument into single argument function.

8. Closures can be used as general function factories if no other method provides quite 
what you need.

9. Objects that implement _call_ can be used as function objects.
# list ( has not call )
# custom class, custom obj 


class A:
    def __init__(self, name):
        self.name = name
        
    def __call__(self):
        print("calling", self)
        
    def __repr__(self):
        return self.name
    


a = A("Mg Mg")        
a()

b = A("b")
b()

l = [a, b]
print(l)


#####################


# object vs variable / identifier
# int object
# function object 

f = 6 # f ( memory address of 6 int object )
a = f # a ( memory address of 6 int object )
# a = 11
print(f)
print(a)
print(hex(id(a)))
print(hex(id(f)))

print("- " * 30)

###########

def add(n):
    f = 1 + n # f ( memory address of 6 int object )
    print(f)
    print(hex(id(f)))
    return f

a = add(5) # a ( memory address of 6 int object )
print(a)
print(hex(id(a)))
print("- " * 30)


###########

def add(n):
    def f():
        return 1 + n
    
    #print(f())
    #print(f)
    return f

a = add(5) # a ( memory address of fun object) ( local n = 5 )
print(a())
print(a)

print("- " * 30)


###########

a = add(10) # a ( memory address of fun ) ( local n = 10 )
print(a())
print(a)

print("- " * 30)
###########


b = add(5) # a ( memory address of fun object) ( local n = 5 )
print(b())
print(b)

print("- " * 30)


c = add(10) # a ( memory address of fun ) ( local n = 10 )
print(c())
print(c)

print("- " * 30)
###########

"""

'''
6
6
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
6
6
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
6
6
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
11
11
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Process finished with exit code 0
'''
