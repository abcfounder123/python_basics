

add_mark = 1

def draw_line():
    print()
    print("- " * 40)
    print()


def check_rank(highest_mark, mark):
    m = {"very good": highest_mark,
         "good": highest_mark * 0.8,
         "pass": highest_mark * 0.4,
         "fail": highest_mark * 0.4}

    if mark == m["very good"]:
        ans = "very good"

    elif mark >= m["good"]:
        ans = "good"

    elif mark >= m["pass"]:
        ans = "pass"

    elif mark < m["fail"]:
        ans = "fail"
    return ans


def exam():
    l = dict()
    mark = 0 # total
    highest_mark = 0
    for i in range(1, 13, 1):
        sub_mark = 0
        for j in range(1, 13, 4): # 1, 5, 9
            ans = int(input(f"{i} * {j} = "))
            highest_mark += add_mark
            if i * j == ans:
                print("True")
                mark += add_mark
                sub_mark += add_mark
            else:
                print("False")
            

        l[f"chapter.{i}"] = sub_mark
        # print(l)
        print(f"chapter{i} mark : {sub_mark}")
        # print(f"total mark : {mark}")
        draw_line()

    status = check_rank(mark=mark, highest_mark=highest_mark)
    return status, mark, l


def form():
    roll_no = input("roll no : ")
    name = input("name : ")
    draw_line()
    return roll_no, name



















"""


# setting
add_mark = 3

highest_mark = 0
marks = 0
sub_marks = dict()
for n in range(3, 10, 2):# 3, 5, 7, 9
    draw_line()
    sub = 0
    for n2 in range(5, 10, 2): # 5, 7, 9
        ans = n * n2
        uans = int(input(f"{n} * {n2} = "))
        highest_mark += add_mark
        if ans == uans:
            marks += add_mark
            sub += add_mark
        
    sub_marks[n] = sub
            
print(marks) 
print(sub_marks)
print(highest_mark)
print(check_rank(highest_mark, marks))




def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

pi = 3.141
argv = []

"m"
""

if __name__ == "__main__":
    test1 = add(1, 2) == 3
    test2 = mul(1, 2) == 2
    test3 = div(1, 2) == 0.5
    print("test1 =", test1)
    print("test2 =", test2)
    print("test3 =", test3)






n1 = 10
if n1 % 2 == 0:
    print(n1, "is even number.")
else:
    print(n1, "is odd number.")

n2 = 3
if n2 % 2 == 0:
    print(n2, "is even number.")
else:
    print(n2, "is odd number.")

n3 = 7
if n3 % 2 == 0:
    print(n3, "is even number.")
else:
    print(n3, "is odd number.")


def even_odd(n):
    if n % 2 == 0:
        print(n, "is even number.")
    else:
        print(n, "is odd number.")

n1 = 10
even_odd(n1)

n2 = 3
even_odd(n2)

n3 = 7
even_odd(n3)



# effect
def even_odd(n):
    if n % 2 == 0:
        print(n, "is even number.")
    else:
        print(n, "is odd number.")

for n in range(1, 1001):
    even_odd(n)


# result
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

for n in range(1, 1001):
    print(n, "is even number.", is_even(n))




class Number:
    def __init__(self, n):
3 * 5 = 15
3 * 7 = 21
3 * 9 = 27

        self.n = n

    def is_even(self):
        if self.n % 2 == 0:
            return True
        else:
            return False

    def even_odd(self):
        if self.n % 2 == 0:
            print(self.n, "is even number.")
        else:
            print(self.n, "is odd number.")





def s(l):
    t = 0
    for i in l:
        t += i
    return t

d = {'chapter.2': 2, 'chapter.3': 4, 'chapter.4': 2}
print(sum(d.values()))
print(s(d.values()))


# setting
add_mark = 3

highest_mark = 0
marks = 0
sub_marks = dict()
for n in range(3, 10, 2):# 3, 5, 7, 9
    draw_line()
    sub = 0
    for n2 in range(5, 10, 2): # 5, 7, 9
        ans = n * n2
        uans = int(input(f"{n} * {n2} = "))
        highest_mark += add_mark
        if ans == uans:
            marks += add_mark
            sub += add_mark
        
    sub_marks[n] = sub
            
print(marks) 
print(sub_marks)
print(highest_mark)
print(check_rank(highest_mark, marks))

"""



