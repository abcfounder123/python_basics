
# instruction ( one ins in one line, semicolon )
# translate ( top to bottom, left to right ) ( override ) ( lifo ) ( stack )
# variable name ( value ) ( data type )
# function ( effect, result )

# OOP ( object oriented programming )
# class ( blueprint of object ) ( data + function )
# obj, instance  ( name, attribute data, method ) ( constructor , magic method, normal method )

#####################

"""

# data + function

s1_name = "Mg Mg"
s1_age = 20
def s1_info():
    print(f"name = {s1_name}\nage = {s1_age}")
    
s2_name = "mama"
s2_age =21
def s2_info():
    print(f"name = {s2_name}\nage = {s2_age}")

s1_info()
s2_info()

#####################
#####################

# OOP
# vocabularies

def f():
    print("f")
    
x = "apple"

#####################

class A:
    "It is a blueprint."
    pass

#####################

A.x = x # add data for class
print(A.x)

#####################

A.y = f # add function for class
A.y()    

#####################

print(A.__dict__) # checking attribute data

#####################
#####################

class A:
    x = "apple" # add data for class
    
    def f(): # add function for class
        print(A.x)

   
A.f() 
A.x = 1 # change value for class attribute (x)
A.f()

#####################
"""

#####################
#####################




# attributes ( class, object ) ( dot notation ) ( getattr and setattr(=) )
# variable attribute ( data )
# methods attribute ( function ) ( magic method, normal method )


# type function  1 argv  --> to check type                    ---> type(x), type(type(x)), type(int)  ( Everything become from type. )
#                3 argvs --> to creat a type , model, class   ---> type("A", (), {"a": 123})
#

# built-in type ( int, str, list, set, .... )
# custom-type ( class keyword, type() ) ( creating a new type, new model & new class)
#

    
# name, data, method

# Computer,
# serial_number, color,
# on, off

