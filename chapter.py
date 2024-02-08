
"""

2.1

name                     >>       int, integer, integer literal
definition               >>       integer
                                  
usage                    >>       directly use
description              >>       mathematical operation

################################################

name                     >>      str, string, string literal
definition               >>      charactor string
                                  
usage                    >>      ' ',  " ", '''  ''', """  """
description              >>      47 methods (upper, lower), 
                                 concatination ( + ), 
                                 * ( n th times )

notes
1. class
2. error
3. literal

################################################

2.2

name                     >>       variable, identifier, label
definition               >>       ကိုယ်စားပြုအမည်
                                  Identifier  ( for all ) ( function, class, method)
                                  variable ( for values )
usage                    >>       =
description              >>       Python has five rules for naming idenfiers. ( one, alpha, number, o, r )
                                  1. An identifiers must contain at least one character.
                                  2. The first character of must be an alphabet or the underscore.
                                  3. The remaining characters may be alphabets, underscores, numbers.
                                  4. Qther characters are not permitted.
                                  5. A reserved word cannot be used as an identifier.


################################################

2.3

name                     >>       assignment operator
definition               >>       assign right ( value ) to left ( identifier )
usage                    >>       =
description              >>       += , -=, *=, /=  မူလတန်ဖိုးကိုပဲ ထပ်ပေါင်းချင်ရင်သုံး


################################################

Note
1. keyword.kwlist

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']

2. tuple assign

################################################

2.4

name                     >>       float, floating-point number
definition               >>       number with .  
usage                    >>       .
description              >>       1. continuous values 17
                                  2. store by 1/10                   --> 0.1 = 1/10
                                  3. int and float are different data types.
                                     so, they can not make operation directly.   
                                     ( before operation, py changed int to float )

                                  4. rounding adds or subtracts to produce closest value
                                         >> round(float)
                                            --> one argument value       --> int
                                            --> two                      --> float                       <----------
                                                ( second arg may be positive(r) or negative(l) )

                                         >> round(int)
                                            --> one argument value       --> int   ,   original value
                                            --> two                      --> int                         <----------
                                                ----> positive second arg      --> original value
                                                ----> negative                 --> round value

                                  5. truncation to drop fractional part
                                         >> int()

note

1. scientific notation for exponent ( e ) ( e1 = 10, e2 = 100 )     -->   1e-10, 1e10 
2. predefined data type ( not for py )
   16bit = 2**16 = 65536 ( 32768 to - 32767 )
3. sys.getsizeof()
4. sys.floatinfo
   --> min , max
5. bin()

################################################

2.5

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

11. unicode name                   --->       N{}
12 . hexadecimal                   --->       x00
13 . hexadecimal value             --->       u0000
     of unicode  ( 16 bit)
14 . hexadecimal value             --->       U00000000
     of unicode  ( 32 bit)
15 . octal value                   --->       000



( 97 ( 141, 61))

################################################

2.6


name                     >>       input
definition               >>
usage                    >>       input()
description              >>       receive input data as str

note
1. int()
2. float()
3. print()
4. root2        --->      **1/2
   root3        --->      **1/3


################################################

2.7

name                     >>       print
definition               >>
usage                    >>       print()
description              >>       1. print str value
                                  2. unlimited input data with ,
                                  3. positional arguments,
                                  4. keyword arguments      --->   by name
                                     for print()            --->   end, sep, file, flush ( in time )

                                                 
note
1. open()

################################################

2.8

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

################################################

2.9 

name                     >>       multiline string, preformatted string
definition               >>
usage                    >>       """   """    ,    '''   '''
description              >>       auto complete \n

################################################

################################################

3.1

name                     >>       expression
definition               >>       mathematical expression, arithmetic expression
usage                    >>       **, * /, + - , =
description              >>       1. simple expression       --->  x = 1
                                  2. complex expression      --->  x = 1 + 2
                                  

name                     >>       arithmatic operator
definition               >>       
usage                    >>       **, * /, + - 
description              >>       1. binary operator          --->  x = 1 - 2
                                  2. unary operator           --->  x = -1
                                  3. precision value          --->  float  
                                  4. error with /             --->  1 - 1/3 -1/3 -1/3

################################################

3.2

name                     >>       mixed type expressions
definition               >>
usage                    >>       make by py
description              >>       int + float and etc.
                                  1 + 0.1
                                 
                                 
################################################                                                            
                                                           
3.3

name                     >>       operator precedence and associativity ( right or left )
definition               >>      
usage                    >>      
description              >>       p, u, e, * / , + -, =
                                  1. parenthesis                   --->   ( )
                                  2. unary minus, unary plus       --->   -1, +1
                                  3. exponent                      --->   **                     --->   Right sided bind     --->   2 ** 2 ** 3
                                                                                                                                    2 ** (2 ** 3)
                                                                                                                                    2 ** 8
                                                                                                                                    256
                                  4. multiplication, division      --->   *, /, //, % 
                                  5. addition, substration         --->   +, -
                                  41. assignment                    --->   =                      --->   Right sided bind     --->   x = y = z = 1


################################################

3.4
 
name                     >>       formatting (  expression )
definition               >>       x, y, z in expression
usage                    >>       
description              >>       3x2 + 2xy - 5       --->   3*(x**2) + 2*x*y - 5

x = n1 + n2              
################################################
                                
3.5
                                 
name                     >>       comment   
definition               >>       
usage                    >>       #
description              >>       python will ignore all lines with the first charactor #

                                                         
################################################

3.6                                

name                     >>       errors
definition               >>
usage                    >>       
description              >>       1. syntax error            --->   1name = "Mg Mg"    
                                  2. runtime error           --->   first_name = "Mg Mg"; full_name = first_name + last_name 
                                  3. logical error, bug      --->   print(f'x / y = {int(input("x = ")) / int(input("y = "))}')


################################################

3.7   hour min sec                                                           

name                     >>       
definition               >>
usage                    >>       
description              >>       
                                 
################################################

3.8                                                             

name                     >>       41 operators   
definition               >>
usage                    >>       
description              >>       
                                 
################################################

3.9                                                      

name                     >>       algorithums  
definition               >>       planning, creating rules and regulations
usage                    >>       pseudo code 
description              >>       pseudo code
                                  1. receive F
                                  2. calculate C
                                  3. show result

                                                    
################################################

3.10   Exercises,

################################################

4 . Conditional Execution

note
1. linear sequence, nonlinear sequence

################################################

4.1, 4.2

name                     >>       boolean, Boolean Expressions
definition               >>       George Boole ( 1815 ---> 1864, the law of thought )
usage                    >>       True, False
description              >>       1. expression with boolean result  
                                     --->   x = True, x = 1 < 2
                
################################################

4.3 The Simple if Statement

name                     >>       if     
definition               >>       translate with conditions
usage                    >>       if conditions:
description              >>       1. If condition is true, translate the conditional code (block of codes)
                
Note
Example . 1, 2,3


if 1 < 2:print("1 is less than 2.")

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

4.4 The if/else Statement

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

4.5 Compound Boolean Expressions

notes
1. boolean operator       --->   and, or, not
2. operator precedence    --->   p, u, e, */, +-, 
                                 < > ==, not, and, or,
                                 =
3. operator asociativity  --->   left to right

################################################

4.6

name                     >>       pass Statement 
definition               >>       to pass 
usage                    >>       pass
description              >>       use for incomplete code block


n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
if n1 < n2:
    pass
    
else:
    pass


################################################

4.7 Floating-point Equality 

note

compare to 3rd of floating points  --->  1 - 1/3 -1/3 -1/3 == 0   --->    round(1 - 1/3 -1/3 -1/3, 3) == 0 

################################################

################################################

4.8 Nested Conditionals 

notes

if condition:
    pass

else:
    pass



################################################

4.9 Multi-way Decision Statements

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

4.10 Multi-way Versus Sequential Conditionals

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

4.11 Conditional Expressions  ( if else tenary operator )

notes


x = int(input("x = "))

even_odd = "even" if x % 2 == 0 else "odd"

print(f"{x} is {even_odd}.")


################################################

4.12 Errors in Conditional Statements

1. tautology                --->   ever true       --->   > 1 or  < 10        --->   answer  - >  and
2. contradiction            --->   ever false      --->   < 1 and  > 10       --->   answer  - >  >, <

################################################

4.13 Logic Complexity

"""
c1 = True
c2 = True
c3 = True

