"""
mutability in functional programming

1. mutable objects ( change, del ) ( list, set )
2. immutable objects ( tuple, frozenset )
3. variables are not object and they only hold a reference to an object.
4. variable and mutability
   - assign value to a variable
     - mutable value assignment
     - immutable value assignment
5. mutable object in fp
   - copying list,
   - shallow copy, deep copy
6. immutable object in fp
   - Changing immutable objects
     - list -> indexing, lc, for
     - slices
   - shallow immutability
   - copying tuple ( shallow copy, deep copy )

#################################################

1. Mutable objects

1. list
2. dict
3. set
4. bytearray
5. memoryview
6. user-defined classes

#################################################

2. Immutable objects

1. int, float, complex,
2. bool,
3. str,
4. tuple,
5. range,
6. frozenset,
7. bytes
8. NoneType

#################################################

3. variables are not object and they only hold a reference to an object.

# t variable.1 ( 0x215c8769340 , 0x215c8769500, 0x7ffddc8fca18 )
t = (10, 20, 30)  # tuple object. 1
print(hex(id(t)))

t = (3, 2, 1)     # tuple object. 2
print(hex(id(t)))

t = int(4)        # int object. 1
print(hex(id(t)))

t = (10, 20, 30)  # tuple object. 1
print(hex(id(t)))

#################################################

tuple အသစ်ဖန်တီးလိုက်တယ်။
အသစ်ရဲ့ လိပ်စာကို t ရဲ့ reference အဖြစ်သတ်မှတ်သည်။

ပထမ tuple ဟာ ရှိနေတုန်းပါပဲ။
ပြန်သုံးလည်းရသလို ပြန်မသုံးလည်းရပါတယ်။

ပြန်မသုံးခဲ့ရင်တော့ python က ဖျက်ပေးမှာပါ။

t = (10, 20, 30)
print("refrence of first tuple ( t ) = ", hex(id(t)))

t = (3, 2, 1)
print("refrence of second tuple ( t ) = ", hex(id(t)))

# ပြန်သုံး
y = (10, 20, 30)
print("refrence of first tuple ( y ) = ", hex(id(y)))

#################################################
#################################################

# 300 cinema
# mutable obj
t = [10, 20, 30]  # list object. 1
print(hex(id(t)))
t = [10, 20, 30]  # list object. 2
print(hex(id(t)))

# immutable obj ( to avoid memory lose )
t = (10, 20, 30)  # tuple object. 1
print(hex(id(t)))
t = (10, 20, 30)  # tuple object. 1
print(hex(id(t)))

#################################################

# 10 --> immutable obj ---> same address

obj1 = [10, 20, 30] # list object. 1  # [0x7ffdc2dccad8,
print(hex(id(obj1[0])))
obj2 = [10, 20, 30]  # list object. 2
print(hex(id(obj2[0])))

obj3 = (10, 20, 30)  # tuple object. 1
obj3[0] = 40
print(hex(id(obj3[0])))
obj4 = (10, 20, 30)  # tuple object. 1
print(hex(id(obj4[0])))

#################################################

# immutable obj ( to avoid memory lose )
obj = (["a", "b", "c"], 20, 30)  # tuple object  --->  0x21227cb2280  --->  (0x250a022d100, 0x250a022d100, 0x7ffdc2dccd58)
                           # list object   --->  0x250a022d100  --->  [0x7ffdc2dd4ce0, 0x7ffdc2dd5100, 0x7ffdc2dd54a0]
obj[0][0] = 10   # 0x7ffdc2dccad8   --->         0x250a022d100  --->  [0x7ffdc2dccad8, 0x7ffdc2dd5100, 0x7ffdc2dd54a0]
print(obj)

obj[0].clear()

print(obj)

#################################################
#################################################


4. variable and mutability  ( variable --->  refrence assign, create obj )

4.1 assign value to a variable

# assign
# immutable obj
# =   assign old value ( old refrence )

t = (10, 20, 30)
t2 = (10, 20, 30)
t3 = (10, 20, 30)
t4 = (10, 20, 30)
print(hex(id(t)))
print(hex(id(t2)))
print(hex(id(t3)))
print(hex(id(t4)))
print()


# mutable obj
# =  assign old or new ( new obj and new refrence )
l = [10, 20, 30]
l2 = [10, 20, 30]
l3 = [10, 20, 30]
l4 = [10, 20, 30]
print(hex(id(l)))
print(hex(id(l2)))
print(hex(id(l3)))
print(hex(id(l4)))


######################

# mutable value assignment
# =
# assign value ( old / new value -> new obj / new refrence )
# assign refrence ( old refrence )
# +=, -=, ( refrence obj change)


l = [1, 2, 3]
l2 = [1, 2, 3] # new obj / new refrence
print(hex(id(l)))
print(hex(id(l2)))


l += l2 # ( refrence obj change )

print(l)
print(l2)
print(hex(id(l)))
print(hex(id(l2)))

######################

l = [1, 2, 3]
l2 = l # assign refrence ( old refrence )
print(hex(id(l)))
print(hex(id(l2)))

l += l2 # ( refrence obj change ) # +
print(l)
print(l2)
print(hex(id(l)))
print(hex(id(l2)))

######################

# immutable value assignment
# =
# assign value ( old value old refrence / new value new refrence )
# assign refrence ( old refrence )
# +=, -=, ( new obj create ) ( can not change value )

l = (1, 2, 3)
l2 = (1, 2, 3)  # old value  old refrence
print(hex(id(l)))
print(hex(id(l2)))

l = (1, 2, 3)
l2 = (1, 2, 3, 4)  # new value new refrence
print(hex(id(l)))
print(hex(id(l2)))

l = (1, 2, 3)
l2 = l # assign refrence ( old refrence )
print(hex(id(l)))
print(hex(id(l2)))

l += l2 # ( assign new value ) ( new obj create ) ( new refrence )
# l = l + l2 = (1, 2, 3) + (1, 2, 3) = (1, 2, 3, 1, 2, 3) # new obj

print(l)
print(l2)
print(hex(id(l)))
print(hex(id(l2)))

#################################################

5. mutable object in fp
function မှာ mutable obj ထည့်လိုက်ရင် ‌မ‌ေပြာင်းလဲဘူးလို့ အာမမခံနိုင်
မ‌ေပြာင်း‌ေအာင်ထားလို့ရတဲ့နည်းမရှိ

def f(x):
    x[0] = 0


l = [1, 2, 3]  # 001

f(l)  # x = l ---> reference assign

print(l)  # [0, 2, 3]

function ထဲကို mutable obj ထည့်တဲ့အခါ ကိုယ်ကမပြင်‌ေပမယ့် တစ်ခြားသူက modify လုပ်ခဲ့ရင် ‌ေပြာင်းသွားနိုင်
ဒါမှမဟုတ် တစ်ခြား function ‌ေတွနဲ့ တွဲသံုးတဲ့အခါမှာလည်း ‌ေပြာင်းသွားနိုင်

######################

5.1 copying list
မူရင်း data ‌ေပြာင်းလဲမသွားဖို့ copy တန်ဖိုးထည့်ရန်လိုအပ်


def f(x):
    x[0] = 0

l = [1, 2, 3]  # 001

f(list(l))   # x = list(l) ---> x =  [1, 2, 3]   # 002

print(l) # [1, 2, 3]


list fun က list အသစ်ဖန်တီး‌ေပး

######################

ဒီနည်းကလည်း အဆင်‌ေတာ့‌ေပြသွား‌ေပမယ့် အားနည်းချက်‌ေတွရှိ
1. copy ကူးဖို့ကို သတိရဖို့လိုအပ်
2. data ဟာ အရမ်းများရင် copy ကူးတဲ့အခါ အချိန်ကုန်
3. function ‌ေတွ အဆင့်ဆင့် သံုးခဲ့မယ်ဆိုရင် copy ‌ေတွအများကြီးဖြစ်သွားနိုင်
တစ်ချို့‌ေတွက copy မကူးမိမှာစိုးလို့ function ထဲမှာ copy ကူးထားရင် နှစ်ကြိမ်စီကူးသလိုလည်းဖြစ်နိုင်‌ေသးသည်။


def f(x):
    x = list(x)  # 003
    x[0] = 0


l = [1, 2, 3]   # 001

f(list(l))   # 002
print(l) # [1, 2, 3]

######################

5.2 shallow copy and deep copy

# list(x), x[:], copy, deep copy,
# copy method,

# shallow copy
def f(x):
    x[3][0] = 0
    print(x)

l = [1, 2, 3, ["apple", "banana"]]  # 001  ( 0010 )

f(list(l))   # 002  ( 0010 )

print(l) # [1, 2, 3, [0, 'banana']]

# shallow copy
def f(x):
    x = list(x)
    x[3][0] = 0

l = [1, 2, 3, ["apple", "banana"]]
f(l)
print(l) # [1, 2, 3, [0, 'banana']]

# shallow copy
# list(x), x[:], copy
# copy method,
from copy import copy

def f(x):
    x = x.copy()
    x[3][0] = 0

l = [1, 2, 3, ["apple", "banana"]]
f(l)
print(l)  # [1, 2, 3, [0, 'banana']]

# deep copy
from copy import deepcopy
def f(x):
    x[3][2][1] = "mangoes"
    print(x)

l = [1, 2, 3, ["apple", "banana", ["orange", 2]]]
f(deepcopy(l))
print(l) # [1, 2, 3, ['apple', 'banana']]

#################################################

6. immutable object in fp

အရိုးရှင်းဆံုးက‌ေတာ့ copy ‌ေတွဘာ‌ေတွကူးမ‌ေနဘဲ immutable obj ထည့်လိုက်ဖို့ပါပဲ။

ပြင်ဖို့လိုအပ်ရင် function ‌ေရးတဲ့ သူကလည်း အထဲမှာ copy ကူး‌ေပါ့။

မကူးဘဲ ပြင်ရင်လည်း error တက်ပြီး အသိ‌ေပးပါလိမ့်မယ်။

def f(x):
    x = list(x)  # [1, 2, 3] --> 02
    x[0] = 0


l = (1, 2, 3)  # 01
f(l)  # x = l ---> refrence assign --> 01
print(l) # (1, 2, 3)

def reverse_data(x):
    x = list(x) # copy
    return x[::-1]  # [3, 2, 1] --> 02


t = (1, 2, 3)  # 01
r = reverse_data(t)
print(t)  # (1, 2, 3)
print(r)


# [ ] create new obj / copy obj

def reverse_data(x):
    return x[::-1]  # new tuple  --> (3, 2, 1) --> 02


t = (1, 2, 3)
r = reverse_data(t)
print(t)  # (1, 2, 3)
print(r)

#####################

6.1 Changing immutable objects ( tuple ) ( list -> indexing, lc, for) ( slices )

ပြင်ချင်ရင် list ‌ေပြာင်းပြီးပြင်
ပြီးရင် tuple ပြနိ‌ေပြာင်းနိုင်

# 1. Using slices
# slices create temporary copies of the tuple.
# should not use when tuples are very large.

# add new element apple into the middle of a tuple at position n
u = v[:n] + (3) + v[n:]

v = (1, 1, 1, 1, 1, 1, 1)
n = 3
u = v[:n] + ("apple", ) + v[n:]
print(v)
print(u)


# remove the element at position n from a tuple
u = v[:n] + v[n+1:]

v = (1, 1, 1, 1, "apple", "banana", 1, 1, 1)
n = 4
u = v[:n] + v[n+1:]
print(v)
print(u)


# temporary copy of v[:n], v[n+1:],
# tuple u.

#####################

# 2. Using list comprehensions
# A list comprehension can take any type of sequence as input,
but always creates a list.
# simple operation on each element of a sequence.

#add 1 to each element in a tuple.

t = (2, 4, 6)
print(t)

t = [x + 1 for x in t]  # list
t = tuple(t)
print(t)

t = (2, 4, 6)
t = tuple([x + 1 for x in t])
print(t)


# replace None
t = (1, 2, 3, 4, 5, 6)
t = tuple([1 for n in t])
print(t)


# replace None
v = (1, 0, 2, 0, 5)
l = ["None" if i == 0 else i for i in v]
print(l)

# [1, 'None', 2, 'None', 5]

#####################

# 3. Using a loop
# complex operation on each element of a sequence

zero ‌ေနာက်မှာ zero အသစ်ထည့်ချင်
so (1, 0, 2, 0, 5) becomes
(1, 0, 0, 2, 0, 0, 5).

v = (1, 0, 2, 0, 5)
u = []
for x in v:
    u.append(x)
    if x == 0:
        u.append(x)

v = tuple(u) # (1, 0, 0, 2, 0, 0, 5)
print(v)

#####################

note - problem with immutable objects

1. ပြင်ချင်ရင် လှည့်ပတ်ရေးဖို့လိုအပ်

2. copy အများကြီးကူး‌ေနလို့ memory ပြည့်သွားနိုင်

data အရမ်းကြီးရင် mutable obj ပဲသံုးပြီး မပြင်မိ‌ေအာင် သတိထား‌ေရးနိုင်။

X  ---> py share immutable object ( refrence )/
        do not copy /
        do not create new immutable obj with same value

#####################

# 6.2 shallow immutability တိမ် အ‌ေပါ်ယံ

immutabiliy ကို ‌ေသချာနားလည်ဖို့လိုအပ်
list ဟာ tuple ထဲ‌ေရာက်‌ေနလို့ ပြင်လို့မရဘူးလို့ မ‌ေတွးရပါဘူး။

t = (1, 2, [5, 9])  # (001, 002, 1001) --> 1001 --> [003, 004]
t[2][1] = "apple"  # 200
print(t)

1. Initially, our tuple contains 3 references.
2. We change the value of one element of the list object.
3. The tuple still contains 3 references to the same 3 objects.

One of those lists now contains different values, 
but it is still the same list object.

The tuple has not changed.

note -> placing a list inside a tuple can not protects the list from being changed.

######################

6.3 copying tuple

# same refrence
t = ([1, 2], [4, 6], [5, 9])
t2 = t
t2[2][1] = "apple"
print(t)
print(t2)

# tuple
t = ([1, 2], [4, 6], [5, 9])
t2 = tuple(t)
t2[2][1] = "apple"
print(t)
print(t2)

# slices
t = ([1, 2], [4, 6], [5, 9])
t2 = t[:]
t2[2][1] = "apple"
print(t)
print(t2)

# deep
from copy import deepcopy
t = ([1, 2], [4, 6], [5, 9])
t2 = deepcopy(t)
t2[2][1] = "apple"
print(t)
print(t2)

#################################################

from copy import deepcopy


l = [1, 2, 3, ["apple", "banana"]]

l1 = l.copy()
l2 = l[:]
l3 = list(l)

l4 = deepcopy(l)

l[3][0] = "l1"
l4[3][0] = "l4"
print(l)
print(l1)
print(l2)
print(l3)
print(l4)


#################################################

from copy import deepcopy


l = (1, 2, 3, ["apple", "banana"])


l2 = l[:]
l3 = tuple(l)

l4 = deepcopy(l)

l[3][0] = "l1"
l4[3][0] = "l4"

print(l)
print(l2)
print(l3)
print(l4)

"""