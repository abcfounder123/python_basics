"""
#####################

# 1. inheritance  ( tightly coupled ) ( is a )
# super class, base class,    parent class
# subclass,    derived class, child class

# 2. composition ( loosely coupled ) ( friendship ) ( has a )
# 3. tightly coupled & loosely coupled
# 4. "is a" relationship & "has a" relationship
# 5. LIFO ( last in first out )

#################################################

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

# sub class of live obj ---> obj
# sub class of live obj ---> human, animals, male, female

#####################

# 1. create class A
# 2. B and C are sub/child/derived classes of A.
# 3. D and E are sub/child/derived classes of B.
# 4. F AND G are sub/child/derived classes of C.

# 5. Z is sub class of D, E , F, G.

#################################################

#           A

#      /        \
#    B           C
#  /   \       /   \
# D     E     F     G
#   \    \   /    /

#          Z

# LIFO

#  MRO   --> Z DEB FGC A

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

#    B
#  /   \
# D     E
#  \   /
#    Z

class Z(D, E, F, G):
    pass
    #x = "x of Z"

print(Z.x)

#################################################

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

#################################################

# Example code of inheritance ( tightly coupled ) ( is a relationships )
# GasEngineCar is a car.
# DieselEngineCar is a car.
#      car
#     /   \
# gas       diesel

class Car:
    def __init__(self, engine):
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

#################################################

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
        self.engine = engine
        self.brake_system = brake_system

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

#################################################

#################################################

Attributes exercises 

1. Laptop တွင် serial_no ပါသည်။ on, off လုပ်နိုင်သည်။

Note

a.  name --> Laptop 
b.  attributes
data --> serial_no
method --> on, off

class Laptop:
    def __init__(self, serial_no):
        self.serial_no = serial_no
    def on(self):
        print("power on")
    def off(self):
        print("power off")

#################################################

2.  Network_Card တွင် speed ပါသည်။ သတ်မှတ် speed ဖြင့် download ဆွဲနိုင်သည်။

a.  name --> Network_Card 
b.  attributes
data --> speed
method --> download

class Network_Card:
    def __init__(self, speed):
        self.speed = speed
    def download(self):
        print(f"download with speed {self.speed}")
    
#################################################
   
3. 1995 တွင် ပေါ်ပေါက်ခဲ့သော DialUp ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 9600bit/s ဖြစ်သည်။ 
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။ 

a.  name --> DialUp 
b.  attributes
data --> speed = 9600bit/s
method --> download

class DialUp:
    def __init__(self):
        self.speed = "9600bit/s"
    def download(self):
        print(f"download with speed {self.speed}")
        
#################################################
        
4. 1999 တွင် ပေါ်ပေါက်ခဲ့သော ADSL ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 2000000bit/s (2Mbit/s)  ဖြစ်သည်။ 
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။     

a.  name --> ADSL
b.  attributes
data --> speed = 2000000bit/s
method --> download

class ADSL:
    def __init__(self):
        self.speed = "2000000bit/s"
    def download(self):
        print(f"download with speed {self.speed}")
    
#################################################

5. 2006 တွင် ပေါ်ပေါက်ခဲ့သော Ethernet ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10Mbit/s  ဖြစ်သည်။ ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။     

a.  name --> ADSL
b.  attributes
data --> speed = 10000000bit/s
method --> download

class Ethernet_2006:
    def __init__(self):
        self.speed = "10000000bit/s"
    def download(self):
        print(f"download with speed {self.speed}")
        
#################################################
    
6. 2014 တွင်  Ethernet_2014 ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) ဖြစ်သည်။ ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။     

a.  name --> Ethernet_2014
b.  attributes
data --> speed = 10000Mbit/s
method --> download

class Ethernet_2014:
    def __init__(self):
        self.speed = "10000Mbit/s"
    def download(self):
        print(f"download with speed {self.speed}")
        
#################################################
        
7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)

a.  name --> Car
b.  attributes
data --> (VIN, engine, tires)
method --> 

class Car:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires
        
#################################################
        
8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

a.  name --> Tires 
b.  attributes
data --> size, pressure = 0 ( psi )
method --> pump()

class Tires:
    def __init__(self, size, pressure=0):
        self.size = size
        self.pressure = pressure
    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump tires to {pressure} psi.")

city_tire = Tires(15)
print(city_tire.size)
print(city_tire.pressure)

city_tire.pump(8)
print(city_tire.pressure)

off_road_tire = Tires(18)
print(off_road_tire.size)
print(off_road_tire.pressure)

off_road_tire.pump(12)
print(off_road_tire.pressure)

( ဗဟုသုတ --> မြို့တွင်းမောင်းသောကားတာယာ၏ size သည် 15 လက်မ ဖြစ်ပြီး လမ်းကြမ်းမောင်းသော ကားတာယာ၏ size သည် 18 လက်မဖြစ်သည်။ ) 

#################################################

9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

a.  name --> Engine 
b.  attributes
data --> fuel_type, state="off"
method --> on(), off()

class Engine:
    def __init__(self, fuel_type, state="off"):
        self.fuel_type = fuel_type
        self.state = state
       
    def on(self):
        self.state = "on"
        print(f"Engine on with {self.fuel_type} fuel type.")
        
    def off(self):
        self.state = "off"
        print(f"Engine off with {self.fuel_type} fuel type.")

#################################################

Combination exercise
10. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)
မေးခွန်း နံပါတ် 8 နှင့် 9 တွင် ဖန်တီးခဲ့သော တာယာနှင့် အင်ဂျင်ကို ယူသုံးပြီး city_car တစ်စီးဖန်တီးပါ။
ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။
ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။ 

class Car:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

class Tires:
    def __init__(self, size, pressure=0):
        self.size = size
        self.pressure = pressure
    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump tires to {pressure} psi.")

class Engine:
    def __init__(self, fuel_type, state="off"):
        self.fuel_type = fuel_type
        self.state = state

    def on(self):
        self.state = "on"
        print(f"Engine on with {self.fuel_type} fuel type.")

    def off(self):
        self.state = "off"
        print(f"Engine off with {self.fuel_type} fuel type.")

# ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။
city_car = Car(VIN="001A", engine=Engine("petrol"), tires=Tires(15))

# ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။
city_car.tires.pump(3)
city_car.engine.on()

#################################################

inheritance exercise
11. Jet လေယာဉ်တွင် တိုက်ခိုက်မှုအမျိုးအစား ၊ အမည်နှင့် ထုတ်လုပ်သောနိုင်ငံဟူသော အချက်အလက်ပါရှိသည်။
( role, name, country )
F35 နှင့် F22 သည် Jet လေယာဉ်ဖြစ်သည်။
       Jet
     /     \
   F35     f22
   
a.  name --> Jet
b.  attributes
data -->  role, name, country
method --> 

class Jet:
    def __init__(self, role, name, country):
        self.role = role
        self.name = name
        self.country = country
        
# F35 သည် Jet လေယာဉ်ဖြစ်သည်။    

class F35(Jet):
    pass

# F22 သည် Jet လေယာဉ်ဖြစ်သည်။
class F22(Jet):
    pass

#################################################

12. 
I, J, K သည် A ၏ sub class ဖြစ်သည်။
X သည် I ၏ sub class ဖြစ်သည်။
Y သည် J ၏ sub class ဖြစ်သည်။
Z သည် K ၏ sub class ဖြစ်သည်။
ပုံဆွဲပါ။
class တည်ဆောက်ပါ။
         A
      / /  \
   I   J    K
  /   /      \
 X   Y        Z
 
class A:
    pass

class I(A):
    pass
class J(A):
    pass
class K(A):
    pass
    
class X(I):
    pass
    
class Y(J):
    pass
    
class Z(K):
    pass

#################################################

13.  အောက်ပါပုံအတိုင်း class တည်ဆောက်ပါ။
 ................  .Fruit
 
 .......  ...../. .....\......\
 
        Apple        Mango          Banana
      ............/.. .\   ...\
          မချစ်စု        စိန်တလုံး    တောသရက်
          
class Fruit:
    pass

class Apple(Fruit):
    pass
class Mango(Fruit):
    pass
class Banana(Fruit):
    pass
    
class မချစ်စု(Mango):
    pass
class စိန်တလုံး(Mango):
    pass
class တောသရက်(Mango):
    pass
    
#################################################
    
multiple inheritance exercises
14. ပန်းသီးနှင့် သစ်တော်သီးသည် သစ်သီးများဖြစ်ကြသည်။
 ပန်းသစ်တော်သီးသည် ပန်းသီးနှင့် သစ်တော်သီးနှစ်မျိုးလုံးမှ မျိုးဗီဇများ အမွေဆက်ခံထားသည်။ 
ထို့ကြောင့် ပန်းသစ်တော်သီးသည် ပန်းသီးလည်း ဖြစ်သလို သစ်တော်သီးလည်းဖြစ်သည်။
ပုံဆွဲပြီး class တည်ဆောက်ပါ။

     Fruit
  /        \
apple     သစ်တော်သီး
  \        /
  ပန်းသစ်တော်သီး

class ပန်းသစ်တော်သီး(apple, သစ်တော်သီး):
    pass
    
ပန်းသစ်တော်သီး MRO ---> ပန်းသစ်တော်သီး, apple, သစ်တော်သီး, Fruit

#################################################

# diamond broblem
        Fruit
    /   /        \
   \   apple     သစ်တော်သီး
    \  \        /
      ပန်းသစ်တော်သီး

class ပန်းသစ်တော်သီး(Fruit, apple, သစ်တော်သီး): # diamond broblem
    pass
ပန်းသစ်တော်သီး MRO ---> ပန်းသစ်တော်သီး, Fruit,  apple, သစ်တော်သီး, Fruit

class Fruit:
    pass

class apple(Fruit):
    pass
class သစ်တော်သီး(Fruit):
    pass

class ပန်းသစ်တော်သီး(apple, သစ်တော်သီး):
    pass
print(ပန်းသစ်တော်သီး.__mro__)

#################################################

15. 
A, B သည် Y ဖြစ်သည်။
C, D, E သည် Z ဖြစ်သည်။
X သည် A, B, C, D, E, F ဖြစ်သည်။
ပုံဆွဲပြီး class တည်ဆောက်ပါ။

       Y
     /   \
    A     B
    
         Z
     /  /  \  
    C  D    E   

A   B   C   D   E  F
 \  \  \   /  /  /
   \ \  \ /  /  /
         X

  Y          Z
/   \    /  /  \  
A   B   C   D   E   F
 \  \  \   /  /   /
   \ \  \ /  /  /
    \ \ \ / / /
     \ \\ ///
     
         X

class Y:
    pass

class Z:
    pass

class A(Y):
    pass
class B(Y):
    pass

class C(Z):
    pass
class D(Z):
    pass
class E(Z):
    pass

class F:
    pass

class X(A, B, C, D, E, F):
    pass

print(X.__mro__)

#################################################

16. X ၏ attributes ကို ရှာဖွေပါက မည့်သည့်အစီအစဉ်အတိုင်းရှာဖွေမည်နည်း။ 
နမူနာ အဖြေ
Method Resolution Order = X -> A  -> B -> C -> D -> E -> F -> Y -> Z

Ans : Method Resolution Order = X ->    A  -> B -> Y ->    C -> D -> E -> Z  ->    F
                                X'>,    A'>,  B'>, Y'>,    C'>, D'>, E'>, Z'> ,    F

#################################################

#################################################

class Engine:
    def __init__(self, fuel):
        self.fuel = fuel
        self.state = "off"

    def start(self):
        self.state = 'on'

    def stop(self):
        self.state = 'off'

    def get_state(self):
        return self.state

    def __str__(self):
        return f"{self.fuel} Engine ({self.state} condition)"

# tire (us)
# tyre (common english)
class Tire:
    def __init__(self, car):
        # different value, different data
        if car == "city car":
            self.tire_name = "city tire"
            self.city_tire_size = 15
        elif car == "off road car":
            self.tire_name = "off road tire"
            self.off_road_tire_size = 18
        else:
            print(f"We have not tires for {car}.")
        self.pressure = 0

    def get_pressure(self):
        return self.pressure

    def pump(self, psi):
        self.pressure = psi

    def __str__(self):
        if hasattr(self, "city_tire_size"):
            size = self.city_tire_size
        elif hasattr(self, "off_road_tire_size"):
            size = self.off_road_tire_size
        else:
            size = None
        return f"{size} inches {self.tire_name} ({self.pressure} psi)"

class Car:
    n = 0
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
        Car.n += 1
        self.vin = f"BMW_{Car.n:0>4}"

    def pump(self, psi):
        self.tires.pump(psi)

    def start(self):
        self.engine.start()

    def get_tire_name(self):
        return self.tires.tire_name

    def __str__(self):
        return f"\nCar No. = {self.vin}\nCar Engine = {self.engine}\nCar Tyres = {self.tires}\n"

# petrol_engine = Engine("petrol")
# diesel_engine = Engine("diesel")

# city_tires = Tire("city car")
# off_road_tires = Tire("off road car")

# snow_tires = Tire("snow car")

city_petrol_car = Car(Engine("petrol"), Tire("city car"))
off_road_diesel_car = Car(Engine("diesel"), Tire("off road car"))

# call method
city_petrol_car.engine.start()
city_petrol_car.start()

# access data
print(city_petrol_car.tires.tire_name)
print(city_petrol_car.get_tire_name())

# access difference data of same class
print(city_petrol_car.tires.city_tire_size)
print(off_road_diesel_car.tires.off_road_tire_size)

cars = list()
# creating cars
for i in range(100):
    cars.append(Car(Engine("petrol"), Tire("city car")))
    cars.append(Car(Engine("diesel"), Tire("off road car")))

# access different data
for car in cars:
    if hasattr(car.tires, "city_tire_size"):
        print(car.tires.city_tire_size)
    elif hasattr(car.tires, "off_road_tire_size"):
        print(car.tires.off_road_tire_size)

# print(cars[0].tires)

cars[3].tires.pump(10)
for car in cars:
    print(car.tires)

for car in cars:
    if car.tires.tire_name == "city tire" and car.tires.pressure != 7:
        car.pump(7)
    elif car.tires.tire_name == "off road tire" and car.tires.pressure != 10:
        car.pump(10)
    car.start()

for car in cars:
    print(car)

#################################################

#################################################
    
class Tire:
    def __init__(self, car, pressure=0):
        self.pressure = pressure
        if car == "city car":
            self.tire_name = "city tire"
            self.city_tire_size = 15
        elif car == "off road car":
            self.tire_name = "off road tire"
            self.off_road_tire_size = 18
        else:
            print(f"We have not tires for {car}.")

    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump tires to {pressure} psi.")

class Engine:
    def __init__(self, fuel_type, state="off"):
        self.fuel_type = fuel_type
        self.state = state

    def __on(self): # _Engine__on()
        self.state = "on"
        print(f"Engine on with {self.fuel_type} fuel type.")

    def off(self):
        self.state = "off"
        print(f"Engine off with {self.fuel_type} fuel type.")

class Car:
    no = 0
    def __init__(self, engine, tires):
        Car.no += 1
        self.VIN = Car.no
        self.engine = engine
        self.tires = tires

    def on(self):
        self.engine._Engine__on()

    def off(self):
        self.engine.off()

    def pump(self, pressure):
        self.tires.pump(pressure)

    def get_size(self):
        return self.tires.size

cars = list()

for i in range(10):
    cars.append(Car(Engine("petrol"), Tire("city car")))
    cars.append(Car(Engine("diesel"), Tire("off road car")))

for car in cars:
    if hasattr(car.tires, "city_tire_size"):
        print(car.tires.city_tire_size)
    elif hasattr(car.tires, "off_road_tire_size"):
        print(car.tires.off_road_tire_size)

#################################################

1. class
Engine , Tyre
Car has Engine and Tyre

#################################################

2. if we use combination method, we need to take care not to use same obj

#################################################

3. call method / access data

city_petrol_car.engine.start()
print(city_petrol_car.tires.size)

#################################################

4. same attribute with different value
        if car == "city car":
            self.size = 15
        elif car == "off road car":
            self.size = 18
        else:
            self.size = None
            print(f"We have not tires for {car}.")

#city_tires = Tire("city car")
#off_road_tires = Tire("off road car")
#snow_tires = Tire("snow car")

#################################################

5. name space 
# call method
city_petrol_car.engine.start()
city_petrol_car.start()

# access data
print(city_petrol_car.tires.size)
print(city_petrol_car.get_size())

#################################################

6. private access 
( engine ကတစ်ဆင့် စက်နှိုးခွင့်မပေး ) 
( ကားကတစ်ဆင့် စက်နှိုးခွင့်ပေး )
def start(self):
        self.engine._Engine__start()
 
#city_petrol_car.engine.start()
city_petrol_car.start()

#################################################

7. different value, different data
        if car == "city car":
            self.tire_name = "city tire"
            self.city_tire_size = 15
        elif car == "off road car":
            self.tire_name = "off road tire"
            self.off_road_tire_size = 18
        else:
            print(f"We have not tires for {car}.")

#################################################
       
8. access difference data of same class

print(city_petrol_car.tires.city_tire_size)
print(off_road_diesel_car.tires.off_road_tire_size)

cars = list()

for i in range(10):
    cars.append(Car(Engine("petrol"), Tire("city car")))
    cars.append(Car(Engine("diesel"), Tire("off road car")))

for car in cars:
    if hasattr(car.tires, "city_tire_size"):
        print(car.tires.city_tire_size)
    elif hasattr(car.tires, "off_road_tire_size"):
        print(car.tires.off_road_tire_size)

#################################################

9. adding obj methods

#################################################

10. adding magic method 
def __str__(self):
       return f"\nCar No. = {self.vin}\nCar Engine = {self.engine}\nCar Tyres = {self.tires}\n"
       
#print(cars[0].tires)      
for car in cars:
    print(car.tires)
    
for car in cars:
    print(car)

#################################################

"""













