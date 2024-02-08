
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

################################################   

2. arithmetic expression

name                     >>       arithmetic expression
definition               >>       
usage                    >>       =  ( +, - )
description              >>       1. simple expression       --->   x = 1
                                  2. complex expression      --->   x = 1 + 2
                                  3. mixed type expression   --->   int + float and etc
                                                             --->   x = 1 + 0.1 = float
                                  4. formatting ( a e )      --->   x, y, z in expression
                                                             --->   3x2 + 2xy - 5
                                                             --->   3*(x**2) + 2*x*y - 5
                               
################################################ 

3. arithmatic operator

name                     >>       arithmatic operator
definition               >>       
usage                    >>       **, * /, + -  ( integer/ floor division, modulus )( / // % )
description              >>       1. binary operator                        --->  x = 1 - 2
                                  2. unary operator                         --->  x = -1
                                  3. to get precision value, py use float   --->  1 + 0.1 = float
                                  4. error with /                           --->  1 - 1/3 -1/3 -1/3

                                                                            --->  `round`

################################################                                                         
                                                           
4. operator precedence and associativity

name                     >>       operator precedence and associativity ( right or left )
definition               >>      
usage                    >>      
description              >>       p, u, e, * / , + -, =
                                  1. parenthesis                   --->   ( )
                                  2. unary minus, unary plus       --->   -1, +1
                                  3. exponent                      --->   **                      --->   Right sided bind     --->   2 ** 2 ** 3
                                                                                                                                     2 ** (2 ** 3)
                                                                                                                                     2 ** 8
                                                                                                                                     256
                                  4. multiplication, division      --->   *, /, //, % 
                                  5. addition, substration         --->   +, -
                                  41. assignment                    --->   =                      --->   Right sided bind     --->   x = y = z = 1

                                
################################################

5. floating-point number

name                     >>       float, floating-point number
definition               >>       number with .  
usage                    >>       .
description              >>       1. continuous values 16 ( 17 )
                                  2. store by 1/10                   --> 0.11 = 1/10 + 1/100
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

import sys

print(sys.float_info.min)

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
                                 2. concatination ( + ), 
                                 3. replication   ( * ) ( n th times )
                                 4. multiline string, preformatted string   --->   """   """    ,    '''   '''
                                                                            --->   auto complete \n
                                 5. indexing ( +, - )
                                 6. slicing ( +, - ) ( + & - )
                                 7. [start:stop:step] [s:p:1]
                                 8. step ( +, - )
                                 9. len()
                                 10. upper()
                                 11. lower()
                                 12. split()
                                 13. user input to upper case letter
                                 14. file output

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

( 97 ( 141, 61))

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
   >>   fill charactor
   >>   <^> alignment
   >>   total charactor count
   
>> .2f  

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
                                 
name = "mg mg"

print(hex(id(name)))

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
                                  tuple assign

################################################

"""

"""

11.
               
name                     >>       comment   
definition               >>       
usage                    >>       #
description              >>       python will ignore all lines with the first charactor #
                                        
################################################

12.                           

name                     >>       errors
definition               >>
usage                    >>       
description              >>       1. syntax error            --->   1name = "Mg Mg"    
                                  2. runtime error           --->   first_name = "Mg Mg"; full_name = first_name + last_name 
                                  3. logical error, bug      --->   print(f'x / y = {int(input("x = ")) / int(input("y = "))}')

################################################

13.

name                     >>       input function
definition               >>
usage                    >>       input()
description              >>       receive input data as str


f = float(input("Enter degree F = "))
c = (f - 32) * 5 / 9
print(f"Degree C value = {c:.2f}")

note
1. int()
2. float()
3. print()
4. root2        --->      **1/2                               < - - - - -  - - - - - 
   root3        --->      **1/3

16 = 2 * 2 * 2 * 2 = 2**4

################################################

14.

name                     >>       print function
definition               >>
usage                    >>       print()
description              >>       1. print str value
                                  2. unlimited input data with ,
                                  3. positional arguments,
                                  4. keyword arguments      --->   by name
                                     for print()            --->   end, sep, file, flush ( in time )

x = 1
y = 1.1
z = "apple"
print(x, y, z, file=open("abcdefg.txt", "w"))

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
                                   
                                   9. remove with value ---> remove()
                                   10.remove with index ---> pop()
                                   11.clear all value ---> clear()
                                   
                                   12.remove with del keyword
                                        >>> indexing ( +, -)
                                        >>> slicing ( +, -)
                                        >>> object
                                        
                                   13. copy a list ---> copy()
                                   14. join lists ---> +
                                                  ---> loop and append()
                                                  ---> extend() 
                                   15. count()
                                   16. sort()     ---> reverse = True
                                   17. reverse()
                                
x = [1, 2, 3, 4, 8]
x.reverse()
print(x)

y = "apple"
for i in y:
    x.append(i)
    print(x)
    
################################################

17. boolean data type

name                     >>       boolean
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

name                     >>       if     
definition               >>       translate with conditions
usage                    >>       if conditions:
description              >>       1. If condition is True, translate the conditional code (block of codes)
                
Note
Example . 1, 2,3

if 1 < 2: print("1 is less than 2.")

if 1 < 2:
    print("1 is less than 2.")
    print("second line.")
    print("third line.")
    print()

n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
if n1 < n2:
    print(f"{n1} is less than {n2}.")

################################################

20. if/else Statement

name                     >>       else   
definition               >>       translate with conditions
usage                    >>       else:
description              >>       1. if condition is false, translate  code (block of codes)
                
Note

n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

if n1 < n2:
    print(f"{n1} is less than {n2}.")

else:
    print(f"{n1} is not less than {n2}.")
    
################################################

"""


"""

21. Nested if

notes

c1 = 1
c2 = 0
c3 = 1
c4 = 1

if c1:
    if c2:
        pass
    else:
        if c3:
            if c4:
                pass
            else:
                pass
        else:
            pass
else:
    if c2:
        pass
    else:
        if c3:
            if c4:
                pass
            else:
                pass
        else:
            pass

################################################

22. if/elif/else Statement ( multi-way decision statement )

name                     >>       elif ( else if )
definition               >>       translate with conditions
usage                    >>       elif conditions:
description              >>       If above condition is not true, check this again.
                                      1. if first condition is not true, check second condition.
                                      2. if second condition is not true, check third condition.
                                         . . .
Note

n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

if n1 < n2:
    print(f"{n1} is less than {n2}.")
    
elif n1 > n2:
    print(f"{n1} is greater than {n2}.")

elif n1 == n2:
    print(f"{n1} is equal to {n2}.")





m = int(input("marks = "))

if m == 100: print("very good.")
elif m > 79: print("good")
elif m > 39: print("not bad")
elif m < 40: print("fail")



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
2. A, a, 1



x = input("Enter some words : ")

if x.isupper():print(f"You entered upper case letter \"{x}\".")

if x.isalpha():
    print(f"You entered alphabetic letter \"{x}\".")

if x.isalnum():
    print(f"You entered alphanumeric letter \"{x}\".")


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

26. Compound Boolean Expressions

notes
1. boolean operator       --->   not, and, or
2. operator precedence    --->   p, u, e, */, +-, 
                                 < > ==, 
                                 not, and, or,
                                 
                                 =
3. operator asociativity  --->   left to right  ( left sided bind )

################################################

27. Floating-point Equality 

note

use round function before comparing floating points  --->  1 - 1/3 -1/3 -1/3 == 0   --->    round(1 - 1/3 -1/3 -1/3, 3) == 0 

################################################

28. Errors in Conditional Statements

1. tautology                --->   ever true       --->   > 1 or  < 10        --->   answer  - >  and
2. contradiction            --->   ever false      --->   < 1 and  > 10       --->   answer  - >  >, <

x = int(input("x = "))
if x > 1 and x < 10:
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


# list, if, elif, else, boolean expression( 1 > 2 , True and True ), conditional executions / statement,
# conditional expression ( ternary operator )

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

################################################

30. dict

name                     >>       dict, dictionary
definition               >>       list of keys and values
usage                    >>       {0 : "a", }, dict()
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
                                        
                                   13. copy a dict              --->    copy method, dict function

                                   14. join dict                --->    loop and d[key] = value
                                                                --->    update()

item_list

No   item     price    stock  exp_date  discount_price   cash back
1.   apple    1        1000   15         0.3
2.   note 11  200      10       _        0
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

# 2. change value
#item_list[1]["price"] = 0.7
for i in item_list:
    if "note" in item_list[i]["item"]:
        item_list[i]["price"] -= item_list[i]["price"] * 10 / 100

print(item_list)
#print(item_list[3]["price"])

# 1. access
order = []
order_list = ["apple", "banana", "beer"]
for k in item_list:
    if item_list[k]["item"] in order_list:
        order.append(item_list[k])

print(order)

print("note" in "redmi note 11")

################################################

"""

"""

31. tuple

name                     >>       tuple
definition               >>       immutable list
usage                    >>       (), tuple() ( at least two or more items )
description              >>       1. Access items               --->    indexing ( +, -)
                                                                --->    slicing ( +, -)
                                                                --->    step ( +, -)
                                
                                  

                                   2. loop through a tuple      --->    
                                   3. check if item in tuple    --->    in
                                   4. check not in tuple        --->    not in
                                   5. count items               --->    len()
                                   
                                   6. count specific item       --->    count()
                                   7. search index              --->    index()
                            
                                   8.delete with del keyword   --->     object

                                   9. join tuple                --->    +


Note
                                  
1. if need to change           ---> change to list
2. to remove duplicate values  ---> set()
                   
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
                                   9. clear                     --->    
                            
                                   10.delete with del keyword   --->    object

                                   11. add                      --->    an element
                                   12. update                   --->    elements
                                   
                                   13. difference  / -          --->    return, do not change original value
                                   14. difference_update        --->    not return, update value
                                   
                                   15. union                    --->    return all
                                   
                                   16. intersection             --->    return same value
                                   17. intersection_update      --->    
                                   
                                   18. symmetric_difference     --->    return all except same value
                                   19. symmetric_difference_update
                                   
                                   20. isdisjoint               --->    return True if not same value in two sets
                                   21. issubset                 --->    x in y
                                   22. issuperset               --->    y in x

################################################

33. frozen set

name                     >>       frozenset
definition               >>       frozenset, unordered list, immutable obj
usage                    >>       frozenset{}
description              >>        1. Access items              --->   can not access / change / delete with index position  
                                  
                                   2. loop through a set        --->    
                                   3. check if item in set      --->    in
                                   4. check not in set          --->    not in
                                   5. count items               --->    len()
                            
                                   6.delete with del keyword   --->    object
                                   
                                   7. difference  / -          --->    return, do not change original value
                                   
                                   8. union                    --->    return all
                                   
                                   9. intersection             --->    return same value
                                   
                                   10. symmetric_difference     --->    return all except same value
                                   
                                   11. isdisjoint               --->    return True if not same value in two sets
                                   12. issubset                 --->    x in y
                                   13 . issuperset               --->    y in x

################################################

Solved Examples Using Sets Formulas
Example 1: 
In a club, each person plays chess or carrom or both. 
The number of people who play chess, carrom or both are 11, 12 and 3 respectively. 
Representing this given information as sets and 
using the set formulae,

Q1.  find the people who play either chess or carrom?

p = chess
q = carrom
n(p) = 11
n(q) = 12
n(p ∩ q) = 3
Applying the set formula,  
n(P∪Q) = n(P) + n(Q) - n(P∩Q) = 11 + 12 - 3 = 20

Answer: The number of people who play either chess or carrom = 20


Q2. who like to play chess only
Q3. who like to play chess only


# let each person has club id No.1 or 2 or 3
# 3 person like both of chess and carrom
# let id of 3 person be 1, 5, 7
p = { 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11}
p = frozenset(p)
q = { 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 5, 7}
q = frozenset(q)
#print(len(q))

x = p.intersection(q)# (P ∩ Q)

print("id of people who like both = ", end="")
print(x)
print(len(x))# n(P∩Q)
print()

ans = p.union(q) # (P ∪ Q)
print("id of people who like either chess or carrom = ", end="")
print(ans)
print(len(ans))# n(P∪Q) total person
print()

# who like to play chess only
# p - ( P ∩ Q)
chess = p - x
print("id of people who like chess only = ", end="")
print(chess)
print(len(chess))
print()

# who like to play carrom only
# q - ( P ∩ Q )
carrom = q - x
print("id of people who like carrom only = ", end="")
print(carrom)
print(len(carrom))

################################################

34. Data types      4 left
 
1. Text Type:	str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	    set, frozenset
6. Boolean Type:	bool
7. Binary Types:	bytes, bytearray, memoryview
8. None Type:	    NoneType


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

multiply all
eg . tuple * 2

#####################

Lists and Tuples are ordered sequences of elements.

Python dictionaries are collections of items that are unordered, indexed and mutable.
This means that there is no specific order to the items in a dictionary, 
and they have their own index values (or keys) that can be used to reference individual elements. 

Python sets are unordered collections of elements.
Set values are immutable.
Set elements are immutable but the set itself is a mutable object, 
so in order to make an immutable set, we use the concept of frozenset. 

set1 = {1,2,3, [1, 2]}

################################################

35. Type casting

1. int(x [,base])
Converts x to an integer. base specifies the base if x is a string.

2. long(x [,base] )
Converts x to a long integer. base specifies the base if x is a string.

3. float(x)
Converts x to a floating-point number.

4. complex(real [,imag])
Creates a complex number.

5. str(x)
Converts object x to a string representation

6. repr(x)
Converts object x to an expression string.

7. eval(str)
Evaluates a string and returns an object.

8. tuple(s)
Converts s to a tuple.

9. list(s)
Converts s to a list.

10. set(s)
Converts s to a set.

11. dict(d)
Creates a dictionary. d must be a sequence of (key,value) tuples.

12. frozenset(s)
Converts s to a frozen set.

13. chr(x)
Converts an integer to a character.

x = 97
y = chr(x)
print(y)

14. unichr(x)
Converts an integer to a Unicode character.

15. ord(x)
Converts a single character to its integer value.
print(ord("a"))

16. hex(x)
Converts an integer to a hexadecimal string.
x = 10
print(hex(x))

17. oct(x)
Converts an integer to an octal string
x = 8
print(oct(x))

################################################



"""

"""

OOP  ---> object ( variable, methods )

Major OOP Concepts
# 1. polymorphism
# 2. inheritance 
# 3. encapsulation ( data hiding )
# 4. abstraction

#################################################

# 1. polymorphism        ( + )           ( __add__ )
# 2. inheritance   ( class lb(kg): )     ( __init__ )
# 3. encapsulation    ( __weight )       ( a.weight = 10 )

class kg:
    def __init__(self, w):
        self.weight = w

    def __str__(self):
        return str(self.weight) + " kg"

    def __add__(self, other):
        if "kg" in other.__str__():
            return kg(self.weight + other.weight)
        elif "lb" in other.__str__():
            return kg(self.weight + (other.weight / 2.2))

class lb(kg):
    def __str__(self):
        return str(self.weight) + " lb"

    def __add__(self, other):
        if "lb" in other.__str__():
            return lb(self.weight + other.weight)
        elif "kg" in other.__str__():
            return lb(self.weight + (other.weight * 2.2))

x = kg(1)
y = lb(2.2)

print(f"{x} + {y} = {x + y}")
print(f"{y} + {x} = {y + x}")

a = x + y
b = y + x
print(a + b)
print(b + a)

# a.weight = 10
# print(a)

#################################################

# Data Hiding and Object Printing
1.  __var
2.  _str_
3.  _repr_
4.  print    -->  str  -->  repr  -->  default repr value ( memory address of obj )

#################################################

# weight.py
class kg:
    def __init__(self, w):
        self.weight = w

    def __repr__(self):
        return str(self.weight) + " kg"

    def __add__(self, other):
        if "kg" in other.__str__():
            return kg(self.weight + other.weight)
        elif "lb" in other.__str__():
            return kg(self.weight + (other.weight / 2.2))

class lb(kg):
    def __repr__(self):
        return str(self.weight) + " lb"

    def __add__(self, other):
        if "lb" in other.__str__():
            return lb(self.weight + other.weight)
        elif "kg" in other.__str__():
            return lb(self.weight + (other.weight * 2.2))

if __name__ == "__main__":
    x = kg(1)
    y = lb(2.2)
    print(f"{x} + {y} = {x + y}")
    print(f"{y} + {x} = {y + x}")

#################################################

# not __repr__()

>> from weight import kg, lb
>> x = kg(1)
>> x
<weight.kg object at 0x7b677e51f0>
>> f"{x}"
'1 kg'
>> y = lb(2.2)
>> y
<weight.lb object at 0x7b67748880>
>> x + y
<weight.kg object at 0x7b677488b0>
>>

#################################################

# with __repr__()
>> from weight import kg,lb
>> x = kg(1)
>> x
1 kg
>> y = lb(2.2)
>> y
2.2 lb
>> x + y
2.0 kg
>> y + x
4.4 lb
>>

#################################################

4. Abstraction

Abstract classes are the classes which contains one or more abstract method;

and abstract methods are the methods which does not contain any implemetation,

but the child-class need to implement these methods otherwise error will
be reported.

In this way, we can force the child-class to implement certain methods in it.

#################################################

# abstraction example.1
from abc import ABCMeta, abstractmethod

class Car(metaclass=ABCMeta):
    def __init__(self, b="ABS system brake"):
        self.brake_system = b

    def brake(self):
        print(f"Brake with {self.brake_system}")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class City_car(Car):
    def __init__(self):
        super().__init__()
        self.engine = "city engine"
        self.tire = "city tire"

    def start(self):
        print(f"{self.engine} start.")

    def stop(self):
        print(f"{self.engine} stop.")

x = City_car()
x.start()
x.stop()
x.brake()

# y = Car()

################################################

# abstraction example.2
# crd freecodecamp 
from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price

    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}\nQuantity: {self.quantity}\nAuthor: {self.author}\nPrice: {self.get_price()}\n"

