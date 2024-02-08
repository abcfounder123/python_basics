# symbolic math exercise  ( picture.1)
# ကြိုး = ရေတွင်း + 1  ( ကြိုးသည် ရေတွင်းထက်တစ်တောင်ပိုသည်။ )
# ရေတွင်း = ကြိုး / 2 + 1 ( ‌ရေတွင်းသည် ကြိုးတစ်ဝက်ထက် တစ်တောင်ပိုသည်။ )
# equation ဖြစ်အောင် နှစ်ခုလုံးကို zero နဲ့ညီအောင်လုပ်မည်။
# 0 = ရေတွင်း + 1 - ကြိုး
# 0 = ကြိုး / 2 + 1 - ရေတွင်း
from sympy import symbols, solve
ကြိုး, ရေတွင်း = symbols('ကြိုး, ရေတွင်း')
equation1 = ရေတွင်း + 1 - ကြိုး
equation2 = ကြိုး / 2 + 1 - ရေတွင်း
answer = solve((equation1,  equation2), dict=True)
print(answer)
#####################
# x = ကြိုး
# y = ရေတွင်း
# x = y + 1  ( ကြိုးသည် ရေတွင်းထက်တစ်တောင်ပိုသည်။ )
# y = x / 2 + 1 ( ‌ရေတွင်းသည် ကြိုးတစ်ဝက်ထက် တစ်တောင်ပိုသည်။ )
# equation ဖြစ်အောင် နှစ်ခုလုံးကို zero နဲ့ညီအောင်လုပ်မည်။
# 0 =  y + 1 - x
# 0 = x / 2 + 1 - y
from sympy import symbols, solve
x, y = symbols('x,y')
eq1 = y + 1 - x
eq2 = x / 2 + 1 - y
ans = solve((eq1, eq2), dict=True)
print(ans)
#####################