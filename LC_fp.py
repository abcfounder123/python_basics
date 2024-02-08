'''
1. introduction

LC is python idiom.
# ဗန်းစကား / ရိုးရာစကား

# loop
# need to check
a = []
for i in range(100):
    a.append(str(i))

print(a)
# map
# no need to check and result is sure
a = list(map(str, range(100)))
print(a)

# list comprehension
# like normal sentence
# use to make list from other iterable obj
# make a list of str(i) for all values of i in range(100)
a = [str(i) for i in range(100)]
print(a)

#################################################

k = [12, 33, 49, 57]
a = []
for x in k:
    a.append(round(x/5)*5)

k = [12, 33, 49, 57]
a = list(map(lambda x: round(x/5)*5, k))

k = [12, 33, 49, 57]
# make a list of round(x/5)*5 for all values of x in  k
a = [round(x/5)*5 for x in k]

#################################################

2. using conditions

k = [-1, 16, 9, -4, 0, 25]
a = []
for x in k:
    if x > 0:
        a.append(x ** 2)
print(a)

a = list(map(lambda x: x**2, filter(lambda x: x > 0, k)))
print(a)
# make a list of squar(x) for all values of x in  k, but only if x greater than zero
a = [x**2 for x in k if x > 0]

print(a)

#################################################

3. nested comprehensions
creating 2D list

[[x for x in range(3)] for y in range(4)]
[[0, 1, 2] for y in range(4)]

[[0, 1, 2],
[0, 1, 2],
[0, 1, 2],
[0, 1, 2]]

[[x + 10*y for x in range(3)] for y in range(4)]
[10*y, 1+10*y, 2+10*y]

[[0, 1, 2],
[10, 11, 12],
[20, 21, 22],
[30, 31, 32]]

outer = []
for y in range(4):
    inner = []
    for x in range(3):
        inner.append(x+10*y)
    outer.append(inner)

#################################################

ans = [[x + 10*y for x in range(y)] for y in range(4)]

[[],
[10],
[20, 21],
[30, 31, 32]]

#################################################

4. creating a flat list
[x + 10*y for x in range(3) for y in range(4)]

outer = []
for x in range(3):
    for y in range(4):
        outer.append(x+10*y)

[0, 10, 20, 30, 1, 11, 21, 31, 2, 12, 22, 32]

# py translate left to right
# barracks is inner list ( inner loop )
# need to change position if you do not use barracks
ans = [[x + 10*y for x in range(3)] for y in range(4)]
print(ans)
ans = [x + 10*y for y in range(4) for x in range(3)]
print(ans)

[[0, 1, 2], [10, 11, 12], [20, 21, 22], [30, 31, 32]]
[0, 1, 2, 10, 11, 12, 20, 21, 22, 30, 31, 32]

#################################################
#################################################
'''