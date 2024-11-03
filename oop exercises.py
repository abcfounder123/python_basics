
'''

Attributes exercises

1. Laptop တွင် serial_no ပါသည်။ on, off လုပ်နိုင်သည်။
2. Network_Card တွင် speed ပါသည်။ သတ်မှတ် speed ဖြင့် download ဆွဲနိုင်သည်။
3. 1995 တွင် ပေါ်ပေါက်ခဲ့သော DialUp ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 9600bit/s ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။
4. 1999 တွင် ပေါ်ပေါက်ခဲ့သော ADSL ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 2000000bit/s (2Mbit/s)  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။
5. 2006 တွင် ပေါ်ပေါက်ခဲ့သော Ethernet ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10Mbit/s  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။
6. 2014 တွင်  Ethernet_2014 ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။
7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)
8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။
9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

Combination exercise

10. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)
မေးခွန်း နံပါတ် 8 နှင့် 9 တွင် ဖန်တီးခဲ့သော တာယာနှင့် အင်ဂျင်ကို ယူသုံးပြီး city_car တစ်စီးဖန်တီးပါ။
ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။
ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။


################################################

1. Laptop တွင် serial_no ပါသည်။ on, off လုပ်နိုင်သည်။

################################################

attributes(variable/data, method)

class   --->  Laptop
data    --->  serial_no
method  --->  on(), off()

################################################

class Laptop:
    def __init__(self, serial_no):
        self.serial_no = serial_no

    def on(self):
        pass

    def off(self):
        pass
        
################################################
        
2.  Network_Card တွင် speed ပါသည်။ သတ်မှတ် speed ဖြင့် download ဆွဲနိုင်သည်။

################################################

class   --->  NetworkCard
data    --->  speed
method  --->  download()

################################################

class NetworkCard:
    def __init__(self, speed):
        self.speed = speed

    def download(self):
        print(f"download with {self.speed}.")

################################################

n1 = NetworkCard("10 Mbps")
n2 = NetworkCard("100 Mbps")
n1.download()
n2.download()

################################################

3. 1995 တွင် ပေါ်ပေါက်ခဲ့သော DialUp ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 9600bit/s ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

################################################

class   --->  DialUp
data    --->  speed = 9600bit/s
method  --->  download()

################################################

class DialUp:
    def __init__(self):
        self.speed = "9600 bit/s"

    def download(self):
        print(f"download with {self.speed}.")


n1 = DialUp()
n1.download()

################################################

4. 1999 တွင် ပေါ်ပေါက်ခဲ့သော ADSL ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 2000000bit/s (2Mbit/s)  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

################################################

class   --->  ADSL
data    --->  speed = 2000000 bit/s (2 Mbit/s)
method  --->  download()

################################################

class ADSL:
    def __init__(self):
        self.speed = "2000000 bit/s (2 Mbit/s)"

    def download(self):
        print(f"download with {self.speed}.")


n1 = ADSL()
n1.download()

################################################

5. 2006 တွင် ပေါ်ပေါက်ခဲ့သော Ethernet ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10Mbit/s  ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

################################################

class   --->  Ethernet
data    --->  speed = 10Mbit/s
method  --->  download()

################################################

class Ethernet2006:
    def __init__(self):
        self.speed = "10Mbit/s"

    def download(self):
        print(f"download with {self.speed}.")


n1 = Ethernet2006()
n1.download()

################################################

6. 2014 တွင်  Ethernet_2014 ဟူသော network card အမျိုးအစား၏ download ဆွဲနိုင်သော အမြန်နှုန်း speed သည် 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်) ဖြစ်သည်။
ထိုအမြန်နှုန်းဖြင့် download ဆွဲနိုင်သည်။

################################################

class   --->  Ethernet2014
data    --->  speed = 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်)
method  --->  download()

################################################

class Ethernet2014:
    def __init__(self):
        self.speed = "peed = 10000Mbit/s  ( တစ်စက္ကန့်လျှင် 1250 မီဂါဘိုက်)"

    def download(self):
        print(f"download with {self.speed}.")


n1 = Ethernet2014()
n1.download()

################################################

7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)

################################################

class   --->  Car
data    --->  VIN, tires, engine
method  --->  

################################################

class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine
        
################################################

8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

################################################

class   --->  Tire
data    --->  size, pressure = 0 ( psi )
method  --->  pump(p)

################################################

def pump(p):
    print(f"pump to {p}psi.")

################################################

class Tire:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump to {pressure}psi.")


t1 = Tire(15)
print(t1.__dict__)

t1.pump(20)
print(t1.__dict__)

################################################

9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

################################################

class   --->  Engine
data    --->  fuel_type, state = "off" 
method  --->  on(), off() 

################################################

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off" 
        
    def on(self):
        self.state = "on"
        print(f"{self.fuel_type} Engine On.")
        
    def off(self):
        self.state = "off"
        print(f"{self.fuel_type} Engine Off.")
        
################################################

e1 = Engine("Petrol")
e2 = Engine("Diesel")

e1.on()
e2.on()

e1.off()
e2.off()

################################################

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            self.state = "on"
            print(f"{self.fuel_type} Engine On.")
        else:
            print("already on")

    def off(self):
        if self.state == "on":
            self.state = "off"
            print(f"{self.fuel_type} Engine Off.")
        else:
            print("already off")


e1 = Engine("Petrol")
e2 = Engine("Diesel")

e1.on()
e1.on()
e1.on()

################################################

Combination exercise

10. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, engine, tires)

မေးခွန်း နံပါတ် 8 နှင့် 9 တွင် ဖန်တီးခဲ့သော တာယာနှင့် အင်ဂျင်ကို ယူသုံးပြီး city_car တစ်စီးဖန်တီးပါ။
ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။

ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။


################################################

class   --->  Car
data    --->  VIN, tires, engine 
method  --->  

################################################

class Tire:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump to {pressure}psi.")


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        self.state = "on"
        print(f"{self.fuel_type} Engine On.")

    def off(self):
        self.state = "off"
        print(f"{self.fuel_type} Engine Off.")


class Brake:
    def __init__(self, t):
        self.type = t

    def brake(self):
        print(f"Brake with {self.type} brake system.")


class Car:
    def __init__(self, VIN, tires, engine, brake):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine
        self.brake = brake


# မေးခွန်း နံပါတ် 8 နှင့် 9 တွင် ဖန်တီးခဲ့သော တာယာနှင့် အင်ဂျင်ကို ယူသုံးပြီး city_car တစ်စီးဖန်တီးပါ။
# ကားနံပါတ်မှာ 001A ၊ တာယာမှာ 15 လက်မ၊ ဆီအမျိုးအစားမှာ petrol ဓါတ်ဆီ ဖြစ်သည်။
city_car = Car("001A", Tire(15), Engine("petrol"), Brake("ABS"))

# ထိုကားကို လေဖိအား 3 psi ထိလေထိုးပြီး စက်နှိုးပါ။
city_car.tires.pump(3)
city_car.engine.on()
city_car.brake.brake()

################################################

car1 = Car(Tire(), Engine(), Brake())
print(car1.__dict__)

car1 = Car(Tire(), Engine(), Brake())
print(car1.__dict__)

car1 = Car(Tire(), Engine(), Brake())
print(car1.__dict__)

print(Car.n)

################################################

class Tire:
    def __init__(self, size=15):
        self.size = size
        self.pressure = 0

    def pump(self, pressure):
        self.pressure = pressure
        print(f"pump to {pressure}psi.")


class Engine:
    def __init__(self, fuel_type="petrol"):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        self.state = "on"
        print(f"{self.fuel_type} Engine On.")

    def off(self):
        self.state = "off"
        print(f"{self.fuel_type} Engine Off.")


class Brake:
    def __init__(self, t="ABS"):
        self.type = t

    def brake(self):
        print(f"Brake with {self.type} brake system.")


class Car:
    n = 0

    def __init__(self, tires, engine, brake):
        Car.n += 1
        self.VIN = f"BMW_{Car.n:0>4}"
        self.tires = tires
        self.engine = engine
        self.brake = brake

    def __repr__(self):
        return f"{self.VIN}"


cars = []
for _ in range(15):
    cars.append(Car(Tire(), Engine(), Brake()))

print(cars[-1].VIN)

print(Car.n)

################################################

'''
