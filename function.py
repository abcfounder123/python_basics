"""
0.Defining Functions


def name(par):
    '''doc-strings'''
    statements   
    return value


def  = keyword for standard function definition (keyword)
name = function name ( identifier for function object )
()   = parenthesized list of formal parameters
:    = code block
____ = indent ( function body)

'''doc'''  = str value for function's documentation
statements = code section in function body
return     = used to exit a function and return a value (keyword)  ( default value ---> None )

################################################

1. invoke, call
2. more than one place, decomposition,
3. where?
   --->  built-in function,
   --->  preinstalled module, external module,
   --->  directly from our code
4. def, name, (), :, indent, doc, body, return
5. same name of function

################################################

6. parameterized function

parameter
A.standard / normal parameter       --->  (x, y)
B.special parameter                 --->  /, *
1.positional only parameter         --->  (x, y, /)
2.keyword only parameter            --->  (*, x, y)
3.default parameter                 --->  (a, b, c=0), default parameter = c
4.variable length parameter         --->  (*args), (**kwargs)
  (arbitrary number of argument)

################################################

7.arguments
1.positional arguments              --->  (2, 3)
2.keyword arguments                 --->  (x=2, y=3)
3.default arguments                 --->  (a, b, c=0), default argument = 0
4.variable length arguments         --->  arbitrary number of positional or keyword arguments

################################################

8.analysis on parameter list
check special parameters            --->  /, *, =, (*args), (**kwargs)

################################################

9.reading and writing function's documentation  ---> help, __doc__
10.reading full documentation                   ---> www.python.org

################################################

11.effect and result of functions

effect
---> side effect
---> modifies external/ global state, interacts with input/output, ...

result
---> return value
---> purely computes a value

################################################

12.Type of function by their behavior
1. (effect only) function            ---> difference_update
2. (result only) function            ---> difference
3. (effect and result) function      ---> pop

################################################

13.learning method for using strange function
1.read documentation before use, determine effect and result
2.test documentation
3.test as you like

################################################

14.Type of function by their location
built-in function
external function
custom function

################################################

15.Type of function by their behavior concept ( effect & result concepts )
1.pure function                      --->  result only function
2.impure function                    --->  function with side effects

################################################

6.A.usage of standard / normal parameter
positional arguments                 --->   (2, 3)
keyword arguments                    --->   (x=2, y=3)
mixed                                --->   (2, y=3)

def f_z(x, y):
    z = x ** 2 + 2 * x * y + y ** 2
    return z


z = f_z(2, 3)
print(z)

z = f_z(x=2, y=3)
print(z)

z = f_z(2, y=3)
print(z)

################################################

6.B.1.usage of positional only parameter     ---> (x, y, /)


def add(x, y, /):
    return x + y


add(1, 2)

################################################

6.B.2.usage of keyword only parameter        ---> (*, x, y)


def info(*, name, age, phone_no):
    print(f"name = {name}")
    print(f"age = {age}")
    print(f"phone No = {phone_no}")


info(phone_no="09953212", name="Mg Mg", age=20)

################################################

6.B.3.usage of default parameter             --->   (a, b, c=0)


def f_z(x, y, c=0):
    z = x ** 2 + 2 * x * y + y ** 2 + c
    return z


z = f_z(1, 2)
print(z)

################################################

8.analysis on parameter list
check special parameters          --->   /, *
positional only parameter         --->   a, b
keyword only parameter            --->   e, f
standard / normal parameter       --->   c, d


def add(a, b, /, c, d, *, e, f):
    return a + b + c + d + e + f

add(1, 2, 3, 4, e=5, f=6)
add(1, 2, c=3, d=4, e=5, f=6)
add(1, 2, 3, d=4, e=5, f=6)

################################################

6.B.4.variable length parameter              ---> (*args)
a.arbitrary number of positional arguments


def my_sum2(*numbers):
    print(numbers)


my_sum2()
my_sum2(1, 2)
my_sum2(1, 2, 3, 4, 5)
my_sum2(1, 2, 3, 4, 5, "apple", "banana", 1.3, {"name": "Mg Mg"})


# sample usage
def my_sum(*args):
    ans = 0
    for number in args:
        ans += number
    return ans


x = my_sum(1, 2, 3)
print(x)

add_1_100 = my_sum(*range(1, 101))  # 1 + 2 + 3 + ... + 100 = 5050
print(add_1_100)  # 5050

################################################

6.B.4.variable length parameter         ---> (**kwargs)
b.arbitrary number of keyword arguments


def info(**kwargs):
    print(kwargs)


info(name="Mg Mg", age=20, ph_no="09123456")

################################################

9.reading and writing function's documentation

reading function's documentation
--->   help(), __doc__

from operator import add
help(add)
print(add.__doc__)

################################################

writing function's documentation


def add(a, b, /):
    '''Same as a + b.'''
    return a + b


help(add)

################################################

writing function's documentation


def print_month(year, month):
    '''
    print a month's calendar string (multi-line).

    >> print_month(2024, 2)

    output ==>

       February 2024
    Mo Tu We Th Fr Sa Su
             1  2  3  4
     5  6  7  8  9 10 11
    12 13 14 15 16 17 18
    19 20 21 22 23 24 25
    26 27 28 29
    '''
    import calendar
    ans = calendar.month(year, month)
    print(ans)


print_month(2024, 10)

################################################

print(print_month.__doc__)
help(print_month)

################################################

10.reading full documentation     --->  https://docs.python.org/3/library/calendar.html
w = colum wide of space = 2
l = line count = 1
(theyear, themonth, w=2, l=1)

from calendar import month
help(month)

################################################

11.effect and result of functions

effect
---> side effect
---> modifies external/ global state, interacts with input/output, ...

result
---> return value
---> purely computes a value

################################################

input
effect ---> read user input
result ---> return user input

print
effect --->  Prints the values to a stream, or to sys.stdout by default.
result --->  None

upper
effect --->   None
result --->   Return a copy of the string converted to uppercase.

lower
effect --->   None
result --->   Return a copy of the string converted to lowercase.

strip
effect --->
result --->   Return a copy of the string with leading and trailing whitespace removed.
              If chars is given and not None, remove characters in chars instead.

pop
effect ---> Remove an arbitrary set element.
result ---> return a removed element.

################################################

12.Type of function
1. (effect only) function        ( eg.difference_update )
2. (result only) function        ( eg.difference )
3. (effect and result) function  ( eg.pop )

################################################

12.1.(result only) function
difference
effect     --->   None
result     --->   Return the difference of two or more sets as a new set.

s = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 9}
s3 = {3, 4, 11}

s4 = s.difference(s2, s3)
print(s, s2, s3, s4)

################################################

12.2.(effect only) function
difference_update
effect     --->   Remove all elements of another set from this set.
result     --->   None

s = {1, 2, 3, 4}
s2 = {1, 2}

ans = s.difference_update(s2)
print(ans)
print(s, s2)

# print(set.difference_update.__doc__)

################################################

12.3.(effect and result) function
pop
effect     --->   remove an arbitrary set element
result     --->   return popped value

s = {2, 3, 4, "a", "b"}
ans = s.pop()
print(ans)
print(s)

# print(s.pop.__doc__)
# help(set.pop)

################################################

13.learning method for using strange function

example: using difference method
step.1     --->   read documentation before use, determine effect and result.

s = {1, 2, 3, 4, 5, 6}

print(s.difference.__doc__)
print("\n", "- " * 21, "\n")

# effect = no side effect
# result = new set of difference result
#          the difference of two or more sets as a new set.

################################################

# step.2     --->   test doc

s = {1, 2, 3, 4, 5, 6}
s1 = {1, 2}
s2 = {3, 4}
actual_result = {5, 6}
ans = s.difference(s1, s2)
print(ans, " --> ", ans == actual_result)

################################################

# step.3     --->   test as you like

# a.test with 0 set, 1 set

s = {1, 2, 3, 4, 5, 6}
s1 = {1, 2}
actual_result = {1, 2, 3, 4, 5, 6}
ans = s.difference()
print(ans, " --> ", ans == actual_result)

s = {1, 2, 3, 4, 5, 6}
s1 = {1, 2}
actual_result = {3, 4, 5, 6}
ans = s.difference(s1)
print(ans, " --> ", ans == actual_result)

################################################

# b.test with other iterable obj

# 1. list
s = {1, 2, 3, 4, 5, 6}
l1 = [1, 2]
l2 = [3, 4]
ans = s.difference(l1, l2)
actual_result = {5, 6}
print(ans, " --> ", ans == actual_result)

# 2. tuple
s = {1, 2, 3, 4, 5, 6}
t1 = (1, 2)
t2 = (3, 4)
ans = s.difference(t1, t2)
actual_result = {5, 6}
print(ans, " --> ", ans == actual_result)

# 3. dict
s = {1, 2, 3, 4, 5, 6}
d1 = {1: "apple", 2: "banana"}
d2 = {3: "apple", 4: "banana"}
ans = s.difference(d1, d2)  # test with d.keys()
actual_result = {5, 6}
print(ans, " --> ", ans == actual_result)

s = {"apple", "banana", "orange", "mangoes", "X", 1, 2, "a", "b"}
d1 = {1: "apple", 2: "banana"}
d2 = {3: "apple", 4: "X"}
ans = s.difference(d1.values(), d2.values(), d1.keys(), [1, 2], ("a", "b"))  # d.values
actual_result = {"orange", "mangoes"}
print(ans, " --> ", ans == actual_result)

################################################

"""

