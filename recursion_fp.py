'''
ပုစ္ဆာကို တစ်ဆင့်ချင်းခွဲပြီး‌ ဖြေရှင်းဖို့သုံးသည်။
ပင်ကို သဘာဝကိုယ်တိုင်က ထပ်တလဲလဲဖြေရှင်းမှ အဆင်ပြေမယ့် ပြသနာတွေဆိုရင် recursion ကို သုံးသည်။
loop အစားအသုံးပြုသည်။

#################################################

1. Direct Recursion

2. Indirect Recursion

#################################################

1. Direct Recursion ( tail, head, tree, nested)

a.Tail Recursion

If a recursive function calling itself and that recursive call is
the last statement in the function then it’s known as Tail Recursion.

After that call the recursive function performs nothing.
The function has to process or perform any operation at the time of calling and
it does nothing at returning time.

In tail recursion, the processing occurs before the recursive call
# recurse ‌ေနာက်မှဖြစ်တာ tail


# tail
def fun(n):
    if n > 0:
        print(n, end=" ")
        
        # tail in the function
        fun(n - 1)  # f(2) # f(1) # f(0)


fun(3)  # 3 2 1
print()
# fun(3)
# fun(1)
# fun(0)

#################################################

# tail recursion ( 3 2 1 )
if 3 > 0:
    print(3, end=" ")
    if 2 > 0:
        print(2, end=" ")
        if 1 > 0:
            print(1, end=" ")
            if 0 > 0:
                print(0, end=" ")
                fun(0 - 1)

print()
# head recursion, ( 1 2 3 )
if 3 > 0:
    if 2 > 0:
        if 1 > 0:
            if 0 > 0:
                fun(0 - 1)
                print(0, end=" ")
            print(1, end=" ")
        print(2, end=" ")
    print(3, end=" ")

#################################################

# tail
if 3 > 0:
    print(3, end=" ")
    fun(3 - 1)

if 2 > 0:
    print(2, end=" ")
    fun(2 - 1)

if 1 > 0:
    print(1, end=" ")
    fun(1 - 1)
    
if 0 > 0:
    print(0, end=" ")
    fun(0 - 1)

#################################################

b. Head Recursion
If a recursive function calling itself and that recursive call is the first statement in the function
then it’s known as Head Recursion.

There’s no statement, no operation before the call.
The function doesn’t have to process or perform any operation at the time of calling and all operations are done at returning time.

# head
def fun(n):
    if n > 0:
        # head in the function
        fun(n - 1)
        print(n, end=" ")


fun(3)
# fun(2)
# fun(1)
# fun(0)

print()

#################################################

if 3 > 0:
    if 2 > 0:
        if 1 > 0:
            if 0 > 0:
                fun(0 - 1)
                print(0, end=" ")
            print(1, end=" ")
        print(2, end=" ")
    print(3, end=" ")

#################################################

# head
if 3 > 0:
    fun(3 - 1)
    print(3, end=" ")

if 2 > 0:
    fun(2 - 1)
    print(2, end=" ")

if 1 > 0:
    fun(1 - 1)
    print(1, end=" ")

if 0 > 0:
    fun(0 - 1)
    print(0, end=" ")

#################################################

c. Tree Recursion
If a recursive function calling itself for more than one time then it’s known as
Tree Recursion.
( Linear Recursion ---> If a recursive function calling itself for one time
then it’s known as Linear Recursion. )

# tree
#count = [0, ]
def fun(n, c=count):
    #c[0] += 1
    #print(f"f({n})")
    if n > 0:
        print(n, end=" ")

        # Calling once
        fun(n - 1)

        # Calling twice
        fun(n - 1)


fun(3)
print()
print(count)

#################################################

if (3 > 0):
    print(3, end=" ")
    if (2 > 0):
        print(2, end=" ")

        if (1 > 0):
            print(1, end=" ")

            if (0 > 0):
                print(0, end=" ")
                fun(0 - 1)
                fun(0 - 1)

            if (0 > 0):
                print(0, end=" ")
                fun(0 - 1)
                fun(0 - 1)

        if (1 > 0):
            print(1, end=" ")
            if (0 > 0):
                print(0, end=" ")
                fun(0 - 1)
                fun(0 - 1)

            if (0 > 0):
                print(0, end=" ")
                fun(0 - 1)
                fun(0 - 1)

    if (2 > 0):
        print(2, end=" ")
        if (1 > 0):
            print(1, end=" ")
            if (0 > 0):
                print(0, end=" ")
                fun(0 - 1)
                fun(0 - 1)

            if (0 > 0):
                print(0, end=" ")
                fun(0 - 1)
                fun(0 - 1)

        if (1 > 0):
            print(1, end=" ")
            if (0 > 0):
                print(0, end=" ")
                fun(0 - 1)
                fun(0 - 1)

            if (0 > 0):
                print(0, end=" ")
                fun(0 - 1)
                fun(0 - 1)

#################################################

if (3 > 0):
    print(3, end=" ")
    fun(3 - 1)
    fun(3 - 1)
    
if (2 > 0):
    print(2, end=" ")
    fun(2 - 1)
    fun(2 - 1)
    
if (1 > 0):
    print(1, end=" ")
    fun(1 - 1)
    fun(1 - 1)

if (0 > 0):
    print(0, end=" ")
    fun(0 - 1)
    fun(0 - 1)    

#################################################
        
# 3     2 1 1     2 1 1

# linear ( recursion depth = 4 ) ( count = 4 )
#     3
#     2
#     1     
#     0      

# non linear ( recursion depth = 4 ) ( count = 15 )
#                  3
#         2                  2
#    1       1          1         1
#  0   0   0   0      0   0     0    0

# non linear ( recursion depth = 4 ) ( count = 40 )
#                                     3
#          2                          2                      2
#   1      1      1            1      1      1        1      1      1
# 0 0 0  0 0 0  0 0 0        0 0 0  0 0 0  0 0 0    0 0 0  0 0 0  0 0 0

# non linear ( recursion depth = 5 ) ( count = 31 )
#                                    4
#                 3                                        3 
#        2                 2                       2                 2                
#    1        1       1        1               1        1       1        1
#  0   0    0   0   0   0    0   0           0   0    0   0   0   0    0   0

#################################################

d. Nested Recursion
# a recursive function passing parameter as a recursive call
# recursion inside the recursion

# Nested Recursion
# if n greater than 100, n - 10
# else: 91

count = [0, ]

def fun(n, c=count):
    c[0] += 1
    print(f"fun({n})")
    if (n > 100):
        return n - 10
    return fun(fun(n + 11))

print(fun(95))  # 91
print(count)

#################################################

# 99
fun(99)

fun(110)
fun(100)

fun(111)
fun(101)

#################################################

# 99 --> fun(fun(99 + 11) --> fun(fun(110))  --> fun(100)
if 99 > 100:
    return 99 - 10
return fun(fun(99 + 11)

# 110 --> 100
if 110 > 100:
    return 110 - 10
return fun(fun(110 + 11)

# 100 --> fun(fun(100 + 11))  --> fun(fun(111)) --> fun(101) --> 91
if 100 > 100:
    return 100 - 10
return fun(fun(100 + 11)

# 111 --> 101
if 111 > 100:
    return 111 - 10
return fun(fun(n + 11)

# 101 --> 91
if 101 > 100:
    return 101 - 10
return fun(fun(n + 11)

#################################################

if n > 100:
    return n - 10
return fun(fun(n + 11)

#################################################

2. Indirect Recursion
In this recursion,
there may be more than one functions and
they are calling one another in a circular manner.

# Python program to show Indirect Recursion
def funA(n):
    print(f"A({n})")
    if n > 0:
        #print("", n, end='')

        # Fun(A) is calling fun(B)
        funB(n - 1)

def funB(n):
    print(f"B({n})")
    if n > 0:
        #print("", n, end='')

        # Fun(B) is calling fun(A)
        funA(n - 1)

funA(22)

#################################################

'''

