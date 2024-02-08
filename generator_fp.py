"""

1. introduction

fibonacci iterator

# consume data for two var
def fibonacci():
    print("fib")
    c = 0
    n = 1
    while True:
        print("loop")
        yield c
        c, n = n, c + n


fib_10 = [f for i, f in zip(range(11), fibonacci())]
print(fib_10)

print("- " * 20)

#################################################

# call function many times
def fibonacci(n):
    print(f"fib({n})")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib_10 = fibonacci(10)
print(fib_10)
print("- " * 20)

#################################################

from functools import lru_cache
@lru_cache()
def fibonacci(n):
    print(f"fib({n})")
    if n==0:
        x = 0
    elif n==1:
        x = 1
    else:
        x = fibonacci(n-1) + fibonacci(n-2)
    return x

print("Recursion with lru_cache")
print("Answer =", fibonacci(10))
print("- " * 20)

#################################################

# less recursion
# consume data for fib elements
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

print("answer =", fibonacci(10))

#################################################

2. chaining iterators

# chain two iterators
def chain2(it1, it2):
    for x in it1:
        yield x
    for x in it2:
        yield x

for i in chain2(range(4), reversed(range(3))):
    print(i)

#################################################

3. generator comprehension

a = [str(i) for i in range(100)]

# only need an iterator, not an actual list
# can use generator
# 100 values are not created in memory
# for long series
g = (str(i) for i in range(100))

#################################################

4. generator test

# color codes
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
m = "\033[1;36m"
w = "\033[1;37m"

# generator
def A(n):
    for i in range(n):
        yield i

# generator to iterable objects
print(w,"  generator object  ", r)
print(A(10) , '\n')

print(w,"  generator values to list.  ", g)
print(list(A(10)), '\n')

print(w,"  generator values to tuple  ", b)
print(tuple(A(10)), '\n')

print(w,"  generator values to set  ", p)
print(set(A(10)), '\n')

print(w,"  generator values to dict  ", m)
print(dict(zip(A(10),A(10))))

#################################################

5. map and filter with generator

def sq(n):
    return n ** 2

def is_even(n):
    return n % 2 == 0


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = map(sq, filter(is_even, l))

print(list(i))

#################################################

# generator

def sq(n):
    return n ** 2

def is_even(n):
    return n % 2 == 0

# generator comprehension
g = (sq(n) for n in l if is_even(n))

print(list(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#################################################

map နဲ့ filter ပေါင်းထားတာကို generator comprehension နဲ့ ပြန်ရေးပြထားတာပါ။
စုံကိန်းတွေကို စစ်ထုတ်ပြီး နှစ်ထပ်ကိန်းတင်ဖို့ ရေးထားတာပါ။

generator comprehension ကတော့ iterators တွေလိုပဲ တစ်ခါ ထုတ်ပြီးရင် ကုန်သွားပါတယ်။

လေးထောင့်ကွင်းထဲမှာ loop ပတ်ရင် list comprehension ဖြစ်ပါမယ်။

လက်သည်းကွင်းထဲမှာ loop ပတ်ရင် generator comprehension ဖြစ်ပါမယ်။

#################################################

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# generator generate iterator
def g(l):
    for n in l:
        if n % 2 == 0:
            yield n ** 2


g1 = g(l) # iterator
print(list(g1))
print(list(g1))

g2 = g(l) # iterator
print(list(g2))
print(list(g2))

#################################################

g က generator function

generator ဆိုတာက ထုတ်ပေးသူ

ဘာကို ထုတ်ပေးလဲဆိုတော့ iterators တွေထုတ်ပေးတာ။

generator obj တွေက ပုံမှန် iterators တွေနဲ့ အတူတူပါပဲ။

ထုတ်ရင် ကုန်သွားပါတယ်။

generator function ကတော့ အကြိမ်ကြိမ်သုံးနိုင်ပါတယ်။


စာရင်းထဲက စုံကိန်းတွေကို စစ်ထုတ်ပြီး နှစ်ထပ်ကိန်းတင်ဖို့ ရေးထားတဲ့ generator function ပါ။

#################################################
#################################################

# can use deepcopy to act like generator

i = map(sq, filter(is_even, l)) # 4, 16, 36, 64, 100

deep_copy = deepcopy(i) # create new refrence / new iterators 4, 16, 36, 64, 100

print("original 1st = ", next(i))    
print("deep copy 1st = ", next(deep_copy))
print("original 2nd = ", next(i))    
print("deep copy 2nd = ", next(deep_copy))
print("original 3rd = ", next(i))    
print("deep copy 3rd = ", next(deep_copy))
print("original 4th = ", next(i))    
print("deep copy 4th = ", next(deep_copy))
print("original 5th = ", next(i))    
print("deep copy 5th = ", next(deep_copy))

#################################################
#################################################

"""