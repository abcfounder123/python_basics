
'''
" custom literal "
#####################
class အမည်ကို မသုံးဘဲ တိုက်ရိုက်ဖန်တီးနိုင်တာကို literal လို့ခေါ်ပါတယ်။
( literal ---> တိုက်ရိုက် / ရိုးရှင်းသော )
a = 1 # int literal
b = 1.1 # float literal
c = "hello" # str literal
#####################
ကျွန်တော်က အောက်ပါအတိုင်း custom literal နှစ်ခုဖန်တီးချင်ပါတယ်။
x = 1 .kg # kg literal
y = 2.2 .lb  # lb literal
#####################
ပုံမှန်အားဖြင့်တော့ kg object ဖန်တီးချင်ရင် Kg class ကိုသုံးရပါတယ်။
ဥပမာ။   ။ x = Kg(1)
#####################
ကျွန်တော်က Kg class ကို မသုံးဘဲ quote တွေထည့်လိုက်ရင် str object ဖြစ်သွားသလိုမျိုး ဖန်တီးချင်တာပါ။
#####################
s = str("hello") အစား
s = "hello" ဆိုပြီး သုံးလို့ရသလိုမျိုး
x = 1 .kg
y = 2.2 .lb
အစရှိသဖြင့် အလွယ်တကူ သုံးချင်လို့ မူရင်း code ထဲမှာ အောက်က function နှစ်ခု ထပ်ဖြည့်လိုက်ပါတယ်။
#####################
# creating custom literal ( kg )
@literal(float, int, name="kg")
def kg(self):
    return Kg(self)
# creating custom literal ( lb )
@literal(float, int, name="lb")
def lb(self):
    return Lb(self)
#####################
functional နှစ်ခုကို decorate လုပ်ပြီးတဲ့အခါ kg , lb ဆိုပြီး တိုက်ရိုက်ချရေးလို့ရသွားပါပြီ။
ရိုးရိုးနဲ့  literal နှစ်မျိုးလုံးကို စမ်းပြထားပါတယ်။
#####################
Note
1. custom literal ဖန်တီးဖို့အတွက် external module နှစ်ခုကို install လုပ်ပေးဖို့လိုအပ်ပါတယ်။
pip install custom_literals
pip install forbiddenfruit
#####################
source code in comment
#####################

'''

# creating custom literal
# for education purpose
from custom_literals import literal

class Kg:
    "Kilogram ---> weight in metric unit"

    def __init__(self, w):
        self.weight = w

    def __repr__(self):
        return str(self.weight) + " kg"

    def __add__(self, other):
        if "kg" in other.__str__():
            return kg(self.weight + other.weight)
        elif "lb" in other.__str__():
            return kg(self.weight + (other.weight / 2.2))

class Lb:
    "Pound ---> weight in SI unit"

    def __init__(self, w):
        self.weight = w

    def __repr__(self):
        return str(self.weight) + " lb"

    def __add__(self, other):
        if "lb" in other.__str__():
            return lb(self.weight + other.weight)
        elif "kg" in other.__str__():
            return lb(self.weight + (other.weight * 2.2))

# creating custom literal ( kg )
@literal(float, int, name="kg")
def kg(self):
    return Kg(self)


# creating custom literal ( lb )
@literal(float, int, name="lb")
def lb(self):
    return Lb(self)

x = 1.kg
y = 2.2.lb
print(f"{x} + {y} = {x + y}")
print(f"{y} + {x} = {y + x}")

"""
if _name_ == "_main_":
    x = Kg(1)
    y = Lb(2.2)
    print(f"{x} + {y} = {x + y}")
    print(f"{y} + {x} = {y + x}")

    print(" -" * 30)

    x = 1.kg
    y = 2.2.lb
    print(f"{x} + {y} = {x + y}")
    print(f"{y} + {x} = {y + x}")

    print(" -" * 30)

"""