'''
#################################################

Example.1 ---> Factorials

factorial(6!) = 6 * 5 * 4 * 3 * 2 * 1 = 720

4!  ကို ရှာမယ်ဆိုပါစို့။
# direct way
4! = 4 * 3 * 2 * 1

# step by step
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = ?
1! = 1
2! = 2 * 1 = 2
3! = 3 * 2 = 6
4! = 4 * 6 = 24

def factorial(n):
    if n > 1:
        f = n * factorial(n - 1)

    else:
        f = 1

    return f

print(factorial(6))


def factorial(n):
    print(f"{n}!")
    if n > 1:
        f = n * factorial(n - 1)
        print(f"{n}! =", end=" ")
        print(f)
    else:
        print(f"{n}! =", end=" ")
        f = 1
        print(f)
    print(f"{n}!  <---   closed")
    return f

print(factorial(4))




x = 4 *  f(3)

4!
3!
2!
1!
1! = 1
2! = 2
3! = 6
4! = 24
24

"""
# step by step
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = ?

1! = 1
2! = 2 * 1 = 2
3! = 3 * 2 = 6
4! = 4 * 6 = 24
"""

def factorial(n):
    if n > 1:
        x = n * factorial(n - 1)
    else:
        x = 1
    return x

print(factorial(4))


def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

print(fac(4))


def fac_t(n):
    return 1 if n == 1 else n * fac_t(n - 1)

print(fac_t(4))


def f(n):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f

print(f(4))


def f(n):
    f = 1
    for i in range(1, n+1, 1):
        f *= i
        print(f"{i}! = {f} ")
    return f

print(f(1000))


n * n * n * 1

###########

Recursion limits ( time, memory, )

recursion ရဲ့ အဆင့်တစ်ခုစီတိုင်းဟာ function ကို ‌အသံုးပြု‌ေနခြင်းဖြစ်သည်။
4! ဆိုရင် function ‌ေလးကြိမ်
1000! ဆိုရင် function အကြိမ်တစ်‌ေထာင်

function တစ်ကြိမ်အလုပ်လုပ်တိုင်း အချိန်ပိုကုန်
memory ပိုကုန်သည်။ ( fuction ရဲ့ လက်ရှိအ‌ေခြအ‌ေနကို သိမ်းဆည်းဖို့ ) ( local variable သိမ်းဖို့ )
‌ေနာက်တစ်ခုရှိ‌ေသးတာက python မှာ recursion 1000 ထိပဲသံုးခွင့်‌ေပးထား။

from sys import setrecursionlimit, getrecursionlimit

print(getrecursionlimit())
setrecursionlimit(3)  # depth
print(getrecursionlimit())

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

print(fac(2))

#######

# not include this fact in code ( if n < 0 : factorial = 0 )
# factorial
# if 0 or 1 : factorial = 1
# if more than 1:
# eg. factorial of 3 = 1 * 2 * 3 = 6
# eg. factorial of 6 = 1 * 2 * 3 * 4 * 5 * 6
# while loop

def factorial(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f

#print(factorial(1))
print(factorial(6))


def factorial(n):
    f = 1
    i = 1
    while i < n+1:
        f *= i
        i += 1
    return f

#print(factorial(1))
print(factorial(6))

#####################

# for loop
def factorial(n):
    x = 1
    for i in range(1, n + 1, 1):
        x *= i
    return x


# print(factorial(0))
print(factorial(6))

#####################

# recursion
def factorial(n):
    if n > 1:
        x = n * factorial(n - 1)
    else:
        x = 1
    return x

print(factorial(6))

# recursion
# ternary operator
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1
    
print(factorial(6))

#####################

#####################

"""
Fibonacci numbers

F0 = 0
F1 = 1
F2 = F1 + F0 = 1
F3 = F2 + F1 = 2

...

F(n) = F(n - 1) + F(n - 2)  <--- 
f2   = f1       + f0
f100 = f99      + f98
f798 = f797     + f796

each element is the sum of the two previous elements.
f0, f1, f2, f3, f4, f5, f6
0,  1,  1,  2,  3,  5,  8, 13, 21...

"""

# f0 = 0
# f1 = 1
# f(n) = f(n - 1) + f(n - 2)

def f(n):
    print(f"f({n})")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)

# f0, f1, f2, f3, f4, f5, f6
# 0,  1,  1,  2,  3,  5,  8, 13, 21..
print(f(4))


f(4)   --->   f(3) + f(2)   --->   2 + 1  --->   3


f(3)   --->   f(2) + f(1)   --->   1 + 1  --->   2

f(2)   --->   f(1) + f(0)   --->   1 + 0  --->   1

f(2)   --->   f(1) + f(0)   --->   1 + 0  --->   1

                  f(4)
        f(3)               f(2)
   f(2)      f(1)      f(1)    f(0)
f(0)   f(1)

# loop
def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for _ in range(n-1):  # 0 1 2
            a, b = b, a + b  # 2, 3
        return b

# f0, f1, f2, f3, f4, f5, f6
# 0,  1,  1,  2,  3,  5,  8, 13, 21..

# 0, 1,

# 1, 1
# 1, 2
# 2, 3
# 3, 5
print(fibonacci(6))

'''