if c1 and c2 and c3:
    print("All are True.")


if c1 or c2 or c3:
    print("At least one is true.")

c1 = 0
c2 = 0
c3 = 0

# ?
if not(c1 and c2 and c3):
    print("All are false.")



c1 = True
c2 = True
c3 = 0

#?
if not(c1 or c2 or c3):
    print("At least one is fasle.")



# c1, c2, not c3
# c1, not c2, c3
# not c1, c2, c3

# order
# must do ---> name, color, size, item count,
# choose one ---> bank card or cash on delivery

# delivery
# must do ---> address confirm, ph No confirm

name = input("Item name : ")
color = input("Item color : ")
size = input("Item size : ")
count = input("Item count : ")
bank_card = input("card payment confirm : ")
cash_on_delivery = input("COD confirm : ")

orders = []
delivery_items = []
card_or_cod = bank_card if bank_card else cash_on_delivery
order = name and color and size and count and (bank_card or cash_on_delivery)
if order:
    new_order = [name, color, size, count, card_or_cod]
    orders.append(new_order)
    address = input(f"Please confirm address and ph No for {new_order} : ")
    if address:
        delivery_items.append([new_order, address])
        print(f"{new_order} will be send to {address} by delivery partner kerry in one week.")


"""
################################################

################################################


5.1 The while Statement 
5.2 Definite Loops vs. Indefinite Loops 
5.3 The for Statement
5.4 Nested Loops 

5.5 Abnormal Loop Termination 
>>>   5.5.1 The break statement 
>>>   5.5.2 The continue Statement 

5.6 while/else and for/else 
5.7 Infinite Loops

5.8 Iteration Examples
>>>   5.8.1 Computing Square Root 
>>>   5.8.2 Drawing a Tree 
>>>   5.8.3 Printing Prime Numbers 

>>>   5.8.4 insisting on proper input




x = input("Enter integer : ")
c = 1
while not x.isdigit():
    if c > 5:
        print("Exceed 5 times.")
        break
    x = input("Enter integer : ")
    c += 1

else:
    print("correct")


x = input("Enter integer : ")
c = 1
while not x.isdigit():
    x = input("Enter integer : ")
    c += 1
time_s = "time" if c == 1 else "times"
print(f"You tried {c} {time_s} to input proper data.")





x = input("Enter integer : ")
c = 1
while not x.isdigit():
    if c >= 5:
        print("Exceed 5 times.")
        break
    x = input("Enter integer : ")
    c += 1

else:
    print("correct")


for c in range(1, 6):
    x = input("Enter integer : ")
    if x.isdigit():
        print("correct")
        break

else:
    print("Exceed 5 times.")






##########################################

##########################################

Chapter . 6  ( Using Functions )

6.1 Introduction to Using Functions
notes
1. pip install
2. import
3. using function

#####################

6.2 Functions and Modules

function >> block of codes
module >> block of functions (  .py )

#####################

6.3 The Built-in Functions / user defined functions

notes
1. dir ( လမ်းညွှန် ) ဘာမှမထည့်ရင် လက်ရှိဖိုင်ကိုပြ 
2. _builtins_.print()

['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 
'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 
'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 
'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 
'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 
'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 
'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 
'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 
'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 
'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 
'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', 
'__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 
'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 
'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 
'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 
'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 
'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 
'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

#####################

6.4 Package
package >> block of modules ( folder )
1. internal package
2. external package

#####################

6.5 Techniques for Importing Functions and Modules 

import လုပ်နည်း
1. import math  ( normal import )
2. import math as m  ( normal import with identifier )

3. from math import sqrt( specific import )
4. from math import *  ( all )

#####################

chapter.7  ( writing function )
1. function definition 
name                 -->      definition, creating, writing 
definition           --> 
usage                -->      def
description 
1. def
2. name    ( +-*/ ရေးခိုင်း )
3. parameters  ကန့်သတ်ချက် / စည်းမျဉ်း
4. body
5. return
6. docstring

2. function invocation 
invoke, call, use
()
help

chapter.7 exercises

x နှင့် y တန်ဖိုးနှစ်ခုလက်ခံပြီး 

x + y တန်ဖိုး ပြန်ပေးမည့်

 add ဟူ၍ အမည်ရှိသော function တစ်ခုတည်ဆောက်ပါ။

docstring အဖြစ် အောက်ပါစာကို ထည့်ပါ။

It is a adding function of two numbers.
It will return x + y.
eg.   add(1,2) == 3



def add(n1, n):
    ans = n1 + n2
    return ans


x = add()
print(x)


#####################


Chapter . 8 >> More on Functions

8.1.1 Global Variables ( global scope )
global ဖိုင်တစ်ခုလုံးနဲ့ဆိုင်

8.1.2 local လက်ရှိနေရာမှာပဲဆိုင် ( local scope )

global vs local နာမည်တူရင်ဘာဖြစ်မလဲ
>> precedence ---> local
>> in local scope, we can use loacl variable only


8.1.3 အပြင်က global တန်ဖိုးကို function နဲ့ပြင်ချင်ရင် ဘာကိုသုံးရမလဲ။ ( global keyword)

x = 1

def change_value_of_X():
    global x
    x += 1

change_value_of_X()
print(x)
change_value_of_X()
print(x)

8.2 Default Parameters ပျက်ကွက်လို့ရသော စည်းမျဉ်း
default value ပျက်ကွက်လျှင် ဖြစ်မည့်တန်ဖိုး



def add(n1, n2=0):
    ans = n1 + n2
    return ans


x = add(10)
print(x)


8.3 Introduction to Recursion 
function က သူ့ဘာသာပြန်ခေါ်ပြီး
ထပ်ကာထပ်ကာအလုပ်လုပ်အောင်ရေးထားတဲ့ function


def x(n):
    print(n)
    if n:x(n-1)


def x2(n):
    print(n)
for i in range(10, -1, -1):
    x2(i)

x(10)

ကျန်နေ

8.4 Making Functions Reusable 
8.5 Functions as Data


def add(n1, n2):
    return n1 + n2

print(add(1, 2))




8.6 Lambda Expressions
(nameless function )

c = 1
if c == 1:
    x = "time"
else:
    x = "times"

x = "time" if c == 1 else "times"


def add(n1, n2):
    return n1 + n2

add2 = lambda n1, n2: n1 + n2

print(add(1, 2))
print(add2(1, 2))

8.7 Generators  ---> yield

x = [1, 2, 3, 4, 5]
for i in x:
    print(i)

for i in range(1, 6):
    print(i)



8.8 Local Function Definitions

x = 1
def f():
    y = 1


def add(n1, n2):
    return n1 + n2
    
def calculate():
    def add(n1, n2):
        pass
        
    

8.9 Decorators


#####################

#####################

Chapter.9
Objects
9.1 Using Objects
1. create  --->  =
2. where   --->  RAM, . . .

x = 1
s = "a"
f = open("mydata.txt", "w")


9.2 string object
creating  -->      '  ', "  ", '''   ''', """   """
                   str()
                   
idexing
x = "apple"
x[0], x.__getitem__(0)

length
len(x), x.__len__() 

        
#class
creating, define, identify 

1. data
2. method

x = 1
x + y, x.__add__(y)
x * 10, z = x.__mul__(10)



9.4 fraction object
name           ---> fraction
dfinition
usage          ---> fraction.Fraction()
description    ---> numerator, denominator, +,  *, /


9.5 Turtle Graphics Objects
name           ---> turtle 
dfinition
usage          ---> turtle.Turtle(), turtle.Screen()
description    ---> 
Turtle object
1. speed(int)
2. pencolor("lightgrey"), pensize(int), penshape(str)
3. left(degree), right()
4. penup(), pendown()
5. setpos(x, y)  ---> 
6. forward(pix),backward()
7. home()
8. write("str value"), write(self, arg, move=False, align='left', font=('Arial', 8, 'normal'))
9. setheading(degree)   --->  
10. circle(radius)
11. shape(shape), 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.

Screen object
1. setup(l,w)
2. bgcolor("gray")
3. title(str)
4. bgcolor("orange")

import turtle
x = turtle.Turtle()
x.write()
print(help(x))



#####################

 
 
9.6 Graphics with tkinter Objects 
numeric_data_type.1
notes
1.binary number       0,1
2.decimal number      0,1,2,3,4,5,6,7,8,9
3.octal number        0,1,2,3,4,5,6,7
4.hexadecimal number  0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
5. int  ---> int()
6. bin   ---> bin()
7. oct   ---> oct()
8. hex  ---> hex()


#####################

numeric converter 1 & 2

1.Label
2.Entry                --->   get, delete, insert
3.Button, Checkbutton  --->   command
4.IntVar, ...          --->   variable in python
                              1. x = int()
                              2. x = 1
                     
                              variable in Tk
                              1. x = IntVar()
6.grid, pack
7.mainloop
 
#####################

name        --->   numeric converter
Note
1.mybin()   --->   decimal to binary
  >>   z = ""
  >>   d != 0
  >>   d % 2
  >>   d = d // 2
  
2.myoct()   --->   decimal to octal
  >>   z = ""
  >>   d! = 0
  >>   d % 8
  >>   d = d // 8
  
3.myhex()   --->   decimal to hexadecimal
  >>   z = ""
  >>   d! = 0
  >>   d % 16 == 10: z += "a"
  >>   d % 16 == 11: z += "b"
  >>   d % 16 == 12: z += "c"
  >>   d % 16 == 13: z += "d"
  >>   d % 16 == 14: z += "e"
  >>   d % 16 == 0
  >>   d = d // 16
  
#####################

name         --> traffic light object
definition   --> GUI
usage        --> tkinter.Tk()
description  -->

1.canvas(root,w,h)
2.pack()
3.create_rectangle(root, y, x, y),create_oval(x,y, x,y), create_text()
4.itemconfigure(item, text/color = ... )
5.after(1000,count, var)

#####################

name        ---> BMI
definition  ---> Body Mass Index 
usage       ---> 
description ---> BMI = kg / m**2
note
1.cm = total_inches * 2.54
2.m  = cm / 100
3.kg = lb * 0.45
4.BMI = kg / ( m**2 )


#####################

#9.7 Other Standard Python Objects
object
1.data   - variable
2.method - function

#####################

#9.8 Object Mutability and Aliasing
Aliasing
name        --> Aliasing
definition  --> pointing one object like name and nickname 
usage       --> = 
description --> 
1. = is creating object
2. x = str("Myo Thant Zin")
   x is the address of MyothantZin
   print(x)
   print(id(x)) 

3. x = str("Myo Thant Zin") # myothantzin
   y = x #phoethargyi
   z = y #abc
   print(id(x))
   print(id(y))
   print(id(z))
   x, y, z address are same
   
note
1. id()

#####################

name        --->   immutable object
definition  --->   object that cannot change
usage   
description --->   interger,string, tuple

#####################

name        --->   mutable object
definition  --->   object that can change
usage   
description --->   tkinter, turtle, list


#####################


name        --->   list, heterogeneous list (mixed different types of object)
defination  --->   list
usage       --->   list(), [1, 2, 3]
descrition  ---> 

1. mutable object, iterable object
2. indexing           --->   1. l[positive index]
                             2. l[negative index]
                                l.__getitem__(index)
3. slicing            --->   l[start : stop : step]
4. append()
5. assigning /
   changing values    --->   =
                             l[index] = value 
                             l.__setitem__(index, value)
6. parallel assigning --->   l[0],l[1],l[2] = 3, 2, 1
                             l[0:3] = 3, 2, 1
7. swap               --->   l[0], l[1], l[2] = l[2], l[1], l[0]
9. looping            --->   for

   >> for i in l:
          print(i)
   
   >> for i in range(0,len(l), 1): 
          print(l[i])
   
   >> for i in range(len(l)-1, -1, -1):
          print(l[i])
   
   >> for i in reversed(l):
          print(i)

#####################


#####################

name                --->    generator
usage               --->    yield
description         --->    list()                         <---   generator to list       
                    --->    tuple(), set(), dict()
                    --->    ()                             <---    lc to generator
                            >>   [0, 1, 2, 3, 4]           <---    list
                            >>   [i for i in range(5)]     <---    list ( conprehension )
                            
                            >> g = (i for i in range(5))   <---    generator ( conprehension )
                            >> def g():                    <---    generator
                                   for i in range(5):
                                       yield i
                            
#####################

1.color codes       --->    "\033[_;_;_m"    
                    --->    "\033[text style;text color;background color m"
                    --->    text style           -->   0, 1(bold) , 2(under line), 3(negative.1), 5(negative.2)
                    --->    text color           -->   30 to 37 ( b, r, g, y, b, p, c, w )
                    --->    background color     -->   40 to 47 ( b, r, g, y, b, p, c, w )

#####################


list comprehension
1.regular list conprehension       <---   loop, nested loop
2.parallel list conprehension      <---   loop, nested loop ( zip )

#####################

Why should be used lc?

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]      <---   easy to create   

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140,
141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164,
165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188,
189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212,
213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236,
237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 
285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 
309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 
333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 
357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 
381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 
405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 
429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 
453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 
477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 
501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 
525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 
549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 
573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 
597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 
621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 
645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 
669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 
693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 
717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 
741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 
765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 
789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 
813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 
837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 
861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 
885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 
909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 
933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 
957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 
981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]


l = list()
for i in range(1, 1001):
    l.append(i)
print(l)


l = [i for i in range(10000001)]


1. if we use much data, it is hard to create.
2. so, we use loop. 
3. loop is a little long.
4. so, we use list comprehension.

#####################

Why should be used generator?

1. if we use much data, it is hard to store in RAM. 
2. RAM can not store much data. 
3. generator do not use much memory.
3. if we can handle one by one, we use generator. 

g = (i for i in range(10000001))
print(g.__next__())

#####################

note
>>   if else   <---  tenary operator / conditional expression

#####################


"""
