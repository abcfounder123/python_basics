

"""
control flow practice.2 ---> simple calculator

################################################

# "1 + 2"   ---> w.get()
# "="
# 3 ---> eval(w.get())

# "1 + 2 = 3"
# "1 + 2" + "=" + str(3)
# w.get() + "=" + str(eval(w.get()))

################################################

# lambda     --->   anonymous function

# def Vs lambda

def add(x, y, /, a, b, *, c, d):
    return x + y


l = lambda x, y, /, a, b, *, c, d: x + y

ans1 = add(1, 2, 3, 4, c=5, d=6)
ans2 = l(1, 2, 3, 4, c=5, d=6)
print(ans1, ans2)

################################################

def x():
    print("1")


l = lambda: print("1")

x()
l()

################################################

#  eval     -->   evaluates a string expression as code

ans = eval("1+2+3")
print(ans)

################################################

# nested loop

fs = ['789/', '456*', '123-', '0.+%']

for f in fs:  # f = '789/'
    print(f)
    for c in f:
        print(c)

################################################

# calculator.1

from tkinter import *

x = Tk()
w = StringVar(x)
e = Entry(x, textvariable=w)
e.pack(pady=20, padx=20)

f = Frame(x)
f.pack()

Button(f, text="7", fg="black", command=lambda: w.set(w.get() + "7")).pack(side="left", pady=5)
Button(f, text="8", fg="black", command=lambda: w.set(w.get() + "8")).pack(side="left", pady=5)
Button(f, text="9", fg="black", command=lambda: w.set(w.get() + "9")).pack(side="left", pady=5)
Button(f, text="/", fg="black", command=lambda: w.set(w.get() + "/")).pack(side="left", pady=5)

f2 = Frame(x)
f2.pack()

Button(f2, text="4", fg="black", command=lambda: w.set(w.get() + "4")).pack(side="left", pady=5)
Button(f2, text="5", fg="black", command=lambda: w.set(w.get() + "5")).pack(side="left", pady=5)
Button(f2, text="6", fg="black", command=lambda: w.set(w.get() + "6")).pack(side="left", pady=5)
Button(f2, text="*", fg="black", command=lambda: w.set(w.get() + "*")).pack(side="left", pady=5)

f3 = Frame(x)
f3.pack()

Button(f3, text="1", fg="black", command=lambda: w.set(w.get() + "1")).pack(side="left", pady=5)
Button(f3, text="2", fg="black", command=lambda: w.set(w.get() + "2")).pack(side="left", pady=5)
Button(f3, text="3", fg="black", command=lambda: w.set(w.get() + "3")).pack(side="left", pady=5)
Button(f3, text="-", fg="black", command=lambda: w.set(w.get() + "-")).pack(side="left", pady=5)

f4 = Frame(x)
f4.pack()

Button(f4, text="0", fg="black", command=lambda: w.set(w.get() + "0")).pack(side="left", pady=5)
Button(f4, text=".", fg="black", command=lambda: w.set(w.get() + ".")).pack(side="left", pady=5)
Button(f4, text="+", fg="black", command=lambda: w.set(w.get() + "+")).pack(side="left", pady=5)
Button(f4, text="%", fg="black", command=lambda: w.set(w.get() + "%")).pack(side="left", pady=5)

f5 = Frame(x)
f5.pack()
Button(f5, text="Clr", fg="black", command=lambda: w.set("")).pack(side="left", pady=5)
Button(f5, text="=", fg="black", command=lambda: w.set(eval(w.get()))).pack(side="left", pady=5)

x.mainloop()

################################################

# calculator.2
from tkinter import *

x = Tk()
w = StringVar(x)
e = Entry(x, textvariable=w)
e.pack(pady=20, padx=20)

fs = ['789/',
      '456*',
      '123-',
      '0.+%',
      ]

for row in fs:
    f = Frame(x)
    f.pack()
    for col in row:  # %
        Button(f, text=col, fg="black", command=lambda c=col: w.set(w.get() + c)).pack(side="left", pady=5)

f5 = Frame(x)
f5.pack()
Button(f5, text="Clr", fg="black", command=lambda: w.set("")).pack(side="left", pady=5)
Button(f5, text="=", fg="black", command=lambda: w.set(eval(w.get()))).pack(side="left", pady=5)

x.mainloop()

"""




