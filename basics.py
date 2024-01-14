"""

1. input data 
2. calculate data 
3. output data

################################################

Data types ( built-in , custom )

1. Text Type:	str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	    set, frozenset
6. Boolean Type:	bool
7. Binary Types:	bytes, bytearray, memoryview
8. None Type:	    NoneType

################################################

Immutable types
1. int, float, complex, 
2. bool, 
3. str, 
4. tuple, 
5. range, 
6. frozenset, 
7. bytes
8. NoneType

Mutable types:
1. list
2. dict
3. set
4. bytearray
5. memoryview
6. user-defined classes

################################################

# complex number
# i = imaginary

x2 − 2x + 2 = 0.

x = ( 2 ± root(-4) ) / 2   <--- root(-4) = root(4) * root(-1) = 2 * i = 2i

x =( 2 ± 2i ) / 2

x = 1 ± i

x = 1 + i and x = 1 − i

################################################

1. int

name                     >>       int, integer, integer literal
definition               >>       integer
usage                    >>       directly use
description              >>       1. mthematical operation  

# int x = 1;   <--- C programming language
x = int(1);
x = 1
1

################################################   

2. arithmetic expression

name                     >>       arithmetic expression
definition               >>       
usage                    >>       arithmetic operator
description              >>       1. simple expression       --->   x = 1, 1 + 2
                                  2. complex expression      --->   x = 1 + 2 - 1
                                  3. mixed type expression   --->   int + float and etc
                                                             --->   x = 1 + 0.1 = float

# int and float
1 + 2.5

1.0 + 2.5 = 3.5

1 + 2 = 3

#######

# int and str
x = "1"
y = 1

# print(y + x)
print(y + int(x)) # 2
print(str(y) + x) # 11

#######

# int and chr

x = "A"
y = 65
print(y + ord(x)) # A = 65, ord ---> chr to unicode No
print(chr(y) + x) # a = 97, chr ---> unicode No to chr

################################################ 

3. arithmatic operator

name                     >>       arithmatic operator
definition               >>       
usage                    >>       **, * /, + -  ( integer/ floor division, modulus )( / // % )
description              >>       1. binary operator                        --->  1 - 2
                                  2. unary operator                         --->  -1
                                  3. to get precision value, py use float   --->  1 + 0.1 = float
                                  4. error with /                           --->  1 - 1/3 -1/3 -1/3

10 / 3 = 3.333
10 // 3 = 3
10 % 3 = 1


print(4 - 3) # binary minus ( sub )
print( - 3)  # unary minus ( neg )
print(dir(1))

e3 = 10 * 10 * 10 

2e3 = 2 * 1000 = 2000
2e-3 = 2 / 1000 = 0.002

1.1102230246251565e-16

0.00000000000000011102230246251565

################################################                                                         

4. operator precedence and associativity

name                     >>       operator precedence and associativity ( right or left )
definition               >>      
usage                    >>      
description              >>       p, e, u, * / , + -, ...,  =
                                  1. parenthesis                   --->   ( )
                                  2. exponent                      --->   **                      --->   Right sided bind     --->   2 ** 2 ** 3
                                                                                                                                     2 ** (2 ** 3)
                                                                                                                                     2 ** 8
                                                                                                                                     256
                                  3. unary minus, unary plus       --->   -1, +1                                                                                                     

                                  4. multiplication, division      --->   *, /, //, % 
                                  5. addition, substration         --->   +, -
                                  41. assignment                   --->   =                      --->   Right sided bind     --->   x = y = z = 1
x = 1 + 2 - 2 * 3 / (-2) ** 2
print(x)

Note
1. root 2, 3, 4 --> x = 4 ** (1/2), x = 16 ** (1/4)

################################################

5. floating-point number

name                     >>       float, floating-point number
definition               >>       number with .  
usage                    >>       .
description              >>       1. continuous values( 17 )
                                  2. normal division return float. ---> /
                                  3. int and float are different data types.
                                     so, they can not make operation directly.   
                                     ( before operation, py changed int to float )

                                  4. rounding adds or subtracts to produce closest value
                                         >> round(float)
                                            --> one argument value       --> int
                                            --> two                      --> float                       <----------
                                                ( second arg may be positive(r) or negative(l) )


                                  5. truncation to drop fractional part
                                         >> int()

                                  6. sys.float_info --> min , max

# 1. continuous values( 17 )
x = 1.234567890123456789
print(x)


import sys

print(sys.float_info.max)


e1 = 10
e2 = 100

e308 = 100000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000
000000000000000

e-1 = 0.1
e-2 = 0.01
e-3 = 0.001

e-308 =
0.00000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000
000000000000001

################################################

6. charactor string ( immutable object )

name                     >>      str, string, string literal
definition               >>      charactor string

usage                    >>      ' ',  " ", '''  ''', """  """,
description              >>      1. 47 methods (upper, lower), 
                                 2. concatination ( + ), 
                                 3. replication   ( * ) ( n th times )
                                 4. multiline string, preformatted string, doc string   --->   """   """    ,    '''   '''
                                                                            --->  auto complete \n
                                 5. indexing ( +, - )
                                 6. slicing ( +, - ) ( + & - )
                                 7. [start:stop:step] [s:p:1]
                                 8. step ( +, - )
                                 9. len()
                                 10. upper()
                                 11. lower()
                                 12. split()

x = "abcfounder@gmail.com"
user_name, domain = x.split("@")
print(user_name)
print(domain)

domain_name, email_type = domain.split(".")
print(domain_name)
print(email_type)

################################################

7. control code ( str )

name                     >>       control codes, escapse charactors, special charactors
definition               >>
usage                    >>       \
description              >>

1 .                        --->       \
2 .                        --->       '
3 .                        --->       "

4 . bell alarm             --->       a
5 . back space             --->       b
6 . form feed              --->       f
7 . new line               --->       n
8 . carriage return        --->       r
9 . horizontal tab         --->       t      
10 . vertical tab          --->       v


11 . unicode name                  --->       N{}
12 . hexadecimal                   --->       x00
13 . hexadecimal value             --->       u0000
     of unicode  ( 16 bit)
14 . hexadecimal value             --->       U00000000
     of unicode  ( 32 bit)

15 . octal value                   --->       000

path = "C:\\Users\\User\\PycharmProjects\\python_9_1\\fundamentals.py"
print(path)

x = 'I\'m  Mg Mg.'
print(x)

y = "I am \"Mg Mg\"."
print(y)

a
97, 61, 141

################################################

8. string formatting

name                     >>       string formatting
definition               >>
usage                    >>       format(), f
description              >>

1. format()  >>>   positional argument    --->       "{}  {}  {}".format("apple", "banana", "orange")
                                          --->       "{2}  {1}  {0}".format("apple", "banana", "orange")
                                          --->        index error
             >>>   keyword argument       --->       "{f1}  {f2}  {f3}".format(f1="apple", f2="banana", f3="orange")

2. f         >>>          --->       f"{f1}  {f2}  {f3}"


3. format methods  ( f, a, t )
   >>   :
   >>   fill charactor (" ")
   >>   <^> alignment
   >>   total charactor count

>> .2f                                                                                     
"abc"
total = 3
range ---> -3, ...,  2

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

################################################

9. identifier

name                     >>       variable, identifier, label
definition               >>       ကိုယ်စားပြုအမည်
                                  Identifier  ( for all ) ( function, class, method)
                                  variable ( for values )
usage                    >>       =
description              >>       Python has five rules for naming idenfiers. ( one, alpha, number, o, r )
                                  1. An identifier must contain at least one character.
                                  2. The first character of an identifier must be an alphabet or the underscore.
                                  3. The remaining characters may be alphabets, underscores, numbers.
                                  4. Qther characters are not permitted.
                                  5. A reserved keyword cannot be used as an identifier.
                                  6. 

import keyword

print(keyword.kwlist)

Note

1. keyword.kwlist

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']

################################################

10. assignment operator

name                     >>       assignment operator
definition               >>       assign right ( value ) to left ( identifier )
usage                    >>       =
description              >>       += , -=, *=, /=  မူလတန်ဖိုးကိုပဲ ထပ်ပေါင်းချင်ရင်သုံး

################################################

11.comment 

name                     >>       comment   
definition               >>       
usage                    >>       #
description              >>       python will ignore all lines with the first charactor #

# print(1)
# print(2)

################################################

12.                           

name                     >>       errors
definition               >>
usage                    >>       
description              >>       1. syntax error            --->   1name = "Mg Mg"    
                                  2. runtime error           --->   first_name = "Mg Mg"; full_name = first_name + last_name 
                                                                    print(f'x / y = {int(input("x = ")) / int(input("y = "))}')
                                  3. logical error, bug      --->

################################################

13.

name                     >>       input function
definition               >>
usage                    >>       input()
description              >>       receive input data as str

f = float(input("Enter degree F = "))
c = (f - 32) * 5 / 9
print(f"Degree C value = {c:.2f}")

c = float(input("Enter degree C = "))
f = (c * 9 / 5) + 32
print(f"Degree F value = {f:.2f}")

from tkinter import *

root = Tk()
degree_f = DoubleVar(root)
degree_c = DoubleVar(root)

def cal():
    x = float(degree_f.get())
    ans = (x - 32) * 5 / 9
    degree_c.set(ans)

f = Frame(root, borderwidth=40)
f.pack()
Label(f, text="Degree Fahrenheit = ").pack(side=LEFT)
Entry(f, textvariable=degree_f).pack(side=LEFT)

Button(root, text="Calculate", command=cal).pack()

f2 = Frame(root, borderwidth=40)
f2.pack()
Label(f2, text="Degree Celsius  =  ").pack(side=LEFT)
Entry(f2, textvariable=degree_c).pack(side=LEFT)

root.mainloop()

note
1. int()
2. float()
3. print()
4. root2        --->      **(1/2)                            
   root3        --->      **(1/3)

16 = 2 * 2 * 2 * 2 = 2**4

4 ** 2

print(2 ** 4 )
print(16 ** (1/4))

################################################

14.

name                     >>       print function
definition               >>
usage                    >>       print()
description              >>       1. print str value
                                  2. unlimited input data with ,
                                  3. positional arguments,
                                  4. keyword arguments      --->   by key name
                                     for print()            --->   end, sep, file, flush ( in time )

x = 1
y = 1.1
z = "apple"
print(x, y, z, file=open("abcdefg.txt", "w"))

def add(n1, n2):
    return n1 + n2

add(1, 2)  # positional arguments
add(n2=1, n1=2)  # keyword arguments

note
1. open()

################################################

15.

name                     >>       algorithums  
definition               >>       planning, creating rules and regulations
usage                    >>       pseudo code 
description              >>       pseudo code
                                  1. receive F
                                  2. calculate C
                                  3. show result

################################################

16. list ( mutable object )

name                     >>       list
definition               >>
usage                    >>       []
description              >>        1. Access items
                                        >>> indexing ( +, -)
                                        >>> slicing ( +, -)
                                        >>> step ( +, -)
                                   2. change item value
                                        >>> indexing ( +, -)
                                        >>> slicing ( +, -)
                                   3. loop through a list (iterable object)
                                   4. check if item in list ---> in
                                   5. check if item not in list ---> not in
                                   6. len()

                                   7. Add item ---> append()
                                   8. add item with index --> insert()

                                   9. remove with value ---> remove() ---> remove first value
                                   10. remove with index ---> pop()   ---> pop
                                   11. clear all value ---> clear()

                                   12.remove with del keyword
                                        >>> indexing ( +, -)
                                        >>> slicing ( +, -)
                                        >>> object

                                   13. copy a list ---> copy()  ---> method  
                                                   ---> list()
                                   14. join lists ---> +          ---> list to list
                                                  ---> loop and append()
                                                  ---> extend()   ---> list to iterable obj
                                   15. count()
                                   16. sort()     ---> reverse = True
                                   17. reverse()

1. user input fruit
2. check fruit in our store
3. reply          

x = [1, 2, "banana", 3, 4, "orange", 2.0] # 001

int_list = []
str_list = []

for i in x:
    if type(i) == int:
        int_list.append(i)
    if type(i) == str:
        str_list.append(i)

print(int_list)
print(str_list)

################################################

17. boolean data type

name                     >>       boolean, bool
definition               >>       George Boole ( 1815 ---> 1864, the law of thought )
usage                    >>       True, False
description              >>       1. expression with boolean result  
                                     --->   x = True, x = 1 < 2
                                  2. comparison operators produce boolean result ( >, <, >=, <=, ==, != ) ( in,  not in )

################################################

18 . Conditional Execution

note

1. linear sequence, nonlinear sequence

################################################

19. Simple if Statement

name                     >>       if, if Statement, conditional sttements   
definition               >>       translate with conditions
usage                    >>       if conditions:
description              >>       1. If condition is True, translate the conditional code (block of codes)

Note
Example . 1, 2,3

if c:
    print("paln.A")
    print("a")

else:
    print("paln.B")

if 1 < 2:
    print("1 is less than 2.")
    print("second line.")
    print("third line.")
    print()

print("statement")    

n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
if n1 < n2:
    print(f"{n1} is less than {n2}.")

################################################

20. if/else Statement

name                     >>       else   
definition               >>       translate with conditions
usage                    >>       else:
description              >>       1. if condition is False, translate code (block of codes)

Note

n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

c1 = n2 < n1
c2 = n1 < n2

if c1:print(f"{n1} is greater than {n2}.")

else:print(f"{n1} is not greater than {n2}.")

if c2:print(f"{n1} is less than {n2}.")

else:print(f"{n1} is not less than {n2}.")

################################################

21. Nested if

notes

c1 = 1 # water sensor.2  ( low level ) ( True )
c2 = 0 # electric ( true )
c3 = 0 # short curcit ( false )
c4 = 0 # water sensor.1  ( low level ) ( True )

if c1:
    if c2:
        if c3:
            print("message motor error")
        else:
            print("motot --->  water 1")
    else:
        print('generator --> electric')
        if c3:
            print("message motor error")
            print("close generator")


       else:
            print("motot --->  water 2")

################################################

22. if/elif/else Statement ( multi-way decision statement )

name                     >>       elif ( else if )
definition               >>       translate with conditions
usage                    >>       elif conditions:
description              >>       If above condition is not true, check this again.
                                      1. if first condition is not true, check second condition.
                                      2. if second condition is not true, check third condition.
                                         . . .

################################################

n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

if n1 < n2:
    print(f"{n1} is less than {n2}.")

elif n1 > n2:
    print(f"{n1} is greater than {n2}.")

elif n1 == n2:
    print(f"{n1} is equal to {n2}.")


################################################

m = int(input("marks = "))

if m == 100: print("very good.")
elif m >= 80: print("good")
elif m >= 40: print("not bad")
elif m < 40: print("fail")

# know
if c1: print("very good.")
if not c1 and c2: print("good")
if not c1 and not c2 and c3: print("not bad")
if not c1 and not c2 and not c3 and c4: print("fail")


if m == 100: print("very good.")

if 100 > m >= 80: print("good")

if 40 <= m < 80 : print("not bad")

if m < 40: print("fail")

################################################

motes

if d1:
    pass
elif d2:
    pass
elif d3:
    pass
elif d4:
    pass   
else:
    pass

################################################

23. Versus conditional statements

notes
1. parallel
2. A, a, 1, +

x = input("Enter some words : ")

if x.isupper():print(f"You entered upper case letter \"{x}\".")

if x.isalpha():print(f"You entered alphabetic letter \"{x}\".")

if x.isalnum():print(f"You entered alphanumeric letter \"{x}\".")

################################################

24. 

name                     >>       pass Statement 
definition               >>       to pass 
usage                    >>       pass
description              >>       use to pass incomplete code block

n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

if n1 < n2:
    pass


else:
    pass

################################################

x = 1 + 2

25. Conditional Expressions  ( if else operator, ternary operator )

name                     >>       conditional Expressions, if else operator, ternary operator 
definition               >>       ternary --> three components
usage                    >>       value_1 condition value_2
description              >>       
notes

x = int(input("x = "))

even_odd = "even" if x % 2 == 0 else "odd"

print(f"{x} is {even_odd}.")

################################################
################################################

26. Compound Boolean Expressions

notes
1. boolean operator       --->   not, and, or
2. operator precedence    --->   p, e, u, * / // %, +-, 
                                 < > ==, 
                                 not, and, or,

                                 =
                                 p, e, u, */, +-, c, b     

                                 (not, and, or)
3. operator asociativity  --->   left to right  ( left sided bind )

# 0     or   [1, 2]   or  [1, 3]
# False or   True     or   True
# True    or   True
# True ( l )

###########

# step.1 ( accept any ) ( or )

c = input("paid class feee : ")
c2 = input("member : ")
c3 = input("fund : ")

if c or c2 or c3:
    print("access class")

###########

# step.2 ( accept all ) ( and )
c = input("operator check : ")
c2 = input("Engine check : ")
c3 = input("Rocket check : ")
c4 = input("Weather check : ")

if c and c2 and c3 and c4:
    print("Rocket is ready to lunch.")

###########

# step.3 ( accept one + accept all ) ( or + and )
c = input("paid class feee : ")
c2 = input("member : ")

c3 = input("fund : ")

if (c or c2) and c3:
    print("access special class")

###########

# step.4 ( not )
def less_credit(n):
    return n < 11000

def under_age(age):
    return age <= 18

amount = int(input("Credit amount : "))
buyer_age = int(input("age : "))

if not less_credit(amount) and not under_age(buyer_age):
    print("You can buy Beer.")

if less_credit(amount) or under_age(buyer_age):
    print("You can not buy Beer.")


print(0 or [1, 2] or [1, 3]) 

################################################

27. Floating-point Equality 

note

use round function before comparing floating points  --->  1 - 1/3 -1/3 -1/3 == 0   --->    round(1 - 1/3 -1/3 -1/3, 3) == 0 


result = 1 - 1/3 -1/3 -1/3
print(round(result, 6) == 0)


1.1102230246251565e-16
0.00000000000000011102230246251565
################################################

28. Errors in Conditional Statements

1. tautology                --->   ever true       --->   > 1 or  < 10        --->   answer  - >  and
2. contradiction            --->   ever false      --->   < 1 and  > 10       --->   answer  - >  >, <


x = int(input("x = "))
if x < 1 and x > 10:
    print(f"{x} is between 1 and 10.")

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

# list, if, elif, else, boolean expression( 1 > 2 , True and True ), conditional executions / statement,
# conditional expression ( ternary operator )

################################################

# order

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

################################################

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

################################################

30. dict

name                     >>       dict, dictionary
definition               >>       list of keys and values
usage                    >>       {0 : "apple", }, dict()
description              >>       1. Access items               --->    d[key], keys(), values(), items()
                                  2. change item value          --->    d[key] = value

                                   3. loop through a dict       --->    d, d.keys(), d.values(), d.items()
                                   4. check if item in dict     --->    in
                                   5. check if item not in dict --->    not in
                                   6. count items               --->    len()

                                   7. Add one item              --->    d[key] = value
                                   8. update new items          --->    update()


                                   9. remove with key           --->    pop(key)
                                   10.remove last item          --->    popitem()
                                   11.clear all value           --->    clear()

                                   12.remove with del keyword
                                        >>> del d[key]
                                        >>> object

                                   13. copy a dict,             --->    copy method, dict function
                                       create new dict 

                                   14. join dict                --->    loop and d[key] = value
                                                                --->    update()

################################################

item_list

No   item     price    stock  exp_date  discount_price   cash back
1.   apple    1        1000   15         0.3
2.   note 11  200      10       _        0                10
3.


item_list[row]["price"] += 1

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

################################################

# 2. change value
#item_list[1]["price"] = 0.7
for i in item_list:
    if "note" in item_list[i]["item"]:
        item_list[i]["price"] -= item_list[i]["price"] * 10 / 100

print(item_list)
#print(item_list[3]["price"])

################################################

# 1. access
order = []
order_list = ["apple", "banana", "beer"]
for k in item_list:
    if item_list[k]["item"] in order_list:
        order.append(item_list[k])

print(order)

################################################

################################################

d = {
       "item": "apple",
       "price": 1,
       "exp_date": 5,
       "stock": 10000
}

# d[key], keys(), values(), items()

# d["item"]  # key index
k = ['item', 'price', 'exp_date', 'stock'] # keys()
v = ['apple', 1, 5, 10000] # values()
i = [('ite', 'apple'), ('pric', 1), ('exp_date', 6), ('stock', 100)] # items()

################################################

# loop
for k in d:
    print("keys =", k, end=", ")
    print("values =", d[k])

for k, v in d.items():
    print("keys =", k, end=", ")
    print("values =", v)

################################################

# update / join two dict with loop
d = {
       "item": "apple",
       "price": 1,
       "exp_date": 5,
       "stock": 10000
}
d2 = dict()

for k, v in d.items():
    d2[k] = v
    print(d2)

################################################

2D
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
   if item_list[i]["exp_date"] <= 10:
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

################################################

31. tuple

name                     >>       tuple
definition               >>       immutable list
usage                    >>       tuple(), () ( at least two items ), comma
description              >>       1. Access items               --->    indexing ( +, -)
                                                                --->    slicing ( +, -)
                                                                --->    step ( +, -)



                                   2. loop through a tuple      --->    
                                   3. check if item in tuple    --->    in
                                   4. check not in tuple        --->    not in
                                   5. count items               --->    len()

                                   6. count specific item       --->    count()  # x.count(2)
                                   7. search index              --->    index()  # x.index("banana")

                                   8.delete with del keyword   --->     del object

                                   9. join tuple                --->    +

Note

1. if need to change           ---> change to list
2. to remove duplicate values  ---> set()

###########

x = ("apple", "apple", "banana", 1, 1, 2, 2, 2)

l = list(x) # ["apple", "apple", "banana", 1, 1, 2, 2, 2]
del l[-5:] # ['apple', 'apple', 'banana']

d_t = tuple(l) # ('apple', 'apple', 'banana')
print(x)
print(l)
print(d_t)

###########

x = ("apple", "apple", "banana", 1, 1, 2, 2, 2)
print(x)

s = set(x) # {'apple', 1, 2, 'banana'}
print(s)

rm_d = tuple(s) # ('apple', 1, 2, 'banana')
print(rm_d)

################################################                                

32. set

name                     >>       set
definition               >>       set, unordered list
usage                    >>       {}, set()
description              >>        1. Access items              --->   can not access / change / delete with index position  

                                   2. loop through a set        --->    
                                   3. check if item in set      --->    in
                                   4. check not in set          --->    not in
                                   5. count items               --->    len()

                                   6. remove                    --->    error
                                   7. discard                   --->    no error
                                   8. pop                       --->    random 
                                                                        effect --> delete one element 
                                                                        result --> poped element

                                   9. clear                     --->    

                                   10. delete with del keyword  --->   del object

                                   11. add                      --->    an element
                                   12. update                   --->    elements ( x.update(iter))

                                   13. difference, -            --->    return, do not change original value
                                   14. difference_update        --->    not return, update value

                                   15. union, |                 --->    return all

                                   16. intersection, &          --->    return same value
                                   17. intersection_update      --->    

                                   18. symmetric_difference, ^  --->    return all except same value
                                   19. symmetric_difference_update

                                   20. isdisjoint               --->    return True if not same value in two sets
                                   21. issubset                 --->    ex in ey, x.issubset(y)
                                   22. issuperset               --->    ey in ex, x.issuperset(y)

x = {1, "apple", 1.2, 2}
y = {1, 2}
z = {"apple", 1.2, 1}

a = {1} # subset of x, y, z, b
b = {1, "apple", 1.2, 2}
d = {5, 6, 7, 1, 2}

################################################

33. frozen set

name                     >>       frozenset
definition               >>       frozenset, unordered list, immutable obj
usage                    >>       frozenset{}
description              >>        1. Access items              --->   can not access with index position  

                                   2. loop through a set        --->    
                                   3. check if item in set      --->    in
                                   4. check not in set          --->    not in
                                   5. count items               --->    len()

                                   6.delete with del keyword    --->    object

                                   7. difference,   -           --->    return, do not change original value

                                   8. union, |                  --->    return all  

                                   9. intersection, &           --->    return same value

                                   10. symmetric_difference, ^  --->    return all except same value

                                   11. isdisjoint               --->    return True if not same value in two sets
                                   21. issubset                 --->    ex in ey, x.issubset(y)
                                   22. issuperset               --->    ey in ex, x.issuperset(y)

################################################

Solved Examples Using Sets Formulas
Example 1: 
In a club, each person plays chess or carrom or both. 
The number of people who play chess, carrom or both are 11, 12 and 3 respectively. 
Representing this given information as sets and 
using the set formulae,

################################################

mg mg, ma ma, aung aung

chess - mg mg, ma ma, aung aung
c - mg mg, ma ma
cook - ma ma, aung aung
w - mg mg, ma ma, aung aung

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
# 3 person like both of chess and carrom
# let id of 3 person be 1, 5, 7

p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} # chess
q = {1, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20} # carrom

#print(len(q))

x = p.intersection(q)# (P ∩ Q)

print("id of people who like both = ", end="")
print(x)

print(len(x))# n(P∩Q) --> len(P & Q)
print()

ans = p.union(q)  # (P ∪ Q)
print("id of total people in club = ", end="")
print(ans)
print(len(ans))# n(P∪Q) total person  ---> len(P | Q)
print()

################################################

#Q1.  total people in club
#  | ---> union
p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} # chess
q = {1, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20} # carrom

print("Q1.  number total people in club =", len(p | q))
print("Q1.  names of total people in club =", p | q)

################################################

Q2. who like to play chess only

p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} # chess
q = {1, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20} # carrom

# number of  who like to play chess only  ---> n(p) - n(P ∩ Q) ---> len(p) - len(p & q)
# &  ---> intersection
print("number of  who like to play chess only  ---> n(p) - n(P ∩ Q) =", len(p) - len(p & q))
print("names of  who like to play chess only  ---> p - (P ∩ Q) =", p - (p & q))

################################################

Q3. who like to play carrom only

p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} # chess
q = {1, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20} # carrom

# number of  who like to play carrom only  ---> n(p) - n(P ∩ Q) ---> len(p) - len(p & q)
# &  ---> intersection
print("number of  who like to play carrom only  ---> n(q) - n(P ∩ Q) =", len(q) - len(p & q))
print("names of  who like to play carrom only  ---> q - (P ∩ Q) =", q - (p & q))

################################################

# if you do not want to change group data, you can use frozenset.
p = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}) # chess
q = frozenset({1, 5, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20}) # carrom

# p.update([21, 22, 23])
# number of  who like to play chess only  ---> n(p) - n(P ∩ Q) ---> len(p) - len(p & q)
# &  ---> intersection
print("number of  who like to play chess only  ---> n(p) - n(P ∩ Q) =", len(p) - len(p & q))
print("names of  who like to play chess only  ---> p - (P ∩ Q) =", p - (p & q))

################################################

ans = 3 ^ 2
#   1 1
#   1 0

#   0 1
print(ans)

################################################

p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} # chess
q = {12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 5, 7}

ans = p ^ q
print(ans)

################################################

34. Data types      4 left

1. Text Type:	    str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	    set, frozenset
6. Boolean Type:	bool
7. Binary Types:	bytes, bytearray, memoryview
8. None Type:	    NoneType

x = None
print(x)

print(dir(x)) # 25
['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__']

################################################

Immutable types
1. int, float, complex, 
2. bool, 
3. str, 
4. tuple, 
5. range, 
6. frozenset, 
7. bytes
8. NoneType

Mutable types:
1. list
2. dict
3. set
4. bytearray
5. memoryview

6. user-defined classes

################################################

multiply all
eg . tuple * 2

################################################
################################################

Lists and Tuples are ordered sequences of elements.
ordered ---> indexing
mutable   ---> update, delete, assign

ordered ---> indexing
immutable   ---> can not ( update, delete, assign )

Python dictionaries are collections of items that are unordered, indexed and mutable.
unordered ---> no index
indexed   ---> own index values (or keys)
mutable   ---> update, delete, assign

This means that there is no specific order to the items in a dictionary, 
and they have their own index values (or keys) that can be used to reference individual elements. 

Python sets are unordered collections of elements.

Set is a mutable object but Set elements must be immutable obj.
unordered ---> no index
mutable   ---> update, delete, assign
immutable elements  ---> can not ( update, delete, assign )

set1 = {1, 2, 3, (1, 2)}
print(set1)

s1 = {1, 2, 3, 4, 5}
s2 = {"apple", "banana"}
m = {frozenset(s1), frozenset(s2)}
print(m)

to make an immutable set, we use the concept of frozenset. 
s1 = frozenset({1, 2, 3, 4, 5})

################################################

35. Type casting

1. int(x [,base]), result = decimal value, int value
Converts x to an integer. base specifies the base if x is a string.

x = int(2)
print(x)

x = int(2.65)
print(x)

x = int('100', base=2)
print(x)
x = int('100', base=8)
print(x)
x = int('100')
print(x)
x = int('100', base=16)
print(x)

x = int('0b100', base=0) # "b" = binary numbering system
print(x)
x = int('0O100', base=0) # "O"  = octal numbering system
print(x)
x = int('100') # directly use = decimal numbering system
print(x)
x = int('0x100', base=0) # "x"  = hexadecimal numbering system
print(x)

c = input("code No : ")
b = int(input("base :"))

x = int(c, b)
print(x)

long x = 10;

import sys
x = 1000000000000000000000000000000000000000000000000000000000000  # 28, e16 --> 32 bytes, e30 = 40 bytes, e60 = 52 bytes

print(sys.getsizeof(x))

s = set()  # empty = 216, 4 elements = 216, 5 elements = 472

d = {"name": "Mg Mg"} # 64 , 1 = 184
print(sys.getsizeof(d))  # empty = 160,

x = "apple"
print(hex(id(x)))
c = input("code No (0b, 0O, 0x ): ")  # 0x107cd02bb70
x = int(c, base=0)
print(x)

2. long(x [,base] )
Converts x to a long integer. base specifies the base if x is a string.

3. float(x)
Converts x to a floating-point number.

s = 5
f = float(s)
print(f)

a = 1 + 2.5 + 4
print(a)

a = 1 + int(2.5) + 4
print(a)

4. complex(real [,imag])
Creates a complex number.

z = 5 + 3j
x = 5 + 3j
print(z)
print(z.real)
print(z.imag)
print(x * z)

z = complex(5, 3)
x = complex(5, 3)
print(z)
print(z.real)
print(z.imag)
print(x * z)

5. str(x)
Converts object x to a string representation

n = 1
s = str(n) # "1"
print(s)
print(type(s))

6. repr(x)
Converts object x to an expression string.

x = 1
print(repr(x))

7. eval(str)
Evaluates a string and returns an object.

s = "1 + 2"
print(s)
print(eval(s))

8. tuple(s)
Converts s to a tuple.

9. list(s)
Converts s to a list.

10. set(s)
Converts s to a set.

11. dict(d)
Creates a dictionary. d must be a sequence of (key,value)

l = [["name", "MG Mg"], ["age", 20], ("ph No", "0911112")]
d = dict(l)
print(d)

12. frozenset(s)
Converts s to a frozen set.

13. chr(x)
Converts an integer to a character.

x = 4096
print(x)
y = chr(x)
print(y)

import sys
print(sys.getsizeof(y))

14. unichr(x)
Converts an integer to a Unicode character.

15. ord(x)
Converts a single character to its integer value.

x = 4096
print(chr(x))


x = "က"
print(ord(x)) # 4096
print(hex(ord(x))) # 0x1000

print(ord("a"))

16. hex(x)
Converts an integer to a hexadecimal string.

x = 15
h = hex(x)
print(h)
print(int(h, base=0))

17. oct(x) 
Converts an integer to an octal string

101

x = 8
print(oct(x))


################################################
################################################

function, module, package

oop, obj

#import m

#from m import pi, add

# all, *
#from m import *

# change name
#import m as x
#from m import pi as mypi

################################################
################################################

"""