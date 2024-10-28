
"""
1. days in months
2. string formatting
3. leap year
4. calculating start days of month
5. ...
6. ...

################################################

1. days in months

start_day = first day is Sunday or Monday or . . . .
num_days = 28 or 29 or 30 or 31

Mon Tue Wed Thu Fri Sat Sun
                          1
2    3


Mon Tue Wed Thu Fri Sat Sun
      1   2   3   4   5   6
  7   8   9  10  11  12  13
 14  15  16  17  18  19  20
 21  22  23  24  25  26  27
 28  29  30  31


Mon Tue Wed Thu Fri Sat Sun
      1   2   3   4   5   6
  7   8   9  10  11  12  13
 14  15  16  17  18  19  20
 21  22  23  24  25  26  27
 28


Mon Tue Wed Thu Fri Sat Sun
                      1   2
  3   4   5   6   7   8   9
 10  11  12  13  14  15  16
 17  18  19  20  21  22  23
 24  25  26  27  28


A   B   C   D    E    F   G   H
1   2   3   4    5    6   7   8
9   10  11  12

################################################


step.1 ---> days in month

print("Mon Tue Wed Thu Fri Sat Sun")
start_day = 5
num_days = 30

for n in range(1, 31):
    print(n, end="   ")
    if n % 7 == 0:
        print()

################################################

Mon Tue Wed Thu Fri Sat Sun
1   2   3   4   5   6   7
8   9   10   11   12   13   14
15   16   17   18   19   20   21
22   23   24   25   26   27   28
29   30

################################################

step.2 ---> add start day
>> print("    " * start_day, end="")

print("Mon Tue Wed Thu Fri Sat Sun")
start_day = 5
num_days = 30
print("    " * start_day, end="")
for n in range(1, 31):
    print(n, end="   ")
    if n % 7 == 0:
        print()

################################################

Mon Tue Wed Thu Fri Sat Sun
                    1   2   3   4   5   6   7
8   9   10   11   12   13   14
15   16   17   18   19   20   21
22   23   24   25   26   27   28
29   30

################################################

step.3 ---> proper way to add start day
>> f"{n:<4}"
>> (start_day + n) % 7 == 0

print("Mon Tue Wed Thu Fri Sat Sun")
start_day = 1
num_days = 30
print("    " * start_day, end="")
for n in range(1, 31):
    print(f"{n:<4}", end="")
    if (start_day + n) % 7 == 0:
        print()

################################################

Mon Tue Wed Thu Fri Sat Sun
    1   2   3   4   5   6
7   8   9   10  11  12  13
14  15  16  17  18  19  20
21  22  23  24  25  26  27
28  29  30

################################################

step.4 --->  using 'num_days' as a 'stop value' in range
>> range(1, num_days + 1)

print("Mon Tue Wed Thu Fri Sat Sun")
start_day = 1
num_days = 30
print("    " * start_day, end="")

for day in range(1, num_days + 1):
    print(f"{day:3} ", end="")
    if (start_day + day) % 7 == 0:
        print()

################################################

Mon Tue Wed Thu Fri Sat Sun
      1   2   3   4   5   6
  7   8   9  10  11  12  13
 14  15  16  17  18  19  20
 21  22  23  24  25  26  27
 28  29  30

################################################
################################################

2. string formatting

format methods  ( f, a, t )
>>   :
>>   fill charactor (" ")
>>   <^> alignment  ( < )
>>   total charactor count

################################################

# f, a, t ---> -, >, 20
x = "My Self"
s = f"{x:-^20}"
print(s)

################################################

------My Self-------

# 6 space + 7 characters + 7 space  = 20

################################################

h1 = "No"
h2 = "Name"
h3 = "age"
line = "-" * 41
data = [
     (1, "Mg Mg", 20),
     (2, "Ma Ma", 30),
     (3, "Hla Hla", 20),
     (4, "Mg Ba", 30),
     (5, "U Mya", 20),
     (6, "Tun Tun", 30),
     (7, "mama", 20)
]

print(line)
print(f"|{h1:^6}|{h2:^24}|{h3:^7}|")
print(line)

for i in data:
    print(f"|{i[0]:^6}|{i[1]:^24}|{i[2]:^7}|")
    print(line)

################################################

# proper style
for i in data:
    no, name, age = i
    print(f"|{no:^6}|{name:^24}|{age:^7}|")
    print(line)


################################################

-----------------------------------------
|  No  |          Name          |  age  |
-----------------------------------------
|  1   |         Mg Mg          |  20   |
-----------------------------------------
|  2   |         Ma Ma          |  30   |
-----------------------------------------
|  3   |        Hla Hla         |  20   |
-----------------------------------------
|  4   |         Mg Ba          |  30   |
-----------------------------------------
|  5   |         U Mya          |  20   |
-----------------------------------------
|  6   |        Tun Tun         |  30   |
-----------------------------------------
|  7   |          mama          |  20   |
-----------------------------------------

################################################

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
width = 12

for d in days:
    print(f"{d:^{width}}", end="")

print()

start_day = 1
num_days = 30
print(" " * width * start_day, end="")
for n in range(1, 31):
    print(f"{n:^{width}}", end="")
    if (start_day + n) % 7 == 0:
        print()

################################################

   Monday     Tuesday    Wednesday    Thursday     Friday     Saturday     Sunday
                 1           2           3           4           5           6
     7           8           9           10          11          12          13
     14          15          16          17          18          19          20
     21          22          23          24          25          26          27
     28          29          30

################################################
################################################

3. leap year

Julius Caesar
julian calendar    45 BC
---> 365, +1 day in 4 years(leap year) (.25 in each year)  ---> 365.25
--->  11 minutes longer  , 128 years 1 day faster , 384 --> 3 days faster

Pope Gregory XIII
Gregorian calendar 1582   ---> 365.2425
--->  - 3 days in every 400 years  ---> - 1 day in every 100 years not 400
--->  3030 --> 1 day

################################################

Zeller's congruence
Christian Zeller

################################################

2. leap year
step.1 ---> program to decide leap year

year = 1700
if year % 4 == 0:
    print("julian calendar leap year")

################################################

year = 1700
if year % 4 == 0:
    if year % 100 != 0:
        print("Gregorian calendar leap year.1")

    if year % 400 == 0:
        print("Gregorian calendar leap year.2")

################################################

step.2 ---> creating function to decide leap year

def leap_year_g(year):
    if year % 4 == 0:
        if year % 100 != 0:
            print(f"{year} Gregorian calendar leap year.1")

        if year % 400 == 0:
            print(f"{year} Gregorian calendar leap year.2")


leap_year_g(1600)
leap_year_g(1700)
leap_year_g(1800)
leap_year_g(1900)
leap_year_g(2000)

################################################

def leap_year_f(year):
    if year % 4 == 0:
        print(f"{year} julian calendar leap year")


leap_year_f(1700)
leap_year_f(1800)
leap_year_f(1900)
leap_year_f(2000)

################################################

step.3 ---> creating useful function for checking leap year

def leap_year_g(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True

        if year % 400 == 0:
            return True

    return False

################################################

def leap_year_f(year):
    if year % 4 == 0:
        return True
    return False


print(leap_year_g(1700))
print(leap_year_f(1700))

################################################
################################################

4. calculating start days of month 

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# 0000/00/8   ---> 0, 0, 7  passed
# 0000/02/2   ---> 0, 1, 1  passed --> month + day  ---> 31 + 1 ---> 32 days passed
# 0002/02/2   ---> 1, 1, 1  ---> 365 + 31 + 1 --> 397 days passed
# print(days[397 % 7])  # if start day is Sunday
# days[(start_day + n) % 7]  # proper way for various start day

MONTHS = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# print(DAYS_IN_MONTH[1])


def is_leap_year(year):
    """Julian calendar leap year"""
    return year % 4 == 0


def days_in_month(year, month):
    if month == 2 and is_leap_year(year):
        return 29
    return DAYS_IN_MONTH[month]


print("Mon Tue Wed Thu Fri Sat Sun")
start_day = 5  # Saturday
num_days = 32
print("    " * start_day, end="")
for n in range(1, num_days + 1):
    print(f"{n:<4}", end="")
    if (start_day + n) % 7 == 0:
        print()

print()

# 0000/02   ---> after one month passed  ---> 31 days passed ---> start day of second month is 32
# If the start day of our calendar is Saturday, it will be Tuesday after 31 days
# So, start day of second month is Tuesday (32)
print(days[(start_day + n) % 7])  # 5 Tuesday

################################################

Mon Tue Wed Thu Fri Sat Sun
                    1   2   
3   4   5   6   7   8   9   
10  11  12  13  14  15  16  
17  18  19  20  21  22  23  
24  25  26  27  28  29  30  
31  32

Tuesday

################################################

print("Mon Tue Wed Thu Fri Sat Sun")
start_day = 0  # Monday
num_days = 32
print("    " * start_day, end="")
for n in range(1, num_days + 1):
    print(f"{n:<4}", end="")
    if (start_day + n) % 7 == 0:
        print()

print()

# If the start day of our calendar is Monday, it will be Thursday after 31 days
# So, start day of second month is Thursday (32)
print(days[(start_day + n) % 7])

################################################

Mon Tue Wed Thu Fri Sat Sun
1   2   3   4   5   6   7   
8   9   10  11  12  13  14  
15  16  17  18  19  20  21  
22  23  24  25  26  27  28  
29  30  31  32  

Thursday

################################################

print("- " * 20)
print("second month")
print()
print("Mon Tue Wed Thu Fri Sat Sun")
start_day = 3  # Thursday
num_days = 28
print("    " * start_day, end="")
for n in range(1, num_days + 1):
    print(f"{n:<4}", end="")
    if (start_day + n) % 7 == 0:
        print()

################################################

- - - - - - - - - - - - - - - - - - - -
second month

Mon Tue Wed Thu Fri Sat Sun
            1   2   3   4
5   6   7   8   9   10  11
12  13  14  15  16  17  18
19  20  21  22  23  24  25
26  27  28  

################################################
################################################
“""

