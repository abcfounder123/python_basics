# custom objects
# rational numbers

"""
from fractions import Fraction
x = Fraction(2, 6)
print(x)
#x.denominator = 3

print("-" * 30)

class F():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator == 0:
            raise ZeroDivisionError(f"F({numerator}, {denominator})")
        else:
            self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return F(n, d)

    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return F(n, d)

    def __mul__(self, other):
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return F(n, d)

    def __truediv__(self, other):
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return F(n, d)

    def __setattr__(self, key, value):
        if key not in ("numerator", "denominator"):
            raise AttributeError(f"'Fraction' object has no attribute '{key}'")
        elif key in self.__dict__:
            raise AttributeError(f"can't set attribute '{key}'")
        else:
            self.__dict__[key] = value



y = F(2, 6)

print(y)
#AttributeError: 'Fraction' object has no attribute 'n'
#can't set attribute 'numerator'

"""

"""
111, Mg Mg, 300000
222, Ma Ma, 400000
333, Hla Hla, 500000
444, Mya Mya, 600000
555, Kyaw Kyaw, 700000
666, Aung Aung, 800000
777, Mg Mg, 900000
888, Ma Ma, 100000
"""

"""
Bank account
1. initializes data of bank account object (account No, name, balance, address, phone no) 
   ( disallow balance less than equal 5 ) ( should limit deposit and withdraw )( account information can only be got via info method )
2. clients may add funds via deposit method. ( limit amount of a deposit or maximum balance)
3. withdraw method prevents a client from withdrawing more money than is in the account.
   overdraft attempt will not change the account balance
4. show data if print obj
5. making fun with color ( "/033[1;31m
6. test obj
7. file of bank account ( account_data.text )
8. database sample ( open, print) ( get, add, delete, commit )
9. test 
"""
"""
red = "\033[1;31m"
green = "\033[1;32m"
end = "\033[0m"
"""
"""
class BankAccount:
    def __init__(self, id, name, balance):
        if balance < 5:
            raise ValueError("Initial value does not less than 5 $.")
        self.__id = id
        self.__name = name
        self.__balance = balance

    def info(self):
        return self.__id, self.__name, self.__balance

    def deposit(self, amount):
        if self.__balance + amount <= 1_000_000:
            self.__balance += amount
            return "\033[1;32m" + "OK" + "\033[0m"
        else:
            return "\033[1;31m" + "Fail" + "\033[0m"

    def withdraw(self, amount):
        if self.__balance - amount >= 5:
            self.__balance -= amount
            return "\033[1;32m" + "OK" + "\033[0m"
        else: return "\033[1;31m" + "Fail" + "\033[0m"

    def __str__(self):
        return "{:<5} {:<10} {:>20}".format(self.__id, self.__name, "\033[1;32m" + str(self.__balance) + "\033[0m")



def test(account):
    print("Before Test")
    print(account)
    print("-" * 20)

    print("Test for deposit")
    print("After testing with deposit 100$.")
    a = account.deposit(100)
    print("deposit state =", a)
    print(account)
    print("-" * 20)

    print("After testing with deposit 1_000_000$.")
    a = account.deposit(1_000_000)
    print("deposit state =", a)
    print(account)
    print("-" * 20)

    print("Test for withdraw")
    print("After testing with  100$.")
    a = account.withdraw(100)
    print("withdraw state =", a)
    print(account)
    print("-" * 20)

    print("After testing with 1_000_000$.")
    a = account.withdraw(1_000_000)
    print("withdraw state =", a)
    print(account)
    print("-" * 20)
    print("-" * 20)


"""

# import this


"""

# stopwatch


from time import time, sleep, asctime

class StopWatch():
    def __init__(self):
        self.reset()

    def reset(self):
        self.start_time = 0
        self.ans = 0
        self.start_condition = False
        self.record = ""

    def start(self):
        if self.start_condition:
            self.record += asctime() + "  >> User click start many times. second start will not work.\n"
        else:
            self.start_time = time()
            self.start_condition = True

    def stop(self):
        if self.start_condition:
            self.ans += round(time() - self.start_time)
            self.start_condition = False
        else:
            self.record += asctime() + f"  >> User clicked stop button before start button.Elapsed time was not be calculated.So, initial value or old value is {self.ans}.\n"

    def elapsed_time(self):
        if self.start_condition:
            return round(time() - self.start_time)
        else:
            return self.ans


x = StopWatch()
x.start()
sleep(1)

x.start()

sleep(2)
x.stop()
print(x.elapsed_time())

#x.reset()

sleep(2)
x.stop()
print(x.elapsed_time())
print(x.record)


"""

