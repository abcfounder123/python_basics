'''
# reducing 

# functions for iterables

# 1. primitive  functions --> iter, next ( function, magic method )
# 2. creation functions --> list, tuple, .. ( shallow copy )

# 3. transforming functions --> map, filter, enumerate, zip
# 4. reducing function --> sum, min

#################################################

# transforming iterables
# note ---> all function transform into iterators

# 1. enumerate(seq, start) ---> transform into tuple
# usage ---> count, loop count, index count,

# 2. zip(seq, seq, .... ) -->  transformed into tuple (terminates when shortest stream is exhausted))
# usage ---> to loop over more than one sequence / iterables, Create and update dictionaries

# 3. filter(fun, seq) ---> transform into  filtered results
# usage ---> to filter elements

# 4. map(fun, seq, seq, ... ) ---> transform into function results
# usage ---> for applying function to each element/s , for  lazy evaluation

# 5. reversed(seq) ---> transform into reversed result
# usage  ---> to reverse elements
# note ---> list already has reverse() method. eg. list.reverse()

################################################

Extra

# 6. sorted  ---> transform into sorted results
# result is not iterators   --> result is list                         <----------- WRANNING
# sorted(seq, key=key, reverse=False)

#################################################
#################################################

1. transforming,
2. reducing,
3. converting ( creation )
4. primitives အခြေခံကျ

################################################

2. reducing
   1. len
   2. sum
   3. min
   4. max
   5. any
   6. all
   7. custom reduce ( functools reduce )
   8. creating pip line with map and reduce ( for processing large data sets )
   9. map , filter and reduce
   10. our enumerate and reduce function
   11. enumerate and reduce

################################################

1. len

################################################

2. sum

# sum all elements
sum(iter, start=0)

# sum all int
x = [1, 2, 3]
print(sum(x, 0))  # 6
print(sum(x, 4))  # 10
print(sum(x, -4))  # 2

# sum all list
x = [1, 2, 3]
y = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# 0 + x + x + x
# error: can not add list and int
#sum(y, 0)


# [] + x + x + x
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
ans = sum(y, [])  # reduce 2D to 1D list
print(ans)

a = ['abc', 'pqr', 'xyz']

# can not sum str
# TypeError: sum() can't sum strings [use ''.join(seq) instead]
# s = sum(a, "")
s = ''.join(a) #  abcpqrxyz
print(s)

################################################

3. min

# return first minium obj

# min int
x = [1, 2, 3, 1]
ans = min(x)
print(ans) # 1


################################################

# min list
# compare list elements ( first, second, third , . . . )
y = [[1, 2, 3], [1, 2, 4], [1, 2, 1, 1]]
ans = min(y)
print(ans) # [1, 2, 1, 1]


################################################

x = list()

# empty list ( x )
#ValueError: min() arg is an empty sequence
#ans = min(x)

# default
# set default value to avoid error
ans = min(x, default=0)  # 0
print(ans)

ans = min(x, default=None)  # None
print(ans)

################################################

x = [
    "2023.04.11",
    "2022.01.12",
    "2021.02. 23"
]
def fun(l):
    return l[:4]

# key
# same as key of sorted function

# by year ( first four str )
ans = min(x, key=fun) # 2021.2. 3
print("minium year :", ans)

################################################

# by month ( index 5 and 6)
ans = min(x, key=lambda l: l[5:7]) # 2022.01.12
print("minium month :", ans)


# readability
from operator import itemgetter
# by month ( index 5 and 6)
ans = min(x, key=itemgetter(5, 6)) # 2022.01.12
print("minium month :", ans)

################################################

4. max

same as min function

################################################

5. any

# True if any of the elements have a true value.
# False if empty
print(any([1, 0, 2])) # 1 is True
print(any(['a', '', 'z'])) # a is True
print(any([0, '', False])) # all False
print(any([])) # empty is False

################################################

def my_any(iter):
    # initial value is False and search True
    ans = False
    for i in iter:
        if bool(i):
            ans = True
            break
    return ans

# same result
print(my_any([1, 0, 2]))
print(my_any(['a', '', 'z']))
print(my_any([0, '', False]))
print(my_any([]))


################################################

6. all

# True if all of the elements have a true value.
# True if empty
print(all([1, 0, 2])) # zero is False
print(all(['a', '', 'z'])) # empty str is False
print(all([1, 'a', True])) # all True
print(all([])) # empty is True

################################################

def my_all(iter):
    # initial value is True and search False
    ans = True
    for i in iter:
        if not bool(i):
            ans = False
            break
    return ans

print(all([1, 0, 2]))
print(all(['a', '', 'z']))
print(all([1, 'a', True]))
print(all([]))

################################################


7. custom reduce ( functools reduce )

def mul(a, b):
    return a * b

# reduce(fun, iter, initializer)
import functools, operator

a = [2, 3, 5, 2]
print(functools.reduce(operator.mul, a)) # 60 # same as sum
# (((2 * 3) * 5) * 2)

print(functools.reduce(lambda x, y: x * y, a, 10)) # 600

# ((((10 *2) * 3) * 5) * 2)

# with no initializer
# empty iter  ---> type error
# one element ---> return one element

# with initializer
# empty iter  ---> return initializer
# one element ---> return fun( initializer and one element )

################################################

8. creating pip line with map and reduce ( for processing large data sets )
9. map, filter and reduce ( sum, len )

strings = ['the', 'joy', 'of', 'coding', 'Python', 'should',
 'be', 'in', 'seeing', 'short', 'concise',
 'readable', 'classes', 'that', 'express', 'a',
 'lot', 'of', 'action', 'in', 'a', 'small', 'amount',
 'of', 'clear', 'code', 'not', 'in', 'reams', 'of',
 'trivial', 'code', 'that', 'bores', 'the', 'reader',
 'to', 'death']

lengths = map(len, strings)
#print(sum(lengths))

average = sum(lengths)/len(strings) # not pip

#average = sum(map(len, strings))/len(strings) # not pip

#################################################

# Ignoring short words
s = filter(lambda x : x not in ('a', 'the', "in", "of"), strings)
s = list(s)

# iter has no length and so we need to change list ( to use len function )
average = sum(map(len, s))/len(s) # not pip
#print(average)


#################################################

# len ကို သုံးဖို့ iter ကို sequence ပြောင်းရ
# ပုံမှန်ဆိုရင် ပြသနာမရှိပေမယ့် Wikipedia လိုမျိုး data အရမ်းများရင် memory မဆန့်

# iter ကို seq မပြောင်းဘဲ wikipedia ကနေ တစ်ကြိမ်တစ်ခုထုတ်
# ထုတ်ရင်းနဲ့ ရေတွက်

################################################

#10. our enumerate and reduce function

def sumcount(it):
    sum = 0
    count = 0
    for x in it:
        sum += x
        count += 1
        #print(sum, count)
    return sum, count

s = filter(lambda x : x not in ('a', 'the',  "in", "of"), strings)
# ['joy', 'coding', 'Python', 'should', 'be', 'seeing', 'short', 'concise', 'readable', 'classes', 'that', 'express',
# 'lot', 'action', 'small', 'amount', 'clear', 'code', 'not', 'reams', 'trivial', 'code', 'that', 'bores', 'reader', 'to', 'death']
total, count = sumcount(map(len, s))
average = total/count
print(average)

#################################################

#11. enumerate and reduce

# ရေတွက်ဖို့ enumerate သုံးနိုင်
s = filter(lambda x : x not in ('a', 'the',  "in", "of"), strings)
m = map(len, s)
#e = enumerate(m, 1) # ( count, len )

# sum count
# fp use no loop
def opsumcount(a, b):
    # print(a, b, end="--> ")
    sum = a[1] + b[1]
    count = b[0]
    # print(count, sum)
    return count, sum
import functools
count, total = functools.reduce(opsumcount, enumerate(m, 1)) # tuple ---> (count, value) --> ( 1, 3) --> ( 2, 6 ) --> ( 2, 9)
print(total, count)
average = total/count
print(average)

################################################

'''
