"""

More Control Flow Tools

4.1. if Statements

4.2. for Statements


users = {"Mg Mg": "active", "Ma Ma" : "inactive", "Hla Hla" : "active"}

# change dict size
for user, status in users.items():
    if status == "inactive":
        del users[user]

print(users)
#RuntimeError: dictionary changed size during iteration

###

users = {"Mg Mg": "active", "Ma Ma" : "inactive", "Hla Hla" : "active"}
x = users.copy()
# iterate copy value to change dict size
for user, status in x.items():
    if status == "inactive":
        del users[user]
print(users)

###

users = {"Mg Mg": "active", "Ma Ma" : "inactive", "Hla Hla" : "active"}

# iterate copy value to change dict size
# to avoid memory lose
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

###

users = {"Mg Mg": "active", "Ma Ma" : "inactive", "Hla Hla" : "active"}

# Create a new collection
active_users = list()
inactive_users = list()

for user, status in users.items():
    if status == "active":
        active_users.append(user)
        #active_users.append((user, status))
        #active_users[user] = status
    else:
        inactive_users.append(user)

print(users)
print(active_users)
print(inactive_users)

#######

users = (
    
{"user name" : "Mg Mg",
"password" : "1234561",
"age" : 20,
"email address" : "mgmg123@gmail.com",
"status" : "active",
},

{"user name" : "Ma Ma",
"password" : "1234562",
"age" : 25,
"email address" : "mama456@gmail.com",
"status" : "inactive",
},

{"user name" : "Hla Hla",
"password" : "1234563",
"age" : 30,
"email address" : "hlahla789@gmail.com",
"status" : "active",
}
)

# (dict, dict, dict)

# Create a new collection

active_users = []

for user in users:
    if user["status"] == "active":
        #active_users += [user]
        active_users.append(user)


print(users)
print(active_users)

#######

users = (
    
{"user name" : "Mg Mg",
"password" : "1234561",
"age" : 20,
"email address" : "mgmg123@gmail.com",
"status" : "active",
"marks" : {"myn" : 30, "eng" : 30, "math" : 90}
},

{"user name" : "Ma Ma",
"password" : "1234562",
"age" : 25,
"email address" : "mama456@gmail.com",
"status" : "inactive",
"marks" : {"myn" : 60, "eng" : 90, "math" : 70}
},

{"user name" : "Hla Hla",
"password" : "1234563",
"age" : 30,
"email address" : "hlahla789@gmail.com",
"status" : "active",
"marks" : {"myn" : 50, "eng" : 95, "math" : 80}
}

)

# (dict, dict, dict)
# ()
# 2 step

fail_users = []
pass_users = []
g_users = []
for user in users:
    f_sub = dict()
    g_sub = dict()# {"eng" : 95, "math" : 80}
    for sub, mark in user["marks"].items():
        if mark < 40:
            f_sub[sub] = mark
        else:
            if mark >= 80:
                g_sub[sub] = mark
            
    if f_sub:
        fail_users += [[user["user name"], f_sub]]
        
    else:
        #pass_users += [user["user name"]]
        pass_users.append(user["user name"])
        if g_sub:
            g_users += [[user["user name"], g_sub]]

print(users)
print(fail_users)
print(pass_users)
print(g_users)

#######

print([1, 2, 3] + [["mg mg", {"math" : 80}]])
l = [1, 2, 3]
l.append(4)
l.append(5)
print(l)

#######

#4.3. The range() Function     --->  to iterate over a sequence of numbers

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
    print(i)
    

# start , stop, step
# numbers list  --> range() with list(), tuple

even = list(range(2, 101, 2))
print(even)

# index and value --> range() with ordered list ( list, tuple, str)

l = "abcdefg"
l = ["a", "b", "c", "d", "e", "f", "g"] # 0  to  6
for i in range(len(l)):
    print(i, l[i])
    
#######

04.4. break and continue Statements, and else Clauses on Loops
break         ---> breaks out of the innermost enclosing for or while loop.

continue      ---> continues with the next iteration of the loop
loop + else   --->   executed when the loop terminates through exhaustion of the iterable (with for)
                     or when the condition becomes false (with while),
                     but not when the loop is terminated by a break statement.

# break
# join

x = [1, 4, 6, 5, 7, 9]
y = [1, "a", 2, "b", 3]

c = False

for i in x:
    if i in y:
        c = True
        break
    #print(i, "another code")

print(c)

"Return True if two sets have a null intersection."
# disjoin
x = [4, 5, "a"]
y = [1, "a", 2, "b", 3]
c = True
for i in x:
    if i in y:
        c = False
        break

print(c)


for n in range(2, 12):
    x = 2
    
    while x < n//2 + 1:
        print(n , " ---> ", x)
        if n % x == 0:
            #print(n, 'equals', x, '*', n // x)
            break
        x += 1
    else:
        # loop all items
        print(n, 'is a prime number')

#######

2 = 
3 = 2

4 = 2, 3

5 = 2, 3, 4

7 =  2 3 4 5 6  8 9 10 . . . . 

8 = 2 3 4 5 6 7

11 = 2 3 4 5  6 7 8 9 10


for n in range(2, 12):
    for x in range(2, n//2 + 1):
        print(n , " ---> ", x)
        if n % x == 0:
            #print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop all items
        print(n, 'is a prime number')


#######

for num in range(3, 10):#  3, 4, 5, ...
    if num % 2 == 0:
        print("Found an even number", num)
        continue
        
    
    print("Found an odd number", num)

###########

# 4.5. pass Statements
The pass statement does nothing.
It can be used when a statement is required syntactically but the program requires no action.

n = 4
if n % 2 == 0:
    pass

    
else:
    print(n, "is odd number")


###########

4.6. match Statements


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


error_meaning = http_error(403)
print(error_meaning)


#######

def http_error(status):
    if status == 400:
        return "Bad request"
    elif status == 401 or status == 403:
        return "Not allowed"
    elif status == 404:
        return "Not found"
    elif status == 418:
        return "I'm a teapot"
    else:
        return "Something's wrong with the internet"

error_meaning = http_error(403)
print(error_meaning)


#######

# point is an (x, y) tuple

point = (1, 1)
#point = None , " " , ()
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _: # _ is any value
        print("value error")
        #raise ValueError("Not a point")

###########

# 4.7. Defining Functions

def name(par):
    '''docstrings'''
    statements
    return value

###

# 330  <---  19

x = int(19)
y = x
print(hex(id(x)))
print(hex(id(y)))

###

# 20   <--- fun obj
def x(a, b):
    print(a + b)
    
y = x
print(x)
print(y)

###

# 30   <--- fun obj
x = lambda a, b: print(a * b)
y = x
print(x)
print(y)

###

x = 19
y = 19
print(hex(id(x)))
print(hex(id(y)))


# par, arg ( pos, kw ), default par(default vlue), docstring, return
# action, return value
# effect, result ( difference_update, difference ) ( print(), len(), input() )

#####
"""


