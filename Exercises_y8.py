"""
1. str object တစ်ခု ဖန်တီးပါ။
    print(str("x"))

2. int object တစ်ခုဖန်တီးပါ။
    print(str(1))

3. preformatted string တစ်ခုဖန်တီးပါ။

4. arithmetic expression တစ်ခု ဖန်တီးပါ။
x = 6
y = 3

add = x + y
sub = x - y
mul = x * y
div = x / y

print("The sum result is", add)
print("The sub result is", sub)
print("The mul result is", mul)
print("The div result is", div)

5. boolean expression တစ်ခုဖန်တီးပါ။
  True

6. conditional expression တစ်ခု ဖန်တီးပါ။

7. mixed type expression တစ်ခုဖန်တီးပါ။
    x = 1
    y = 3.7
    print(x+y)

8. boolean တန်ဖိုးဖြင့် simple expression တစ်ခုဖန်တီးပါ။
    print(4<5)

9. compound boolean expression တစ်ခုဖန်တီးပါ။
    x = 10
    y = 12
    print(x<y)

10. arithmetic expression တွင် x, y, z တန်ဖိုးများကို format ချပြပါ။
x = 4
y = 9

add = x + y
sub = x - y
mul = x * y
div = x / y

print("The sum result of {} and {} is".format(x,y),add)
print("The sub result of {} and {} is".format(x,y),sub)
print("The mul result of {} and {} is".format(x,y),mul)
print("The div result of {} and {} is".format(x,y),div)

11. python နှင့် မသက်ဆိုင်သော မှတ်ချက်တစ်ခုဖန်တီးပါ။

12. Conditional execution ဆိုသည်မှာ အဘယ်နည်း။
help to execute commands when specified conditions are met.

13. conditional execution တစ်ခုဖန်တီးပါ။
x = int(input("Enter Your ID:"))
if x == 1:
    print("You are a student")

else : print("You are not a student")

14. linear execution တစ်ခုဖန်တီးပါ။

x = 2
y = (x+3)/4
print(f'The result of {x} and {y} is ', y)


15. non linear execution တစ်ခုဖန်တီးပါ။

16. conditional statements ဆိုသည်မှာအဘယ်နည်း။
used to guide the program to make the decision based on the conditions

17. conditional statements တစ်ခုဖန်တီးပါ။
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i != 1:
        print("It is true")

    else :
        print("It is false")

18. conditional expression ဆိုသည်မှာ အဘယ်နည်း။
x = int(input("Enter Your ID:"))
decision = "You are a student" if x == "1" else "You are not a student."
print(decision)


19. pass statement ၏ အသုံးဝင်ပုံကို ဖော်ပြပါ။
helps to avoid errors when the code is empty.
20. multiway desicision statement ဆိုသည်မှာ အဘယ်နည်း။

21. multi-way desicision statement တစ်ခုဖန်တီးပါ။
x = int(input("Enter your ID:"))

if x == 1:
    print("Welcome")
    y = int(input("Enter your password:"))
    if y == 1:
        print("Successfully")

    else: print("Your password is wrong.")

elif x == 2:
        print("Welcome")
        y = int(input("Enter your password:"))
        if y == 2:
            print("Successfully")

        else:
            print("Your password is wrong.")

else : print("Try again")

22. Multi-way Versus Sequential Conditionals ဆိုသည်မှာအဘယ်နည်း။

23. နမူနာတစ်ခုဖန်တီးပါ။
x = int(input("Enter your ID:"))
if x == 1:
    print("welcome")

if x == 2:
    print("welcome")

if x < 1 :
    print("try again")

24. nested conditions ဖန်တီးပါ။
x = int(input("Enter your ID:"))
if x == 1:
    print("Welcome")
    y = int(input("Enter your password:"))
    if y == 1:
        print("Successfully")
    else: print("Your password is wrong.")

else : print("Try again")

25. nested while loop ဖန်တီးပါ။

26. nested for loop ဖန်တီးပါ။

27. conditional statements တွင် ဖြစ်ပေါ်လာနိုင်သော သတိထားရမည့် အခြေအနေနှစ်ခုကို ဖော်ပြပါ။
tautology
contradiction


28. operator precedence ကို ရှင်းပြပါ။
operator having the highest precedence will evaluate first.

29. operator associativity ကို ရှင်းပြပါ။
* and / have the same precedence. When both have to calculate in the same expression, the left one will be evaluated first.
print(2 * 8 /3)

30. unary operator နှစ်ခုကို ရေးပါ။
- +
31. binary operator တစ်ခု အလုပ်လုပ်ရန် operand  ဘယ်နှစ်ခု လိုအပ်သနည်း။
2

32. error အမျိုးအစား သုံးခုကို ရေးပါ။

syntax error
runtime error
logical error


33.  "abcdefghijklmnop" ၏ စာလုံးအရေအတွက်ကို ရေတွက်ရန် မည်သည့် function ကို အသုံးပြုရမည်နည်း။
လက်တွေ့သုံးပြပါ။

34. python တွင် ရေတွက်၍ရသော အရာရာတိုင်းအတွက်  အရေအတွက်စုစုပေါင်းကို သိရှိရန် မည်သည့် function ကို အသုံးပြုရမည်နည်း။

35. တစ်ခုခုကို နားမလည်သဖြင့် အကူအညီတောင်းလိုလျှင် မည့်သည့် function ကို အသုံးပြုရမည်နည်း။
help()

"""