"""
class Computer:
    count = 0
    
    def __init__(self):
        Computer.count += 1
        self.serial_number = f"Dell_3214_{Computer.count:0>5}"
        self.color = "black" if Computer.count % 2 == 0 else "white"
        self.state = "Off"
    
    def on(self):
        self.state = "On"
        print(f"{self.serial_number} --> Power on.")
        
    def off(self):
        self.state = "Off"
        print("Power off.")
    
    def show_info(self):
        inf = f'Computer Model No = {self.serial_number}\ncolor = {self.color}\npower state = {self.state}.'
        return inf
        
    def __repr__(self):
        return self.serial_number

computers = []
for i in range(10):
    computer = Computer()
    computers.append(computer)

class Car:
    pass

for i in range(10):
    car = Car()
    computers.append(car)

for c in computers[:10:3]:
    c.os = "window 11"

for obj in computers:
    if type(obj) == Computer:
        if hasattr(obj, "os"):
            pass
        else:
            obj.os = "linux" # installing OS
        print(obj.os)

####

# Car
# serial_No, color, engine_state
# engineOn, engineOff

# Exercise 

class Car:
    count = 0 # class data, variable, attribute
    def __init__(self):
        Car.count += 1
        self.serial_No = f"BMW_{Car.count:0>4}"
        self.color = "black" if Car.count % 2 == 0 else "white"
        self.engine_state = "off"
        
    def engineOn(self):
        self.engine_state = "on"
        
    def engineOff(self):
        self.engine_state = "off"
    
    def __repr__(self):
        # f"Car No: {self.serial_No}, Engine state: {self.engine_state}"
        return self.serial_No + self.engine_state


cars = []
for _ in range(10):
    cars.append(Car())

print(cars)

for car in cars:
    car.engineOn()

print(cars)       

#####################

# step.1  ---> (creating objects, checking obj attributes, creating new attributes)

c1 = Car()
c2 = Car()
c3 = Car()
c4 = Car()

print(c1.__dict__)
print(c2.__dict__)
print(c3.__dict__)
print(c4.__dict__)

print()

c1.brake = "ABS brake system"
c2.brake = "ABS brake system"
c3.brake = "ABS brake system"
c4.brake = "ABS brake system"

print(c1.__dict__)
print(c2.__dict__)
print(c3.__dict__)
print(c4.__dict__)

print()

#####################

# step.2 (creating objects, checking obj attributes, creating new attributes)

cars = []
for _ in range(4):
    cars.append(Car())

print(cars[0].__dict__)
print(cars[1].__dict__)
print(cars[2].__dict__)
print(cars[3].__dict__)

print()

cars[0].brake = "ABS brake system"
cars[1].brake = "ABS brake system"
cars[2].brake = "ABS brake system"
cars[3].brake = "ABS brake system"

print(cars[0].__dict__)
print(cars[1].__dict__)
print(cars[2].__dict__)
print(cars[3].__dict__)

print()

#####################

# step.3 (creating objects, checking obj attributes, creating new attributes)

class Car:
    count = 0
    def __init__(self):
        Car.count += 1
        self.serial_No = Car.count
        self.color = "black" if Car.count % 3 == 1 else "white"
        self.engine_state = "off"
        
    def engineOn(self):
        if self.engine_state == "on":
            print(self.serial_No, "already On.")
            
        else:
            self.engine_state = "on"
            print(self.serial_No, "On")
        
    def engineOff(self):
        if self.engine_state == "off":
            print(self.serial_No, "already off.")
        else:
            self.engine_state = "off"
            print(self.serial_No, "Off")
    
    def __repr__(self):
        return "Car No: " + str(self.serial_No) + ", " + "Engine state: " + self.engine_state
        

cars = []
for _ in range(4):
    cars.append(Car())

for car in cars:
    print(car.__dict__)
    
print()

for car in cars:
    car.brake = "ABS brake system"

for car in cars:
    print(car.__dict__)
    
print()

#####################

# step.4 ( controlling objects )

class Car:
    count = 0
    def __init__(self):
        Car.count += 1
        self.serial_No = f"BMW_{Car.count:0>4}"
        self.color = "black" if Car.count % 3 == 1 else "white"
        self.engine_state = "off"

    def engineOn(self):
        if self.engine_state == "on":
            print(f"{self.serial_No} already On.")
            
        else:
            self.engine_state = "on"
            print(f"{self.serial_No} On")
        
    def engineOff(self):
        if self.engine_state == "off":
            print(f"{self.serial_No} already off.")
        else:
            self.engine_state = "off"
            print(f"{self.serial_No} Off")
    
    def __repr__(self):
        return f"Car No: {self.serial_No}, Engine state: {self.engine_state}"
    
    def fmt(n):
        return f"BMW_{n:0>4}"

cars = []
for _ in range(10):
    cars.append(Car())

print(cars)

for car in cars:
    if int(car.serial_No[-4:]) % 3 == 1:
        car.engineOn()

for car in cars:
   car.engineOff()

#####################

# step.5 ( python data storage style ( immutable data type ) )

# c1  ( 10 ---> (serial_No : 5, color: 0x1aac3a41df0)

# c2  ( 20 ---> (serial_No : 6, color: 0x1aacc838bb0))

# c3  ( 30 ---> (serial_No : 7, color: 0x1aac3a41df0)

# c4  ( 40 ---> (serial_No : 8, color: 0x1aacc838bb0))

c1 = Car()
print(c1.color)
print(hex(id(c1.color)))

c2 = Car()
print(c2.color)
print(hex(id(c2.color)))

c3 = Car()
print(c3.color)
print(hex(id(c3.color)))

c4 = Car()
print(c4.color)
print(hex(id(c4.color)))

#####################

# step.1 ---> class level data ( creating, changing )

class Car:
    count = 0 # creating clas data
    
    
car = Car()
car2 = Car()

print(Car.__dict__)

print(Car.count) # access class level data from class
print(car.count) # access class level data from obj
print(car2.count) # access class level data from obj

Car.count = 2 # changing class data

print(Car.__dict__)
print(car.__dict__)
print(Car.count) # access class level data from class
print(car.count) # access class level data from obj
print(car2.count) # access class level data from obj

Car.brand = "BMW" # creating new clas data

print(Car.__dict__)
print(car.__dict__)
print(Car.brand) # access class level data from class
print(car.brand) # access class level data from obj
print(car2.brand) # access class level data from obj

#####################

# step.2 ---> class level function ( creating, accessing )

def fmt(number):
    return f"BMW_{number:0>4}"

class Car:
    
    # class
    def fmt_c(number):
        return f"BMW_{number:0>4} ---> cls"
    
    # obj
    def fmt_obj(self, number):
        return f"BMW_{number:0>4} ---> obj"
    
    def __format__(self, format_spec):
        return "1"
    
car1 = Car()

# fun
n1 = fmt(7)

# class method
n2 = Car.fmt_c(8) # fmt_c(8)      # accesss from class
n22 = car1.fmt_c() # fmt_c(car1)  # accesss from obj

# obj method
n3 = Car.fmt_obj("", 8) # fmt_obj(8)    # accesss from class
n4 = car1.fmt_obj(8) # fmt_obj(car1, 8) # accesss from obj

print(n1)
print(n2)
print(n22)
print(n3)
print(n4)

#####################

# step.3 ---> class level function ( creating, accessing )

class Car:

    def __format__(self, format_spec):
        return "1"
    
car1 = Car()

def f1(number):
    return f"BMW_{number:0>4}"

# fun
n1 = f1(7)

# class 
Car.fmt_c = f1  # add new function

# obj 
def f2(self, number):
    return f"BMW_{number:0>4}"

Car.fmt_obj = f2 # add new function

n2 = Car.fmt_c(8) # fmt_c(8)      # accesss from class
n22 = car1.fmt_c() # fmt_c(car1)  # accesss from obj

n3 = Car.fmt_obj("", 8) # fmt_obj(8)    # accesss from class
n4 = car1.fmt_obj(8) # fmt_obj(car1, 8) # accesss from obj

print(n1)
print(n2)
print(n22)
print(n3)
print(n4)
print(car1.__dict__)
print(Car.__dict__)

#####################

# change class data ( function, external)

class Car:
    count = 0
    def __init__(self):
        Car.count += 1  # change class data 
        self.serial_No = f"BMW_{Car.count:0>4}"
        self.color = "black" if Car.count % 3 == 1 else "white"
        self.engine_state = "off"
        
             
print(Car.count)

car1 = Car() # change class data ( function )

print(Car.count) 

Car.count += 10 # change class data ( external )

print(Car.count)

#####################

# step.1  ( create obj data )

car1 = Car()

Car.count += 1
car1.serial_No = f"BMW_{Car.count:0>4}"
car1.color = "black" if Car.count % 3 == 1 else "white"
car1.engine_state = "off"

car2 = Car()

Car.count += 1
car2.serial_No = f"BMW_{Car.count:0>4}"
car2.color = "black" if Car.count % 3 == 1 else "white"
car2.engine_state = "off"

print(car1.__dict__)
print(car2.__dict__)

#######

# step.2   ( create obj data with constructor method )

class Car:
    count = 0
    name = "BMW"
    def __init__(self):
        Car.count += 1  
        self.serial_No = f"BMW_{Car.count:0>4}"
        self.color = "black" if Car.count % 3 == 1 else "white"
        self.engine_state = "off"
    
        
car1 = Car()

car2 = Car()

print(car1.__dict__)
print(car2.__dict__)


#######


# class level data and obj data
# readable , to reduce time and memory

class Car:
    name = "BMW"
    
cars = []
for _ in range(1000000):
    cars.append(Car())

print(cars[0].name)
print(cars[-1].name)

Car.name = "Tasla"

print(cars[0].name)
print(cars[-1].name)


# fun call ---> normal method and magic method
# purpose ---> instance / obj method, class method, static method

class Car:
    count = 0
    name = "BMW"
    def __init__(self):
        Car.count += 1
        self.serial_No = Car.fmt(Car.count)
        self.color = "black" if Car.count % 3 == 1 else "white"
        self.engine_state = "off"

    def engineOn(self):
        if self.engine_state == "on":
            print(f"{self.serial_No} already On.")
            
        else:
            self.engine_state = "on"
            print(f"{self.serial_No} On")
        
    def engineOff(self):
        if self.engine_state == "off":
            print(f"{self.serial_No} already off.")
        else:
            self.engine_state = "off"
            print(f"{self.serial_No} Off")
    
    def __repr__(self):
        return f"Car No: {self.serial_No}, Engine state: {self.engine_state}"
    
    @classmethod
    def change_brand(cls, n):
        cls.name = n
        
    @staticmethod
    def fmt(n):
        return f"BMW_{n:0>4}"



# Car.change_brand = classmethod(change_brand)

car1 = Car()

n = Car.fmt(7)   # fmt(7)
n2 = car1.fmt(9) # fmt(9)

print(car1.__repr__())
print(n)
print(n2)

car1.engineOff()



Car.change_brand("Tasla") # change_brand(Car, "Tasla")

print(Car.count)


"""