'''
###########

# recursion and cache
# Example.2  fibonacci
c = [0, ]


def fibonacci(n, c=c):
    c[0] += 1
    print(f"fib({n})")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Normal recursion")
print("Answer =", fibonacci(20))
print("- " * 20)
print(c)


#print("Answer =", fibonacci(5))

"""
step.1   --->   f(4) = f(3) + f(2)
function ထဲကို 4 ထည့်ပေးလိုက်ရင်   1 နဲ့ 0 မဟုတ်လို့
f(3) + f(2) ဆိုပြီး အောက်ဆုံးအကြောင်းအလုပ်လုပ်ပါမယ်။
+ ဟာ left sided bind ဖြစ်လို့ left operand ( f(3) )ကို အရင်ဖြေရှင်းပါမယ်။ 
note.1 ---> f(2) ကျန်
###########
step.2    --->   f(3) = f(2) + f(1) 
function ထဲကို 3 ထည့်ပေးလိုက်ရင်   1 နဲ့ 0 မဟုတ်လို့
f(2) + f(1) ဆိုပြီး အောက်ဆုံးအကြောင်းအလုပ်လုပ်ပါမယ်။
+ ဟာ left sided bind ဖြစ်လို့ left operand ( f(2) )ကို အရင်ဖြေရှင်းပါမယ်။
note.2 ---> f(1) ကျန်
###########
step.3    --->   f(2) = f(1) + f(0)
function ထဲကို 2 ထည့်ပေးလိုက်ရင်   1 နဲ့ 0 မဟုတ်လို့
f(1) + f(0) ဆိုပြီး အောက်ဆုံးအကြောင်းအလုပ်လုပ်ပါမယ်။
+ ဟာ left sided bind ဖြစ်လို့ left operand ( f(1) )ကို အရင်ဖြေရှင်းပါမယ်။
f(1)  ---> function ထဲကို 1 ထည့်ပေးလိုက်ရင်  1 ပြန်ပေးပါတယ်။
right operand f(0) --->  function ထဲကို 0 ထည့်ပေးလိုက်ရင်  0 ပြန်ပေးပါတယ်။
step.3    --->   f(2) = f(1) + f(0) = 1 + 0  = 1
###########
note.2 က ကျန်ခဲ့တဲ့ right operand f(1)  --> 1
step.2    --->   f(3) = f(2) + f(1) = 1 + 1  = 2
###########
note.1က ကျန်ခဲ့တဲ့ right operand f(2)  -->  step.3 လိုပဲဖြေရှင်း   ---> 1
step.1    --->   f(4) = f(3) + f(2) = 2 + 1  = 3
###########
ပုံဆွဲရင် အောက်ကလိုဖြစ်ပါမယ်။
recursion နှစ်ကြိမ်သုံးတော့ tree recursion ဖြစ်သွားတာပေါ့။
picture.1
                       4

         3                         2

    2        1                1*       0*

1      0
###########
ငါးထည့်လိုက်ရင်တော့ ခုလိုဖြစ်သွားပါမယ်။
picture.2
                                5

                 4                                 3

         3              2                  2*          1*

    2       1       1     0            1*      0*

1     0    
ပုံဆွဲပြတာက function တွေ နှစ်ခါထပ်ပြီး အလုပ်လုပ်နေရတာကို သိစေချင်လို့ပါ။
f(4) တုန်းက 
1 သုံးခါ
0 နှစ်ခါ
2 နှစ်ခါ ထပ်ပါတယ်။
စုစုပေါင်း ကိုးကြိမ် အလုပ်လုပ်လိုက်ရပါတယ်။

f(5) မှာတော့ 
1 ငါးခါ
0 သုံးခါ
2 သုံးခါ ထပ်ပါတယ်။
စုစုပေါင်း ဆယ့်ငါးကြိမ် အလုပ်လုပ်လိုက်ရပါတယ်။

တကယ်က f(5) လိုချင်ရင် 4, 3, 2, 1 , 0 ရှာဖို့ Recursion ငါးကြိမ်ပဲလုပ်သင့်တာပါ။
f(5) ပါထည့်တွက်ရင် စုစုပေါင်း ခြောက်ကြိမ်ပေါ့။
အောက်ကပုံလိုမျိုး star ပြထားတဲ့ ထပ်နေတာကို ဖယ်ရမှာပေါ့။

###########
picture.3
                                5

                 4                                    3*

         3                2*                 2*          1*

    2       1*         1*     0*         1*     0*

1     0                                                                                                                                                                                                                                        
ထပ်နေတာတွေကို ဖယ်ဖို့ ရှာပြီးသားကို ပြန်မရှာဖို့ dictionary တစ်ခုထဲမှာ သိမ်းပါ့မယ်။

"""

cache = dict()
def fibonacci(n):
     print(f"fib({n})")
     if n in cache:
         return cache[n]
     elif n==0:
         x = 0
     elif n==1:
         x = 1
     else:
         x = fibonacci(n-1) + fibonacci(n-2)
     cache[n] = x
     #print(cache)
     return x

print("Recursion with cache")
print("Answer =", fibonacci(4))
print("- " * 20)
print(cache)

"""
function ထဲကို လေးထည့်ရင် ပုံတစ်မှာ star ပြထားတဲ့ recursion 1, 0 နှစ်ကြိမ်လျော့သွားပါတယ်။
မူလက ကိုးကြိမ်
cache သုံးလိုက်တော့ ခုနှစ်ကြိမ်ပေါ့။
function ထဲကို ငါးထည့်ရင် ပုံနှစ်မှာ star ပြထားတဲ့ recursion 2, 1, 1, 0 လေးကြိမ်လျော့သွားပါတယ်။
မူလက ဆယ့်ငါးကြိမ်
cache သုံးလိုက်တော့ ဆယ့်တစ်ကြိမ်ပေါ့။
ဒါက မြင်သာအောင်နမူနာပြတာပါ။
တကယ့်တကယ်က lru_cache ဆိုတဲ့ decorator function ကို သုံးလို့ရပါတယ်။
"""

from functools import lru_cache


@lru_cache()
def fibonacci(n):
    print(f"fib({n})")
    if n == 0:
        x = 0
    elif n == 1:
        x = 1
    else:
        x = fibonacci(n-1) + fibonacci(n-2)    
    return x


#from sys import setrecursionlimit
#setrecursionlimit(100_000_000)

print("Recursion with lru_cache")
print("Answer =", fibonacci(100))# 1500

print("- " * 20)

"""
function ထဲကို  4 ထည့်လိုက်ရင်  3 2 1 0 ရှာဖို့ recursion လေးကြိမ်ပဲလုပ်သွားပါတယ်။
f(4) ပါ ထည့်တွက်ရင် စုစုပေါင်း ငါးကြိမ်ပေါ့။
function ထဲကို 5 ထည့်လိုက်ရင် 4 3 2 1 0 ရှာဖို့ recursion ငါးကြိမ်ပဲလုပ်သွားပါတယ်။
f(5) ပါ ထည့်တွက်ရင် စုစုပေါင်း ခြောက်ကြိမ်ပေါ့။
"""
"""
Normal recursion
fib(4)
fib(3)
fib(2)
fib(1)
fib(0)
fib(1)
fib(2)
fib(1)
fib(0)
Answer = 3
- - - - - - - - - - - - - - - - - - - -
Recursion with cache
fib(4)
fib(3)
fib(2)
fib(1)
fib(0)
fib(1)
fib(2)
Answer = 3
- - - - - - - - - - - - - - - - - - - -
Recursion with lru_cache
fib(4)
fib(3)
fib(2)
fib(1)
fib(0)
Answer = 3
- - - - - - - - - - - - - - - - - - - -
[Program finished]
"""

"""

"Tail recursion" is a specific type of recursion where the recursive call is the last operation in the function. 

"Tail call optimization" (TCO) is a way to optimize tail recursive functions. 
It means that the compiler or interpreter can optimize away the current function's call frame before making the tail-recursive call,
reducing the overhead of recursion.

However, Python doesn't provide native tail call optimization, which means that deeply nested recursive calls can lead to
a "RecursionError" due to hitting the maximum recursion depth.

To handle this, you might use an approach called "less recursion." 

This involves transforming a tail-recursive function into an iterative form (eg. using loops) to simulate recursion
without causing a stack overflow.
"""

# fibonacci_less_recursion
def fibonacci(n):
    f = [0, 1]
    for n in range(2, n + 1, 1):# 2, 3, 4, 5
        f.append(f[n - 1] + f[n - 2])
        #print(f)
    return f[n]
    
print("answer =", fibonacci(100000))

"""
answer = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875

[Program finished]

"""

# tail recursion  (normally maximum 1000 depth)
# tree recursion (if use 2 recursion, maximum depth is 2 power 1000)
#  (without TCO and so it will cause error when reaching maximum depth)

a = 0
def fibonacci(n):
    global a
    a += 1
    print(a)
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print("answer =", fibonacci(20)) # 21891
#print("answer =", fibonacci(30)) # recurse 2 692 537 times ( 3 millions )

# recursion error because of maximum depth limit ( 2 power 1000 )
#print("answer =", fibonacci(1000))

'''