class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def __repr__(self):
        return super().__repr__() + f"Pages: {self.pages}\n"

class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return super().__repr__() + f"Branch: {self.branch}\n"


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 300, 200)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 300, 'IT')

print(novel1)
print(academic1)

# del @abstractmethod
#b = Book("book1", 10, "abc", 10)
#print(b)

################################################

Method Overloading:

Two or more methods have the same name but different numbers of parameters or different types of parameters, or both.
These methods are called overloaded methods and this is called method overloading.

Like other languages (for example, method overloading in C++) do, python does not support method overloading by default.
But there are different ways to achieve method overloading in Python.

The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method.

#################################################

# Python doesn't support Method Overloading by default.

class X:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        print(self.value + other)

    def add(self, other1, other2): # li
        print(self.value + other1 + other2)


a = X(1)
a.add(1, 2) # lifo

#################################################

# Method Overloading by using dispatch decorator
# dispatch = ‌သီးသန့်‌ေနရာ
from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result, "   <--- int 2")

@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result, "   <---  int 3 ")

@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(round(result), "   <---  float 3")

def product(*x):
    t = 0
    for i in x:
        t += i
    print(t)

product(1, 2)
product(1, 2, 3)
product(1.1, 2.1, 3.0)
product(1, 2, 3, 4, 5, 0.1)