# attributes ---> class attr, obj attr
# attributes ---> data, function ---> variable attributes, methods attributes

# data / variable attributes  ---> class variable, obj/ instance variable
# methods attributes ---> instance / obj method, class method



# count, name, serial_No, color, engine_state

# class data = count(record), name(common data)
# obj/ instance data = serial_No, color, engine_state 


# engineOn, engineOff, __repr__, change_brand, fmt

# instance method---> engineOn, engineOff, __repr__, 
# class method ---> change_brand
# static method ---> fmt

















# private ( data, method )
# double underscoll  (add "_class name" to variable )
# single underscoll  ( normal variable name) ( notic )
# private access --> access from method
# assign / change new value --> change from method
# delete ---> delete from methods

# attribute check --> __dict__, hasattr(obj, "name")  eg . hasattr(c, "window_version")

# underscoll lesson









#####################

# 1. inheritance  ( tightly coupled ) ( is a )
# super class, base class,    parent class
# subclass,    derived class, child class

# 2. composition ( loosely coupled ) ( friendship ) ( has a )
# 3. tightly coupled & loosely coupled
# 4. "is a" relationship & "has a" relationship
# 5. LIFO ( last in first out )

#####################

#                                    object
#                                  /        \

#                       live obj                unlived obj

#
#                    /            \

