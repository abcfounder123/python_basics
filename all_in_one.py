"""
translate, interpreter
--->    line by line
--->    from top to bottom, left to right, parenthesis ( )

# tac ti toe game
work.1(work.6), work.4(w.7), work.5(w.8)
work.2(w9(w10))
Work3()

################################################

1. data type
2. control flow   ---> operator 41, while, for, if, pratice --> tac ti toe, calculator
3. function
4. OOP
5. FP
6. Algorithm
7. design patterns

################################################

Coding Style
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

Python has five rules for naming identifiers.
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

Data types ( built-in , custom )

1. Text Type:       str ( charactor string )
2. Numeric Types:   int(integer), float, complex
3. Sequence Types:  list, tuple, range
4. Mapping Type:    dict
5. Set Types:       set, frozenset
6. Boolean Type:    bool
7. Binary Types:    bytes, bytearray, memory view
8. None Type:       NoneType

# use
# copy
# new

################################################

# complex number
# i = imaginary part in mathematics,
# In programming, j is used instead of i.
# j = i = root(-1)

x2 − 2x + 2 = 0.
x = ( 2 ± root(-4) ) / 2       <---     root(-4) = root(4) * root(-1) = 2 * j = 2j
x = ( 2 ± 2j ) / 2
x = 1 ± j
x = 1 + j and x = 1 − j

################################################
"""
#  1. Text Type:    str

# str     --->   charactor string
'1000'
"1000"
'''1000'''
"""1000"""
str(1000)