"""

from tkinter import Canvas, Tk, Frame, Button
x = Tk()
c = Canvas(x, width=400, height=800)
c.pack()
c.create_rectangle(100, 100, 300, 620, fill="gray")
c.create_oval(140, 140, 140 + 120, 140 + 120, fill="red")
c.create_oval(140, 140 + 120 + 40, 140 + 120, 140 + 120 + 40 + 120, fill="yellow")
c.create_oval(140, 140 + 120 + 40 + 120 + 40, 140 + 120, 140 + 120 + 40 + 120 + 40 + 120, fill="green")

x.mainloop()


"""

# 2. Restricting access to members (data)
# _
# __
"""
class Account():
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __change_password(self, new_password):
        self.password = new_password

accountNo1 = Account(name = "Mg Mg", password = "123456")
print(accountNo1.__dict__)
print(dir(accountNo1))

accountNo1._Account__change_password(new_password="abc123")

print(accountNo1.__dict__)
"""

"""

# myapp, myfunction, Test

class FunctionTester:
    def __init__(self):
        self.__error = 0
        self.__total = 0
        print("Testing\n")

    def check(self, msg, true_value, func, *args):
        print(" ", msg, " : ", end="")
        self.__total += 1
        calc_value = func(*args)  # Apply function to arguments
        if calc_value == true_value:
            print("\033[1;32m" + "OK" + "\033[0m")
        else:
            self.__error += 1  # Count this failed test
            print("\033[1;31m" + "Failed! >> true value:", true_value, "calculated value:", calc_value, "\033[0m")

    def report_results(self):
        print(self.__total, "tests run")
        print(self.__total - self.__error, "\033[1;32m" + "passed" + "\033[0m")
        print(self.__error, "\033[1;31m" + "failed" + "\033[0m")

# 1, 2, 3, 4, 5, 6, 2, 5
def maxfun(l):
    max = l[0]
    for n in l:
        if n > max:
            max = n
    return max



def sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

t = FunctionTester()

t.check("max_of_three test #1", 99, maxfun, range(100))
t.check("sum function test.1", 10, sum, range(5))
t.report_results()



"""

"""
t = FunctionTester()

t.check("max_of_three test #1", 4, max_of_three, 2, 3, 4)
t.check("max_of_three test #2", 4, max_of_three, 4, 3, 2)
t.check("max_of_three test #3", 4, max_of_three, 3, 2, 4)


t.report_results()




# functiontester


"""

"""

class FunctionTester:
    def __init__(self):
        self.__error = 0
        self.__total = 0
        print("Testing\n")

    def check(self, msg, true_value, func, *args):
        result = True
        print(" ", msg, " : ", end="")
        self.__total += 1
        try:
            calc_value = func(*args)  # Apply function to arguments
            if calc_value == true_value:
                print("OK")
            else:
                self.__error += 1  # Count this failed test
                print("Failed! >> true value:", true_value, "calculated value:", calc_value)
                result = False  # Test failed
        except Exception as e:
            self.__error += 1  # Count this failed test
            print("Exception =", e)
            result = False  # Test failed
        return result  # Notify client of test result

    def report_results(self):
        print(self.__total, "tests run")
        print(self.__total - self.__error, "passed")
        print(self.__error, " failed")


# from functiontester import FunctionTester

def max_of_three_bad(x, y, z):
    result = x
    if y > result:
        result = y
    elif z > result:
        result = z
    return result


def max_of_three_good(x, y, z):
    result = x
    if y > result:
        result = y
    if z > result:
        result = z
    return result


def sum(lst):
    total = 0
    for i in lst:
        total += i
    return total


# return 0 # to do
# stub
def maximum(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max


def sqrt(x):
    return 0.0  # TODO implement the square root function

"""

