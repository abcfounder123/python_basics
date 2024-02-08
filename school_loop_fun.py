
# 1. definite loop
# 2. indefinate loop
# 3. infinite loop

'''
##############################################

s = "abcdefg"


for i in s:
    print(i)

for i in range(0, 7, 1): # 0, ..., 6 # step
    print(s[i])

i = 0
while i < 7:
    print(s[i])
    i += 1

##############################################

# 2.1.interactive loop ( program and user )

c = input("C = ")
while c != "q":
    c = input("C = ")
    

# 2.2. sentinel loops

x = 2
while x > 0:# sentinel condition
    x = int(input("C = "))
    
    
# 2.3. file loop
# 2 3 4 5 6 7 8 100
#

# 2.4. post-test loop ( do while ) 

while True:  # infinite loop
    x = int(input("C = ")) # do
    print(x) # do
    
    if x > 0: # # sentinel condition
        pass
    else:
        break
        
##############################################

# 5 ---> 1, 5 ( 2, 3, 4, ) (6, 7, 8, ....)
n = 11
print(n % 2 == 0)
print(n % 3 == 0)
print(n % 4 == 0)
print(n % 5 == 0)  # 

##############################################

for i in range(2, (n//2) + 1): # 2 3 4 5 
    print(n, "/", i)
    if n % i == 0:
        print(n, "=", i, "*", n//i)
        break
else:
    print("loop successfully")
    print(n , "is a prime number.")


##############################################

def p():
    
    for i in range(2, (n//2) + 1): # 2 3 4 5 
        print(n, "/", i)
        if n % i == 0:
            print(n, "=", i, "*", n//i)
            break
    else:
        print("loop successfully")
        print(n , "is a prime number.")
    
    return True

##############################################

# parameter , n2=0 (default par, default agument)
# argument (positional argument, keyword argument)

##############################################

# pure function
def is_prime(n):
    for i in range(2, (n//2) + 1): # 2 3 4 5 
        #print(n, "/", i)
        if n % i == 0:
            return False
            
    return True



for i in range(1, 101):
    if  is_prime(i):print(i , "is a prime number.")


l = []
for i in range(1000, 2001):
    if  is_prime(i):l.append(i)

print(l)

##############################################

'''


def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

# pure function # 0020
def is_prime(n):
    for i in range(2, (n//2) + 1): # 2 3 4 5 
        #print(n, "/", i)
        if n % i == 0:
            return False
            
    return True

# pure
def p(start, stop, f):
    l = []
    for i in range(start, stop):
        if f(i):
            l.append(i)

    return l

p_100_200 = p(100, 201, is_prime)

print(p_100_200)

e = p(100, 201, is_even)

print(e)

##############################################








