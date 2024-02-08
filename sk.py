
"""
x = "i Go to school By bus.she go to school by bycicle.he go to school by train."
print(x)

ans = ""
l = x.split(".")
for i in l:
    if i:
        ans += i.capitalize() + "."

print(ans)

x = "i Go to school By bus.she go to school by bycicle.he go to school by train."
print(x)
ans2 = [i.capitalize() + "." for i in x.split(".") if i]
print(ans2)

"""

"""
အခန်း (1) 20 marks

1.
10. သည် integer ဖြစ်သည်။

1.Ans : False

2. စာဖန်တီးရန် နည်းလမ်းလေးခုရှိသည်။

2.Ans : There are four types of creating string.They are 1.single code,2.double code,3.single tripple code and 4.double tripple code.

3. variable / ကိုယ်စားပြုအမည် ဖန်တီးရာတွင် လိုက်နာရမည့် စည်းကမ်းချက် ငါးချက်ရှိသည်။

3.Ans : Python has five rules for naming identifiers.(one,a,n,o,r)
       1.An identifier must contain at least one character.
       2.The first character of an identifier must be an alphabet or an underscore.
       3.The remaining characters may be alphabets, underscores and numbers.
       4.No other characters are permitted in identifier.
       5.A reserved word cannot be used as an identifier.


4. မူလတန်ဖိုးကို တစ်ပေါင်းလိုပါက += ကို သုံးနိုင်သည်။

4.Ans : True

5. assignment operator ၏ right operand သည် identifier ဖြစ်သည်။
X = 1
5.Ans : True

6. (x, y, z) = (1, 2, 3) သည် tuple assign ဖြစ်သည်။

6.Ans : True


7. floating point numbers တစ်ဆက်တည်း တန်ဖိုး 17 လုံးအထိ သိမ်းဆည်းနိုင်သည်။

7.Ans : True

*
8.
0.000000000012345678901234567 က
သည် တစ်ဆက်တည်းတန်ဖိုး 17 လုံးရှိသည်။

8.Ans : True


9. round(x)
round function တွင် ထည့်ပေးလိုက်သော တန်ဖိုး x ကို argument ဟုခေါ်သည်။

9.Ans : True

10. round(x)
round function တွင် ထည့်ပေးလိုက်သော x သည် index zero တွင် တည်ရှိသည်။

10.Ans : False

11. round function တွင် int တန်ဖိုးထည့်သွင်းပါက ရလဒ်သည် int သာဖြစ်လာမည်။

11.Ans : True

12. round function တွင် float တန်ဖိုးထည့်သွင်းပါက ရလဒ်သည် float သာဖြစ်လာမည်။

12.Ans : False

13. octal code နံပါတ်ဖြင့် စာတန်ဖိုးများကို ဖော်ပြရန် 0 ကို အသုံးပြုရမည်။

13.Ans : True

14. hexadecimal code နံပါတ်ဖြင့် စာတန်ဖိုးများကို ဖော်ပြရန် x, u, U တို့ကို အသုံးပြုနိုင်သည်။

14.Ans : True

15. print function တွင် keywords argument လေးခုရှိသည်။

15.Ans : True.They are end,sep,file and flush.

16. print function တွင် positional argument လေးခုရှိသည်။

16.Ans : False

17. python တွင် new style ဖြင့် format ချလိုပါက နည်းလမ်းနှစ်ခုသုံးနိုင်သည်။

17.Ans : True.They are .format() and f.

18.  10 + 10. သည် mixed type expression ဖြစ်သည်။

18.Ans : True

19. 1 + 2 - 0 သည် 3 ဖြစ်သည်။

19.Ans : True

20.
while 1: သည် infinite loop ဖြစ်သည်။

20.Ans : True

#####################

အခန်း (2) 35 marks

1. str object တစ်ခု ဖန်တီးပါ။

1.Ans: name = 'HayMann'

2. int object တစ်ခုဖန်တီးပါ။

2.Ans : mark = int(90)

3. preformatted string တစ်ခုဖန်တီးပါ။

3.Ans :
introduction = '''         My Self
                      My name is HayMann.I live in Mdy.

                                                        '''


4. arithmetic expression တစ်ခု ဖန်တီးပါ။

4.Ans : x = 1 - 2

5. boolean expression တစ်ခုဖန်တီးပါ။

5.Ans : x = 1 < 2

6. conditional expression တစ်ခု ဖန်တီးပါ။

6.Ans:

x = int(input("x = "))

ok = "It is ok" if x > 2  else "It is not ok"

print(f"{x}  {ok}.")

7. mixed type expression တစ်ခုဖန်တီးပါ။

7.Ans : x = 10 + 10.2

8. boolean တန်ဖိုးဖြင့် simple expression တစ်ခုဖန်တီးပါ။

8.Ans : x = True

9. compound boolean expression တစ်ခုဖန်တီးပါ။

9.Ans : x = (3**2) < 10

10. arithmetic expression တွင် x, y, z တန်ဖိုးများကို format ချပြပါ။

10.Ans :


11. python နှင့် မသက်ဆိုင်သော မှတ်ချက်တစ်ခုဖန်တီးပါ။

11.Ans : 16bits = 2**16 = 65536

12. Conditional execution ဆိုသည်မှာ အဘယ်နည်း။

12.Ans : 


13. conditional execution တစ်ခုဖန်တီးပါ။


14. linear execution တစ်ခုဖန်တီးပါ။

14.
name = input()
password = int(input())
print(f'Your name is {name}.Password is {password}')

15. non linear execution တစ်ခုဖန်တီးပါ။

15.Ans :

name = input()
password = int(input())
if name == 'Mg Mg' and password == 123:
    print('My brother.Password is right')
else:print('Stranger')


16. conditional statements ဆိုသည်မှာအဘယ်နည်း။


17. conditional statements တစ်ခုဖန်တီးပါ။

17.Ans :


18. conditional expression ဆိုသည်မှာ အဘယ်နည်း။



19. pass statement ၏ အသုံးဝင်ပုံကို ဖော်ပြပါ။

19.Ans : It can use for incomplete code block

20. multiway desicision statement ဆိုသည်မှာ အဘယ်နည်း။


21. multi-way desicision statement တစ်ခုဖန်တီးပါ။

21.Ans :

x = input('User name : ')
if x == 'Ma Ma':
    print('Your name is true.')
    y =input('Password : ')
    if y == '123':
        print('Password is true.')
    else:
        print('Password is wrong.')
elif x == 'Mg Mg':
    print('Your name is true.')
    y = input('Password : ')
    if y == '456':
        print('Password is true.')
    else:
        print('Password is wrong.')
elif x == 'Mya Mya':
    print('Your name is true.')
    if y == '789':
        print('Your password is true.')
    else:
        print('Your password is wrong.')
else:
    print('Your name is wrong.')


22. Multi-way Versus Sequential Conditionals ဆိုသည်မှာအဘယ်နည်း။

22.Ans :  parallel conditional statements

23. နမူနာတစ်ခုဖန်တီးပါ။

23.Ans :

x = input("Enter some words : ")
if x.isupper():print(f"You entered upper case letter \"{x}\".")
if x.islower():print(f'You endtered lower case letter \'{x}\'.')


24. nested conditions ဖန်တီးပါ။

24.Ans :

x = input('Famous Series Name: ')
if x == 'WooYaungWoo':
    print('Famous Series Name is true.')
    y = input('Password : ')
    if y == '123':
        print('Password is true.')
    else:
        print('Password is Wrong.')
else:
    print('Famous series Name is wrong.')


25. nested while loop ဖန်တီးပါ။
i = 0
while i < 10:
    j = 0
    while j < 10:
        print(i, j)

26. nested for loop ဖန်တီးပါ။

26.Ans :

for i in range(10):
    for j in range(10):
        print(i, j)
     
27. conditional statements တွင် ဖြစ်ပေါ်လာနိုင်သော သတိထားရမည့် အခြေအနေနှစ်ခုကို ဖော်ပြပါ။
tautology and contradiction

28. operator precedence ကို ရှင်းပြပါ။

29. operator associativity ကို ရှင်းပြပါ။

30. unary operator နှစ်ခုကို ရေးပါ။

30.Ans : +1, -1

31. binary operator တစ်ခု အလုပ်လုပ်ရန် operand  ဘယ်နှစ်ခု လိုအပ်သနည်း။

31.Ans : need two operands

32. error အမျိုးအစား သုံးခုကို ရေးပါ။

32.Ans : 1.Syntax error
         3.Runtime Exception
         2.Logic error

33.  "abcdefghijklmnop" ၏ စာလုံးအရေအတွက်ကို ရေတွက်ရန် မည်သည့် function ကို အသုံးပြုရမည်နည်း။
လက်တွေ့သုံးပြပါ။

33.Ans : len()
        print(len("abcdefghijklmnop"))

34. python တွင် ရေတွက်၍ရသော အရာရာတိုင်းအတွက်  အရေအတွက်စုစုပေါင်းကို သိရှိရန် မည်သည့် function ကို အသုံးပြုရမည်နည်း။

34.Ans : len()

35. တစ်ခုခုကို နားမလည်သဖြင့် အကူအညီတောင်းလိုလျှင် မည့်သည့် function ကို အသုံးပြုရမည်နည်း။

35.Ans : help()

#####################

အခန်း (3) 45 marks

1. round function ကို ပြည့်စုံစွာ ရှင်းပြပါ။
10 marks


2. identifier ဖန်တီးရန် လိုက်နာရမည့် စည်းကမ်းငါးချက်ကို ရေးပါ။
5 marks
Ans : Python has five rules for naming identifiers.(one,a,n,o,r)
       1.An identifier must contain at least one character.
       2.The first character of an identifier must be an alphabet or an underscore.
       3.The remaining characters may be alphabets, underscores and numbers.
       4.No other characters are permitted in identifier.
       5.A reserved word cannot be used as an identifier.

3. insisting on proper input ကို  while loop ဖြင့် ရေးပါ။ 5 marks

3.Ans :

for loop ဖြင့်ရေးပါ။ 5 marks


4 သင်ထားသော အချက်အလက်ကို အခြေခံ၍ အသုံးဝင်သော program တစ်ပုဒ်ကို ရေးပါ။
20 marks

"""




















