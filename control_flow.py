
'''
control flow

1.statements
  a.normal statements
  b.conditional statements

2.if, else, elif
  >> can only interact with boolean data type
  a.if       --->   True
  b.else     --->   False
  c.elif     --->   else + if  --->  False + True

3.Type casting
  a.implicit type casting    --->   type casting by Py, indirect type casting
  b.explicit type casting    --->   type casting by programmer, direct type casting

4.boolean value from
  a.auto type casting
  b.function
  c.comparison operator

5.finding code block

6.control flow of automatic water motor controller

7.exercise
add motor No.4 

################################################

1.statements
a.normal statements

print("a")
print("b")

################################################

b.conditional statements

condition1 = True
condition2 = False

if condition1:print("a")
if condition2:print("b")

################################################

2.if, else, elif

a.if       --->   True

if True:print("abc")

################################################

b.else     --->   False

if False:
    pass
else:
    print("abc")

################################################

c.elif     --->   else + if  --->  False + True

if False:
    pass
elif True:
    print("abc")
else:
    pass

################################################

3.Type casting

3.a.implicit type casting, indirect type casting, auto type casting by Python

# int data type to boolean data type by Python
if 1:print("b")

################################################

3.b.explicit type casting, direct type casting, type casting by programmer

# int data type to boolean data type by programmer
if bool(1):print("a")

################################################

4.a.boolean value from auto type casting

conditions to become True
>> int, float, complex                       ---> not zero
>> group (str, list, tuple, dict, set, ...)  ---> not empty

fruit = input("Enter a fruit: ")
if fruit:
    print(fruit, "is 10 Myanmar Kyats.")
else:
    print("Empty string.")

################################################

4.b.boolean value from function

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0
    
    
n = int(input("Enter a number: "))
if is_even(n):
    print(n, "is an even number.")
else:
    print(n, "is an odd number.")
    
################################################
    
4.c.boolean value from comparison operator

n = int(input("Enter a number: "))
if n % 2 == 0:
    print("even")
else:
    print("odd")

################################################

5.finding code block

c1 = True
c2 = True
c3 = False

if c1:
    if c2:
        if c3:
            pass
        else:
            print("abc")
    else:
        if c3:
            pass
        else:
            pass

else:
    if c2:
        pass
    else:
        pass

################################################

6.control flow of automatic water motor controller

1. low level, electric, not short cicuit 
c1, c2, not c3   ---> print('motor On')

2. low level, not electric 
c1, not c2       ---> print('generator On'); print('motor On')


################################################

110      --->   print("motor on")
100      --->   print("motor on")

1110     --->   print("motor 2 on")
1010     --->   print("motor 2 on")

11110    --->   print("motor 3 on")
10110    --->   print("motor 3 on")

11111    --->   call mechanic
10111    --->   call mechanic

################################################

low_level = 1
electric = 1
short_circuit = 1
short_circuit2 = 1
short_circuit3 = 1

if low_level:
    if electric:
        if short_circuit:
            if short_circuit2:
                if short_circuit3:
                    print("call mechanic")
                else:
                    print("motor 3 on")
            else:
                print("motor 2 on")
        else:
            print('motor On')
    else:
        print('generator On')
        if short_circuit:
            if short_circuit2:
                if short_circuit3:
                    print('generator Off')
                    print("call mechanic 64")
                else:
                    print("motor 3 on")
            else:
                print("motor 2 on")
        else:
            print('motor On')

################################################

7.exercise

>> add motor No.4 
111110    --->   print("motor 4 on")
101110    --->   print("motor 4 on")

################################################

'''


