# 1. int
# 2. arithmetic expression
# 3. arithmatic operator
# 4. operator precedence and associativity
# 5. floating-point number
# 6. charactor string ( immutable object )
# 7. control code ( str )
# 8. string formatting
# 9. identifier
# 10. assignment operator
# 11.comment
# 12. errors
# 13. input function
# 14. print function
# 15. algorithms
# 16. list ( mutable object )
# 17. boolean data type
# 18 . Conditional Execution
# 19. Simple if Statement
# 20. if/else Statement
# 21. Nested if
# 22. if/elif/else Statement ( multi-way decision statement )
# 23. Versus conditional statements
# 24. pass
# 25. Conditional Expressions  ( if else operator, ternary operator )
# 26. Compound Boolean Expressions
# 27. Floating-point Equality
# 28. Errors in Conditional Statements
# 29. boolean exercises
# 30. dict
# 31. tuple
# 32. set
# 33.frozenset
# 34. built-in types
# 35. type casting

"""
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
description              >>       1. mathematical operation  

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

print(1 + 2.0)
print(float(1) + 2.5)
print(1 + int(2.5))

#######

# int and str
x = "1"
y = 1

#print(y + x)
print(y + int(x))  # 1 + 1 = 2
print(str(y) + x)  # "1" + "1" = "11"

#######

# int and chr

x = "A"
y = 65
print(y + ord(x))  # A = 65, ord ---> chr to unicode No
print(chr(y) + x)  # a = 97, chr ---> unicode No to chr

################################################ 

3. arithmatic operator

name                     >>       arithmatic operator
definition               >>       
usage                    >>       **, * /, + -  ( integer/ floor division, modulus )( / // % )
description              >>       1. binary operator                        --->  1 - 2 , left & right operand
                                  2. unary operator                         --->  -1, right operand
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


# e0 = 1.0
# e1 = 10.0
# e2 = 100.0
# e3 = 1000.0
# e10 = 10000000000.0

# 1e0 = 1 * 1.0
# 1e1 = 1 * 10.0
x = 1e12
print(x)

# e-0 = 1 / e0 = 1 / 1.0 = 1.0 / 1.0 = 1.0
# e-1 = 1 / e1 = 1 / 10.0 = 0.1
# e-2 = 1 / e2 = 1 / 100.0 = 0.01
# e-3  = 1 / e3 = 1 / 1000 = 0.001
# e-10 = 1 / 1000 000 000 0 = 0.000 000 000 1
 

print(1e10)
print(1e-10)


################################################                                                         

4. operator precedence and associativity

name                     >>       operator precedence and associativity ( right or left )
definition               >>      
usage                    >>      
description              >>       p, e, u, * / , + -, ...,  =
                                  1. parenthesis                   --->   ( )
                                  2. exponent                      --->   ** 
                                     --->     Right sided bind     --->   2 ** 2 ** 3
                                                                          2 ** (2 ** 3)
                                                                          2 ** 8
                                                                          256                                 
                                  3. unary minus, unary plus       --->   -1, +1
                                  4. multiplication, division      --->   *, /, //, % 
                                  5. addition, substraction         --->   +, -
                                  41. assignment                   --->   =
                                      --->   Right sided bind      --->   x = y = z = 1

x = 1 + 2 - 2 * 3 / (-2) ** 2
print(x)

Note
print(2 ** 4)  # power 4
print(16 ** (1/4))  # root4
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

                                  4. rounding adds or subtracts to produce the closest value
                                         >> round(float)
                                            --> one argument value       --> int
                                            --> two                      --> float                       <----------
                                                ( second arg may be positive(r)(>5) or negative(l)(5) )


                                  5. truncation to drop fractional part
                                         >> int()

                                  6. sys.float_info --> min(0) , max(inf)


# 1. continuous values( 17 )
x = 1.234567890123456789
print(x)
print(4 / 2)


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
usage                    >>      ' ',  " ", '''  ''', """  """
description              >>      1. 47 methods (upper, lower), 
                                 2. concatenation ( + ), 
                                 3. replication   ( * ) ( n th times )
                                 4. multiline string, preformatted string, doc string ---> """  """, '''   '''
                                                                                      --->  auto complete \n
                                 5. indexing ( +, - )  # practice.1
                                 6. slicing ( +, - ) ( + & - )
                                 7. [start:stop:step] [s:p:1]
                                 8. step ( +, - )
                                 9. len()
                                 10. upper()
                                 11. lower()
                                 12. split()



def mylower(s):
    l = ""
    for c in s:
        u = ord(c)
        if 65 <= u <= 92:
            l += chr(u + 32)
        else:
            l += c
    return l


s = "ABCD"
print(s.lower())
print(mylower(s))

s = "A"
l = chr(ord(s) + 32)
print(s, l)

s = "APPLEapple123apple"
l = ""
for c in s:
    u = ord(c)
    if 65 <= u <= 92:
        l += chr(u + 32)
    else:
        l += c

print(l)
print(s.lower())
print(s.replace("apple", "banana"))

print("1" + "1")  # '11'  "ab"
print("a" * 10)
print("1" * 10)  # 1111111111

x = "abcfounder@gmail.com"
user_name, domain = x.split("@")  # ["abcfounder", "gmail.com"]
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
"""
#             >>>   keyword argument      --->       "{f1}  {f2}  {f3}".format(f1="apple", f2="banana", f3="orange")

