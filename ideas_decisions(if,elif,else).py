"""
################################################

Ideas for decisions (if, elif, else)

1. Greater number (if, else)
2. Greater or equal number (if, elif, else)
3. Largest of three numbers (if, elif, else)
4. Ascending order of three numbers (nested if)
5. Descending order of three numbers (nested if)
6. Grade by marks ( Exercise )
7. Time consumption & readability
8. Dependent conditions & independent conditions
9. Ticket price by age  ( Exercise )
10. Combining conditions by using logical operator
    - independent condition   -->   or
    - dependent condition     -->   and
    - negation, reverse       -->   not
11. Checking leap year

** Exercise 2 --> 6 & 9 

################################################

1. Greater number (if, else)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

################################################

2. Greater or equal number (if, elif, else)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater")
elif b < a:
    print(f"{b} is greater")
else:
    print("They are equal.")

################################################

3. Largest of three numbers (if, elif, else)
a, b, c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(f"{a} is the largest")
elif b > c:  # a is not largest and compare b and c
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")

################################################

4. Ascending order of three numbers (nested if)

1. abc -> if a is smallest, if b is smaller than c            123
2. acb -> if a is smallest, if b is not smaller than c        132

3. bac -> if b is smallest, if a is smaller than c            213
4. bca -> if b is smallest, if a is not smaller than c        312

5. cab -> if c is smallest, if a is smaller than b            231
6. cba -> if c is smallest, if a is not smaller than b        321

5. Descending order of three numbers (nested if)

1. abc -> if a is greatest, if b is greater than c            321
2. acb -> if a is greatest, if b is not greater than c        312

3. bac -> if b is greatest, if a is greater than c            231
4. bca -> if b is greatest, if a is not greater than c        132

5. cab -> if c is greatest, if a is greater than b            213
6. cba -> if c is greatest, if a is not greater than b        123

################################################

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

c1 = a <= b and a <= c
c2 = b <= a and b <= c
c3 = c <= a and c <= b

if c1:  # if a is smallest,
    if b <= c: # if b is smaller than c
        print(f"Ascending order  -> abc : {a}, {b}, {c}")
    else:
        print(f"Ascending order  -> acb : {a}, {c}, {b}")
elif c2:
    if a <= c:
        print(f"Ascending order  -> bac : {b}, {a}, {c}")
    else:
        print(f"Ascending order  -> bca : {b}, {c}, {a}")
else:
    if a <= b:
        print(f"Ascending order  -> cab : {c}, {a}, {b}")
    else:
        print(f"Ascending order  -> cba : {c}, {b}, {a}")

################################################

c1 = a >= b and a >= c
c2 = b >= a and b >= c
c3 = c >= a and c >= b

if c1:  # if a is greatest,
    if b >= c: # if b is greater than c
        print(f"Descending order  -> abc : {a}, {b}, {c}")
    else:
        print(f"Descending order  -> acb : {a}, {c}, {b}")
elif c2:
    if a >= c:
        print(f"Descending order  -> bac : {b}, {a}, {c}")
    else:
        print(f"Descending order  -> bca : {b}, {c}, {a}")
else:
    if a >= b:
        print(f"Descending order  -> cab : {c}, {a}, {b}")
    else:
        print(f"Descending order  -> cba : {c}, {b}, {a}")

################################################
################################################

6. Grade by marks

A             ->   90 to 100
B             ->   80 to 90 (not 90, 89.9)
C             ->   70 to 80 (not 80, 79.9)
D             ->   60 to 70 (not 70, 69.9)
F ( fail )    ->   < 60     (not 60, 59.9)

################################################

# 11 secs
marks = int(input("Enter your marks: "))

a = 90 <= marks <= 100
b = 80 <= marks < 90
c = 70 <= marks < 80
d = 60 <= marks < 70
f = marks < 60

if a:print("Grade: A")
if b:print("Grade: B")
if c:print("Grade: C")
if d:print("Grade: D")
if f:print("Grade: F (Fail)")

#  7 secs to 11
marks = int(input("Enter your marks: "))

a = 90 <= marks <= 100
b = 80 <= marks < 90
c = 70 <= marks < 80
d = 60 <= marks < 70
f = marks < 60

# to be sure to choose only one
if a:print("Grade: A")  # 7 sec
elif b:print("Grade: B") # 8
elif c:print("Grade: C") # 9
elif d:print("Grade: D")
elif f:print("Grade: F (Fail)")

# 7. time consumption & readability
# to be sure to choose only one
# to reduce time consumption
# 2 secs, 6 seconds
# f5 6 * 5 --> 30, A1 --> 2, D4 4 * 4 --> 16   --> 48
marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:print("Grade: A")  # 90
elif 80 <= marks < 90:print("Grade: B")
elif 70 <= marks < 80:print("Grade: C")
elif 60 <= marks < 70:print("Grade: D")
elif marks < 60:print("Grade: F (Fail)")

# F, D, C, B, A
# F5 5 * 5 --> 5, A1 --> 6, D4 3 * 4 --> 12   --> 23
marks = int(input("Enter your marks: "))

if marks < 60:print("Grade: F (Fail)")
elif 60 <= marks < 70:print("Grade: D")
elif 70 <= marks < 80:print("Grade: C")
elif 80 <= marks < 90:print("Grade: B")
elif 90 <= marks <= 100:print("Grade: A")

# if D, C, F, B, A, we can optimize our code to reduce time consumption
# we can change easily because of independent conditions
if 60 <= marks < 70:print("Grade: D")
elif 70 <= marks < 80:print("Grade: C")
elif marks < 60:print("Grade: F (Fail)")
elif 80 <= marks < 90:print("Grade: B")
elif 90 <= marks <= 100:print("Grade: A")

################################################

8. dependent conditions & independent conditions

# dependent conditions

c1 = greater than or equal 90         
c2 = greater than or equal 80         
c3 = greater than or equal 70         
c4 = greater than or equal 60         
c5 = less than 60                     

A             ->   c1
B             ->   not c1, c2
C             ->   not c2, c3
D             ->   not c3, c4
F ( fail )    ->   c5 ( not c4 )

################################################

marks = int(input("Enter your marks: "))

c1 = marks >= 90
c2 = marks >= 80
c3 = marks >= 70
c4 = marks >= 60
c5 = marks < 60

if c1:
    print("Grade: A")
elif c2:
    print("Grade: B")
elif c3:
    print("Grade: C")
elif c4:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

################################################ 

# to reduce time consumption
# not 5 seconds, 1 to 5 seconds   
# we can not change easily because of dependent conditions

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

################################################

Exercises
# we can not change easily because of dependent conditions
# Exercise is to think "reverse order of dependent conditions".    

c1 = less than 60  
c2 = less than 70   
c3 = less than 80 
c4 = less than 90 
c5 = less than equal 100                    

F ( fail )    ->   c1                   independent condition
D             ->   not c1, c2           depend on c1 
C             ->   not c2, c3           depend on c2
B             ->   not c3, c4           depend on c3
A             ->   not c4, c5           depend on c4

# dependent conditions can not make  "D, C, F, B, A", please takecare your order.    
# FDCBA  
    
################################################
################################################

9. Ticket price by age
    
age = int(input("Enter your age: "))

if age < 5:
    print("Ticket is Free!")
elif age <= 18:
    print("Ticket price is $10.")
elif age <= 60:
    print("Ticket price is $20.")
else:
    print("Ticket price is $15 (Senior Discount).")

################################################

Exercises
# we can not change easily because of dependent conditions
# Exercise is to think "reverse order of dependent conditions".    

################################################
################################################

10. Combining conditions by using logical operator
    - independent condition   -->   or
    - dependent condition     -->   and
    - negation, reverse       -->   not
    
################################################
    
11. Checking leap year 

100 200 300 400 500 600 700 800

c1 = if divisible by 400
c2 = if divisible by 100      ( Gregorian Calendar )
c3 = if divisible by 4

################################################

1. c1                        leap year          1600, 2000 
2. not c2 and c3             leap year          1604, 1608, 1612, 
3. else                      not leap year      1601, 1602, 1603, ( 1700, 1800, 1900 )

################################################

year = int(input("Enter a year: "))
c1 = year % 400 == 0
c2 = year % 100 == 0
c3 = year % 4 == 0

if c1:
    print("Leap Year")
elif not c2 and c3:
    print("Leap Year")
else:
    print("Not a Leap Year")

################################################
################################################

year = int(input("Enter a year: "))
c1 = year % 400 == 0
c2 = year % 100 == 0
c3 = year % 4 == 0

# independent condition and same results 
if c1 or (not c2 and c3):
    print("Leap Year")
else:
    print("Not a Leap Year")
    

################################################

# Thinking for reverse checking is always difficult and easiest way is negation
# We can negate the original condition by using De Morgan's Law

# 1700
# not False and (True or not True)
# T and T

# 2001
# not False and (False or not False)
# T and T

year = int(input("Enter a year: "))
c1 = year % 400 == 0
c2 = year % 100 == 0
c3 = year % 4 == 0

# if not divisible by 400 and ( divisible by 100 or not divisible by 4 )
if not c1 and (c2 or not c3):
    print("Not a Leap Year")
else:
    print("Leap Year")

################################################

# if not divisible by 4 or (divisible by 100 and not divisible by 400)

if not c3 or (c2 and not c1):
    print("Not a Leap Year")
else:
    print("Leap Year")
    
################################################
################################################

** Exercise 1 and 2 --> 6 & 9

Exercises.1  ( write code )
# we can not change easily because of dependent conditions
# Exercise is to think "reverse order of dependent conditions".    

c1 = less than 60  
c2 = less than 70   
c3 = less than 80 
c4 = less than 90 
c5 = less than equal 100                    

F ( fail )    ->   c1                   independent condition
D             ->   not c1, c2           depend on c1 
C             ->   not c2, c3           depend on c2
B             ->   not c3, c4           depend on c3
A             ->   not c4, c5           depend on c4

# dependent conditions can not make  "D, C, F, B, A", please takecare your order.    
      
      
################################################

Exercises.2  ( write idea and code )

9. Ticket price by age
    
age = int(input("Enter your age: "))

if age < 5:
    print("Ticket is Free!")
elif age <= 18:
    print("Ticket price is $10.")
elif age <= 60:
    print("Ticket price is $20.")
else:
    print("Ticket price is $15 (Senior Discount).")

################################################

Exercises
# we can not change easily because of dependent conditions
# Exercise is to think "reverse order of dependent conditions".    

################################################
################################################

"""