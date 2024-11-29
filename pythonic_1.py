
"""

1. course overview
   1.1.What is Python?
   1.2.Python Basics

2. Data types ( built-in , custom )
   2.1.Groups of built-in data type
   2.2.imaginary(i)
   2.3.complex number example
   2.4.Explanation about built-in data type
   2.5.Notes
   2.6.exercises

3. more about data types
   3.1.sequence type
   3.2.dynamic type, static type
   3.3.Type casting
   3.4.indexing, slicing
   
4. Pythonic ( clean, readable python code )
   4.1.Coding Style
   4.2.five rules for naming identifiers
   4.3.variable, identifiers, labels 
   
################################################

1. course overview

################################################

1.1.What is Python?
Python is a high-level, interpreted programming language.

It uses line-by-line execution (interpreted) and processes code from top to bottom, left to right, 
and respects syntax rules like parentheses ().

->    translate, interpreter
->    line by line
->    from top to bottom, left to right, parenthesis ( )

work.1
work.2
work.3

work.1(work.4); work.2(work.5(work.6)); work.3

################################################

1.2.Python Basics

1. data type
2. control flow
3. function
4. OOP
5. FP
6. Algorithm
7. design patterns

Advanced Python
Builds on the basics with 10x more depth in knowledge and practical applications.

################################################

1. data type
-> built-in 15
-> custom / user-defined data types

################################################

2. control flow
-> operators ( 41 )
-> Loops and conditional statements ( while, if, for )
-> practice (water motor, tac ti toe, calculator)

################################################

3. function
-> using built-in functions
-> rewriting built-in functions for better understanding
-> creating custom functions for specific tasks

################################################

4. OOP
-> objects & classes, relationships between objects ( inheritance, polymorphism, ... )
-> exercises
-> practice (chess game , django framework)

################################################

5. FP
-> programming paradigms ( imperative & declarative )
-> fundamentals concepts ( map, filter, iterator, recursion, .. )
-> control flow in FP ( functional methods to simplify loops and conditions )
-> exercises with FP concepts

################################################

6. Algorithm
-> basics of algorithm design and analysis
-> use cases in data structures
-> problem solving & optimisation

################################################

7. design patterns -> 23

-> Creational Patterns: 5
    -> singleton
         application တစ်ခုမှာ setting object တစ်ခုပဲရှိသင့်တာမျိုး ၊ class တစ်ခုကို object တစ်ခုသာ ဖန်တီးခွင့်ပေးတာမျိုး
         Ensures a class has only one instance, e.g., a settings object for an application.

-> Structural Patterns: 7
     ->  decorator
          မူရင်း data မထိခိုက်ဘဲ update လုပ်နိုင်အောင် ပုံစံချ
          Allows functionality to be added without altering the original object.

-> Behavioral Patterns: 11
     -> iterator
         မူရင်း data မထိခိုက်ဘဲ access ပြုလုပ်နိုင်စွမ်း
         Provides a way to access elements of a collection without modifying the underlying data.

################################################
################################################

2. Data types ( built-in , custom )

2.1.Groups of built-in data type

1. Text Type:            str
2. Numeric Types:        int, float, complex
3. Sequence Types:       list, tuple, range
4. Mapping Type:         dict
5. Set Types:            set, frozenset
6. Boolean Type:         bool
7. Binary Types:         bytes, bytearray, memoryview
8. None Type:            NoneType

################################################

step.1 -> know
step.2 -> handle ( create, access, update, delete )
step.3 -> create new data types ( kg, lb, dollar, kyats )

################################################

2.2.imaginary(i)

# complex number -> 3 + 2i ->  3 + 2j
# i = imaginary = root(-1)

x2 − 2x + 2 = 0.

x = ( 2 ± root(-4) ) / 2   <--- root(-4) = root(4) * root(-1) = 2 * i = 2i

x =( 2 ± 2i ) / 2

x = 1 ± i

x = 1 + i and x = 1 − i

################################################

-> 3 + 2 j  # (x, y) move 3 steps right and 2 step up
-> -3 + 2 j  # (x, y) move 3 steps left and 2 step up
 .                 .

 .  .  .  .  .  .  .
          0  1  2  3

 .                 .
################################################

2.3.complex number example

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.axhline(y=0, color='black')
ax.axvline(x=0, color='black')

c1 = -3 + 2j   # pythagorean theorem = 9 + 4 = 13 = 3.61 from original point(0, 0)
ax.plot(c1.real, c1.imag, 'ro')  # 'ro' = red circle
ax.text(c1.real + 0.2, c1.imag, f'{c1}', fontsize=12, color='green')

c2 = -3 - 2j
ax.plot(c2.real, c2.imag, 'ro')  # 'ro' = red circle
ax.text(c2.real + 0.2, c2.imag, f'{c2}', fontsize=12, color='red')

c3 = 3 + 2j
ax.plot(c3.real, c3.imag, 'ro')  # 'ro' = red circle
ax.text(c3.real + 0.2, c3.imag, f'{c3}', fontsize=12, color='red')

c4 = 3 - 2j
ax.plot(c4.real, c4.imag, 'ro')  # 'ro' = red circle
ax.text(c4.real + 0.2, c4.imag, f'{c4}', fontsize=12, color='red')

c5 = c3 - 2
ax.plot(c5.real, c5.imag, 'ro')  # 'ro' = red circle
ax.text(c5.real + 0.2, c5.imag, f'{c5}', fontsize=12, color='red')

c6 = c3 + 1j
ax.plot(c6.real, c6.imag, 'ro')  # 'ro' = red circle
ax.text(c6.real + 0.2, c6.imag, f'{c6}', fontsize=12, color='red')

c6 = -4 + 4j
ax.plot(c6.real, c6.imag, 'ro')  # 'ro' = red circle
ax.text(c6.real + 0.2, c6.imag, f'{c6}', fontsize=12, color='red')

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_xlabel('Real Numbers (Left/Right)')
ax.set_ylabel('Imaginary Numbers (Up/Down)')
ax.grid(True)
plt.show()

################################################

2.4.Explanation about built-in data type

1. Text Type   
str -> sequence of characters

2. Numeric Types      
int -> integer value
float -> number with floating-point
complex -> number with j, real part & imaginary part

3. Sequence Types      
str -> sequence of characters
list -> ordered collection of elements. ( mixed data types )
tuple -> ordered collection of elements
range -> sequence of numbers
# range    --->   range(start=0, stop=10, step=1)
# generate a sequence of number

range(10)  
-> range(start=0, stop=10, step=1)  
-> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(1, 10)  # 1, 2, 3, 4, 5, 6, 7, 8, 9
range(1, 10, 2)  # 1, 3, 5, 7, 9
range(2, 101, 2)  # 2, 4, 6, ...., 100
range(100, 1, -2)  # 100, 98, 96, ..., 4, 2

4. Mapping Type   
dict -> key-value pairs

5. Set Types -> unordered collections of unique elements      
set -> mutable, unordered collections of unique elements
frozenset -> immutable version of a set

6. Boolean Type       
bool -> logical values

7. Binary Types -> to store binary data    
bytes -> immutable sequence of bytes ( b"Hello" )
bytearray -> mutable sequence of bytes ( bytearray(b'Apple') )
memoryview -> allows manipulation of memory of a binary object without copying it  
-> memoryview(a)
-> <memory at 0x104d3cdc0>
immutable, mutable, direct access & do not copy

8. None Type -> represents the absence of a value or a null value
NoneType

9. Callable Types -> special types of objects that can be called like functions
functions
methods
classes
lambdas

################################################

2.5.Notes

1. Text Type:            str
2. Numeric Types:        int, float, complex
3. Sequence Types:       list, tuple, range
4. Mapping Type:         dict
5. Set Types:            set, frozenset
6. Boolean Type:         bool
7. Binary Types:         bytes, bytearray, memoryview
8. None Type:            NoneType

1. single quotes, double quotes, triple quotes -> ' ', " ", '''  ''', """ """

2.a. number -> 1, 2, 3, -1, -2, 0
2.b. number with floating-point -> 12.5, 1.25, 0.125, -12.5, 1.
2.c. number with j
-> 3 + 2 j  # (x, y) move 3 steps right and 2 steps up

3.a. square brackets [ ]
3.b. parentheses ( ), comma separated value -> 1, 2, 3
3.c. range()

4. curly braces { }, colon :

5.a. curly braces { } , at least one value without colon
5.b. frozenset()

6. True, False,  Boolean expression -> 1 < 2

7.a. b"apple"
7.b. bytearray(b'apple')
7.c. memoryview(b"apple")
# <memory at 0x1005f2080>

8. None

################################################

2.6.exercises

b'apple'
bytearray(b'apple')
memoryview(b"apple")
# <memory at 0x1005f2080>
'1000'
"1000"
'''1000'''

3 + 2j
1j
1000
0
1000.0
["apple", "banana", "orange"]
[]
list()
()
tuple()
("Mg Mg", 20, 5.5)
range(10)
{"name": "Mg Mg", "age": 20, "height": 5.5}
{
    "name": "Mg Mg",
    "age": 20,
    "height": 5.5
}
{"apple", "banana", "orange"}
{}
set()
frozenset()
frozenset({'apple', 'orange', 'banana'})  # frozenset
frozenset(['apple', 'orange', 'banana'])
frozenset(('apple', 'orange', 'banana'))

1000
0
int()
True
False
bool()
None

{}
{1, }

(1)
("apple")

(1,)
("apple",)
1, 2, 3
1,

"1000"
str(1000)

1000
int("1000")

1000.0
float(1000)
float("1000")

x = {}
print(x)
print(type(x))

################################################

# boolean value exercise

0
0.0

1
1000
12.5
0.1
0.000001

{}  # empty dict
set()  # empty set
[]  # empty list
()  # empty tuple
frozenset()  # empty frozenset
""  # empty str
''
""""""
''''''
b""
bytearray(b"")

################################################
################################################

3. more about data types

3.1.sequence type

list
->   homogeneous(same) sequence of element
->   ["apple", "banana", "orange"]     <-   fruits
->   numbers = [1, 2, 3]               <-   numbers

tuple    
->   heterogeneous sequence of element    
->   ("Mg Mg", 20, 5.5)            <-   name, age, height
->   coordinates = (1, 2, 3)       <-   x, y, z

range    
->   sequence of number                    (1, 2, 3, 1 000 000)

################################################

3.2.dynamic type, static type

dynamic type 

->  allows variables to change types during runtime

x = 1
x = 2
x = "apple"  # new data type

static type
x = 1
x = 2  # same data type

################################################

3.3.Type casting

1. implicit type casting 
-> type casting by py, indirect type casting
-> float, boolean value

2. explicit type casting 
-> type casting by programmer, direct type casting
-> int(2.9)

################################################

implicit type casting ( float )

ans = 1 + 1.6
print(ans)

################################################

explicit type casting ( float )

float to int
1. truncate, int 
->  1 + int(1.6)    --->  1 + 1  = 2
2. round         
->  1 + round(1.6)  --->  1 + 2  = 3

int to float  
->  float(1) + 1.6  --->  1.0 + 1.6 = 2.6

################################################

implicit type casting ( Boolean )

True result
int, float --->  not zero
group      --->  str, list, tuple, dict, set, ... ---> not empty

False result
zero, empty

################################################

3.4.indexing, slicing

################################################

indexing

"abcdefg"
a  b  c  d  e  f  g
0  1  2  3  4  5  6
7  6  5  4  3  2  1 -

total = 7
range ---> -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6
 
-> -t, ..., t-1

-> positive index, negative index
-> total - abs(easy)

middle element
odd  ---> t // 2
even ---> rm -> t // 2, 
          lm = rm - 1

################################################

slicing

-> start, stop, step
-> left to right -> + 
-> right to left -> - 

f5 = x[:5]
l5 = x[-5:] 
r = x[::-1]

"abcdefg"
a  b  c  d  e  f  g
0  1  2  3  4  5  6  positive index
7  6  5  4  3  2  1  negative index

l5 = x[-5:]  
l5r = x[-1:-6:-1]
l5r = l5[::-1]
r = x[::-1]
f5 = x[:5]
f5r = x[4::-1]

total = odd
start = m - n // 2
stop = m + n // 2 + 1

total = even
start = m - n // 2
stop = m + n // 2

m = x[start:stop]
print(m)

mr = m[::-1]
print(mr)

################################################
################################################

4. Pythonic ( clean, readable python code )

4.1.Coding Style
1. 4 space, no tab
2. not exceed 79 characters                                                                         
3. blank lines, 2, 1
4. comment, #
5. docstrings
6. space ---> operator --> l, r / comma, colon --> r
7. UpperCamelCase ---> class name
8. lowercase_with_underscores  ---> function, method, variable
9. self  --->   first parameter of method  ( other )
10. UTF-8
11. identifier ---> ASCII

################################################

4.2.five rules for naming identifiers
( one, alpha, number, o, r )
1. An identifier must contain at least one character.
2. The first character of an identifier must be an alphabet or the underscore.
3. The remaining characters may be alphabets, underscores, numbers.
4. Qther characters are not permitted.
5. A reserved keyword cannot be used as an identifier.
6. meaningful

################################################

import keyword
print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

################################################

4.3.variable, identifiers, labels  

variable         -> varying value
identifiers      -> ကိုယ်စားပြုသူ
labels           -> လိပ်စာကတ်

################################################


"""