"""

from turtle import Screen, TurtleScreen, RawTurtle
from math import sin, cos, tan

def plot_function():
	pen.color("black")
	pen.up()
	x = min_x
	pen.setposition(x, eval(relationship))
	pen.down()

	while x < max_x:
		pen.setposition(x, eval(relationship))
		print(x, eval(relationship))
		x += pixel

	pen.up()

width, height = 600, 600
min_x, max_x = -10, 10
min_y, max_y = -10, 10
font = ("areal", 30, "bold")
# total x = max x - min x = 10 - ( - 10 ) = 20
# 600px = 20
# 1px = ?
# 1px = 20 / 600 = 0.03333333333333333
pixel = (max_x - min_x)/width # 1 px

relationship = "2*x"
# tkinter canvas ပေါ်မှာဆွဲချင်ရင် TurtleScreen
screen = Screen()

screen.setup(width=width, height=height)
screen.screensize(width, height)

screen.setworldcoordinates(min_x, min_y, max_x, max_y)
screen.bgcolor("gray")
screen.tracer(0)
#screen.tracer(0, 0)
# 0 do not draw pen
# (n, delay)
# n th update, delay time ( default value = 10 ms)

# မျက်နှာပြင်တစ်ခုပေါ်မှာပဲ ဆွဲဖို့
pen = RawTurtle(screen)
pen.hideturtle()
'''
'fastest’ :  0
‘fast’    :  10
‘normal’  :  6
‘slow’    :  3
‘slowest’ :  1
'''
pen.speed("fast")

plot_function()
screen.update()
screen.mainloop()

"""

"""

from turtle import Screen, TurtleScreen, RawTurtle
from math import atan2, pi, sin, cos, tan

def draw_grid():
		pen.up()
		pen.color("green")
		x = min_x
		while x <= max_x:
			pen.setposition(x, min_y)
			pen.down()
			pen.setposition(x, max_y)
			pen.up()
			x += xinc # Next x

		y = min_y
		while y <= max_y:
			pen.setposition(min_x, y)
			pen.down()
			pen.setposition(max_x, y)
			pen.up()
			y += yinc


def set_label():
    pen.color("black")
    pen.setposition(min_x , 0)
    pen.down()
    pen.setposition(max_x , 0)
    pen.up()

    pen.setposition(0, max_y)
    pen.down()
    pen.setposition(0, min_y)
    pen.up()

    py = 2*yinc
    px = 2*xinc
    pen.setposition(0 - px , 0 - py)
    pen.down()
    pen.write("0", font=font)
    pen.up()

    pen.setposition(max_x - px, 0 - py)
    pen.down()
    pen.write("X", font=font)
    pen.up()

    pen.setposition(0 - px, max_y - py)
    pen.down()
    pen.write("Y", font=font)
    pen.up()


def plot_function():
	pen.color("black")
	pen.up()
	x = min_x
	pen.setposition(x, eval(relationship))
	pen.down()

	while x < max_x:
		pen.setposition(x, eval(relationship))
		x += pixel

	pen.up()

width, height = 600, 600
min_x, max_x = -10, 10
min_y, max_y = -10, 10 # -10, 100
font = ("areal", 30, "bold")
pixel = (max_x - min_x)/width # 1 px

n = 20
xinc = (max_x - min_x)/n
yinc = (max_y - min_y)/n



relationship = "sin(x)"
screen = Screen()

screen.setup(width=width, height=height)
screen.screensize(width, height)

screen.setworldcoordinates(min_x, min_y, max_x, max_y)
screen.bgcolor("gray")
screen.tracer(0)

pen = RawTurtle(screen)
pen.hideturtle()
pen.speed("fast")

draw_grid()
set_label()
plot_function()
screen.update()
screen.mainloop()


"""

"""


from turtle import TurtleScreen, RawTurtle
from math import sin, cos, tan
from tkinter import*

def draw_grid():
	pen.up()
	pen.color("green")
	x = min_x
	while x <= max_x:
		pen.setposition(x, min_y)
		pen.down()
		pen.setposition(x, max_y)
		pen.up()
		x += xinc  # Next x

	y = min_y
	while y <= max_y:
		pen.setposition(min_x, y)
		pen.down()
		pen.setposition(max_x, y)
		pen.up()
		y += yinc

def set_label():
	pen.color("black")
	pen.setposition(min_x, 0)
	pen.down()
	pen.setposition(max_x, 0)
	pen.up()

	pen.setposition(0, max_y)
	pen.down()
	pen.setposition(0, min_y)
	pen.up()

	py = 2 * yinc
	px = 2 * xinc
	pen.setposition(0 - px, 0 - py)
	pen.down()
	pen.write("0", font=font)
	pen.up()

	pen.setposition(max_x - px, 0 - py)
	pen.down()
	pen.write("X", font=font)
	pen.up()

	pen.setposition(0 - px, max_y - py)
	pen.down()
	pen.write("Y", font=font)
	pen.up()


def clear():
    pen.clear()
    draw_grid()
    set_label()

def plot_function():
	pen.up()
	x = min_x
	pen.setposition(x, eval(e.get()))
	pen.down()

	while x < max_x:
		pen.setposition(x, eval(e.get()))
		# screen.update()
		x += pixel
	screen.update()

width, height = 600, 600
min_x, max_x = -10, 10
min_y, max_y = -10, 10 # -10, 100
pixel = (max_x - min_x)/width # 1 px 
font = ("areal", 30, "bold")

n = 20
xinc = (max_x - min_x)/n
yinc = (max_y - min_y)/n

root = Tk()
root.title("Data Plotting")
canvas = Canvas(root)
canvas.config(width=width, height=height)
canvas.pack()

relationship = StringVar()
e = Entry(root, textvariable=relationship, font=font)
e.pack()

Button(root, text="Plot data", command=plot_function, font=font).pack()
Button(root, text="clear", command=clear, font=font).pack()


screen = TurtleScreen(canvas)
screen.setworldcoordinates(min_x, min_y, max_x, max_y)
screen.bgcolor("gray")
screen.tracer(0)
# margin
#min_x, max_x = min_x + 2, max_x - 2
#min_y, max_y = min_y + 2, max_y - 2

pen = RawTurtle(screen)
pen.hideturtle()
pen.speed("fast")

clear()

root.mainloop()










"""

