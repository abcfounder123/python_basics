
"""

phrase = input("Enter a phrase: ") # "a Ba."
clean_list = []

for charactor in phrase.lower():
    if charactor.isalnum() and charactor != " ":
        clean_list.append(charactor)

palindrome = clean_list == clean_list[::-1]

if palindrome:
    print(f"\"{phrase}\" is a palindrome.")

else:
    print(f"\"{phrase}\" is not a palindrome.")



space = " "
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
rm_list = space + punctuations

phrase = input("Enter a phrase: ") # "a Ba."
clean_list = []

for charactor in phrase.lower():
    if charactor not in rm_list:
        clean_list.append(charactor)

palindrome = clean_list == clean_list[::-1]

if palindrome:
    print(f"\"{phrase}\" is a palindrome.")

else:
    print(f"\"{phrase}\" is not a palindrome.")


#palindrome
# x == x[::-1]
# "" in rm_list
# str.lower() , upper()
# x == x[::-1]

def paldrome_check(phrase):
    space = " "
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    rm_list = space + punctuations

    clean_list = []

    for charactor in phrase.lower():
        if charactor not in rm_list:
            clean_list.append(charactor)

    palindrome = clean_list == clean_list[::-1]

    if palindrome:
        return f"\"{phrase}\" is a palindrome."

    else:
        return f"\"{phrase}\" is not a palindrome."


# test
check_list = {"A man, a plan, a canal, Panama!": "\"A man, a plan, a canal, Panama!\" is a palindrome.",
              "Hello, World!": "\"Hello, World!\" is not a palindrome.",
              "121": "\"121\" is a palindrome.",
              }

for q, ans in check_list.items():
    print(ans == paldrome_check(q))



A man, a plan, a canal, Panama!

Hello, World!



Enter a phrase: A man, a plan, a canal, Panama! <enter>
"A man, a plan, a canal, Panama!" is a palindrome.

Enter a phrase: Hello, World! <enter>
"Hello, World!" is not a palindrome.
"""








"""

# when calling function ---> 2 (pos , key name)   <-----


# default parameter
# *  ---> packing pos argv
#    ---> unpacking collection
# ** ---> packing kwargvs
#    ---> unpacking dict, 
#    


def add(**n):# pack
    total = 0
    for i in n.values():
        total += i

    return total


day1 = add(item1=10, item2=200, item3=300)
print(day1)

day1_list = {"item1": 10, "item2": 200, "item3": 300}
year1_list = {"item1": 1000, "item2": 20000, "item3": 300000}


print(add(**day1_list))
print(add(**year1_list))

"""


"""

#######

# when calling function ---> 2 (pos , key name)   <-----

def x(a, b, c):
   pass
   
x(1, 2, 3)
x(a=1, b=2, c=3)
x(1, 2, c=3)

#######

# *  ---> packing pos argv
#    ---> unpacking collection
# ** ---> packing kwargvs
#    ---> unpacking dict,  

#######

parameters 
1. normal parameters
2. default parameters
3. special parameters 

#######

4.8.3. Special parameters
4.8.3.1. Positional-or-Keyword Arguments   --->   /    *
4.8.3.2. Positional-Only Arguments         --->   p    /
4.8.3.3. Keyword-Only Arguments            --->   *    p
4.8.3.4. Function Examples
4.8.3.5. recap အနှစ်ချုပ်                      --->   p / standard * kw

#######

def name(a:int, b:int, c:int, /, d, e, f, *, x, y, z:float, name:str, j=0, i=0) -> dict:
    ans = dict()
    return ans
    
   
1. normal parameters  -->  a, b, c, d, e, f, x, y, z
2. default parameters -->  j, i
3. special parameters -->  /, *

groups --> pos only, standard,  kw only

#######

4.9. Coding Style
1. 4 space
2. not exceed 79 characters
3. blank lines
4. comment
5. docstrings
6. space ---> operator, comma   ( eg. l = [1, 2, 3] )
7. UpperCamelCase ---> class name  ( eg. class DroneVehicale(): )
8. lowercase_with_underscores  ---> function, method ( eg. def fly_drone(): )
9. self  --->   first parameter of method  ( eg.   def fly_drone(self, a, b, c): )
10. UTF-8
11. identifier ---> ASCII



#######

5. list

1. list as stacks
( last_in , first_out )
---> append()
---> pop()


box = []
box.append(1)
box.append(2)
box.append(3)
box.append(4)
print(box)

box.pop()
print(box)

box.pop()
print(box)

box.pop()
print(box)

box.pop()
print(box)


#######

2. list as queues  ( first_in, first_out )
---> deque from collections
---> popleft()

from collections import deque

que = []
que = deque(que)
que.append(1)
que.append(2)
que.append(3)
que.append(4)
print(que)

print(que.popleft())
print(que)

print(que.popleft())
print(que)

print(que.popleft())
print(que)

print(que.popleft())
print(que)


3. list comprehensions

"""
# data accept
l = [1, 2, 3, 4, 5, 6, 7, 8]
square = []

#calculate square
for i in l:
    if i % 2 == 0:
        square.append(i ** 2)
    
print(square) # show result

s = [i ** 2 for i in l if i % 2 == 0]
print(s)







"""
def f(a:int, b:int, c:int, /, x, y, z, *, name:str, age:int, ph:str) -> dict:
    ans = dict()
    return
    
f("a", 2, 3, 1, 2, z=3, name="mg mg", ph="09123456", age=20)

print(f.__annotations__)

"""