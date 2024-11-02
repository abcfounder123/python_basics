
"""
A. Object and Label
1. A label is not an object.
2. A label can store an address.
3. Some function & method can create a new object.
4. An obj can have multiple labels.
5. A label can change various address.
6. An obj can have multiple data and multiple functions.
7. An object is a combination of attributes and methods.

B. OOP (object-oriented programming)
B.1. class
C.2. object

C. Creating blueprint
C.1. Creating class
C.2. Creating Object
C.3. getting attribute
C.4. using method
C.5. adding or changing new attribute
C.6. checking all attribute
C.7. overriding/creating magic method
C.8. Creating many objects
C.9. Handling many objects

################################################

1. A label is not an object.
2. A label can store an address.

# list object 1 , address 1
# label  --->  x, y, z

x = ["apple", "banana"]
y = x
z = y

x.append("orange")
y.append("mangoes")
print(x)
print(y)

################################################

3. Some function & method can create a new object.

# int object 3, float object 1

x = 1  # int object.1
y = 2  # int object.2
z = x + y  # int object.3  ( add magic method create new int obj )

a = x / y  # float object.1  ( truediv magic method create new float obj )

print(hex(id(x)))
print(hex(id(y)))
print(hex(id(z)))
print(hex(id(a)))

################################################

4. An obj can have multiple labels.

x = int()  # int obj.1  ---> x, b
y = list()  # list obj.1  ---> y, c
z = dict()  # dict obj.1  ---> z, a
a = z  # copy ---> address of dict obj.1
b = x
c = y

print("x =", hex(id(x)))
print("y =", hex(id(y)))
print("z =", hex(id(z)))
print("a =", hex(id(a)))
print("b =", hex(id(b)))
print("c =", hex(id(c)))

################################################

5. A label can change various address.

x = int()  # int obj.1
print(x)
print(hex(id(x)))

x = list()  # list obj.1
print(x)
print(hex(id(x)))

x = dict()  # dict obj.1
print(x)
print(hex(id(x)))

################################################

6. An obj can have multiple data and multiple functions.

1. str             --->   character string + 86 methods
2. int             --->   integer value    + 56 methods
3. 15 data types   --->   about 1000 methods

################################################

7. An object is a combination of attributes and methods.

object
>> attributes + methods

attributes (data)
---> age, name, car_no, wheel, brand, brake_system, mouth

methods (function)
---> walk, speak, brake, bite
---> double_underscore (dunder)(magic), normal, constructor

################################################

B. OOP (object-oriented programming)

1. class
>> blueprint of objects
>> combine data and function

2. obj, instance

################################################

class   ---> Human, Dog, Car, Laptop, Robot
object  ---> mg_mg, dog.1, car_1, laptop_1, robot_1

################################################

C. Creating blueprint

class
name --->  Human
attributes --->  head 1, hand 2, leg 2 (name, age, ID)
methods    --->  say(), write(), walk()

################################################

C.1. Creating class

class Human:
    def __init__(self, n):
        self.head = 1
        self.hand = 2
        self.leg = 2
        self.name = n

    def say(self):
        print(f"hello, I am {self.name}.")

################################################

C.2. Creating Object

mg_mg = Human("Mg Mg")  # human obj 1

################################################

C.3. getting attribute

print(mg_mg.name)

################################################

C.4. using method

mg_mg.say()

################################################

C.5. adding or changing new attribute

mg_mg.age = 20

################################################

C.6. checking all attribute

print(mg_mg.__dict__)

################################################

C.7. overriding/creating magic method

# original method
def __repr__(self):
    return f"<__main__.Human object at {hex(id(self))}>"

# this overrides original method
def __repr__(self):
        return f"Human.{self.name}"

################################################

class Human:
    def __init__(self, n):
        self.head = 1
        self.hand = 2
        self.leg = 2
        self.name = n

    def say(self):
        print(f"hello, I am {self.name}.")

    def __repr__(self):
        return f"Human.{self.name}"

################################################

C.8. Creating many objects

humans = []
for i in range(1, 1001):
    humans.append(Human(i))

################################################

C.9. Handling many objects

print(humans)
print(humans[-1])

humans[0].say()
humans[-1].say()

################################################

class Human:
    def __init__(self, n):
        self.head = 1
        self.hand = 2
        self.leg = 2
        self.name = n

    def say(self):
        print(f"hello, I am {self.name}.")

    def __repr__(self):
        return f"Human.{self.name}"


humans = []
for i in range(1, 1001):
    humans.append(Human(i))

print(humans)
print(humans[-1])

humans[0].say()
humans[-1].say()

################################################

"""