#            human                     animals

#         /          \

#     male              female


#    /  \                      \
# mg mg  aung aung               ma ma


# super class  of mg mg ---> male, human, live obj, obj
# super class of ma ma  ---> female, human, live obj, obj

# super class of live obj ---> obj
# sub class of live obj ---> human, animals, male, female

#####################

# 1. create class A
# 2. B and C are sub/child/derived classes of A.
# 3. D and E are sub/child/derived classes of B.
# 4. F AND G are sub/child/derived classes of C.

# 5. Z is sub class of D, E , F, G.
"""

                A
                
            /       \
          B           C
        /    \      /   \
      D      E    F      G
       \     \    /      /
      
                Z
                


class A:
    head = 1
    pass


class B(A):
    x = "x"
    pass

class C(A):
    pass


class D(B):
    y = "y"
    pass

class E(B):
    pass


class F(C):
    pass

class G(C):
    pass


print(D.head) # A
print(D.x)    # B
print(D.y)

class Z(D, E , F, G):
    pass

### 

#  ORANGE

task.1 ---> draw diagram and create class.
1. create class E
2. N is a subclass of E.
3. G is a subclass of E.
4. A is a subclass of N and G.
5. O and R  are subclasses of A.
6. X is a subclass of O and R.
     E
  /    \
 N     G
  \    /
    A
  /   \
O      R
 \    /
   X

white , black

x = "white"

x = "black"

print(x)


class E:
    x = "E"
    pass

class N(E):
    x = "N"
    pass

class G(E):
    x = "G"
    pass
        
class A(N, G):
    x = "A"
    pass

class O(A):
    x = "O"
    pass
    
class R(A):
    x = "R"
    pass

class X(O, R):
    x = "X"
    pass

#print(X.__mro__)

print(.x)


# direct class
# indirect class


# ပုံကြည့်ပြီး စာရေးပါ။ class ဖန်တီးပါ။

                         စားစရာ
                  /         |       \
              အသီး      အရွက်     အသား    
            /    \
      ပန်းသီး      သစ်တော်သီး
          \      /
         ပန်းသစ်တော်

# ပန်းသစ်တော်, ပန်းသီး , သစ်တော်သီး,  အသီး ,  စားစရာ
# ပန်းသီး , အသီး , စားစရာ


class စားစရာ:
    pass
    
class အသီး(စားစရာ):
    pass
class အရွက်(စားစရာ):
    pass
class အသား(စားစရာ):
    pass

class ပန်းသီး(အသီး):
    pass
class သစ်တော်သီး(အသီး):
    pass

class ပန်းသစ်တော်(ပန်းသီး, သစ်တော်သီး):
    pass

print(ပန်းသစ်တော်.__mro__)

task.3 ---> စာဖတ်ပြီး ပုံဆွဲပါ။ ပုံကိုကြည့်ပြီး  class တည်ဆောက်ပါ။
# ဖြစ်သည်  ---> " is a "
1. ကွန်ပြူတာသည် အမျိုးအစားတစ်ခုဖြစ်သည်။
2. personal computer နှင့် super computer သည် ကွန်ပြူတာဖြစ်သည်။
3. laptop နှင့် desktop သည် personal computer ဖြစ်သည်။
4. mac book air နှင့် mac book pro သည် laptop ဖြစ်သည်။
 

                      ကွန်ပြူတာ
                      /    \
       personal computer   super computer
           /         \
         laptop        desktop
      /       \  
mac book air   mac book pro

"""



