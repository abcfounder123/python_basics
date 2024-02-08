# decorator

#################################################
'''
def b():
    print("Hello abc!")

# b()

#################################################

# decorator
def a(f):
    """add lines"""

    def c(): # closures, wrapper
        print("- " * 49)
        f()
        print("- " * 49)

    return c

"""
def x():
    print("- " * 49)
    b()
    print("- " * 49)

x()
"""
# decorate
b = a(b) # third fun closed first fun obj

b()
#################################################

# decorate with @

def a(f):
    """add lines"""

    def c():
        print("- " * 49)
        f()
        print("- " * 49)

    return c

@a
def b():
    print("Hello abc!")

b()

#################################################

# return
def a(f):
    """add lines"""

    def c():
        print("- " * 49)
        result = f()
        print(result)
        print("- " * 49)

    return c

@a
def b():
    return "Hello abc!"

b()

#################################################

# return
def a(f):
    """add lines, split user name and domain name"""

    def c():
        print("- " * 49)
        result = f()
        user_name, domain = result.split("@") # ["abc", "gmail.com"]
        print(f"Your name : {user_name}.")
        print(f"Domain name : {domain}.")
        print("- " * 49)

    return c

@a
def b():
    return "abc@gmail.com"

b()

#################################################

# return, return
def a(f):
    """split email and return user name and domain name, mail type"""

    def c():
        user_name, domain = f().split("@") #["abc", "gmail.com"]
        domain, mail_type = domain.split(".")  # ["gmail", "com"]
        return user_name, domain, mail_type

    return c

@a
def b():
    return "abc@gmail.com"

d = {"com": "commercial account",
     "edu": "education account",
     "org": "nonprofit organization account",
     "gov": "government account"}

user, domain, mail_type = b()

print(f"Your name : {user}")
print(f"Domain name : {domain}")
print(f"It is {d[mail_type]}.")

#################################################

# parameter
import re

def is_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

# 2
def a(f):
    """split email and return user name and domain name, mail type"""
    # 3
    def c(e):
        user_name, domain = f(e).split("@") # "abc@gmail.com".split("@")  --> ["abc", "gmail.com"]  # None.split("@")
        domain, mail_type = domain.split(".") #  ["gmail", "com"]
        return user_name, domain, mail_type

    return c

# 1
@a
def b(email):
    if is_email(email):
        return email
    else:
        print("It is not an Email.")
        return None

# c = a(b) # decorate --> third fun which closed fun No.1
# b = a(b) # decorate --> third fun which closed fun No.1  --> first function overried by third fun  --> @a

d = {"com": "commercial account",
     "edu": "education account",
     "org": "nonprofit organization",
     "gov": "government website"}

user, domain, mail_type = b("abc@gmail.com")
print(f"Your name : {user}.")
print(f"Domain name : {domain}.")
print(f"it is {d[mail_type]}.")

user, domain, mail_type = b("abc@gmail")
print(f"Your name : {user}.")
print(f"Domain name : {domain}.")
print(f"it is {d[mail_type]}.")

#################################################

import re

def is_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

# return, return
def a(f):
    """split email and return user name and domain name, mail type"""
    print("A")
    def c(e):
        e = f(e) # email / None
        if type(e) == str:
            user_name, domain = f(e).split("@")
            domain, mail_type = domain.split(".")
            return (user_name, domain, mail_type)
        else:
            return None
    return c

@a
def b(email):
    if is_email(email):
        return email
    else:
        print("It is not an Email.")
        return None

d = {"com": "commercial account",
     "edu": "education account",
     "org": "nonprofit organization",
     "gov": "government website"}

result = b("abcfounder682@gmail.com")# None / (user_name, domain, mail_type)
if type(result) == tuple:
    user, domain, mail_type = result # tuple unpack
    print(f"Your name : {user}.")
    print(f"Domain name : {domain}.")
    print(f"it is {d[mail_type]}.")

'''

'''
#################################################

#################################################

# instrument, logging, Authentication

import time

def a(f):
    def c():
        start = time.time() # 1 million
        result = f() # 2 sec
        end = time.time() # 1 million + 2 sec
        execution_time = end - start # 2 sec
        print(f"{f.__name__} took {execution_time} seconds.")

        return result
    return c

@a
def f1():
    r = 0
    for i in range(100001):
        r += i
    return r

@a
def f2():
    l = [i for i in range(10000001)]
    return l

@a
def f3():
    l = []
    for i in range(10000001):
        l.append(i)
    return l

result1 = f1()
result2 = f2()
result3 = f3()

#################################################

import time

performance_metrics = dict()

def a(f):
    def c(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"{f.__name__} took {execution_time} seconds.")
        performance_metrics[f.__name__] = {
            "execution_time": execution_time
        } # logging
        return result
    return c

@a
def b():
    time.sleep(2)

@a
def d():
    time.sleep(3)

b()
d()

print(performance_metrics)

#################################################

# memory-profiler     <-----  minus
from memory_profiler import profile
# python -m memory_profiler fp.py

import time

performance_metrics = dict()

def a(f):
    def c(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"{f.__name__} took {execution_time} seconds.")
        performance_metrics[f.__name__] = {
            "execution_time": execution_time
        } # logging
        return result
    return c

@profile
@a
def f2():
    l = [i for i in range(1001)]
    return l

#f3 = profile(a(f3))
@profile
@a
def f3():
    l = []
    for i in range(1001):
        l.append(i)
    return l

result2 = f2()
result3 = f3()
print(performance_metrics)

"""
print("1 MiB =", 1 * 2 ** 20, "bytes")
print("1 MB =", 1 * 10 ** 6, "bytes")

#  28.4 MiB --> Mebibyte ( binary_based unit of storage )  
#  1 MiB = 2 ** 20 bytes = 1048576 bytes
#  1 MB  = 10 ** 6 bytes = 1000000 bytes
"""

#################################################

# recursion and cache
# Example.2  fibonacci
@profile
def fibonacci_1(n):
    print(f"fib({n})")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_1(n-1) + fibonacci_1(n-2)
 
print("Normal recursion")
print("Answer =", fibonacci_1(2))
print("- " * 20)

#################################################

cache = dict()

@profile
def fibonacci_2(n):
     print(f"fib({n})")
     if n in cache:
         return cache[n]
     elif n==0:
         x = 0
     elif n==1:
         x = 1
     else:
         x = fibonacci_2(n-1) + fibonacci_2(n-2)
     cache[n] = x
     return x

print("Recursion with cache")
print("Answer =", fibonacci_2(2))
print("- " * 20)

#################################################

from functools import lru_cache

@lru_cache()
@profile
def fibonacci_3(n):
    print(f"fib({n})")
    if n==0:
        x = 0
    elif n==1:
        x = 1
    else:
        x = fibonacci_3(n-1) + fibonacci_3(n-2)    
    return x

print("Recursion with lru_cache")
print("Answer =", fibonacci_3(2))
print("- " * 20)

#################################################

#################################################

Authentication <--------- to write

'''


'''
#################################################
#################################################

# User database (for demonstration purposes)
user_db = {
    "user1": "password1",
    "user2": "password2",
}

# Function to check user credentials
def authenticate(username, password):
    def check_credentials(username, password):
        return username in user_db and user_db[username] == password

    if check_credentials(username, password):
        return lambda func: func
    else:
        raise PermissionError("Authentication failed")

# Example functions that require authentication
@authenticate(username="user1", password="password")
def secure_function():
    return "This is a secure function."

# Usage
try:
    result = secure_function()
    print(result)
except PermissionError as e:
    print(e)


'''


#################################################

#################################################
#################################################
#################################################
#################################################
#################################################