#################################################

2. Method overriding ( LIFO )
# override လွှမ်းမိုး

---> derived class method "overrides" the method provided in the base class.

################################################

Design Patterns & Python

What is a Design Pattern?
Design Patterns are concrete solutions for reoccurring problems.
They satisfy the design principles and can be used to understand and illustrate them.
They provide a NAME to communicate effectively with other programmers.

#################################################

1. Iterator Pattern
The essence of the Iterator Factory method Pattern is to 
"Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation."
.

aggregate ( စုပေါင်း )
exposing ( မြင်သာအောင်ပြ )
representation ( ကိုယ်စားပြု )

#################################################

2. Decorator Pattern 
( မူလအရာကို မထိခိုက်ဘဲ  မွမ်းမံနိုင်စွမ်း )
The decorator pattern is a design pattern that 
allows behavior to be added to an existing object dynamically.
behaviour ( အပြုအမူ လုပ်ဆောင်ချက် )

#################################################

3. Strategy Pattern
The strategy pattern (also known as the policy pattern) is 
a particular software design pattern, 
whereby algorithms behavior can be selected at runtime.

#################################################

4. Adapter Pattern
The adapter pattern is a design pattern that 
translates one interface for a class into a compatible interface 

#################################################

# 1. Iterator Pattern
class MyIter():
    def __init__(self, v):
        self.v = v
        self.p = 0

    def __next__(self):
        try:
            value = self.v[self.p]
            self.p += 1
            # print ("Iteration done.")
            return value
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        print("------->   work iter of myiter")
        return self