# u = velocity in meter per sec,
# theta = radian value of degree (45 ° = 0.785),
# t = time in seconds
# g = 9.8 ( force due to gravity )

# f(t) = u*sin(theta)*t - 0.5*g*t**2

# if  f(t) == 0 , it will stop
# 50*sin(0.785)*x - 0.5*9.8*x**2
# 15
# eval(e.get()) >= 0:



































"""

13.9 dynamic content ( instance variable ) ( extra --> dynamically create instance methods )

user , data ပေါ်မူတည်ပြီးပြောင်းလဲတဲ့ content ကို dynamic content လို့ခေါ်
ဥပမာ။ ။ Facebook ကို မောင်မောင် account နဲ့ဝင်ရင် mg mg နဲ့ဆိုင်တာတွေပြပေးသလိုမျိုး။

object ပေါ်မူတည်ပြီးပြောင်းလဲတဲ့ variable ကို instance variable လို့ခေါ်

#####################

instance variable

create           --->   1. normal
                           >> init
                        2. dynamically create
                           >> dot ( need rules of naming )
                           >> setattr(obj, attr, value) ( no rule )
                            
access           --->   1. dot
                        2. getattr(obj, attr)
                        3. __dict__

delete           --->   1. del
                        2. delattr(obj, attr)

#####################

instance method
create           --->   1. normal
                        2. dynamically create
                           >> dot ( need rules of naming )
                              # for one obj
                              import types
                              mg_mg.calculate_grade = types.MethodType(calculate_grade, mg_mg)
                              
                              # for all obj ( as class attributes )
                              Student.calculate_grade = calculate_grade
                              
                           >> setattr(obj, attr, value) ( no rule) 
                              setattr(Student, "", calculate_grade)
                              getattr(mg_mg, "")()

access           --->   1. dot
                        2. getattr(obj, attr)()
                           note   --->   if you want to check all method, use __dir__()
                        
delete           --->   1. dot   --->   del
                        2. delattr(obj, attr)


#####################

Note

1. instance variable ကို dot နှင့်ဖန်တီးလျှင် 
rule လိုအပ်
x.a = 10

2. setattr နှင့် getattr, delattr ဆိုလျှင် ဘာမှမလိုအပ်
setattr(x, "", 10)

3. ပေးချင်ရာပေးထားရင် dot နဲ့ဖျက်မရ / access လုပ်မရ
setattr(mg_mg, "history of Mg Mg", "mg mg has good characters.")
print(getattr(mg_mg, "history of Mg Mg"))
delattr(mg_mg, "history of Mg Mg")

4. When using setattr, getattr and delattr functions, attributes name must be string.
5. if you want to check all method, use __dir__()


#  do not need to explain
#  def calculate_grade(self):
         self.grade = .....
         return self.grade                                                       
# >> ma_ma.cal = calculate_grade
#       ma_ma.cal(ma_ma) # <---
#                                                                               
#>> setattr(obj, attr, value) ( no rule )
#      setattr(ma_ma, "", calculate_grade)
#      print(getattr(ma_ma, "")(ma_ma))                                                    <-------

"""

