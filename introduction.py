"""
#################################################

# Python
# 1. easy
# 2. many information
# 3. multi purposes
# 4. learning curve
# 5. a programming language

#################################################

1. basic syntax
2. advance syntax
3. semantics
4. create

1. control flow
2. OOP, FP
3. algorithms, design patterns

#################################################
"""
"""
# programming
# computer programming
# data ---> voice, charactor, number, photo, video, file....
# input data
# control flow
# output data

i = input()
ans = i.upper()
print(ans)

#################################################

# x = str()
# print(len(dir(x)))  # str --> 81, 74, 48, 35, 46, 57

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', 
 'capitalize', 'casefold', 'center', 'count', 'encode',
 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#################################################

# design patterns
# algorithms

# data
# built-in data type
# custom data

# pseudocode
# input F
# calculate C ---> c = (f-32) * 5 / 9
# output answer

# RAM
# memory address
# identifier

#################################################

# code

f = int(input("Degree Fahrenheit : "))
c = (f - 32) * 5 / 9
print("Degree Celsius =", c)

#################################################

f = 100
c = (f - 32) * 5 / 9
print("Degree Celsius =", c)

f = 150
c = (f - 32) * 5 / 9
print("Degree Celsius =", c)

f = 212
c = (f - 32) * 5 / 9
print("Degree Celsius =", c)

#################################################

# function

def x():
    c = (f - 32) * 5 / 9
    print("Degree Celsius =", c)


f = 100
x()

f = 150
x()

f = 212
x()

#################################################

# pure function

def x(f):
    c = (f - 32) * 5 / 9
    print("Degree Celsius =", c)

x(f=212)
x(100)
x(150)
x(212)

#################################################

# alias

y = a = b = x
y(100)
a(150)
b(212)

#################################################

# F     C
100   37.8
150   65.6
212   100

#################################################

# parameter
# default parameter
# standard form
# /
# *

# argument
# default argument
# positional argument
# keyword arguments


def x(*, f):
    c = (f - 32) * 5 / 9
    print("Degree Celsius =", c)


x(f=212)


x(212)


strip(chars=None, /)
#################################################

programming paradigm
1. imperative paradigm
---> procedural programming
---> OOP

2. declarative paradigm ( SQL )
select * from students where english >= 80
---> functional programming

#################################################

method
magic method ---> + ( __add__ ), - ( __sub__ )

help()
dir()

built-in function
custom function

built-in class
custom class

doc string

module ---> ( eg. math module )
package ( eg. tkinter )
framework ( eg. django )

literal

int x = 2;

x = int(2) # normal

x = 2  # literal

################################################

################################################

 Data types      4 left

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

def calculate_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print("Degree Celsius =", celsius)

def calculate_fahrenheit(celsius):
 fahrenheit = (celsius * 9 / 5) + 32
 print("Degree Fahrenheit =", fahrenheit)

calculate_celsius(fahrenheit=212)
calculate_fahrenheit(celsius=100)

#################################################


def say_hello(name):
    print("Hello, I'm", name)

say_hello("Mg Mg")
say_hello(70)
say_hello("Aung Net")


#################################################

class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, I'm", self.name)


p1 = Human(name="Mg Mg")
p2 = Human("Ma Ma")

p1.say_hello()
p2.say_hello()


################################################

class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, I'm", self.name)

class Age:
    def __init__(self, age):
        self.age = age

    def is_retire(self):
        return self.age > 60

    def __add__(self, other):
        return Age(self.age + other)

    def __sub__(self, other):
        return Age(self.age - other)

    def __repr__(self):
        return str(self.age) + " age"

class Dog:
    def __init__(self, name):
        self.name = name

    def bite(self):
        print(self.name, "bite.")

    def say_hello(self):
        print("dong sound")

mg_mg = Human(name="Mg Mg")
age = Age(70)
aung_net = Dog("Aung Net")

mg_mg.say_hello()
print(age.is_retire())
aung_net.bite()
aung_net.say_hello()

print(age + 1)
print(age.__add__(1))


#################################################

class Age:
    def __init__(self, age):
        self.age = age

    def is_retire(self):
        return self.age > 60

    def __add__(self, value, /):
        "Return self+value."
        return Age(self.age + value)

    def __sub__(self, other):
        return Age(self.age - other)

    def __repr__(self):
        return str(self.age) + " age"

age = Age(70)
help(age)

################################################




class Kg:
    "Kilogram ---> weight in metric unit"

    def __init__(self, w):
        self.weight = w

    def __repr__(self):
        return str(self.weight) + " kg"

    def __add__(self, other):
        if isinstance(other, Kg):
            return Kg(self.weight + other.weight)
        elif isinstance(other, Lb):
            return Kg(self.weight + (other.weight / 2.2))


class Lb:
    "Pound ---> weight in SI unit"

    def __init__(self, w):
        self.weight = w

    def __repr__(self):
        return str(self.weight) + " lb"

    def __add__(self, other):
        if isinstance(other, Lb):
            return Lb(self.weight + other.weight)
        elif isinstance(other, Kg):
            return Lb(self.weight + (other.weight * 2.2))


kg = Kg(1)
lb = Lb(4.4)
print(kg + lb)
print(lb + kg)

print(kg + kg)



################################################

import math

print(dir(math))
print(math.pi)

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb',
'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma',
'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan',
'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

################################################
################################################

# creating custom literal
# for education purpose


from custom_literals import literal


class Kg:
    "Kilogram ---> weight in metric unit"
    def __init__(self, w):
        self.weight = w

    def __repr__(self):
        return str(self.weight) + " kg"

    def __add__(self, other):
        if "kg" in other.__str__():
            return Kg(self.weight + other.weight)
        elif "lb" in other.__str__():
            return Kg(self.weight + (other.weight / 2.2))

    def __sub__(self, other):
        if "kg" in other.__str__():
            return Kg(self.weight - other.weight)
        elif "lb" in other.__str__():
            return Kg(self.weight - (other.weight / 2.2))


class Lb:
    "Pound ---> weight in SI unit"
    def __init__(self, w):
        self.weight = w

    def __repr__(self):
        return str(self.weight) + " lb"

    def __add__(self, other):
        if "lb" in other.__str__():
            return Lb(self.weight + other.weight)
        elif "kg" in other.__str__():
            return Lb(self.weight + (other.weight * 2.2))

    def __sub__(self, other):
        if "lb" in other.__str__():
            return Lb(self.weight - other.weight)
        elif "kg" in other.__str__():
            return Lb(self.weight - (other.weight * 2.2))

# creating custom literal ( kg )
@literal(float, int, name="kg")
def kg(self):
    return Kg(self)

# creating custom literal ( lb )
@literal(float, int, name="lb")
def lb(self):
    return Lb(self)


if __name__ == "__main__":

    x = Kg(2)  # normal
    y = Lb(2.2)
    print(f"{x} + {y} = {x.__sub__(y)}")
    print(f"{y} + {x} = {y.__sub__(x)}")

    print(" -" * 30)

    x = 2 .kg  # literal
    y = 2.2 .lb
    print(f"{x} + {y} = {x - y}")
    print(f"{y} + {x} = {y - x}")

    print(" -" * 30)


x = 1  # int object
y = int(2)
print(x + y)
print(y + x)

"""