class My_obj():
    def __init__(self, *items):
        self.items = items

    def __iter__(self):
        print("------->   work iter of myobj")
        return MyIter(self.items)


obj = My_obj(1, 2, 3, "apple", "banana")
for item in obj:
    print(item)

print("- " * 30 )

obj2 = MyIter([1, 2, 3, "apple", "banana"])
for i in obj2:
    print(i)

print("- " * 30 )

for i in "abcdefg1436":
    print(i)

#################################################    
    
# 2. Decorator Pattern 
class UnderlineWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return "<u>{}</u>".format(self.obj.render())

class ItalicWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return "<i>{}</i>".format(self.obj.render())

class BoldWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return "<b>{}</b>".format(self.obj.render())

class HeaderWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return "<h1>{}</h1>".format(self.obj.render())

class WrittenText:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

x = WrittenText("Myself")
z = BoldWrapper(x)
print(z.render())

y = ItalicWrapper(UnderlineWrapper(BoldWrapper(x)))
print(y.render())

bu = HeaderWrapper(BoldWrapper(UnderlineWrapper(x)))
print(bu.render())

print(x.render())

#################################################

# 3. strategy pattern
# runtime မှာ ရွေးချယ် လုပ်နိုင်စွမ်း

class IR_system:
    def __init__(self):
        self.sensor = "Electro optical targeting system(IR)"

    def search_target(self):
        print(f"{self.sensor} search infrared radiation of the target.")
        