"""
import types


class Student:
    def __init__(self, name, myn, eng, math):
        self.name = name  # instance variable
        self.myanmar = myn
        self.english = eng
        self.math = math

    def total_marks(self):  # instance method
        return self.myanmar + self.english + self.math



mg_mg = Student("Mg Mg", 70, 70, 70)
ma_ma = Student("Ma Ma", 75, 80, 80)

# dynamic content
print(mg_mg.total_marks())
print(ma_ma.total_marks())


# dynamically create instance variable
mg_mg.history = "mg mg has good characters."
print(mg_mg.history)

#setattr(mg_mg, "+", "mg mg has good characters.")
#print(getattr(mg_mg, "+"))
#delattr(mg_mg, "+")


#print(mg_mg.__dict__["myanmar"])


def calculate_grade(self):
    if self.total_marks() >= 235:
        self.grade = "A"
    elif self.total_marks() >= 210:
        self.grade = "B"
    else:
        self.grade = "C"
    return self.grade


# for mg mg
#mg_mg.cal_grade = types.MethodType(calculate_grade, mg_mg)

# for all obj
Student.cal_grade = calculate_grade


mg_mg.cal_grade()
print(mg_mg.grade)
#print(mg_mg.__dir__())

ma_ma.cal_grade()
print(ma_ma.grade)
#print(ma_ma.__dir__())



"""







"""

object ပေါ်မူတည်ပြီးပြောင်းလဲတဲ့ variable ကို instance variable လို့ခေါ်

class variable = ?

#####################

class variable

create           --->   1. normal
                        2. dynamically create
                           >> dot ( need rules of naming )
                           >> setattr(n, attr, value) ( no rule )
                            
access           --->   1. dot
                        2. getattr(n, attr)
                        3. __dict__

delete           --->   1. del
                        2. delattr(n, attr)
                        

Descriptions
1. class is obj, instance   ---> isinstance(obj, cls)
2. check obj type           --->   type function, __class__
3. check class name         --->   __class__.__name__
4. obj, instance has own data. 
5. n = class name or obj name ( inside the class, use self instead of obj)

Note 
1. if you want to change class attribute, use class name.
2. if you use obj name, py will create new obj attribute.
                       
"""

"""

class Student:
    school = "Abc School"
    year = 2023
    def __init__(self, name, myn, eng, math):
        self.name = name  # instance variable
        self.myanmar = myn
        self.english = eng
        self.math = math

    def info(self):
        return f"name = {self.name}\nschool name = {Student.school}"



mg_mg = Student("Mg Mg", 70, 70, 70)
ma_ma = Student("Ma Ma", 75, 80, 80)

print(mg_mg.info())
print(ma_ma.info())





print(mg_mg.info())
print(ma_ma.info())


"""










class Student:
    school = "ABC University"
    total_cost = 20000
    total_amount = 0
    received_amount = 0
    
    def __init__(self, name, myn, eng, math, payment=0, payment_history=""):
        self.name = name  # instance variable
        self.myanmar = myn
        self.english = eng
        self.math = math
        self.payment = payment
        self.payment_history = payment_history
        Student.total_amount += Student.total_cost
        Student.received_amount += payment

    def total_marks(self):  # instance method
        return self.myanmar + self.english + self.math

    def info(self):
        inf = f'''
        School = {Student.school}
        Name = {self.name}
        subjects       marks
        Myanmar        {self.myanmar}
        English        {self.english}
        Math           {self.math}
        
        payment = {self.payment}
        left payment = {self.check_amount()}
        payment history = {self.payment_history}'''

        return inf

    def pay(self, amount, date):
        self.payment += amount
        Student.received_amount += amount
        self.payment_history += f"add {amount} in {date}, "

    def check_amount(self):
        return Student.total_cost - self.payment



print(Student.total_amount)
print(Student.received_amount)


mg_mg = Student("Mg Mg", 70, 70, 70)
ma_ma = Student("Ma Ma", 75, 80, 80, 20000, "add 20000 in 2.6.2022" )

mg_mg.pay(1000, "2.6.2022")

print(Student.total_amount)
print(Student.received_amount)
print(ma_ma.check_amount())
print(mg_mg.check_amount())

print(Student.__dict__)



"""
print(Student.school)
print(mg_mg.school)
print(ma_ma.school)

print(Student.__dict__)
"""















"""
13.10 class variable 
class ကိုယ်တိုင်က object တစ်ခု
class X:
    pass

a = X

type(a)
type(X)

a.__class__
X.__class__

# type function ==  _class_


X.__name__
a.__class__.__name__
X.__class__.__name__

# instance မှာ ကိုယ်ပိုင် variable တွေရှိ

# class ကိုယ်တိုင်က instance ဖြစ်လို့ ကိုယ်ပိုင် variable ရှိ


class X:
  no = 0  # class variable 

"""
