
'''
# iterators
# iterate over a series of value ( one after the other ) ( one / next one / next one / .... )
# iterators can iterate one time.

def sq(n):
    #print(f"sq({n})")
    return n ** 2

x = [1, 2, 3, 4, 5] # list ---> iterable obj
i = map(sq, x) # map object , iterators


print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i)) # no item in iterator
# print(next(i)) # StopIteration

for a in i:
    print("loop =", a)


ans = []

for a in x:
    ans.append(sq(a)) # 5
    
print(ans)



#################################################

# iterables objects ( __next__() ) ( list, tuple, str, range ) --> sequences ( mutable seq and immutable seq ) ( each element with index )
# iterators can be create with iterables by using iter function.
# using for loop with iterables, it will create new iterator in each loop. ( new iterator in each loop )

x = [1, 2, 3, 4, 5]

i = iter(x) # list_iterator object

print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

#################################################

x = range(1, 6)
i = iter(x) # range_iterator
print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


#################################################

# iterators to sequence ( list, unpacking iterable, tuple, .... ) ( no values left in iterator )
# ( many purposes --> to find length, use more than once, access different order, to print, ... )


x = [1, 2, 3, 4, 5]

i = iter(x) # list_iterator
print(i)
# print(next(i))

l = list(i) # iterator  --> mutable sequence ( list ) --> ( no values left in iterator )
print(l)


x = [1, 2, 3, 4, 5]

i = iter(x) # list_iterator
print(i)

l = [*i] # unpack iter in a list
print("unpack result =", l)


#################################################

# lazy evaluation

class Fib:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        f = self.a
        self.a, self.b = self.b , self.a + self.b
        return f

iterator1 = Fib()
iterator2 = Fib()

print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))

print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))

n = 0

for i in iterator:
    print(f"fib {n} = {i}.")
    if n == 5:
        n += 1
        break
    n += 1


for i in iterator:
    print(f"fib {n} = {i}.")
    if n == 10:
        n += 1
        break
    n += 1


for i in iterator:
    print(f"fib {n} = {i}.")
    if n == 15:
        n += 1
        break
    n += 1

#################################################


class Fib:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        f = self.a
        self.a, self.b = self.b , self.a + self.b
        return f

iterator1 = Fib()
iterator2 = Fib()

for n, i in enumerate(iterator1, 0):
    print(f"fib {n} = {i}")
    if n == 1000:
        break
    n += 1


for n, i in enumerate(iterator2, 0):
    print(f"fib {n} = {i}.")
    if n == 5:
        break
    n += 1

for n, i in enumerate(iterator2, 6):
    print(f"fib {n} = {i}.")
    if n == 10:
        break
    n += 1


#################################################

# 0, 1, 1, 2, 3, 5, 8

# lazy evaluation
a = 0
b = 1
def fib():
    print("evaluation")
    global a, b
    f = a
    a, b = b, a + b
    return f

for n in range(1000):
    print("loop")
    print(f"fib {n} = {fib()}.")


#################################################

# functions for iterables
# 1. primitive  functions --> iter, __next__ ( function, magic method )
# 2. creation functions --> list, tuple, .. ( shallow copy )
# 3. transforming functions --> map, filter, enumerate, zip
# 4. reducing function --> sum, min

def f(n):
    
    return chr(n)

x = [65, 66, 67, 68, 69]

i = map(f, x) # map object

#print(next(i))

print(x)
print(list(i))


#################################################

def add(n1, n2, a, b):
    return n1 + n2 + a + b

x = [1, 2, 3, 4, 5]
y = [5, 6, 8, 3, 1]
a = [1, 2, 3, 4, 5]
b = [5, 6, 8, 3, 1]

i = map(add, x, y, a, b) # map object with 2 args
#l = list(i)
#print(l)
print(x + y)


print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
#print(next(i))

#################################################

def even(n):
    #print("evalute", n)
    return n % 2 == 0

x = range(1, 11)

i = filter(even, x)
print(i)

l = list(i)
print(l)


print(next(i))
print(next(i))

def even(n):
    n1, n2 = n
    #print("evalute", n)
    return n1 % 2 == 0 and n2 % 2 == 0

x = [(1, 1), (2, 2), (3, 3), (6, 4)]


i = filter(even, x)
print(i)

print(next(i))
print(next(i))

#################################################

x = [1, 2, 3, 4, 5]
y = ["apple", "banana", "orange"]
i = enumerate(y, 1) # counting number
print(i)
print(next(i))
print(next(i))

#################################################

x = [1, 2, 3, 4, 5]
x = [1, 2, 3, 4, 5]
x = [1, 2, 3, 4, 5]
x = [1, 2, 3, 4, 5]
i = zip(x, x, x, x)
print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


a = b = c = d = [1, 2, 3, 4, 5]
a, b, c, d, e = zip(a, b, c, d)
print(a)
print(b)
print(c)
print(d)
print(e)
print()

a, b, c, d = zip(a, b, c, d, e)
print(a)
print(b)
print(c)
print(d)

a = b = c = d = [1, 2, 3, 4, 5]
a, b, c, d = zip(*zip(a, b, c, d))
print(a)
print(b)
print(c)
print(d)


#################################################


sub = ["myanmar", "english", "math", "chemistry", "physics", "bio"]
marks = [10, 20, 30, 40, 50, 80]
i = zip(marks, sub)
l = list(i)
print(l)

# zip(zip())
z = [(10, 'myanmar'), (20, 'english'), (30, 'math'), (40, 'chemistry'), (50, 'physics'), (80, 'bio')]
# unpack data --> a, b, c, d, e, f = z
o = zip(*z)
m, s = o
print(m)
print(s)


#################################################

# zip( zip() )
sub = ["myanmar", "english", "math", "chemistry", "physics", "bio"]
marks = [10, 20, 30, 40, 50, 80]
s, m = zip(*zip(sub, marks))
print(s)
print(m)

#################################################
#################################################

# reduce function ( sum, min, max )

marks = [10, 20, 30, 40, 50, 80]
total = max(marks)
print(total)

#################################################

# lambda x, y: x + y
def a(n1, n2):
    return n1 + n2

from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(a, numbers)

print(total)

#################################################

# lambda x, y: x + y
def a(n1, n2):
    print(f"a({n1}, {n2})")
    return n1 + n2

def f(f2, l):
    print(f"f({f2}, {l})")
    if not l:
        return 0
    else:
        return f2(l[0],  f(f2, l[1:]))

numbers = [1, 2, 3, 4, 5]
total = f(a, numbers)

print(total)

#################################################
#################################################
'''