class Radar_system:
    def __init__(self):
        self.sensor = "APG-81"

    def search_target(self):
        print(f"{self.sensor} search high frequency electro-magnetic waves that are reflected of the target.")

class Projectile:
    def __init__(self, system):
        self.system = system

    def search_target(self):
        self.system.search_target()

class IR_missile(Projectile):
    def __init__(self):
        self.system = IR_system()

class Radar_missile(Projectile):
    def __init__(self):
        self.system = Radar_system()

missile1 = IR_missile()
missile1.search_target()

missile2 = Radar_missile()
missile2.search_target()

#################################################

# 4. adaptor pattern

class IR_system:
    def __init__(self):
        self.sensor = "Electro optical targeting system"

    def search_target(self):
        print(f"{self.sensor} search infrared radiation of the target.")

class Radar_system:
    def __init__(self):
        self.sensor = "APG-81"

    def search_target(self):
        print(f"{self.sensor} search high frequency electro-magnetic waves that are reflected of the target.")

class Projectile:
    def __init__(self, system):
        self.system = system

    def search_target(self):
        self.system.search_target()

class IR_missile(Projectile):
    def __init__(self):
        self.system = IR_system()

class Radar_missile(Projectile):
    def __init__(self):
        self.system = Radar_system()

# adapter pattern
class Gps_adapter:
    def __init__(self, missile):
        self.missile = missile
        self.sensor = "GPS system"

    def search_target(self):
        print(f"{self.sensor} will guide missile.")
        self.missile.search_target()

class IR_adapter:
    def __init__(self, missile):
        self.missile = missile
        self.sensor = IR_system()

    def search_target(self):
        self.missile.search_target()
        self.sensor.search_target()

missile1 = IR_missile()
missile1.search_target()

missile1 = Gps_adapter(missile1)
print("- " * 30)
missile1.search_target()

missile2 = Radar_missile()
print("- " * 30)
missile2.search_target()

missile2 = Gps_adapter(missile2)
print("- " * 30)
missile2.search_target()
print("- " * 30)

# decorator
r_ir = Gps_adapter(IR_adapter(Radar_missile()))
r_ir.search_target()
print("- " * 30)

"""