"""
# pos
# key
# pos + key
# *args  ( pack, unpack ) (pos)
# **kwargs ( pack, unpack ) (kw)
# pos + *args
# kw + **kwargs
# pos + **
# pos + kw + **
# pos + * + kw + **
# print     ---> *  +  default par


def x(a, b, c=3, d=4):
    print(a, b, c, d)
    return a + b + c + d


total = x(1, 2)
print(total)


# kw arg
add(b=20, a=100)


s = {1, 2, 3, 4}
s2 = {1, 2}
# call
# return value
print(s.difference(s2))
print(s, s2)

# action ---> update
print(s.difference_update(s2))
print(s, s2)

# return value, action ---> remove
s = {1, 2, 3, 4}
print(s)
print(s.pop())
print(s)
help(set)


#######

def name(fp):
    '''docsting'''
    statement
    
    

The keyword def introduces a function definition. def name
It must be followed by the function name and the parenthesized list of formal parameters. (f p)

The statements that form the body of the function start at the next line, and must be indented.  ____statements

The first statement of the function body can optionally be a string literal;
this string literal is the function’s documentation string, or docstring.




# action, return value
# effect, result ( difference_update, difference ) ( print(), len(), input() )

# par, arg ( pos, kw ), default par(default vlue), docstring, return

help()

identrifier   --->   local, global, module, builtin


"""