"""
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


x = "{}  {}  {}"
print(x.format("apple", "banana", "orange"))


practice.2   --->   format table

################################################

9. identifier

name                     >>       variable, identifier, label
definition               >>       ကိုယ်စားပြုအမည်
                                  Identifier  ( for all ) ( value, function, class, method, module)
                                  variable ( for values )
usage                    >>       =
description              >>       Python has five rules for naming identifiers. ( one, alpha, number, o, r )
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
definition               >>       assign right ( obj ) (memory address) to left ( identifier )
usage                    >>       =
description              >>       += , -=, *=, /=, //=, %=, **  မူလတန်ဖိုးကိုပဲ ထပ်ပေါင်းချင်ရင်သုံး


################################################

11.comment 

name                     >>       comment   
definition               >>       
usage                    >>       #
description              >>       python will ignore all lines with the first charactor #


# receive fahrenheit value from user
f = float(input("Enter degree F = "))

# F to C formula
c = (f - 32) * 5 / 9

# output Celsius value
print(f"Degree C value = {c:.2f}")

################################################

12. errors                          

name                     >>       errors
definition               >>
usage                    >>       
description              >>       1. syntax error            --->   1name = "Mg Mg"    
                                  2. runtime error           --->   first_name = "Mg Mg"; full_name = first_name + last_name 
                                                                    print(f'x / y = {int(input("x = ")) / int(input("y = "))}')
                                  3. logical error, bug      --->

################################################

13. input function

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

16 = 2 * 2 * 2 * 2 = 2 ** 4

4 ** 2

print(2 ** 4 )
print(16 ** (1/4))

################################################

14. print function

name                     >>       print function
definition               >>
usage                    >>       print()
description              >>       1. print str value
                                  2. unlimited input data with ,
                                  3. positional arguments,
                                  4. keyword arguments      --->   by key name
                                     for print()            --->   end, sep, file, flush ( in time )

help(print)

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

15. algorithms

name                     >>       algorithms  
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

practice.3   --->   Nested if
practice.4   --->   automatic water motor controller

################################################

22. if/elif/else Statement ( multi-way decision statement )

name                     >>       elif ( else if )
definition               >>       translate with conditions
usage                    >>       elif conditions:
description              >>       If above condition is not true, check new condition again.
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

practice.4   --->   elif ( exam fail/pass with marks )

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

24. pass

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

x = 1 + 2  = 3

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
2. operator precedence    --->   p, e, u, * /, +-, 
                                 < > ==, 
                                 not, and, or,

                                 =
                                 p, e, u, */, +-, c, b     

                                 (not, and, or)
3. operator associativity  --->   left to right  ( left sided bind )
4. or --> True  -->  first T
5. and ---> False -->  first F
False or   True

not True = False

print(True or not True and False or not True and True or False)


# 0     or   [1, 2]   or  [1, 3]
# False or   True     or   True
# True    or   True
# True ( l )

###########

practice.6   --->    boolean exercises

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

# list, if, elif, else, boolean expression( 1 > 2 , True and True ), conditional executions / statement,
# conditional expression ( ternary operator )

practice.6   --->    boolean exercises
practice.7   --->   order
practice.8   --->   beer
practice.9   --->   palindrome check

################################################

30. dict

name                     >>       dict, dictionary
definition               >>       list of keys and values
usage                    >>       {}, {0 : "apple", }, dict()
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

l = ["Mg Mg", 20, "0995443300"]
print(l[1])

d = {0: "Mg Mg", 1: 20, 2: "0995443300", -3: "Mg Mg", -2: 20, -1: "0995443300"}
print(d[-1])

user1 = {"name": "Mg Mg", "age": 20, "phNo": "0995443300"}
print(user1)
print(user1["age"])  # access
print(list(user1))   # user1 ---> user1.keys()
print(user1.keys())
print(user1.values())
print(user1.items())

# change
user1["name"] = "Ma Ma"
# add
user1["Email"] = "mama@gmail.com"
print(user1)

# loop
for i in user1:   # user1 ---> user1.keys()
    print(i)

print()

for i in user1.keys():
    print(i)
    
print()

for i in user1.values():
    print(i)

print()

# step.1
for i in user1.items():  # (k, v)
    print(i)

print()

# step.2
for i in user1.items():
    k = i[0]
    v = i[1]
    print(k, "=", v)

print()

# step.3
for i in user1.items():
    k, v = i
    print(k, "=", v)

print()

# step.4
for k, v in user1.items():
    print(k, "=", v)

print("Ma Ma" in user1.values())
print("Email" in user1.keys())

user1 = {"name": "Mg Mg", "age": 20, "phNo": "0995443301", "email": "mgmg@gmail.com"}
user2 = {"name": "Ma Ma", "age": 21, "phNo": "0995443302", }
user3 = {"name": "Mya Mya", "age": 30, "phNo": "0995443303", }

users = [user1, user2, user3]   # users[-5:]  , [:5], [m-2:m+2] ---> t = 10, m = 5, 3:7 ---> 3, 4, 5, 6
# name = users[0]["name"]   = 


for user in users:
    if "email" in user:
        pass
        # print(user["email"])
    else:
        v = input(f"Enter your email({user['name']}): ")
        user["email"] = v

print(users)

################################################

practice.10   --->   2D  data, nested dict

practice.11   --->   2D  data with rate formula
https://drive.google.com/file/d/1vMWvbMAgvsZhRgmV-29wbvgsaWjL4ZZK/view?usp=drivesdk

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

                                   8.delete with del keyword   --->     del identifier/ object

                                   9. join tuple                --->    +  --->  new tuple

Note

1. if need to change           ---> change to list
2. to remove duplicate values  ---> set()

###########

t = (1, 2, 2, 2, 3, "banana", 4, 5)
positive_index = t.index("banana")
print(positive_index)

total_count = len(t)
negative_index = (total_count - positive_index)
print(- negative_index)

################################################

x = ("apple", "apple", "banana", 1, 1, 2, 2, 2)

l = list(x)  # ["apple", "apple", "banana", 1, 1, 2, 2, 2]
del l[-5:]  # ['apple', 'apple', 'banana']

d_t = tuple(l)  # ('apple', 'apple', 'banana')
print(x)
print(l)
print(d_t)

################################################

x = ("apple", "apple", "banana", 1, 1, 2, 2, 2)

x = list(x)  # ["apple", "apple", "banana", 1, 1, 2, 2, 2]
del x[-5:]  # ['apple', 'apple', 'banana']

x = tuple(x)  # ('apple', 'apple', 'banana')
print(x)

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

                                   10. delete with del keyword  --->   del label/ object

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
                                   21. issubset                 --->    ex in ey, x.issubset(y), self in other
                                   22. issuperset               --->    ey in ex, x.issuperset(y), other in self


x = {1, "apple", 1.2, 2}
y = {1, 2}
z = {"apple", 1.2, 1}

a = {1}  # subset of x, y, z, b
b = {1, "apple", 1.2, 2}
d = {5, 6, 7, 1, 2}


print(x.issuperset(b))
print(b.issuperset(x))
print(x.issubset(b))
print(b.issubset(x))

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

                                   6. delete with del keyword    --->    del label / object

                                   7. difference,   -           --->    return, do not change original value

                                   8. union, |                  --->    return all  

                                   9. intersection, &           --->    return same value

                                   10. symmetric_difference, ^  --->    return all except same value

                                   11. isdisjoint               --->    return True if not same value in two sets
                                   12. issubset                 --->    ex in ey, x.issubset(y)
                                   13. issuperset               --->    ey in ex, x.issuperset(y)

################################################

practice.12   --->   Solved Examples Using Sets Formulas

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

print(dir(x))  # 25


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

set1 = {1, 2, 3, {"name": "Mg Mg"}, "apple"}
print(set1)

s1 = {1, 2, 3, 4, 5}
s2 = {"apple", "banana"}
m = {frozenset(s1), frozenset(s2)}
print(m)

l = [1, 2, 3, 4, 5]
l2 = ["apple", "banana"]
m = {tuple(l), tuple(l2)}
print(m)

to make an immutable set, we use the concept of frozenset. 
s1 = frozenset({1, 2, 3, 4, 5})

################################################

35. Type casting ( implicit, explicit ) ( indirect type casting / type by py, type casting by programmer )


x = 1
y = 1.2
z = x + y
print(z)

z = True + 1.2
print(z)

x = 1
y = 1.2
z = x + int(y)
print(z)

x = 1
y = 1.2
z = float(x) + y
print(z)

################################################

1. int(x [,base]), result = decimal value, base 10, int value
Converts x to an integer. base specifies the base if x is a string.

x = int(2)
print(x)

x = int(2.65)
print(x)

x = int('10', base=2)
print(x)
x = int('10', base=8)
print(x)
x = int('10', base=10)
print(x)
x = int('10', base=16)
print(x)

x = int('0b10', base=0)  # "b" = binary numbering system
print(x)
x = int('0O10', base=0)  # "O"  = octal numbering system
print(x)
x = int('10', base=0)  # directly use = decimal numbering system
print(x)
x = int('0x10', base=0)  # "x"  = hexadecimal numbering system
print(x)

c = input("code No : ")
b = int(input("base :"))

x = int(c, b)
print(x)


c = input("code No (0b, 0O, 0x ): ")  # 0x107cd02bb70
x = int(c, 0)
print("decimal value =", x)

#####################

help(int)

--->  int(x, base=10)

Convert a number or string to an integer,                  ---> x = int(1.2),  x = int("10")
 
return 0 if no arguments are given.                        ---> x = int()  # x = 0

If x is a number, return x.__int__().                      ---> x = int(10)  # x = 10 ( int object  )

For floating point numbers, this truncates towards zero.   ---> x = int(1.9)  # x = 1

If base is given, 
then x must be a string instance representing an integer literal in the given base.
                                                           ---> int("1010101", base=2), 
                                                           --->  x = int("k", 21)
 
integer literal in the base 2   ---> 0, 1
integer literal in the base 8   ---> 0, 1, 2, 3, 4, 5, 6, 7
integer literal in the base 10  ---> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
integer literal in the base 16  ---> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
                                ---> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

integer literal in the base 36  ---> 0, 1, ...., 35(a, b, c, ...  ( count 36 )
 
The literal can be preceded by '+' or '-' and be surrounded by whitespace.    
                                ---> x = int(" -f ", base=16)
                                
The base defaults to 10.        ---> x = int("10")   # x = int("10", base=10)

Valid bases are 0 and 2-36.     ---> x = int("10", base=36) , x = int("z", 36)  # 0 to 35(z)

Base 0 means to interpret the base from the string as an integer literal.
>> zero + code No
>> base from the string         ---> 0b (base 2), 0o (base 8), 0x (base 16)      
                                ---> int('0b10', base=0)

#####################

import sys

x = 0  # 28, e10 --> 32 bytes, e30 = 40 bytes, e60 = 52 bytes
print(sys.getsizeof(x))

s = set()  # empty = 216, 4 elements = 216, 5 elements = 472
print(sys.getsizeof(s))

d = {"name": "Mg Mg"}  # 64 , 1 = 184
print(sys.getsizeof(d))

#####################

2. long(x, base )   ( removed in py 3 )
Converts x to a long integer. base specifies the base if x is a string.


3. float(x)
Converts x to a floating-point number.
Convert a string or number to a floating point number, if possible.

s = 5
f = float(s)
print(f)

x = "100"
f = float(x)
print(f)

x = True
f = float(x)
print(f)


4. complex(real, img)
Creates a complex number.
Create a complex number from a real part and an optional imaginary part.

z = 5 + 3j
x = 5 + 3j
print(z)
print(z.real)
print(z.imag)
print(x + z)

z = complex(5, 3)
x = complex(5, 3)
print(z)
print(z.real)
print(z.imag)
print(x + z)

help(z)

5. str(x)
Converts object x to a string representation

n = 1
s = str(n)  # "1"
print(s)
print(type(s))

6. repr(x)
Converts object x to an expression string.

x = 1
r = repr(x)  # "1"
print(r)
print(type(r))


class X:
    def __str__(self):
        return "haha"

    def __repr__(self):
        return f"<__main__.X object at {hex(id(self))}>"


x = X()
print(x)
print(repr(x))

y = X()
print(y)
print(repr(y))


7. eval(str)
Evaluates a string and returns an object.

s = "1 + 2"
e = eval(s)  # 1 + 2 = 3
print(s)
print(e)


8. tuple(s)
Converts s to a tuple.
l = [1, 2, 3]
t = tuple(l)
print(t)


9. list(s)
Converts s to a list.

d = {'name': 'MG Mg', 'age': 20, 'ph No': '0911112'}
k = list(d.keys())
print(k)
v = list(d.values())
print(v)
i = list(d.items())
print(i)


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

x = 0x1000  # 4096
print(x)
y = chr(x)
print(y)


14. unichr(x)
Converts an integer to a Unicode character.


15. ord(x)
Converts a single character to its integer value.

x = 4096
print(chr(x))

x = "က"
print(ord(x))  # 4096

print(hex(ord(x)))  # 0x1000
print(ord("a"))


16. hex(x)
Converts an integer to a hexadecimal string.

x = 4096
h = hex(x)  # "0x1000"
print(h)

print(int(h, base=0))


17. oct(x) 
Converts an integer to an octal string

x = 8
o = oct(x)  # "0o10"
print(o)

print(int(o, 0))


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

practice.13   --->   square root / ํF to ํC

################################################
################################################

"""