"""

1. str object တစ်ခု ဖန်တီးပါ။
    print(str("x"))
    
2. int object တစ်ခုဖန်တီးပါ။
    print(str(1))
    
3. preformatted string တစ်ခုဖန်တီးပါ။

4. arithmetic expression တစ်ခု ဖန်တီးပါ။
x = 6
y = 3

add = x + y
sub = x - y
mul = x * y
div = x / y

print("The sum result is", add)
print("The sub result is", sub)
print("The mul result is", mul)
print("The div result is", div)
 
5. boolean expression တစ်ခုဖန်တီးပါ။
  True
  
6. conditional expression တစ်ခု ဖန်တီးပါ။

7. mixed type expression တစ်ခုဖန်တီးပါ။
    x = 1
    y = 3.7
    print(x+y)
    
8. boolean တန်ဖိုးဖြင့် simple expression တစ်ခုဖန်တီးပါ။
    print(4<5)
    
9. compound boolean expression တစ်ခုဖန်တီးပါ။
    x = 10
    y = 12
    print(x<y)
    
10. arithmetic expression တွင် x, y, z တန်ဖိုးများကို format ချပြပါ။
x = 4
y = 9

add = x + y
sub = x - y
mul = x * y
div = x / y

print("The sum result of {} and {} is".format(x,y),add)
print("The sub result of {} and {} is".format(x,y),sub)
print("The mul result of {} and {} is".format(x,y),mul)
print("The div result of {} and {} is".format(x,y),div)

11. python နှင့် မသက်ဆိုင်သော မှတ်ချက်တစ်ခုဖန်တီးပါ။

12. Conditional execution ဆိုသည်မှာ အဘယ်နည်း။
help to execute commands when specified conditions are met.

13. conditional execution တစ်ခုဖန်တီးပါ။
x = int(input("Enter Your ID:"))
if x == 1:
    print("You are a student")

else : print("You are not a student")

14. linear execution တစ်ခုဖန်တီးပါ။

x = 2
y = (x+3)/4
print(f'The result of {x} and {y} is ', y)


15. non linear execution တစ်ခုဖန်တီးပါ။

16. conditional statements ဆိုသည်မှာအဘယ်နည်း။
used to guide the program to make the decision based on the conditions 

17. conditional statements တစ်ခုဖန်တီးပါ။
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i != 1:
        print("It is true")

    else :
        print("It is false")
        
18. conditional expression ဆိုသည်မှာ အဘယ်နည်း။
x = int(input("Enter Your ID:"))
decision = "You are a student" if x == "1" else "You are not a student."
print(decision)


19. pass statement ၏ အသုံးဝင်ပုံကို ဖော်ပြပါ။
helps to avoid errors when the code is empty.
20. multiway desicision statement ဆိုသည်မှာ အဘယ်နည်း။

21. multi-way desicision statement တစ်ခုဖန်တီးပါ။
x = int(input("Enter your ID:"))

if x == 1:
    print("Welcome")
    y = int(input("Enter your password:"))
    if y == 1:
        print("Successfully")

    else: print("Your password is wrong.")

elif x == 2:
        print("Welcome")
        y = int(input("Enter your password:"))
        if y == 2:
            print("Successfully")

        else:
            print("Your password is wrong.")

else : print("Try again")
 
22. Multi-way Versus Sequential Conditionals ဆိုသည်မှာအဘယ်နည်း။

23. နမူနာတစ်ခုဖန်တီးပါ။
x = int(input("Enter your ID:"))
if x == 1:
    print("welcome")

if x == 2:
    print("welcome")

if x < 1 :
    print("try again")
    
24. nested conditions ဖန်တီးပါ။
x = int(input("Enter your ID:"))
if x == 1:
    print("Welcome")
    y = int(input("Enter your password:"))
    if y == 1:
        print("Successfully")
    else: print("Your password is wrong.")

else : print("Try again")

25. nested while loop ဖန်တီးပါ။

26. nested for loop ဖန်တီးပါ။

27. conditional statements တွင် ဖြစ်ပေါ်လာနိုင်သော သတိထားရမည့် အခြေအနေနှစ်ခုကို ဖော်ပြပါ။
tautology
contradiction


28. operator precedence ကို ရှင်းပြပါ။
operator having the highest precedence will evaluate first.

29. operator associativity ကို ရှင်းပြပါ။
* and / have the same precedence. When both have to calculate in the same expression, the left one will be evaluated first.
print(2 * 8 /3)

30. unary operator နှစ်ခုကို ရေးပါ။
- +
31. binary operator တစ်ခု အလုပ်လုပ်ရန် operand  ဘယ်နှစ်ခု လိုအပ်သနည်း။
2

32. error အမျိုးအစား သုံးခုကို ရေးပါ။

syntax error
runtime error
logical error


33.  "abcdefghijklmnop" ၏ စာလုံးအရေအတွက်ကို ရေတွက်ရန် မည်သည့် function ကို အသုံးပြုရမည်နည်း။
လက်တွေ့သုံးပြပါ။

34. python တွင် ရေတွက်၍ရသော အရာရာတိုင်းအတွက်  အရေအတွက်စုစုပေါင်းကို သိရှိရန် မည်သည့် function ကို အသုံးပြုရမည်နည်း။

35. တစ်ခုခုကို နားမလည်သဖြင့် အကူအညီတောင်းလိုလျှင် မည့်သည့် function ကို အသုံးပြုရမည်နည်း။
help()
"""