help("a".split)
#help(print) # effect ---> Prints the values to a stream, or to sys.stdout by default.

# effect ---> print, input data from console
# result ---> return str result from input data
name = input("Name : ") 
print(name.split())



"""
s = {1, 2, 3}
#help(s.difference_update)# effect ---> Remove all elements of another set from this set.

#help(s.difference) # result --> new set


s = {1, 2, 3, 4, 5, 6}
s1 = {1, 3}
s2 = {1, 2}
ans = s.difference(s1, s2)
print(ans)
print(s)


def add(a, b):
    "It is add function."
    return a + b

# help(add)
# help(print)
# print(add.__doc__)
# print(print.__doc__)

#s = {1, 2, 3}
#help(s.isdisjoint)

def isdisjoin(a, b):
    "Return True if two iterable objects have a null intersection."
    c = True
    for i in a:
        if i in b:
            c = False
            break
    return c
    

l = [1, 2, 3, 4]
t = ("apple", "banana", "orange")
c = isdisjoin(l, t)
#print(c)

s1 = {1, 2, 3}
s2 = {4, 5, 6, 7}
c = isdisjoin(s1, s2)
print(c)


def isjoin(a, b):
    "Return True if two iterable objects have a intersection."
    c = False
    for i in a:
        if i in b:
            c = True
            break
    return c
    

l = [1, 2, 3, 4]
t = ("apple", "banana", "orange")
c = isjoin(l, t)
#print(c)

s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
c = isjoin(s1, s2)
print(c)


def add(a, b, c):
    return a + b + c

print(add(1, 2, 3))
print(add(a=1, b=2, c=2))
print(add(1, 2, c=2))


# when calling function ---> 2 (pos , key name)   <-----

# default parameter
# * ---> packing pos argv
#   ---> unpacking collection
# ** ---> packing kwargvs
#    ---> unpacking dict


def add(*n):
    total = 0
    for i in n:
        total += i
    return total


print(add(1, 2, 3, 4, 5))
print(add(1, 2))

l = [1, 1, 1, 100, 100, 200, 200, 200, 300]
total_amount = add(*l)
print(total_amount)


def add(**n):
    total = 0
    for i in n.values():
        total += i
    return total

#print(add(a=1, b=2, c=3, item1=100, item2=200))

l = {"item1": 500, "item2": 1000, "item3": 3000, "item4": 100}
total = add(**l)
print(total)


#positional argument
total = add(1, 2, 3)
#print(total)

# keyword argument
total = add(a=1, c=3, b=2)
print(total)

# default


# pos + kw
total = add(1, 2, c=3)

print(total)

print("- " * 21)
# pos + *args
def f(a, b, c, *l):
    print(a)
    print(b)
    print(c)
    print(l)


f(1, 2, 3, 4)


print("- " * 21)
# kw + **kwargs
def f(a, b, c, **l):#pack
    print(a)
    print(b)
    print(c)
    print(l)


f(d=4, e=5, a=1, g=10, b=2, c=3, name="mg mg")



print("- " * 21)
# pos + *arg, kw
def f(a, b, *l, c=0):#pack
    print(a)
    print(b)
    print(c)
    print(l)


f(1, 2, 3, 4, 5, c=100 )


print("- " * 21)
# pos + *arg, kw + **kwargs
def f(a, b, *l, c, g, **d):#pack
    print(a)
    print(b)
    print(c)
    print(g)
    print(l)
    print(d)


f(1, 2, 3, 4, 5, c=100, name="mg mg", age=20, g=20)




# Arbitrary Argument Lists
def add(*numbers): # pack
    ans = 0
    for number in numbers:
        ans += number
    return ans

total = add(1, 2, 3, 4, 5, 6,7, 8, 9, 10)
print(total)

l = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]

total = add(*l) # unpack
print(total)


# dict
def add(**kwargs):# pack
    ans = 0
    for i in kwargs.values():
        ans += i
    return ans

total = add(a=1, b=2, c=3, d=4, e=5, age=20)
print(total)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'age': 20}
total = add(**d) # unpack
print(total)




# mix   --->   pos arg, kw arg
# mix   --->   pos arg, *args
# mix   --->   pos arg, *args, kw arg, **kwargs

4.8. More on Defining Functions
4.8.1. Default Argument Values
Important warning: The default value is evaluated only once. 
This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. 
For example, the following function accumulates the arguments passed to it on subsequent calls:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) # f("user1")
print(f(2))
print(f(3))


[1]
[1, 2]
[1, 2, 3]


def f(name, d=dict(), **x):
    d[name] = x
    return d

print(f("user1", age=20, id=12345))
print(f("user2", age=20, id=123456))
print(f("user3", age=20, id=1234567))


{'user1': {'age': 20, 'id': 12345}}
{'user1': {'age': 20, 'id': 12345}, 'user2': {'age': 20, 'id': 12345}}

If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
# l = [a, b, c]
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

4.8.2. Keyword Arguments

Functions can also be called using keyword arguments of the form kwarg=value.

When a final formal parameter of the form **name is present, 
it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. 
This may be combined with a formal parameter of the form *name (described in the next subsection) 
which receives a tuple containing the positional arguments beyond the formal parameter list. 
(*name must occur before **name.)

4.8.3. Special parameters
4.8.3.1. Positional-or-Keyword Arguments   --->   /    *
4.8.3.2. Positional-Only Arguments         --->   p    /
4.8.3.3. Keyword-Only Arguments            --->   *    p
4.8.3.4. Function Examples
4.8.3.5. recap အနှစ်ချုပ်                      --->   standard
                                                  p / standard * kw


# p only
def add(a, b, c, /):
    return a + b + c


#positional argument
total = add(1, 2, 3)
print(total)
# keyword argument
#total = add(a=1, c=3, b=2)
print(total)


# kw only
def add(*, a, b, c):
    return a + b + c


#positional argument
#total = add(1, 2, 3)
print(total)

# keyword argument
total = add(a=1, c=3, b=2)
print(total)



def info(*, name, age, email, ph):
    pass

info(name="mg mg", ph="0987654", age=20, email="abc@gmail.com")


# mix / and *
def add(a, b, c, /, d, e, f, *, g, h, i):
    return a + b + c + d + e + f + g + h + i

total = add(1, 1, 1, 1, 1, f=1, g=1, h=1, i=1)
print(total)


4.8.4. Arbitrary Argument Lists 
4.8.5. Unpacking Argument Lists

def add(*numbers):
    t = 0
    for number in numbers:
        t += number
    return t

x = [1, 1, 1, 1, 1, 1, 1]

#print(add(x)) # TypeError: unsupported operand type(s) for +=: 'int' and 'list'

print(add(*x))


def add(a, b, c, d):
    return a + b + c + d

x = [1, 1, 1, 1]

#print(add(x)) # TypeError: add() missing 3 required positional arguments: 'b', 'c', and 'd'

print(add(*x))


4.8.6. Lambda Expressions
add = lambda a, b, c: a + b + c




def add(a, b, c):
    return a + b + c

x = lambda a, b, c: a + b + c

print(add(1, 2, 3))
print(x(1, 2, 3))

print(add(a=1, b=2, c=2))
print(x(a=1, b=2, c=2))

print(add(1, 2, c=2))
print(x(1, 2, c=2))


def f1(s):
    print(s.upper())


f2 = lambda s:print(s.upper())

f1("abc")
f2("abc")




def f1(s):
    return s.upper()
f1("abc")
f1 = lambda s: s.upper()
f1("abc")



4.8.7. Documentation Strings
print(my_function.__doc__)



4.8.8. Function Annotations မှတ်ချက်
annotations are stored in __annotations__
def f(x:str, y:str) -> str:
    return f"Hello {x} {y}"




import sys

def add(x, y):
   return x + y

print(add(int(sys.argv[1]), int((sys.argv[2]))))





4.9. Coding Style
1. 4 space
2. not exceed 79 characters
3. blank lines
4. comment
5. docstrings
6. space ---> operator, comma
7. UpperCamelCase ---> class name
8. lowercase_with_underscores  ---> function, method
9. self  --->   first parameter of method
10. UTF-8
11. identifier ---> ASCII




5. list
1. list as stacks
( last_in , first_out )
---> append()
---> pop()

2. list as queues  ( first_in, first_out )
---> deque from collections
---> popleft()


from collections import deque
que = []
que = deque(que)
que.append(1)
que.append(2)
que.append(3)
que.append(4)
print(que)

print(que.popleft())
print(que)

print(que.popleft())
print(que)

print(que.popleft())
print(que)


print(que.popleft())
print(que)


3. list comprehensions


l = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10]]

square = []

for r in l:
    for i in r:
        if i % 2 == 0:
            square.append(i ** 2)

print(square)

s = [i ** 2 for r in l for i in r if i % 2 == 0]
print(s)



# 6       .
# 5
# 4
# 3       .
# 2
# 1       .
# # # # # # # # # # #
0 1 2 3 4 5 6 7 8 9 10
###########################
5, 3
25, 9

5, 6
3. An Informal Introduction to Python
3.1. Using Python as a Calculator
3.1.1. Numbers
3.1.2. Strings
3.1.3. Lists

3.2. First Steps Towards Programming

4. More Control Flow Tools
4.1. if Statements
4.2. for Statements
4.3. The range() Function
4.4. break and continue Statements, and else Clauses on Loops
4.5. pass Statements
4.6. match Statements

4.7. Defining Functions

4.8. More on Defining Functions
4.8.1. Default Argument Values
4.8.2. Keyword Arguments
4.8.3. Special parameters
4.8.3.1. Positional-or-Keyword Arguments
4.8.3.2. Positional-Only Parameters
4.8.3.3. Keyword-Only Arguments
4.8.3.4. Function Examples
4.8.3.5. Recap

4.8.4. Arbitrary Argument Lists 
4.8.5. Unpacking Argument Lists 
4.8.6. Lambda Expressions
4.8.7. Documentation Strings
4.8.8. Function Annotations  def x(a:int, b:str) -> list:

4.9. Coding Style

5. Data Structures
5.1. More on Lists
5.1.1. Using Lists as Stacks
5.1.2. Using Lists as Queues
5.1.3. List Comprehensions
5.1.4. Nested List Comprehensions

5.2. The del statement
5.3. Tuples and Sequences
5.4. Sets
5.5. Dictionaries
5.6. Looping Techniques
5.7. More on Conditions
5.8. Comparing Sequences and Other Types

6. Modules
6.1. More on Modules
6.1.1. Executing modules as scripts
6.1.2. The Module Search Path
6.1.3. “Compiled” Python files

6.2. Standard Modules
6.3. The dir() Function

6.4. Packages
6.4.1. Importing * From a Package
6.4.2. Intra-package References
6.4.3. Packages in Multiple Directories

7. Input and Output
7.1. Fancier Output Formatting
7.1.1. Formatted String Literals
7.1.2. The String format() Method
7.1.3. Manual String Formatting
7.1.4. Old string formatting

7.2. Reading and Writing Files
7.2.1. Methods of File Objects
7.2.2. Saving structured data with json

8. Errors and Exceptions
8.1. Syntax Errors
8.2. Exceptions
8.3. Handling Exceptions
8.4. Raising Exceptions
8.5. Exception Chaining
8.6. User-defined Exceptions
8.7. Defining Clean-up Actions
8.8. Predefined Clean-up Actions
8.9. Raising and Handling Multiple Unrelated Exceptions
8.10. Enriching Exceptions with Notes

9. Classes
9.1. A Word About Names and Objects
9.2. Python Scopes and Namespaces
9.2.1. Scopes and Namespaces Example

9.3. A First Look at Classes
9.3.1. Class Definition Syntax
9.3.2. Class Objects
9.3.3. Instance Objects
9.3.4. Method Objects
9.3.5. Class and Instance Variables

9.4. Random Remarks

9.5. Inheritance
9.5.1. Multiple Inheritance

9.6. Private Variables
9.7. Odds and Ends
9.8. Iterators
9.9. Generators
9.10. Generator Expressions


"""