"""
################################################

#  2. Numeric Types:    int(integer), float, complex

# int     --->   integer (whole number)
1000

int(1000)
int("1000")

# float     --->   floating point number

1000.0
float("1000")
0.
.0

# complex number   --->   nj
3 + 2j  # move 3 steps right and 2 step up
0j
1j

################################################

# 3. Sequence Types:    list, tuple, range

# list     --->   []
[]  # empty list
[1, 2, 3]  # elements
["apple", "banana", "orange"]

# tuple    --->   (), (only one element,)
("Mg Mg", 20, 5.5)

# range    --->   range(start=0, stop, step=1)
# generate a sequence of number
range(10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(1, 10)  # 1, 2, 3, 4, 5, 6, 7, 8, 9
range(1, 10, 2)  # 1, 3, 5, 7, 9
range(2, 101, 2)  # 2, 4, 6, ...., 100
range(100, 1, -2)  # 100, 98, 96, ..., 4, 2

################################################

# 4. Mapping Type
# key-value pairs
# dict     --->   {}
# dictionary
{}
{"name": "Mg Mg"}
{"name": "Mg Mg", "age": 20, "height": 5.5}

{
    "name": "Mg Mg",
    "age": 20,
    "height": 5.5

}

#
[80, 90, 75]
(80, 90, 75)

["apple", "orange", "banana"]
("apple", "orange", "banana")

{
    "Myanmar": 80,
    "English": 75,
    "Math": 90
}

################################################

# 5. Set Types:     set, frozenset
# group

# bread ---> flour, salt
# cake  ---> sugar, condensed milk, flour, salt

# set        --->   {,}, set
# don't accept mutable data  ---> list, dict, set
x = {"apple", "banana", "orange", 1, 1.0, }

bread = {"flour", "salt"}
cake = {'sugar', 'condensed milk', 'flour', 'salt'}

u = bread.union(cake)
print(u)

i = bread.intersection(cake)
print(i)

print(bread.issubset(cake))
print(cake.issuperset(bread))

print(bread.issubset(cake))
print(cake.issuperset(bread))

# frozenset  --->   frozenset()
x = ["apple", "banana", "orange"]
f = frozenset(x)

################################################

# 6. Boolean Type:
# bool     --->   True, False
1
1.0
0j
True
False
bool(1)

################################################

# 7. Binary Types:  bytes, bytearray, memory view
# immutable, mutable, direct access & do not copy

# bytes ---> store in binary value
# 1 bit ---> 0, 1 ---> probability 2

0
1

0  0
0  1
1  0
1  1

0  0  0
0  0  1
0  1  0
0  1  1
1  0  0
1  0  1
1  1  0
1  1  1

0  0  0  0  0  0  0  0
......................
1  1  1  1  1  1  1  1

# 2 power n of bit
# 1 byte --> 8 bits ---> probability 256 ---> 0 to 255 ---> 00000000 to 11111111
# bytes can only contain ASCII literal characters ---> 0 to 255 ( က 4096 )
# ASCII

x = b"apple"  # 1100001  1110000  1110000  # a = 97, p = 112
print(x)
print(x[1])
print(bin(x[1]))

# bytearray
xa = bytearray(x)
print(xa)
xa[0] = 98
print(xa)
# print(xa[0])

# 100MB
# 200MB
# 150MB

# memory view
x = bytearray(b"apple")
y = bytearray(b"apple")
m = memoryview(x)
# print(m)
m[0] = 100

# print(x)
# print(str(x))
# print(str(y))
# print(str(m))

################################################

# 8. None Type:
# NoneType     --->   None
None

################################################

# Type casting
# implicit type casting    --->   type casting by py, indirect type casting
# explicit type casting    --->   type casting by programmer, direct type casting
# float, boolean value

ans = 1 + 1.6
# print(ans)

# float to int
# 1. truncate, int  --->  1 + int(1.6)    --->  1 + 1  = 2
# 2. round          --->  1 + round(1.6)  --->  1 + 2  = 3
# 3. int to float   --->  float(1) + 1.6  --->  1.0 + 1.6 = 2.6

################################################

# complex number example
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.axhline(y=0, color='black')
ax.axvline(x=0, color='black')

c1 = -3 + 2j   # pythagorean theorem = 9 + 4 = 13 = 3.61 from original point(0, 0)
ax.plot(c1.real, c1.imag, 'ro')  # 'ro' = red circle
ax.text(c1.real + 0.2, c1.imag, f'{c1}', fontsize=12, color='red')

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

Immutable data types
1. int, float, complex,
2. bool,
3. str,
4. tuple,
5. range,
6. frozenset,
7. bytes
8. NoneType

Mutable data types:
1. list 
2. dict 
3. set  
4. bytearray
5. memoryview
6. user-defined classes

################################################

# True
# int, float ---> not zero
# group      --->  str, list, tuple, dict, set, ... ---> not empty

################################################

sequence type     ---> list, tuple, range
list      --->   homogeneous(same) sequence of element ["apple", "banana", "orange"]
tuple     --->   heterogeneous sequence of element     ("Mg Mg", 20, 5.5)
range     --->   sequence of number                    (1, 2, 3, 10000000)

################################################

sequence

# contiguous blocks of memory

# retrieves the reference
# the size of each element = 8 bytes
# starting memory location  ---> 100
# first element  ---> 108   <--- 100 + (size * 1)
# second element ---> 116   <--- 100 + (size * 2)
# third element  ---> 124   <--- 100 + (size * 3)
# 10th element   ---> 180   <--- 100 + (size * 10)

# sequence  
# indexing ---> pos, neg
# ? = total - n
# access, update, del
# slicing [start: stop: step]

# length 10  ---> len()

# total 45   --->  0 to 44
middle element =  23  = 22

division  ---> 45 / 2   =  22.5
floor div ---> 45 // 2  =  22
modulo    ---> 45 % 2   =  1

x = "abcdefg"

"abcdefg"
#  a  b  c  d  e  f  g
#  0  1  2  3  4  5  6
# -7 -6 -5 -4 -3 -2 -1

# t = 7
# positive index of a = 0
# negative index of a = t - 0 = -7

# positive index of b = 1
# negative index of b = t - 1 = -6

# positive index of g = t - 1 = 6
# negative index of g = -1

# access
# print(x[3])

x = ["apple", "banana", "orange"]
print(x)

# update
x[1] = "mangoes"
print(x)

# delete
del x[-1]
print(x)

################################################

# object
# name Mg Mg on paper ---> data
# real object Mg Mg   ---> data + methods --> walk, speak
# str ---> character string + 86 methods
# int ---> integer value    + 56 methods
# 15 data types ---> about 1000 methods

# methods
# normal methods ---> upper
# magic methods, double underscore methods, dunder methods  ---> __add__

# normal methods
# is, not is
# isupper
# upper

"""