'''

#################################################

# transforming iterables
# note ---> all function result ---> iterators

# 1. enumerate(seq, start) ---> transform into tuple
# usage ---> element count, loop count, index count, 

# 2. zip(seq, seq, .... ) -->  transformed into tuple (terminates when shortest stream is exhausted))
# usage ---> to loop over more than one sequence / iterables, Create and update dictionaries

# 3. filter(fun, seq) ---> transform into  filtered results
# usage ---> to filter elements 

# 4. map(fun, seq, seq, ... ) ---> transform into function results
# usage ---> for applying function to each element/s , for  lazy evaluation

# 5. reversed(seq) ---> transform into reversed result
# usage  ---> to reverse elements
# note ---> list already has reverse() method. eg. list.reverse()

Extra

# 6. sorted  ---> transform into sorted results
# result is not iterators   --> result is list                         <----------- WRANNING
# sorted(seq, key=key, reverse=False)

#################################################

# 1. enumerate(seq, start) ---> transform into tuple
# usage ---> element count, loop count, index count, 

y = ["apple", "banana", "orange"]

# transform into tuple
for t in enumerate(y, 1):
    print(f"transformed result = {t}")

# counting index
for index, value in enumerate(y):
    print(f"index of {value} = {index}")


# loop count
for count, value in enumerate(y, 1):
    print("loop count =", count)
    print(value)


#################################################

# 2. zip(seq, seq, .... ) -->  transformed into tuple (terminates when shortest stream is exhausted))
# usage ---> to loop over more than one sequence / iterables, Create and update dictionaries

fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
for i in zip(fields, values):
    print(i)


fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
d = dict(zip(fields, values)) # iterators to sequence ( dict )
print(d)


l = [('name', 'John'), ('last_name', 'Doe'), ('age', '45'), ('job', 'Python Developer')]
d = dict(l)

l = list(d.items())
print(l)

#################################################

# 3. filter(fun, seq) ---> transform into  filtered results
# usage ---> to filter elements 


def f(n):
    return n > 5

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = list(filter(f, n))
print(i)


n = ["apple", "banana", "orange", "abc"]
i = list(filter(lambda n: len(n) <= 5, n))
print(i)

d = {"apple": 100, "banana": 1000, "orange": 3000}
fd = dict(filter(lambda n: n[1] > 100, d.items())) # ("apple", 100)

print(fd)


#################################################

# 4. map(fun, seq) ---> transform into function results
# usage ---> for applying function to each element/s , for  lazy evaluation


def f(n):
    return n - 1

l = [2, 4, 6, 8]
i = list(map(f, l))
print(i)


def f(n1, n2):
    return n1 + n2

l = [2, 4, 6, 8]
l2 = [1, 2, 3, 4]
i = list(map(f, l, l2))
print(i)

# lazy evaluation
def discount_10(item_price): # ("Note.10", 400000)
    print("evaluate ......")
    item, price = item_price
    if price >= 600000: 
        price = price * 0.9
    return (item, price)

d = {"Note.10": 400000, "Note.11": 500000, "Note.12": 600000, "Note.12 5G": 700000, "Note.12 pro": 800000}

discount = map(discount_10, d.items())
print(next(discount))
print(next(discount))

discount = dict(map(discount_10, d.items()))
print(discount)



#################################################

# lazy evaluation
def add_20_percent(item_price):
    print("evalute", item_price)
    item, price = item_price
    return item, price * 1.2

# iterators to sequence
d = {"Note.10": 400000, "Note.11": 500000, "Note.12": "Na", "Note.12 5G": 700000, "Note.12 pro": 800000}
#print(items)


discount = map(add_20_percent, d.items())
print(next(discount))
print(next(discount))
print(next(discount))

items_new_price = dict(map(add_20_percent, d.items()))
print(items_new_price)

#################################################

# 5. reversed(seq) ---> transform into reversed result
# usage  ---> to reverse elements
# note ---> list already has reverse() method. 

x = (1, 2, 5, 4)
reverse_x = reversed(x)

print(next(reverse_x))
#for i in reverse_x:
#    print(i)

# iterators to sequence 
print(tuple(reverse_x))

#################################################

# middle seven

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
n = 7 
m = len(x) // 2
s = m - n//2
stop = m + n//2
y = x[s:stop] # middle 7 elements
print(y)


r_y = list(reversed(y))
print(r_y)

print(y[::-1])

#################################################

# not iterators   --> result is list
# sorted(iterable, key=key, reverse=False)  
# 6. sorted  ---> transform into sorted results


dates = [
 '2019/04/06',
 '2017/04/15',
 '2019/03/21',
 '2018/04/10',
 '2019/04/08',
 '2017/03/20',
 '2018/06/30',
 '2019/09/30',
 '2018/04/11',
 '2017/03/14']

s = sorted(dates) # by year, month, date # ascending
print(s)


s = sorted(dates, reverse=True) # by year, month, date # descending
print(s)

s2 = sorted(dates, key=lambda x: x[5:7])# sort by month
print(s2)

#################################################

# to readablity

from operator import itemgetter

dates = [
 '2019/04/06',
 '2017/04/15',
 '2019/03/21',
 '2018/04/10',
 '2019/04/08',
 '2017/03/20',
 '2018/06/30',
 '2019/09/30',
 '2018/04/11',
 '2017/03/14']

s2 = sorted(dates, key=itemgetter(5, 6))# sort by month ( index 5 and 6 )
print(s2)


s2 = sorted(dates, key=lambda x: x[5:7])# sort by month
print(s2)


def add_2_1(s):  # 2019/04/06
    k = int(s[-2]) + int(s[-1])  # 0 + 6
    print(k)
    return k

s2 = sorted(dates, key=add_2_1)# sort by addition of last two chr
print(s2)

#################################################

# selection sort 
s2 = sorted(dates, key=itemgetter(0, 1, 2, 3, 5, 6, 8, 9))
print(s2)

select = [0, 1, 2, 3, 5, 6, 8, 9]
s2 = sorted(dates, key=itemgetter(*select))
print(s2)

#################################################

#  sort by unicode charactor
fruits = ['Banana', 'apple', 'Apricot', 'Clementine', 'avocado']

sorted_fruits = sorted(fruits)
print(sorted_fruits)

# sort by code No ( unicode )
# ['Apricot', 'Banana', 'Clementine', 'apple', 'avocado']

#################################################




fruits = ['Banana', 'apple', 'Apricot', 'Clementine', 'avocado', 'ab']

sorted_fruits = sorted(fruits, key=lambda x: x.lower()) # sort by all alphabet
print(sorted_fruits)


sorted_fruits = sorted(fruits, key=lambda x: x[0].lower()) # sort by first chr
print(sorted_fruits)

# sort by all alphabet ( code No of lower characters )
#['ab', 'apple', 'Apricot', 'avocado', 'Banana', 'Clementine']
#['apple', 'Apricot', 'avocado', 'ab', 'Banana', 'Clementine']  < --- sort by first chr

#################################################

# to readablity


from operator import methodcaller

fruits = {'Banana', 'apple', 'Apricot', 'Clementine', 'avocado', 'ab'}

sorted_fruits = sorted(fruits, key=lambda x: x.lower()) # sort by all alphabet
print(sorted_fruits)

sorted_fruits = sorted(fruits, key=methodcaller("lower"))
print(sorted_fruits)



#['ab', 'apple', 'Apricot', 'avocado', 'Banana', 'Clementine']

#################################################

# reverse=True
reverse_sorted_fruits = sorted(fruits, key=methodcaller("lower"), reverse=True)
print(reverse_sorted_fruits)

#['Clementine', 'Banana', 'avocado', 'Apricot', 'apple', 'ab']

#################################################

# obj.method() 
#After f = methodcaller('name'), the call f(b) returns b.name().


# obj.method("positional argument", bar="keyword argument")
#f = methodcaller('name', 'foo', bar=1), the call f(b) returns b.name('foo', bar=1).    


from operator import methodcaller
# step.1
f = methodcaller('upper') # f(x) returns x.upper().

x = "apple"
c = x.upper() # method call ( oop )
c2 = f(x)     # function call( fun )

print(c)
print(c2)


# step.2 ( method with positional argument )
pf = methodcaller('pop', 0) # f(obj) returns obj.pop(3).
l = [1, 2, 3, 4, 5]

p = l.pop(0) # method call ( oop )
#p = pf(l)   # function call( fun )

print(p)
print(l)

#######

from operator import methodcaller

class A:
    def __init__(self, l):
        self.data = l
        
    def c_sort(self, *, reverse):
        # print("c_sort")
       
        return sorted(self.data, reverse=reverse)
        

x = A(l=[5, 2, 3, 1, 4])

# step.3 ( method with keyword argument )
sf = methodcaller('c_sort', reverse=False) # f(obj) returns obj.c_sort(reverse=False).
rsf = methodcaller('c_sort', reverse=True) # f(obj) returns obj.c_sort(reverse=True)

s = x.c_sort(reverse=False)
s2 = sf(x)

rs = x.c_sort(reverse=True)
rs2 = rsf(x)

print(s)
print(s2)
print(rs)
print(rs2)

#######

from operator import methodcaller


class A:
    def __init__(self, l):
        self.data = l
        
    def t(self, *args, **kwargs):
        print(args)
        print(kwargs)
        
        

x = A(l=[5, 2, 3, 1, 4])

# step.4 ( method with positional and keyword argument )
f = methodcaller('t', 1, 2, "apple", 1.2, name="Mg Mg", age=10) 

x.t(1, 2, "apple", 1.2, name="Mg Mg", age=10)
f(x)



x = 3
r = x + 1
r2 = x.__add__(1) # def __add__(self, other): 
print(r)
print(r2)


from operator import methodcaller

def add(e):
    return e + 1

f1 = [3, 2, 5, 1]

all_f = map(methodcaller("__add__", 1),  f1) # x // 2

print(list(all_f))


#################################################

from operator import add

x = 3

r = x + 1          # literal
r2 = x.__add__(1)  # OOP
r3 = add(x, 1)     # function

def a(n1, n2):
    return n1 + n2

r4 = a(x, 1)     # function

print(r)
print(r2)
print(r3)
print(r4)


def a(n1, n2, n3, n4):
    return n1 + n2 + n3 + n4

f1 = [3, 2, 5, 1]
f2 = [3, 2, 5, 1]
f3 = [3, 2, 5, 1]
f4 = [1, 2, 3, 4]

all_f = map(a, f1, f2, f3, f4) # 2 args
#print(next(all_f))
#print(next(all_f))
print(list(all_f))


all_f2 = map(lambda n1, n2, n3, n4 : n1 + n2 + n3 + n4, f1, f2, f3, f4) # custom nameless function to add 3 args
print(list(all_f2))


def f(*numbers): 
    total = 0
    for number in numbers:
        total += number
    return total

all_f = map(f, f1)
print(list(all_f))

all_f = map(f, f1, f2)
print(list(all_f))

all_f = map(f, f1, f2, f3)
print(list(all_f))

all_f = map(f, f1, f2, f3, f4)
print(list(all_f))



####


#################################################


f1 = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]    
f2 = [('apple', 4), ('banana', 2), ('pear', 5), ('orange', 1)]
f3 = [('apple', 5), ('banana', 2), ('pear', 5), ('orange', 1)]


all_f = map(lambda x, y, z: (x[0], x[1] + y[1] + z[1]), f1, f2, f3)
print(list(all_f))

def fun(x, y, z):
    return x[0], x[1] + y[1] + z[1]

all_f = map(fun, f1, f2, f3)
print(list(all_f))


#################################################
#################################################

# အားလံုး‌ေပါင်းရန်
# first room ကို total list ပို့ရန်


# structured programming

f1 = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
f2 = [('pear', 5), ('orange', 1), ('apple', 3), ('banana', 2), ('mangoes', 10)]
f3 = [('apple', 4), ('banana', 2), ('pear', 5), ('orange', 1), ('strawberry', 10)]
f4 = [('orange', 1), ('pear', 5), ('banana', 2), ('apple', 4), ('mangoes', 10), ('strawberry', 10)]

# all_f =  [('apple', 14), ('banana', 8), ('pear', 20), ('orange', 4), ('mangoes', 20), ('strawberry', 20)]

all = f1 + f2 + f3 + f4
print(all)

d = dict() 
for i in all: # ('apple', 3)
    fruit, count = i
    if fruit not in d:
        d[fruit] = count
    else:
        d[fruit] += count

print(d)
# print(list(d.items()))


def sent(sub, super):
    ans = list()
    for i in sub: # ('apple', 3)
        item = i[0]
        new = (item, super[item])
        ans.append(new)
    return ans

print(sent(f1, d))
print(sent(f2, d))
print(sent(f3, d))
print(sent(f4, d))


#################################################

s_f1 = list()
for i in f1:
    fruit, count = i
    new = (fruit, d[fruit])
    s_f1.append(new)
        
print(s_f1)

#################################################
#################################################

#####################

# copying values of iterators
# shallow copy and deep copy

from copy import copy, deepcopy

def sq(n):
    #print(f"sq({n})")
    return n ** 2

def is_even(n):
    #print(f"is even({n})")
    return n % 2 == 0

#####################

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

f = filter(is_even, l) # 2, 4, 6, 8, 10

i = map(sq, f) # 4, 16, 36, 64, 100


#shallow_copy = i  # same refrence
shallow_copy = copy(i) # same refrence

#####################

print("original 1st = ", next(i))
print("copy 1st = ", next(shallow_copy))
print("original 2nd = ", next(i))
print("copy 2nd = ", next(shallow_copy))

print(" -" * 21)

#################################################

# fp with oop

# 1. attrgetter ( access )
# 2. itemgetter                       
# 3. methodcaller

from operator import attrgetter

class PetrolEngine:
    def __init__(self):
        self.name = "petrol engine"
    
class Car:
    count = 0

    def __init__(self, price):
        self.engine = PetrolEngine()
        self.color = "blue"
        self.price = price
        Car.count += 1
        self.bin = Car.count

    def __repr__(self):
        return f"Car No : {self.bin} ( {self.price} $ )"

cars = list()
for i in range(1, 11):
    cars.append(Car(i * 100000))

#f = attrgetter("price")
#print(f(cars[5]))

def f(obj):
    return obj.price

sort_by_price = sorted(cars, key=attrgetter("price"), reverse=True)
#print(sort_by_price)

expensive_5 = sort_by_price[:5]
#print(expensive_5)

cheap_5 = sort_by_price[-5:]
#print(cheap_5)


# change attr value
def change_price(obj):
    obj.price *= 0.9
    return obj

def price_more_than_500000(obj):
    return obj.price > 500000

f = filter(price_more_than_500000, cars) # 600000
discount_cars = map(change_price, f)
#print(list(discount_cars))
#print(cars)


#discount_cars = list(map(change_price, filter(price_more_than_500000, cars)))
#print(discount_cars)

discount_cars = list(map(change_price, filter(lambda obj: obj.price > 500000, cars)))
print(discount_cars)




# step.1 ( acess attribute )
car = Car(500000)

print(car.bin)
print(car.price)
print(car.color)

f = attrgetter("bin") # obj.bin
f2 = attrgetter("price")
f3 = attrgetter("color")

print(f(car))
print(f2(car))
print(f3(car))


# step.2
f = attrgetter("bin", "price", "color") # (1, 500000, 'blue')

# step.3
f = attrgetter("engine.name") # obj.engine.name

def f2(obj):
    return obj.engine.name

print(car.engine.name)
print(f(car))
print(f2(car))


#################################################
#################################################

Standard operators as functions                                                              < ---------- left

After f = attrgetter('name'), the call f(b) returns b.name.
After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last).

def resolve_attr(obj, attr):
    for name in attr.split("."):
        obj = getattr(obj, name)
    return obj

def attrgetter(*items): # ("bin", "price", "color")
    if any(not isinstance(item, str) for item in items):
        raise TypeError('attribute name must be a string')
    if len(items) == 1:
        attr = items[0] # upper
        
        def g(obj):
            return resolve_attr(obj, attr)
    else:
        def g(obj):
            return tuple(resolve_attr(obj, attr) for attr in items)
    return g

#################################################

"""

from operator import itemgetter

l = ["apple", "banana", "orange"]
 
def itemgetter2(*items): # (1, )
    if len(items) == 1:
        item = items[0] # 1
        def g(obj):
            return obj[item] # l[1] # "banana"
    else:
        def g(obj):
            return tuple(obj[item] for item in items) # (0, -1)
    return g


t2 = itemgetter2(1)

print(l[1])
print(t2(l))


"""

#################################################

# result   --->   element or tuple
# 1. dict  ---> itemgetter(key) , (key, key, ... ) 
# 2. list   ---> itemgetter(index), ( index, index, ... )
    
#################################################

def methodcaller(name, /, *args, **kwargs):
    def caller(obj):
        return getattr(obj, name)(*args, **kwargs)#getattr("apple", "upper")() # "apple".upper()
    return caller


upper_2 = methodcaller("upper")

#def upper_2(obj):
#    return getattr(obj, "upper")()


def upper_1(s):
    return s.upper()


s = "apple"
u = s.upper() # oop method
u2 = upper_1(s) # normal fun
u3 = upper_2(s)# 
#getattr("apple", "upper")() 
# "apple".upper()


print(u)
print(u2)
print(u3)




def methodcaller(name, /, *args, **kwargs):# args=(2, ), kwargs={}
    def caller(obj):
        return getattr(obj, name)(*args, **kwargs)#getattr("apple", "upper")() # "apple".upper()
    return caller


add_2 = methodcaller("__add__", 1)

#def add_2 (obj):
#    return getattr(obj, "__add__")(1) # obj.__add__(1)


def add_1(n1):
    return n1 + 1


x = 3

r = x + 1          # literal
r2 = x.__add__(1)  # OOP
r3 = add_1(x)     # function
r4 = add_2(x)

print(r)
print(r2)
print(r3)
print(r4)



#1. sample of attrgetter function with one argument
def atg(attr):
    def c(obj):
        return getattr(obj, attr)
    return c

# same version ---> attrgetter
def atgs(*attr):
    def c(obj):
        if len(attr) == 1:
            return getattr(obj, attr[0])
        elif len(attr) > 1:
            v = []
            for a in attr:
                v.append(getattr(obj, a))
            return v
    return c



#################################################
#################################################         


from operator import methodcaller

add_2 = methodcaller("__mul__", 2)

#def add_2 (obj):
#    return getattr(obj, "__add__")(1) # obj.__add__(1)

#def add_2 (obj):
#    return getattr(obj, "__sub__")(1) # obj.__sub__(1)

#def add_2 (obj):
#    return getattr(obj, "__mul__")(2) # obj.__mul__(2)

x = 3

r1 = x.__mul__(2)  # OOP
r2 = add_2(x)      # func

print(r1)
print(r2)

##########

def methodcaller(name, /, *args, **kwargs):# args=(2, 3), kwargs={"name":"mg mg", "age": 18}
    def caller(obj):
        return getattr(obj, name)(*args, **kwargs)#getattr(obj, "upper")() # obj.upper()
    return caller

# methodcaller("__mul__", 2, 3, name="mg mg", age=18)

args = (2, 3)
kwargs={"name":"mg mg", "age": 18}

print(args)
print(*args)

print(kwargs)

print(*kwargs) # print("name", "age")
#print(**kwargs) # print(name="mg mg", age=18)
#print(*args, **kwargs) # print(2, 3, name="mg mg", age=18 )

###########

args = (2, 3, "apple", 1.2)
kwargs={"end":" ---> \n", "sep": " -> "}

print(*args, **kwargs) # print(2, 3, "apple", 1.2, end= " ---> \n", sep= " -> ")

###########

args = (2,)
kwargs={}

print(*args, **kwargs) # print(2)

'''



# methodcaller ( obj.fun(arg, kwargs) ---> fun(obj) )

# itemgetter ( obj[-1] ---> fun(obj) )

# attrgetter ( obj.data  ---> fun(obj) )







