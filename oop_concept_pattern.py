"""

OOP  ---> object ( variable, methods )

Major OOP Concepts
# 1. polymorphism
# 2. inheritance
# 3. encapsulation ( data hiding )
# 4. abstraction

#################################################

# 1. polymorphism        ( + )           ( __add__ )
# 2. inheritance   ( class lb(kg): )     ( __init__ )
# 3. encapsulation    ( __weight )       ( a.weight = 10 )

#################################################

class Weight:
    def __init__(self, w):
        self.weight = w
    
class kg(Weight):

    def __repr__(self):
        return str(self.weight) + " kg"

    def __add__(self, other):
        if "kg" in other.__str__():
            return kg(self.weight + other.weight)
        elif "lb" in other.__str__():
            return kg(self.weight + (other.weight / 2.2))

class lb(Weight):
        
    def __repr__(self):
        return str(self.weight) + " lb"

    def __add__(self, other):
        if "lb" in other.__str__():
            return lb(self.weight + other.weight)
        elif "kg" in other.__str__():
            return lb(self.weight + (other.weight * 2.2))

class List(list):
    def __add__(self, other):
        l = []
        if len(self) == len(other):
            for i in range(len(self)):
                l.append(self[i] + other[i])
        else:
            for i in self:
                l.append(i)
            for i in other:
                l.append(i)
        return List(l)
        
    

x = kg(1)
y = lb(2.2)

print(f"{x} + {y} = {x + y}")
print(f"{y} + {x} = {y + x}")

a = x + y
b = y + x
print(a + b)
print(b + a)

# a.weight = 10
# print(a)

#################################################

class Weight:
    def __init__(self, w):
        self.weight = w
        
    def __add__(self, other):
        if "kg" in self.__str__() and "kg" in other.__str__():
            return kg(self.weight + other.weight)
        elif "lb" in self.__str__() and "lb" in other.__str__():
            return lb(self.weight + other.weight)
        elif "kg" in self.__str__() and "lb" in other.__str__() :
            return kg(self.weight + (other.weight / 2.2))
        elif "lb" in self.__str__() and "kg" in other.__str__() :
            return lb(self.weight + (other.weight * 2.2))
    
class kg(Weight):

    def __repr__(self):
        return str(self.weight) + " kg"


class lb(Weight):
        
    def __repr__(self):
        return str(self.weight) + " lb"

x = kg(1)
y = lb(2.2)

print(f"{x} + {y} = {x + y}")
print(f"{y} + {x} = {y + x}")

a = x + y
b = y + x
print(a + b)
print(b + a)

#################################################

class List(list):
    def __add__(self, other):
        l = []
        if len(self) == len(other):
            for i in range(len(self)):
                l.append(self[i] + other[i])
        else:
            #raise TypeError("can only add list to list (with same length)")
            for i in self:
                l.append(i)
            for i in other:
                l.append(i)
        return List(l)
        
#################################################

# Data Hiding and Object Printing
1.  __var
2.  _str_
3.  _repr_
4.  print    -->  str  -->  repr  -->  default repr value ( memory address of obj )

#################################################

# weight.py
class kg:
    def __init__(self, w):
        self.weight = w

    def __repr__(self):
        return str(self.weight) + " kg"

    def __add__(self, other):
        if "kg" in other.__str__():
            return kg(self.weight + other.weight)
        elif "lb" in other.__str__():
            return kg(self.weight + (other.weight / 2.2))

class lb(kg):
    def __repr__(self):
        return str(self.weight) + " lb"

    def __add__(self, other):
        if "lb" in other.__str__():
            return lb(self.weight + other.weight)
        elif "kg" in other.__str__():
            return lb(self.weight + (other.weight * 2.2))

if __name__ == "__main__":
    x = kg(1)
    y = lb(2.2)
    print(f"{x} + {y} = {x + y}")
    print(f"{y} + {x} = {y + x}")

#################################################

# not __repr__()

>> from weight import kg, lb
>> x = kg(1)
>> x
<weight.kg object at 0x7b677e51f0>
>> f"{x}"
'1 kg'
>> y = lb(2.2)
>> y
<weight.lb object at 0x7b67748880>
>> x + y
<weight.kg object at 0x7b677488b0>
>>

#################################################

# with __repr__()
>> from weight import kg,lb
>> x = kg(1)
>> x
1 kg
>> y = lb(2.2)
>> y
2.2 lb
>> x + y
2.0 kg
>> y + x
4.4 lb
>>

#################################################

4. Abstraction

Abstract classes are the classes which contains one or more abstract method;

and abstract methods are the methods which does not contain any implemetation,

but the child-class need to implement these methods otherwise error will
be reported.

In this way, we can force the child-class to implement certain methods in it.

#################################################
metaclass=ABCMeta

# abstraction example.1
from abc import ABCMeta, abstractmethod

class Car(metaclass=ABCMeta):
    def __init__(self, b="ABS system brake"):
        self.brake_system = b

    def brake(self):
        print(f"Brake with {self.brake_system}")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class City_car(Car):
    def __init__(self):
        Car.__init__(self)
        self.engine = "city engine"
        self.tire = "city tire"

    def start(self):
        print(f"{self.engine} start.")

    def stop(self):
        print(f"{self.engine} stop.")

x = City_car()
x.start()
x.stop()
x.brake()

# y = Car()

################################################

# abstraction example.2
# crd freecodecamp


from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None #0.2

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price

    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}\nQuantity: {self.quantity}\nAuthor: {self.author}\nPrice: {self.get_price()}\n"

class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def __repr__(self):
        return super().__repr__() + f"Pages: {self.pages}\n"

class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return super().__repr__() + f"Branch: {self.branch}\n"


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 300, 200)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 300, 'IT')

print(novel1)
print(academic1)
novel1.set_discount(None)


# del @abstractmethod
#b = Book("book1", 10, "abc", 10)
#print(b)

################################################

Method Overloading:

Two or more methods have the same name but different numbers of parameters or different types of parameters, or both.
These methods are called overloaded methods and this is called method overloading.

Like other languages (for example, method overloading in C++) do, python does not support method overloading by default.
But there are different ways to achieve method overloading in Python.

The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method.

#################################################

# Python doesn't support Method Overloading by default.

class X:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        print(self.value + other)

    def add(self, other1, other2): # li
        print(self.value + other1 + other2)


a = X(1)
a.add(1, 2) #lifo

#################################################

# Method Overloading by using dispatch decorator
# dispatch = ‌သီးသန့်‌ေနရာ
from multipledispatch import dispatch


@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result, "   <--- int 2")

@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result, "   <---  int 3 ")

@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(round(result), "   <---  float 3")


e = [1, 2, 3, 4, 5, 0.1, 100]

def product(*x): # ()
    try:
        t = x[0]
        for i in x[1:]:
            t *= i
    except IndexError:
        t = 0

    print(t)
    #return t

product() # no arg <--- index error
product(0)
product(1, 2)
product(1, 2, 3, 1.)
product(1.1, 2.1, 3.0)
product(1, 2, 3, 4, 5, 0.1)
product(*e)

x = 1
x = 2


#################################################

from multipledispatch import dispatch

class MyInt:
    def __init__(self, value):
        self.value = value

    @dispatch(int)
    def __add__(self, other):
        return MyInt(self.value + other)

    @dispatch(float)
    def __add__(self, other):
        #print(self.value + round(other))
        #print(float(self.value) + other)
        return MyInt(self.value + round(other))

    @dispatch(str)
    def __add__(self, other):
        #print(self.value + ord("A"))
        #print(chr(self.value) + other)
        return MyInt(self.value + ord("A"))

    def __repr__(self):
        return str(self.value)

n = MyInt(65)

print(n + 1)
print(n + 5.7)
print(n + "A")

#################################################

class MyInt:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, int):
            return MyInt(self.value + other)
        if isinstance(other, float):
            return MyInt(self.value + round(other))
        if isinstance(other, str):
            return MyInt(self.value + ord("A"))

    def __repr__(self):
        return str(self.value)


n = MyInt(65)

print(n + 1)
print(n + 5.7)
print(n + "A")

#################################################

2. Method overriding ( LIFO )
# override လွှမ်းမိုး

---> derived class method "overrides" the method provided in the base class.

x = 1
x = 2


def red():
    print("red")


def blue():
    print("blue")


def black(self):
    print("black")


class P:
    def x(self):
        print("white")


class C(P):
    pass


obj1 = C()
obj2 = C()

obj1.x()
obj2.x()

C.x = black  # add attribute x to C
obj1.x()
obj2.x()

obj1.x = blue
obj2.x = red
obj1.x()
obj2.x()

################################################

Design Patterns & Python

What is a Design Pattern?
Design Patterns are concrete solutions for reoccurring problems.
They satisfy the design principles and can be used to understand and illustrate them.
They provide a NAME to communicate effectively with other programmers.

#################################################

1. Iterator Pattern
The essence of the Iterator Factory method Pattern is to
"Provide a way to access the elements of an aggregate object sequentially without exposing 
its underlying representation."
.

aggregate ( စုပေါင်း )
exposing ( မြင်သာအောင်ပြ )
representation ( ကိုယ်စားပြု )

#################################################

2. Decorator Pattern
( မူလအရာကို မထိခိုက်ဘဲ  မွမ်းမံနိုင်စွမ်း )
The decorator pattern is a design pattern that
allows behavior to be added to an existing object dynamically.
behaviour ( အပြုအမူ လုပ်ဆောင်ချက် )

#################################################

3. Strategy Pattern
The strategy pattern (also known as the policy pattern) is
a particular software design pattern,
whereby algorithms behavior can be selected at runtime.

#################################################

4. Adapter Pattern
The adapter pattern is a design pattern that
translates one interface for a class into a compatible interface

#################################################

# 1. Iterator Pattern
class MyIter():
    def __init__(self, v):
        self.v = v
        self.p = 0

    def __next__(self):
        print("working next method of myiter")
        try:
            value = self.v[self.p]
            self.p += 1
            # print ("Iteration done.")
            return value
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        print("------->   work iter of myiter")
        return self


class FruitsList():
    def __init__(self, *items):
        self.items = items
        self.p = 0
        
    def __next__(self):
        print("working next method of fruit ")
        try:
            value = self.items[self.p]
            self.p += 1
            # print ("Iteration done.")
            return value
        except IndexError:
            raise StopIteration()
    
    def __iter__(self):
        print("------->   work iter of fruitlist")
        return self


class BookShelve():
    def __init__(self, **items):
        self.items = items
        
    
    def __iter__(self):
        print("------->   work iter of bookshelve")
        data = list(self.items.keys())
        return MyIter(data)


x = MyIter([1, 2, 3,  5, 6, 7])
for i in x:
    print(i)

print("- " * 30 )

fruits = FruitsList("apple", "banana")
for item in fruits:
    print(item)

print("- " * 30 )

shelve1 = BookShelve(mgmg="book1", aungaung="book2", mama="book3")
for item in shelve1:
    print(item)

print("- " * 30 )

#################################################

# 1. Iterator Pattern
class MyIter():
    def __init__(self, v):
        self.v = v
        self.p = 0

    def __next__(self):
        try:
            value = self.v[self.p]
            self.p += 1
            # print ("Iteration done.")
            return value
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        print("------->   work iter of myiter")
        return self

class My_obj():
    def __init__(self, *items):
        self.items = items

    def __iter__(self):
        print("------->   work iter of myobj")
        return MyIter(self.items)


obj = My_obj(1, 2, 3, "apple", "banana")
for item in obj:
    print(item)

print("- " * 30 )

obj2 = MyIter([1, 2, 3, "apple", "banana"])
for i in obj2:
    print(i)

print("- " * 30 )

for i in "abcdefg1436":
    print(i)

#################################################

# 2. Decorator Pattern
class Header_3:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return f"<h3>{self.obj.render()}</h3>"

class ItalicWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return "<i>{}</i>".format(self.obj.render())

class HeaderWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        return f"<h1>{self.obj.render()}</h1>"


class UnderlineWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        #print("render()  --->  UnderlineWrapper")
        return f"<u>{self.obj.render()}</u>"


class BoldWrapper:
    def __init__(self, obj):
        self.obj = obj

    def render(self):
        #print("render()  --->  BoldWrapper")
        return f"<b>{self.obj.render()}</b>"


class NormalText:
    def __init__(self, text):
        self.text = text

    def render(self):
        #print("render()  --->  NormalText")
        return self.text

normal_text = NormalText("Myself")
print(normal_text.render())

y = ItalicWrapper(UnderlineWrapper(BoldWrapper(normal_text)))
print(y.render())

ubh = HeaderWrapper(BoldWrapper(UnderlineWrapper(normal_text)))
print(ubh.render())

hub = BoldWrapper(UnderlineWrapper(HeaderWrapper(normal_text)))
print(hub.render())

ubh = Header_3(BoldWrapper(UnderlineWrapper(normal_text)))
print(ubh.render())

hub = BoldWrapper(UnderlineWrapper(Header_3(normal_text)))
print(hub.render(), file=open("text2.html", "w"))

print(normal_text.render())
#  "<b>{Myself}</b>"













y = ItalicWrapper(UnderlineWrapper(BoldWrapper(x)))
print(y.render())

bu = HeaderWrapper(BoldWrapper(UnderlineWrapper(x)))
print(bu.render())

print(x.render())
#################################################

# 3. strategy pattern
# runtime မှာ ရွေးချယ် လုပ်နိုင်စွမ်း

class IR_system:
    def __init__(self):
        self.sensor = str("Electro optical targeting system(IR)")

    def search_target(self):
        print("strategy", 1)
        print(f"{self.sensor} search infrared radiation of the target.")

class Radar_system:
    def __init__(self):
        self.sensor = "APG-81"

    def search_target(self):
        print("strategy", 2)
        print(f"{self.sensor} search high frequency electro-magnetic waves that are reflected of the target.")

class Projectile:
    def __init__(self, system):
        self.system = system

    def search_target(self):
        print("strategy")
        self.system.search_target()

class IR_missile(Projectile):
    def __init__(self):
        self.system = IR_system()

class Radar_missile(Projectile):
    def __init__(self):
        self.system = Radar_system()

missile1 = IR_missile()
missile1.search_target()
#missile1.system.search_target()

missile2 = Radar_missile()
missile2.search_target()

print(dir(missile1)) # 'search_target', 'system'
print(dir(missile1.system)) #  'search_target', 'sensor'

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'search_target', 'system']

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'search_target', 'sensor']

#################################################



# 4. adaptor pattern

class Adapter:
    def __init__(self, missile, system):
        self.missile = missile
        self.sensor = system

    def search_target(self):
        self.sensor.search_target()
        self.missile.search_target()


class Gps_adapter(Adapter):
    def __init__(self, missile):
        Adapter.__init__(self, missile, Gps_system())


class Radar_adapter(Adapter):
    def __init__(self, missile):
        Adapter.__init__(self, missile, Radar_system())


class IR_adapter(Adapter):
    def __init__(self, missile):
        Adapter.__init__(self, missile, IR_system())


class IR_system:
    def __init__(self):
        self.sensor = "Electro optical targeting system"

    def search_target(self):
        print("ir")
        print(f"{self.sensor} search infrared radiation of the target.")


class Radar_system:
    def __init__(self):
        self.sensor = "APG-81"

    def search_target(self):
        print("radar")
        print(f"{self.sensor} search high frequency electro-magnetic waves that are reflected of the target.")


class Gps_system:
    def __init__(self):
        self.sensor = "GPS system"

    def search_target(self):
        print("ir")
        print(f"{self.sensor} will guide missile.")


class Missile():
    def __init__(self, system):
        self.system = system

    def search_target(self):
        self.system.search_target()


missile1 = Missile(IR_system())
missile1.search_target()

missile1 = Gps_adapter(missile1)
print("- " * 30)
missile1.search_target()

missile2 = Missile(Radar_system())
print("- " * 30)
missile2.search_target()

missile2 = Gps_adapter(missile2)
print("- " * 30)
missile2.search_target()
print("- " * 30)

# decorator
r_ir = Gps_adapter(IR_adapter(Missile(Radar_system())))
r_ir.search_target()
print("- " * 30)

r_ir = Gps_adapter(Radar_adapter(Missile(IR_system())))
r_ir.search_target()
print("- " * 30)



class Adapter:
    def __init__(self, missile, system):
        self.missile = missile
        self.sensor = system

    def search_target(self):
        self.sensor.search_target()
        self.missile.search_target()



class IR_system:
    def __init__(self):
        self.sensor = "Electro optical targeting system"

    def search_target(self):
        print("ir")
        print(f"{self.sensor} search infrared radiation of the target.")


class Radar_system:
    def __init__(self):
        self.sensor = "APG-81"

    def search_target(self):
        print("radar")
        print(f"{self.sensor} search high frequency electro-magnetic waves that are reflected of the target.")


class Gps_system:
    def __init__(self):
        self.sensor = "GPS system"

    def search_target(self):
        print("ir")
        print(f"{self.sensor} will guide missile.")


class Missile():
    def __init__(self, system):
        self.system = system

    def search_target(self):
        self.system.search_target()



missile1 = Missile(IR_system())
missile1.search_target()

missile1 = Adapter(missile1, Gps_system())
print("- " * 30)
missile1.search_target()

missile2 = Missile(Radar_system())
print("- " * 30)
missile2.search_target()

missile2 = Adapter(missile2, IR_system())
print("- " * 30)
missile2.search_target()
print("- " * 30)

# decorator
r_ir = Adapter(Adapter(Missile(Radar_system()), IR_system()), Gps_system())
r_ir.search_target()
print("- " * 30)
print(type(r_ir))

r_ir = Adapter(Adapter(Missile(IR_system()), Radar_system()), Gps_system())
r_ir.search_target()
print("- " * 30)
print(type(r_ir))





class IR_system:
    def __init__(self):
        self.sensor = "Electro optical targeting system"

    def search_target(self):
        print("ir")
        print(f"{self.sensor} search infrared radiation of the target.")


class Radar_system:
    def __init__(self):
        self.sensor = "APG-81"

    def search_target(self):
        print("radar")
        print(f"{self.sensor} search high frequency electro-magnetic waves that are reflected of the target.")


class Gps_system:
    def __init__(self):
        self.sensor = "GPS system"

    def search_target(self):
        print("ir")
        print(f"{self.sensor} will guide missile.")


class Projectile:
    def __init__(self, system):
        self.system = system

    def search_target(self):
        print("proj")
        self.system.search_target()


class IR_missile(Projectile):
    def __init__(self):
        self.system = IR_system()


class Radar_missile(Projectile):
    def __init__(self):
        self.system = Radar_system()


# adapter class ( missile + GPS )
class Gps_adapter:
    def __init__(self, missile):
        self.missile = missile
        self.sensor = Gps_system()

    def search_target(self):
        self.sensor.search_target()
        self.missile.search_target()


class IR_adapter:
    def __init__(self, missile):
        self.missile = missile
        self.sensor = IR_system()

    def search_target(self):
        self.missile.search_target()
        self.sensor.search_target()


missile1 = IR_missile()
missile1.search_target()

missile1 = Gps_adapter(missile1)
print("- " * 30)
missile1.search_target()

missile2 = Radar_missile()
print("- " * 30)
missile2.search_target()

missile2 = Gps_adapter(missile2)
print("- " * 30)
missile2.search_target()
print("- " * 30)

# decorator
r_ir = Gps_adapter(IR_adapter(Radar_missile()))
r_ir.search_target()
print("- " * 30)
print(type(r_ir))





# adapter class ( missile + GPS )
class Gps_adapter:
    def __init__(self, missile):
        self.missile = missile
        self.sensor = Gps_system()

    def search_target(self):
        self.sensor.search_target()
        self.missile.search_target()


class IR_adapter:
    def __init__(self, missile):
        self.missile = missile
        self.sensor = IR_system()

    def search_target(self):
        self.missile.search_target()
        self.sensor.search_target()


class Radar_adapter:
    def __init__(self, missile):
        self.missile = missile
        self.sensor = Radar_system()

    def search_target(self):
        self.missile.search_target()
        self.sensor.search_target()

class IR_system:
    def __init__(self):
        self.sensor = "Electro optical targeting system"

    def search_target(self):
        print("ir")
        print(f"{self.sensor} search infrared radiation of the target.")


class Radar_system:
    def __init__(self):
        self.sensor = "APG-81"

    def search_target(self):
        print("radar")
        print(f"{self.sensor} search high frequency electro-magnetic waves that are reflected of the target.")


class Gps_system:
    def __init__(self):
        self.sensor = "GPS system"

    def search_target(self):
        print("ir")
        print(f"{self.sensor} will guide missile.")


class Missile():
    def __init__(self, system):
        self.system = system

    def search_target(self):
        self.system.search_target()



missile1 = Missile(IR_system())
missile1.search_target()

missile1 = Gps_adapter(missile1)
print("- " * 30)
missile1.search_target()

missile2 = Missile(Radar_system())
print("- " * 30)
missile2.search_target()

missile2 = Gps_adapter(missile2)
print("- " * 30)
missile2.search_target()
print("- " * 30)

# decorator
r_ir = Gps_adapter(IR_adapter(Missile(Radar_system())))
r_ir.search_target()
print("- " * 30)
print(type(r_ir))



"""