"""

5.1.4. Nested List Comprehensions

 1   2
 3   4
 5   6


 1   3   5
 2   4   6


The transpose AT of a matrix A can be obtained by reflecting the elements along its main diagonal.
Repeating the process on the transposed matrix returns the elements to their original position.

The transpose of a matrix was introduced in 1858 by the British mathematician Arthur Cayley.


m = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]]

[[1, 5, 9],
 [2, 6, 10],
 [3, 7, 11],
 [4, 8, 12]]

# step .1
#print(m[0][2])

mt = []

# step.1
row_t0 = []
for row in m:
    row_t0.append(row[0])
    print(row_t0)

mt.append(row_t0)
print(mt)

row_t0 = []
for row in m:
    row_t0.append(row[1])
    print(row_t0)

mt.append(row_t0)
print(mt)


row_t0 = []
for row in m:
    row_t0.append(row[2])
    print(row_t0)

mt.append(row_t0)
print(mt)


row_t0 = []
for row in m:
    row_t0.append(row[3])
    print(row_t0)

mt.append(row_t0)
print(mt)

####

#step.2
row_t1 = []
for row in m:
    row_t1.append(row[1])
print(row_t1)

row_t2 = []
for row in m:
    row_t2.append(row[2])
print(row_t2)

row_t3 = []
for row in m:
    row_t3.append(row[3])
print(row_t3)

mt = [row_t0,
      row_t1,
      row_t2,
      row_t3
      ]
print(mt)



m = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]]


[[1, 5, 9],
 [2, 6, 10],
 [3, 7, 11],
 [4, 8, 12]]

mt = []

# step.3
for col in range(len(m[0])):
    row_t = []
    for row in m:
        row_t.append(row[col])
    mt.append(row_t)

print(m)
print(mt)

# step.4
lc_mt = [[row[col] for row in m] for col in range(len(m[0]))]
#lc = [row[col] for col in range(len(m[0])) for row in m]

print(lc_mt)


m = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]]

def transport_matrix(m):
    mt = []
    for col in range(len(m[0])):
        row_t = []
        for row in m:
            row_t.append(row[col])
        mt.append(row_t)
    return mt

t = transport_matrix(m)
print(m)
print(t)
print(transport_matrix(t))


m = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]]

def transport_matrix(m):
    return [[row[col] for row in m] for col in range(len(m[0]))]

t = transport_matrix(m)
print(m)
print(t)
print(transport_matrix(t))






m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

mt = []
for i in range(len(m[0])):
    row_t = []
    for row in m:
        row_t.append(row[i])
    mt.append(row_t)

print(m)
print(mt)

mt = [[row[i] for row in m] for i in range(len(m[0]))]
print(mt)


def transport_matrix(m):
    '''
    :param matrix:
    :return: transport matrix

The transpose AT of a matrix A can be obtained by reflecting the elements along its main diagonal.
Repeating the process on the transposed matrix returns the elements to their original position.

The transpose of a matrix was introduced in 1858 by the British mathematician Arthur Cayley.
    '''
    mt = []
    for i in range(len(m[0])):
        row_t = []
        for row in m:
            row_t.append(row[i])
        mt.append(row_t)
    return mt

#help(transport_matrix)

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mt = transport_matrix(m)
print(mt)
print(transport_matrix(mt))



def transport_matrix(m):
    mt = [[row[i] for row in m] for i in range(len(m[0]))]
    return mt

#help(transport_matrix)

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mt = transport_matrix(m)
print(mt)
print(transport_matrix(mt))


###################################


5.3. Tuples and Sequences
5.4. Sets
5.5. Dictionaries
5.6. Looping Techniques
5.7. More on Conditions
5.8. Comparing Sequences and Other Types


sequence type     ---> list, tuple, range
list      --->   homogeneous sequence of element
tuple     --->   heterogeneous sequence of element
range     --->   sequence of number


###############################

5.3. Tuples and Sequences

1. tuple can create with mutable obj

v = ([1, 2, 3],
     [3, 2, 1])

v[0][0] = 0
print(v)


2. multiple assignment is a combination of tuple packing and sequence unpacking.

# tuple packing
t = 12345, 54321, 'hello!'
print(t)


# sequence unpacking
print(*t)
x, y, z = t
print(x, y, z)

# multiple assignment
x, y, z = 12345, 54321, 'hello!'


#################################

5.4. Sets
1. unique value
2. -, |, &, ^
3. set comprehension


a = set('abcdef')
b = set('abcijk')

print(a - b)                              # letters in a but not in b
#{'d', 'e', 'f'}

print(a | b)                              # letters in a or b or both
#abcdefijk

print(a & b)                              # letters in both a and b
#a b c

print(a ^ b)                              # letters in a or b but not both
# d e f i j k


Similarly to list comprehensions, set comprehensions are also supported.

a = set()
for i in 'abracadabra':
    if i not in 'abc':
        a.add(i)
print(a)

a = {i for i in 'abracadabra' if i not in 'abc'}
print(a)


#{'r', 'd'}

################################

5.5. Dictionaries
1. dict to list ---> key list, value list  --->  list(), sorted()
2. dict()       ---> identifier/ variable rule
3. list to dict
4. dict comprehension

d = { 
         222 : "banana",
         111 : "apple",
}

# key to list
print(list(d))
print(sorted(d))

# values to list
print(list(d.values()))
print(sorted(d.values()))


# dict()
#d = dict(222=mama, 111=MgMg)  # identifier rule
d = dict(mama=222, MgMg=111)
print(d)

# list to dict
l = [[222, "ma ma"], [111, "Mg Mg"]]
d = dict(l)
print(d)


d = dict()
for i in range(1, 101):
    d[i] = i ** 2
print(d)

# d comprehension
d = {i: i ** 2 for i in range(1, 101)}
print(d)



##############################

5.6. Looping Techniques

#enumerate([]) ---> position index and corresponding value
# index, value
# can choose index value or another value

# zip([], [])  ---> pair values of two or more sequences
# two or more values

# reversed   ---> sequence in reverse
# sorted     ---> sequence in sorted order


d = {"name": "Mg Mg", "age": 20}
s = {1, "apple", 2} # non sequence
l = ["Mg Mg", "Ma Ma", "Hla Hla"]


for i, v in enumerate(l):
    print(i, v)


l1 = [1, 2]
l2 = ["name", "age"]
l3 = ["Mg Mg", 18]

for a, b, c in zip(l1, l2, l3):
    print(a, b, c)
    



l = [6, 5, 4, 3, 2, 1]
for i in reversed(l):
    print(i)



################################

5.7. More on Conditions
x, y, z = "", "apple", 2
print(x or y or z) # first true argument
print(x and y and z)# lastest argument

5.8. Comparing Sequences and Other Types


('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', 
 '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', 
 '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha256', '_sha3', 
 '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', 
 '_warnings', '_weakref', '_winapi', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 
 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time', 'winreg', 
 'xxsubtype', 'zlib')
 
import sys
print(sys.builtin_module_names)

import f
from f import n, n 
* for all
as 

"""

"""

import module_test
print(module_test.add(1, 2))

"""
#help("modules")
#help("tkinter")


#from m import add
#from m import pi
#from math import pi as p
#print(p)
"""
import sys
l = ["a", "b", "c"]
sys.path.append("C:\\Users\\User\\PycharmProjects\\")
sys.path += l
for i in sys.path:
    print(i)


password_list = ["123", "456"]
for i in range(3):
    try:
        p = input("Enter password :")
        if p in password_list:
            print("correct password and open door.")
            break
        else:
            raise Exception("incorrect password")
    except:
        pass

else:
    print("You tried many times. ")

"""