"""

task.4 ---> စာဖတ်ပြီး ပုံဆွဲပါ။ ပုံကိုကြည့်ပြီး  class တည်ဆောက်ပါ။

1. ဘာသာစကားသည် အမျိုးအစားတစ်ခုဖြစ်သည်။
2. လူနားလည်သော ဘာသာစကားနှင့် စက်နားလည်သော ဘာသာစကားတို့သည် ဘာသာစကားများဖြစ်ကြသည်။
3. မြန်မာဘာသာနှင့် English ဘာသာတို့သည် လူနားလည်သော ဘာသာစကားများဖြစ်ကြသည်
4. programming language သည် စက်နားလည်သော ဘာသာစကားဖြစ်သည်။
5. high level programming language နှင့် low level programming language တို့သည် programming language များဖြစ်ကြသည်။
6. python နှင့် java script သည် high level programming language များဖြစ်ကြသည်။
                               ဘာသာစကား ( syntax, semantics)
                             /                        \
        လူနားလည်သော ဘာသာစကား  (character )      စက်နားလည်သော ဘာသာစကား (machine code)
          /        \                                   \
    မြန်မာဘာသာ    English                          programming language (variable, function, keyword)
                                                   /              \
                             high level programming language    low level programming language
                                   /         \
                              python         java script 
                              
#  python , high level programming language , programming language, စက်နားလည်သော ဘာသာစကား, ဘာသာစကား

# if condition is "rainning", I am happy.
# if condition == "rainning":




# car
            Car
            
         /      \
             
    City car  Off_road car
 
 

class Car:
    brand = "BMW"
    def on(self):
        print(self, "engine on")
    pass

class CityCar(Car):
    tyre = 16
    pass

class OffRoadCar(Car):
    tyre = 18
    pass

class SnowCar(Car):
    tyre = "chain"
    pass

car1 = SnowCar()
print(car1.brand)
car1.on()


# step.1  ( is a ) ( inheritance ) ---> handle complex code
class Car:
    brand = "BMW"
    n = 0
    
    def __init__(self):
        Car.n += 1
        self.serial_no = f"BMW {Car.n:0>4} ({self.__class__.__name__})"
        
    def on(self):
        print(self, "engine on")
        
    def __str__(self):
        return self.serial_no

class CityCar(Car):
    tyre = "16 inches tyre"


class OffRoadCar(Car):
    tyre = "18 inches tyre"
  

class SnowCar(Car):
    tyre = "chain"
 

class TruckCar(Car):
    tyre = "24 inches tyre"
   

car1 = CityCar()
car2 = OffRoadCar()
car3 = SnowCar()
car4 = TruckCar()

cars = [car1, car2, car3, car4]

for car in cars:
    print(car, "--->", car.tyre)

print()

for car in cars:
    car.on()
    

# step.2 ( MRO )
class Car:
    brand = "BMW"
    n = 0
    
    def __init__(self):
        Car.n += 1
        self.serial_no = f"BMW {Car.n:0>4} ({self.__class__.__name__})"
        
    def on(self):
        print(self, "engine on")
        
    def __str__(self):
        return self.serial_no


class CityCar(Car):
    tyre = "16 inches tyre"
    n = 0
    def __init__(self):
        CityCar.n += 1
        self.serial_no = f"BMW {CityCar.n:0>5} ({self.__class__.__name__})"


class OffRoadCar(Car):
    tyre = "18 inches tyre"
 

class SnowCar(Car):
    tyre = "chain"
  

class TruckCar(Car):
    tyre = "24 inches tyre"
 

city_cars = []
for _ in range(10):
    city_cars.append(CityCar())
    
off_road_cars = []
for _ in range(10):
    off_road_cars.append(OffRoadCar())

snow_cars = []
for _ in range(10):
    snow_cars.append(SnowCar())
    





          E               F
        /  \            /  \
Car    A    B          C    D
       
    \  \    /      /  /
      
    
       TruckCar
       

# A, B --> E
# C, D --> F

class A(E):
    pass

class TruckCar(Car, A, B, C, D):
    tyre = "24 inches tyre"
   
# TruckCar, Car, A, B, C, D, E, F, 

#####################


#I           A

#| \     /        \
#Y  |  B           C
#|  | /  | \       /   \
#X  K D   E  J    F     G
# \  \ \  \  |    /   /

#    \ \ \  \ \ /  /
      
#              Z


#  Z D  E  B F G C A

class A:
    x = "x of A"

class B(A):
    pass
    #x = "x of B"
class C(A):
    pass
    #x = "x of C"

class D(B):
    pass
    #x = "x of D"
class E(B):
    pass
    #x = "x of E"
class J(B):
    pass

class F(C):
    pass
    #x = "x of F"
class G(C):
    pass
    #x = "x of G"

#    A

#    C
#  /   \
# F     G
#  \   /
#    Z

#      B
#  /   \  \
# D     E  J
#  \   /  /

#    Z

#  I
#  |  \
#  Y   K
#  |   /
#  X  /
#  |/
#  Z


class I:
    pass

class Y(I):
    pass

class K(I):
    pass

class X(Y):
    pass



# Z(X, Y, K, I, D, E, J, B, F, G, C, A):
# Z(X, K, D, E, J, F, G)

class Z(X, K, D, E, J, F, G):
    pass
    #x = "x of Z"

print(Z.__mro__)


####################

# multiple inheritance

# Z is sub class of D, E , F, G.

# D     E     F     G
#   \    \   /    /

#          Z


class D():
    pass
    #x = "x of D"
class E():
    pass
    #x = "x of E"
class F():
    pass
    #x = "x of F"
class G():
    x = "x of G"
class Z(D, E, F, G):
    pass
    #x = "x of Z"

print(Z.x)

####################
####################

class Hero:
    # common data ( cls data / all obj data )
    blood_effect = "red bloods effect and show damage"

    def __init__(self, name):
        # obj data
        self.name = name

chinese_hero = Hero("zilong")
myanmar_hero = Hero("minsitthar")

print(chinese_hero.blood_effect)
print(myanmar_hero.blood_effect)

Hero.blood_effect = " light red bloods effect and show damage"
print(chinese_hero.blood_effect)
print(myanmar_hero.blood_effect)

Hero.hp_percent = "hp %"

print(chinese_hero.hp_percent)
print(myanmar_hero.hp_percent)


class Computer:
    __count = 0 # class data # _Computer__count
    a = "i am class data"

    def __init__(self):
        Computer.__count += 1
        # obj data
        self.__serialNo = Computer.serial()
        self._color = "black" if Computer.__count % 2 == 0 else "white"
        self.__state = "OFF"

    def serial(): #class method
        i = str(Computer.__count)
        length = len(i)
        if length == 1:
            i = "BMW_000" + i
        elif length == 2:
            i = "BMW_00" + i
        elif length == 3:
            i = "BMW_0" + i
        else:
            i = "BMW_" + i
        return i

    def on(self): # obj method
        self.__state = "ON"
        print(self.__serialNo, "power on")

    def off(self):
        self.__state = "OFF"
        print(self.__serialNo, "power off")

    def show_info(self):
        inf = f'Computer Model No = {self.__serialNo}\ncolor = {self._color}\nstate = {self.__state}'
        print(inf)

    def get_serialNo(self):
        return self.__serialNo

computers = []
for i in range(1000):
    c = Computer()
    computers.append(c)

for computer in computers:
    if computer.get_serialNo() == "BMW_0999":
        computer.showroom_display = True
    else:
        computer.showroom_display = False

# add new instance value
for c in computers[-5:]:
    c.window_version = "window 11"

ready_sale_computers = []
need_update_computers = []

for computer in computers:
    if hasattr(computer, "window_version"):
        ready_sale_computers.append(computer)
    else:
        need_update_computers.append(computer)


#for c in ready_sale_computers:
#    print(c.__dict__)


c = Computer()
#print(c.__dict__) # obj data
# {'_Computer__serialNo': 'BMW_1001', '_color': 'white', '_Computer__state': 'OFF'}

#print(Computer.__dict__) # class data
# {'__module__': '__main__',
#
# '_Computer__count': 1001, 'a': 'i am class data',

# '__init__':<function Computer.__init__ at 0x00000225E14A2830>,
# 'serial': <function Computer.serial at 0x00000225E1901510>,
# 'on': <function Computer.on at 0x00000225E19015A0>, 'off': <function Computer.off at 0x00000225E19016C0>,
# 'show_info': <function Computer.show_info at 0x00000225E19017E0>,
# 'get_serialNo': <function Computer.get_serialNo at 0x00000225E1901750>,

# '__dict__': <attribute '__dict__' of 'Computer' objects>,
#
# '__weakref__': <attribute '__weakref__' of 'Computer' objects>,
# '__doc__': None}


print(Computer.a)
# class data
# change value from cls
Computer.a = "value change (cls data)"

#####################
#####################

# Example code of inheritance ( tightly coupled ) ( is a relationships )
# GasEngineCar is a car.
# DieselEngineCar is a car.
#  f, engin    car
#     /   \
# gas       diesel

class Car:
    def __init__(sele):
        pass

class GasEngineCar(Car):
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))

class DieselEngineCar(Car):
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))

my_car = GasEngineCar(4)
my_car.start()
print()
my_car2 = DieselEngineCar(2)
my_car2.start()
print()


#####################
#####################

# composition ( loosely coupled ) ( has a relationships )
# car has a engine.
# gas , diesel, petro


class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))

class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))

class ABS_brake:
    def brake(self):
        print("safty break with ABS system.")


class Car:
    def __init__(self, engine, brake_system):
        self.engine = engine # engine obj # loosely couple
        self.brake_system = brake_system # # loosely couple

my_car = Car(GasEngine(4), ABS_brake())
my_car.engine.start()
my_car.brake_system.brake()

print()

my_car2 = Car(DieselEngine(2), ABS_brake())
my_car2.engine.start()
my_car2.brake_system.brake()

print()

my_car2.engine = GasEngine(10)
my_car2.engine.start()
print()

class PetrolEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp petrol engine'.format(self.hp))
        
my_car2.engine = PetrolEngine(20)
my_car2.engine.start()


#####################
#####################

# Drone
# color, fan, fan_size, moter_state, gps_loc
# fly, stop, up, down, left, right, auto fly, pre fly

class Drone:
    
    def __init__(self, color, fan, fan_size, moter_state, gps_loc):
        self.color, self.fan, self.fan_size, self.moter_state, self.gps_loc = color, fan, fan_size, moter_state, gps_loc

    def fly(self):
        pass

    def stop(self):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def auto_fly(self):
        pass

    def pre_fly(self):
        pass


d1 = Drone(color="black", fan=4, fan_size=6, moter_state="off", gps_loc="")
print(d1.__dict__)

special_drone = Drone(color="red", fan=1, fan_size=5, moter_state="off", gps_loc="")
print(special_drone.__dict__)

d1.fly()
special_drone.fly()


def self_destroy(self):
    print("destroy")


Drone.destroy = self_destroy
# special_drone.destroy = self_destroy

print(d1.__dict__)
print(special_drone.__dict__)

special_drone.destroy()
d1.destroy()

#####################
#####################

# m.py

add_mark = 1

def draw_line():
    print()
    print("- " * 40)
    print()


def check_rank(highest_mark, mark):
    m = {"very good": highest_mark,
         "good": highest_mark * 0.8,
         "pass": highest_mark * 0.4,
         "fail": highest_mark * 0.4}

    if mark == m["very good"]:
        ans = "very good"

    elif mark >= m["good"]:
        ans = "good"

    elif mark >= m["pass"]:
        ans = "pass"

    elif mark < m["fail"]:
        ans = "fail"
    return ans


def exam():
    l = dict()
    mark = 0 # total
    highest_mark = 0
    for i in range(1, 13, 1):
        sub_mark = 0
        for j in range(1, 13, 4): # 1, 5, 9
            ans = int(input(f"{i} * {j} = "))
            highest_mark += add_mark
            if i * j == ans:
                print("True")
                mark += add_mark
                sub_mark += add_mark
            else:
                print("False")
            

        l[f"chapter.{i}"] = sub_mark
        # print(l)
        print(f"chapter{i} mark : {sub_mark}")
        # print(f"total mark : {mark}")
        draw_line()

    status = check_rank(mark=mark, highest_mark=highest_mark)
    return status, mark, l


def form():
    roll_no = input("roll no : ")
    name = input("name : ")
    draw_line()
    return roll_no, name

#####################

from m import *

roll_no, name = form()
status, total_mark, sub_marks = exam()

student = {
    "name" : name,
    "roll no" : roll_no,
    "status" : status,
    "total mark" : total_mark,
    "marks by chapter" : sub_marks
}


print(student)

#####################
#####################

class A:
    a = 123


A = type("A", (), {"a": 123})

#####################
#####################

class A():

    def __init__(self):
        self.__box = []

    def push(self, book):
        self.__box.append(book)

    def pop(self):
        last_book = self.__box[-1]
        del self.__box[-1]
        return last_book

    def __str__(self):
        return str(self.__box)


box_one = A()

box_one.push("Book.1")
box_one.push("Book.2")
box_one.push("Book.3")
box_one.push("Book.4")
box_one.push("Book.5")
box_one.push("Book.6")
box_one.push("Book.7")
box_one.push("Book.8")
box_one.push("Book.9")
box_one.push("Book.10")

print(box_one)

print(box_one.pop())
print(box_one.pop())
print(box_one.pop())
print(box_one.pop())
print(box_one.pop())

print(box_one.pop())
print(box_one.pop())
print(box_one.pop())
print(box_one.pop())
print(box_one.pop())

print(box_one)

#####################
#####################
int.__init__(n)

def __str__(self):
    return str(self.n) + "(Int)"

def __repr__(self):
    return str(self.n) + "(Int)"

def __add__(self, other):
    return self.n + other.n

def __sub__(self, other):
    return self.n - other.n

int

#####################
#####################

class Integer(int):
    name = "it is my int"
    def is_even(self):
        if self % 2 == 0:
            return True
        else:
            return False

    def even_odd(self):
        if self % 2 == 0:
            return "even number"
        else:
            return "odd number"

x = 1
y = 2
print(len(dir(x)))

n1 = Integer(1)   
n2 = Integer(2)

n1.x = "apple"
print(dir(n1))
print(len(dir(n1)))


l = []
for i in dir(n1):
    if i not in dir(x):
        l.append(i)

print(l)



print(n2.is_even())
print(n2.even_odd())
l = []
for i in range(1, 101):
    l.append(Integer(i))

print(l[0])
print(l)

#####################
#####################

from datetime import date

class Human: # blueprint
    head = 1  # add data for class
    leg = 2
    hand = 2
    def __init__(self, n, a):
        self.name = n # add data for object
        self.age = a  # add data for object
    
    @classmethod
    def change_head(cls, n):
        cls.head = n
    
    @staticmethod
    def birth_year(age):
        return date.today().year - age
    
    
    def info(self): # add function for object
        print(f"name = {self.name}\nage = {self.age}")

#####################

class Student(Human): # inheritance ( copy of Human' blueprint)
    shirt = "white"
    def __init__(self, n, a, student_no, attend_class):
        Human.__init__(self, n, a)
        self.student_no = student_no
        self.attend_class = attend_class
        
    def attend_record(self):
        pass
    

#####################

class Teacher(Human):
    dress = ""
    def __init__(self, n, a, payment, teach_class):
        Human.__init__(self, n, a)
        self.payment = payment
        self.teach_class = teach_class
        
    def teach_record(self):
        pass

        
#####################

student_1 = Student("Mg Mg", 20, "001", "grade_10") # contructing an object
student_1.info()

t1 = Teacher("U Ba", 50, 200000, "grade_5")
t1.info()


Teacher.change_head(3)
print(student_1.head)
print(Human.head)

print(Teacher.head)
print(t1.head)

print(t1.birth_year(30))
"""




