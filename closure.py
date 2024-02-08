'''
# closure
# closed

def fun(p):
    def inner_fun():
        print(f"our private value is {p}.")

    return inner_fun

x = fun(10)
x()

y = fun(20)
y()

#######

# 2 steps
def fun(outer_p):
    def inner_fun(inner_p):
        print(f"second private value is {inner_p}")

    print(f"first private value is {outer_p}")
    return inner_fun

x = fun(10)
x(20)

#######

# 2 steps
def fun(outer_p):
    def inner_fun(inner_p):
        print(f"second private value is {inner_p}  <--- fun 1")

    def inner_fun2(inner_p):
        print(f"second private value is {inner_p}  <--- fun 2")

    def inner_fun3(inner_p):
        print(f"second private value is {inner_p}  <--- fun 3")

    def inner_fun4(inner_p):
        print(f"second private value is {inner_p}  <--- fun 4")

    print(f"first private value is {outer_p}")
    return inner_fun, inner_fun2, inner_fun3, inner_fun4

a, b, c, d = fun(10)

a("apple")
b("babana")
c("orange")
d("mango")

#######

# 3 steps
def fun(outer_p):
    def inner_fun(inner_p):
        print(f"second private value is {inner_p}  <--- fun 1")
        def inner_fun(inner_p):
            print(f"third private value is {inner_p}  <--- fun 5")
        return inner_fun

    def inner_fun2(inner_p):
        print(f"second private value is {inner_p}  <--- fun 2")

    def inner_fun3(inner_p):
        print(f"second private value is {inner_p}  <--- fun 3")

    def inner_fun4(inner_p):
        print(f"second private value is {inner_p}  <--- fun 4")

    print(f"first private value is {outer_p}")
    return inner_fun, inner_fun2, inner_fun3, inner_fun4

a, b, c, d = fun(10)
#a("apple")

# because of return
#x = a("apple")
#x("banana")

a("apple")("banana")

#######

def fun(x):
    print(f"first private value is {x}  <--- f")
    def fun2(y):
        print(f"second private value is {x}, {y}  <--- s")
        def fun3(z):
            print(f"third private value is {x}, {y}, {z}  <--- t")
        return fun3
    return fun2

#fun(1)(2)(3)

f2 = fun(x=10) # fun2 --> x=10
a = f2(y=2)    # fun3 --> x=10, y=2
b = f2(y=3)    # fun3 --> x=10, y=3

a("apple")
b("apple")

###########

class Car:
    def __init__(self, engine, brake):
        self.engine = engine
        self.brake = brake

    def on(self):
        print(f"{self.engine} ON.")

    def off(self):
        print(f"{self.engine} OFF.")

car1 = Car("engine_1", "brake_1")
car1.on()
car1.off()

car2 = Car("engine_2", "brake_2")
car2.on()
car2.off()

def car(engine, brake):
    def on():
        print(f"{engine} ON.")

    def off():
        print(f"{engine} OFF.")

    return on, off

car1_on, car1_off = car("engine_1", "brake_1")
car1_on()
car1_off()

car2_on, car2_off = car("engine_2", "brake_2")
car2_on()
car2_off()

#######

# auto set value
class Car:
    n = 0
    def __init__(self, engine, brake):
        self.engine = engine
        self.brake = brake
        Car.n += 1
        self.bin = Car.n

    def on(self):
        print(f"{self.engine} ON.   <---  Car NO.{self.bin}")

    def off(self):
        print(f"{self.engine} OFF.   <---  Car NO.{self.bin}")


# class variable / mutable obj
def car(engine, brake, n=[0, ]):
    n[0] += 1
    bin = n[0]
    def on():
        print(f"{engine} ON.   <---  Car NO.{bin}")

    def off():
       print(f"{engine} OFF.   <---  Car NO.{bin}")

    return on, off

#######

# auto set value (BIN)
# function call with arg
class Car:
    n = 0
    def __init__(self, engine, brake):
        self.engine = engine
        self.brake = brake
        Car.n += 1
        self.bin = Car.n

    def on(self, mode):
        print(f"{self.engine} ON.   <---  Car NO.{self.bin}   <--- ({mode})")

    def off(self, mode):
        print(f"{self.engine} OFF.   <---  Car NO.{self.bin}   <--- ({mode})")

# create multiple obj
cars = list()
for i in range(1, 10):
    cars.append(Car(f"engine_{i}", f"brake_{i}"))

cars[0].on("quick mode")
cars[0].off("slow mode")

print(cars[0].__dict__)
print("\n", " -" * 21, "\n")

def car(engine, brake, n=[0, ]):
    n[0] += 1
    bin = n[0]

    def on(mode):
        print(f"{engine} ON.   <---  Car NO.{bin}   <--- ({mode})")
        # print(brake, "is ready.")

    def off(mode):
        print(f"{engine} OFF.   <---  Car NO.{bin}   <--- ({mode})")

    return on, off

# create multiple closures
cars = list()
for i in range(1, 10):
    cars.append(car(f"engine_{i}", f"brake_{i}"))

for car in cars:
    print(car)

cars[0][0]("quick mode")
cars[0][1]("quick mode")

#######

print(cars[9][1].__closure__) # bin, engine ( int, str )
print(cars[9][1].__code__.co_freevars) # bin, engine

#######

# on, off ( naming function )
def car(engine, brake, n=[0, ]):
    n[0] += 1
    bin = n[0]
    def on(mode):
        print(f"{engine} ON.   <---  Car NO.{bin}   <--- ({mode})")
        #print(brake, "is ready.")

    def off(mode):
       print(f"{engine} OFF.   <---  Car NO.{bin}   <--- ({mode})")

    return {"on" : on, "off" : off} # for name

#car1 = car("engine_1", "brake_1") # 2 check for first closures
#car1["on"]("quick")

# create multiple closures
cars = list()
for i in range(1, 10):
    cars.append(car(f"engine_{i}", f"brake_{i}"))

for car in cars:
    print(car)

cars[8]["on"]("quick mode")
cars[8]["off"]("slow mode")

print(cars[0]["on"].__closure__) # bin, engine ( int, str )
print(cars[0]["on"].__code__.co_freevars) # bin, engine

"""

#####################

#####################

# closure
# inner function
def f():
    def a():
        print("a")

    def b():
        print("b")

    def c():
        print("c")

    a()
    b()
    c()


f()

# local fun ကို အပြင်က သံုးမရ
# a()

###########

def f():
    def a():
        print("a")

    def b():
        print("b")

    def c():
        print("c")

    return a, b, c

# return ပြန်ရင် အပြင်က သံုးလို့ရ
x, y, z = f()
x()
y()
z()

a, b, c = f()
a()
b()
c()

###########

# closure
def f(v1, v2, v3):
    def a():
        print(v1)

    def b():
        print(v2)

    def c():
        print(v3)

    return a, b, c

# ဆိုင်ရာတန်ဖိုးတစ်ခုစီနဲ့ function 3 ခု return ပြန်
x, y, z = f("variable_1", "variable_2", "variable_3")
x()
y()
z()

# str obj
print(x.__closure__)
print(y.__closure__)
print(z.__closure__)

x, y, z = f(1, 2, 3)
x()
y()
z()

# int obj
print(x.__closure__)
print(y.__closure__)
print(z.__closure__)

x, y, z = f(1, "hi", (1, 2, 3))
x()
y()
z()

# int, str , tuple
print(x.__closure__)
print(y.__closure__)
print(z.__closure__)

# free variables
print(x.__code__.co_freevars)
print(y.__code__.co_freevars)
print(z.__code__.co_freevars)

###########

"""
variable_1
variable_2
variable_3
(<cell at 0x728c038cd0: str object at 0x728c039470>,)
(<cell at 0x728c038d00: str object at 0x728c0394b0>,)
(<cell at 0x728c038d30: str object at 0x728c0394f0>,)

1
2
3
(<cell at 0x728c038d60: int object at 0x7310366930>,)
(<cell at 0x728c038d90: int object at 0x7310366950>,)
(<cell at 0x728c038dc0: int object at 0x7310366970>,)
"""

###########

# closure
# inner fun ‌ေတွကို ပံုမှန် fun လိုမျိုး သံုးနိုင်

def f(v1, v2, v3):
    def a(av1):
        print(v1)

    def b(bv1):
        print(v2)

    def c(cv1):
        print(v3)

    return a, b, c

x, y, z = f("variable_1", "variable_2", "variable_3")
x("a")
y("b")
z("c")

###########

# 1. normal

def add(n, a, b):
    def f(x):
        return x + n
    return f


add_5 = add(5)
print(add_5(1))

add_10 = add(10)
print(add_10(1))

print(add_5.__closure__)
print(add_10.__closure__)
print(add_5.__code__.co_freevars)
print(add_10.__code__.co_freevars)

print(add.__closure__)
print(add.__code__.co_freevars)

#####################

# 2. lambda
def add(n):
    return lambda x: x + n

add_5 = add(5)  # lambda x: x + 5
print(add_5(1))

add_10 = add(10)  # lambda x: x + 10
print(add_10(1))

print(add_5.__closure__)
print(add_10.__closure__)
print(add_5.__code__.co_freevars)
print(add_10.__code__.co_freevars)


#####################

# closing function object

def add_20_percentage(normal):
    return normal * 1.2

def add(n):
    def f(x):
        return n(x)
    return f

add_20 = add(add_20_percentage)
print(add_20(100))

print(add_20.__closure__)
print(add_20.__code__.co_freevars)

print(" -" * 49)

'''
