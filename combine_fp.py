

# combining functions ( creating pipe lines )
# map , filter
'''
class Student:
    def __init__(self, name, age, ph_no, course):
        self.name = name
        self.age = age
        self.ph_no = ph_no
        self.course = course # ["python", "js"]
        #self.new_python_lessons = ["lesson1.mp4", .....]

    def __repr__(self):
        return f"name = {self.name}, age = {self.age}, phone No = {self.ph_no}, Course = {self.course}"

#################################################

students = list()

for i in range(1, 11):
    user = f"user.{i:03}"
    ph = f"09{i:0>9}"
    students.append(Student(user, 20, ph, ["python", ]))

for i in range(11, 21):
    user = f"user.{i:03}"
    ph = f"09{i:0>9}"
    students.append(Student(user, 20, ph, ["python", "js"]))

for i in range(21, 31):
    user = f"user.{i:03}"
    ph = f"09{i:0>9}"
    students.append(Student(user, 20, ph, ["C#", "js"]))

#for student in students:
#    print(student)

new_python_lessons = ["lesson1.mp4", "lesson2.mp4", "lesson3.mp4", "lesson4.mp4", 
                      "lesson5.mp4", "lesson6.mp4", "lesson7.mp4", "lesson8.mp4", 
                      "lesson9.mp4", "lesson10.mp4"]

#################################################

#print("js" in ['python', 'js'])

#def check_py_student(obj):
#    return "python" in obj.course

def check_py_student(obj):
    result = "python" in obj.course
    #print(f"Checking result of {obj.name} : {result}")
    return result

# not pure
def sent(obj):
    #print("Sent new python lessons to", obj.name)
    obj.new_python_lessons = new_python_lessons
    return obj.name


# pip line
sent = map(sent, filter(check_py_student, students))

# step.1
#next(sent)
#next(sent)

# step.2
l = list(sent)

###
# step.2
for i in sent:
    print(i)
    print(" -" * 21)

###

#for
#map   --->   sent
#filter   --->   check py student
#list

#################################################

red = "\033[31m"
green = "\033[32m"
end = "\033[0m"
for student in students:
    if hasattr(student, "new_python_lessons"):
        print(green, student.name, end)
        #print(student.new_python_lessons )
    else:
        print(red, student.name, end)

#################################################

# map , filter

class Student:
    def __init__(self, name, age, ph_no, course):
        self.name = name
        self.age = age
        self.ph_no = ph_no
        self.course = course

    def __repr__(self):
        return f"name = {self.name}, age = {self.age}, phone No = {self.ph_no}, Course = {self.course}"
users = list()

#################################################

students = list()

for i in range(1, 11):
    user = f"user.{i:03}"
    ph = f"09{i:0>9}"
    students.append(Student(user, 20, ph, ["python", ]))

for i in range(11, 21):
    user = f"user.{i:03}"
    ph = f"09{i:0>9}"
    students.append(Student(user, 20, ph, ["python", "js"]))

for i in range(21, 31):
    user = f"user.{i:03}"
    ph = f"09{i:0>9}"
    students.append(Student(user, 20, ph, ["C#", "js"]))

#for student in students:
#    print(student)

new_python_lessons = ["lesson1.mp4", "lesson2.mp4", "lesson3.mp4", "lesson4.mp4", "lesson5.mp4", "lesson6.mp4", "lesson7.mp4", "lesson8.mp4", "lesson9.mp4", "lesson10.mp4"]

#################################################

def check_py_student(obj):
    return "python" in obj.course

def to_sent(attr, lessons):
    def sent(obj):
        setattr(obj, attr, lessons)# obj.attr = lessons
        return obj.name
    return sent

#################################################

def sent_py_lesson(obj):
    obj.new_python_lessons = new_python_lessons
    return obj.name

################################################

sent_py_lesson = to_sent("new_python_lessons", new_python_lessons)

sent_report = list(map(sent_py_lesson, filter(check_py_student, students)))
print(sent_report)


red = "\033[31m"
green = "\033[32m"
end = "\033[0m"
for student in students:
    if hasattr(student, "new_python_lessons"):
        print(green, student.name, end)
    else:
        print(red, student.name, end)

#################################################

new_c_lessons = ["lesson1.mp4", "lesson2.mp4", "lesson3.mp4", "lesson4.mp4", "lesson5.mp4", "lesson6.mp4", "lesson7.mp4", "lesson8.mp4", "lesson9.mp4", "lesson10.mp4"]

def check_c_student(obj):
    return "C#" in obj.course

#################################################
#################################################

def sent_c_lesson(obj):
    obj.new_c_lessons = new_c_lessons
    return obj.name

################################################

sent_c_lesson = to_sent("new_c_lessons", new_c_lessons)

sent_report = list(map(sent_c_lesson, filter(check_c_student, students)))
print(sent_report)


red = "\033[31m"
green = "\033[32m"
end = "\033[0m"
for student in students:
    if hasattr(student, "new_c_lessons"):
        print(green, student.name, end)
    else:
        print(red, student.name, end)

#################################################

new_js_lessons = ["lesson1.mp4", "lesson2.mp4", "lesson3.mp4", "lesson4.mp4", "lesson5.mp4", "lesson6.mp4", "lesson7.mp4", "lesson8.mp4", "lesson9.mp4", "lesson10.mp4"]

sent_js_lesson = to_sent("new_js_lessons", new_js_lessons)

sent_report = list(map(sent_js_lesson, filter(lambda student: "js" in student.course, students)))
print(sent_report)

###

red = "\033[31m"
green = "\033[32m"
end = "\033[0m"

for student in students:
    if hasattr(student, "new_js_lessons"):
        print(green, student.name, end)
    else:
        print(red, student.name, end)

#################################################

# recursion print
def re_p_js(students):
    if students:
        student = students[0]
    else:
        return None
    if hasattr(student, "new_js_lessons"):
        print(green, student.name, end)
        return re_p(students[1:])
    else:
        print(red, student.name, end)
        return re_p(students[1:])

re_p_js(students)


def rep(attr):
    red = "\033[31m"
    green = "\033[32m"
    end = "\033[0m"
    
    def re_p(students):
        if students:
            student = students[0]
        else:
            return None
        if hasattr(student, "new_js_lessons"):
            print(green, student.name, end)
            return re_p(students[1:])
        else:
            print(red, student.name, end)
            return re_p(students[1:])
        return r
    
    


#################################################

def to_sent(attr, lessons):
    def sent(obj):
        setattr(obj, attr, lessons)# obj.attr = lessons
        return obj.name
    return sent


def rep(attr):
    red = "\033[31m"
    green = "\033[32m"
    end = "\033[0m"
    
    def r(students):
        if students:
            student = students[0]
        else:
            return None
        if hasattr(student, attr):
            print(green, student.name, end)
            return r(students[1:])
        else:
            print(red, student.name, end)
            return r(students[1:])
    return r

#################################################

class Student:
    def __init__(self, name, age, ph_no, course):
        self.name = name
        self.age = age
        self.ph_no = ph_no
        self.course = course

    def __repr__(self):
        return f"name = {self.name}, age = {self.age}, phone No = {self.ph_no}, Course = {self.course}"
users = list()

#################################################

students = list()

for i in range(1, 11):
    user = f"user.{i:03}"
    ph = f"09{i:0>9}"
    students.append(Student(user, 20, ph, ["python", ]))

for i in range(11, 21):
    user = f"user.{i:03}"
    ph = f"09{i:0>9}"
    students.append(Student(user, 20, ph, ["python", "js", "fp"]))

for i in range(21, 31):
    user = f"user.{i:03}"
    ph = f"09{i:0>9}"
    students.append(Student(user, 20, ph, ["C#", "js"]))



new_python_lessons = ["lesson1.mp4", "lesson2.mp4", "lesson3.mp4", "lesson4.mp4", "lesson5.mp4", "lesson6.mp4", "lesson7.mp4", "lesson8.mp4", "lesson9.mp4", "lesson10.mp4"]
new_c_lessons = ["lesson1.mp4", "lesson2.mp4", "lesson3.mp4", "lesson4.mp4", "lesson5.mp4", "lesson6.mp4", "lesson7.mp4", "lesson8.mp4", "lesson9.mp4", "lesson10.mp4"]
new_js_lessons = ["lesson1.mp4", "lesson2.mp4", "lesson3.mp4", "lesson4.mp4", "lesson5.mp4", "lesson6.mp4", "lesson7.mp4", "lesson8.mp4", "lesson9.mp4", "lesson10.mp4"]

#################################################

sent_py_lesson = to_sent("new_python_lessons", new_python_lessons)
sent_c_lesson = to_sent("new_c_lessons", new_c_lessons)
sent_js_lesson = to_sent("new_js_lessons", new_js_lessons)

rep_py = rep("new_python_lessons")
rep_js = rep("new_js_lessons")
rep_c = rep("new_c_lessons")

pip_py = map(sent_py_lesson, filter(lambda student: "python" in student.course, students))
pip_c = map(sent_c_lesson, filter(lambda student: "C#" in student.course, students))
pip_js = map(sent_js_lesson, filter(lambda student: "js" in student.course, students))

list(pip_py)
list(pip_js)
list(pip_c)

#rep_py(students)
#rep_js(students)
#rep_c(students)

#################################################

data = [1, 2, 3]
sent_fp_lesson = to_sent("functional_programming", data)

pip_fp = map(sent_fp_lesson, filter(lambda student: "fp" in student.course, students))

list(pip_fp)

rep_fp = rep("functional_programming")
rep_fp(students)

#################################################
#################################################


#################################################

# map , zip

#################################################

users = list()
for i in range(1, 11):
    
    name = f"user{i:04}"
    password = f"{i:x<6}"
    mail = f"{name}@gmail.com"
    user = (i, name, password, mail)
    users.append(user)

print(users)

#################################################

users = [
         ('ID', 'User Name', 'Password', 'Email'),
         (1, 'user0001', '1xxxxx', 'user0001@gmail.com'), 
         (2, 'user0002', '2xxxxx', 'user0002@gmail.com'), 
         (3, 'user0003', '3xxxxx', 'user0003@gmail.com'), 
         (4, 'user0004', '4xxxxx', 'user0004@gmail.com'), 
         (5, 'user0005', '5xxxxx', 'user0005@gmail.com'), 
         (6, 'user0006', '6xxxxx', 'user0006@gmail.com'), 
         (7, 'user0007', '7xxxxx', 'user0007@gmail.com'), 
         (8, 'user0008', '8xxxxx', 'user0008@gmail.com'), 
         (9, 'user0009', '9xxxxx', 'user0009@gmail.com'), 
         (10, 'user0010', '10xxxx', 'user0010@gmail.com'),
         
]

fruits = [
         ('ID', 'Fruit Name', 'Price', 'Stock'),
         (1, 'apple', '1000', '1000'), 
         (2, 'banana', '200', '2000'), 
         (3, 'orange', '500', '3000'), 
         
]

# step.1
def render(data):
    for i, n, p, e in data:
        print(f"{i:^5} {n:^12} {p:^10} {e:^30}")
        
render(users)
print("\n")

render(fruits)
print("\n")

#################################################

# step.2
def render_web(data):
    t = "<table>"
    for id, name, password, mail in data:
        r = f"""
        <tr>
            <td>{id}</th>
            <td>{name}</th>
            <td>{password}</th>
            <td>{mail}</th>
        </tr>
        """
        t += r

    t += "\n</table>"
    return t

t = render_web(users)
print(t)
#print(t, file=open("user_table.html", "w"))

ft = render_web(fruits)
print(ft)
#print(ft, file=open("fruit_table.html", "w"))



 ID    User Name    Password              Email             
  1     user0001     1xxxxx         user0001@gmail.com      
  2     user0002     2xxxxx         user0002@gmail.com      
  3     user0003     3xxxxx         user0003@gmail.com      
  4     user0004     4xxxxx         user0004@gmail.com      
  5     user0005     5xxxxx         user0005@gmail.com      
  6     user0006     6xxxxx         user0006@gmail.com      
  7     user0007     7xxxxx         user0007@gmail.com      
  8     user0008     8xxxxx         user0008@gmail.com      
  9     user0009     9xxxxx         user0009@gmail.com      
 10     user0010     10xxxx         user0010@gmail.com      
 
#################################################

map က column data တွေကိုပဲ ယူတာဖြစ်လို့ 
row data တွေကို ယူစေချင်ရင် zip ကို ကြားခံသုံးရပါတယ်။

( zip က row နဲ့ column ပြောင်း‌ပေးပါတယ်။ )
'''
users = [
         ('ID', 'User Name', 'Password', 'Email'),
         (1, 'user0001', '1xxxxx', 'user0001@gmail.com'), 
         (2, 'user0002', '2xxxxx', 'user0002@gmail.com'), 
         (3, 'user0003', '3xxxxx', 'user0003@gmail.com'), 
         (4, 'user0004', '4xxxxx', 'user0004@gmail.com'), 
         (5, 'user0005', '5xxxxx', 'user0005@gmail.com'), 
         (6, 'user0006', '6xxxxx', 'user0006@gmail.com'), 
         (7, 'user0007', '7xxxxx', 'user0007@gmail.com'), 
         (8, 'user0008', '8xxxxx', 'user0008@gmail.com'), 
         (9, 'user0009', '9xxxxx', 'user0009@gmail.com'), 
         (10, 'user0010', '10xxxx', 'user0010@gmail.com'),
         
]


# tr ---> table row
# th ---> table header
# td ---> table data
def render_user(id, name, password, mail):
    result =  f"""
    <tr>
        <td>{id}</th>
        <td>{name}</th>
        <td>{password}</th>
        <td>{mail}</th>
    </tr>
    """
    return result

#r = render_user(1, "mag mg", "123456", "mgmg123@gmail.com")
#print(r)

#################################################

render_list = list()

# step.1 ---> loop
for user in users: #  ('ID', 'User Name', 'Password', 'Email'),
    render_list.append(render_user(*user))

#print(render_list[0])

#################################################

# step.2  ---> zip , map

a = list(zip(*users)) # row data to column data
# print(a)

render_list2 = map(render_user, *a)
#print(next(render_list2))

#################################################
# step.3 ---> fp mode
render_list2 = map(render_user, *zip(*users)) # pip line
#print(next(render_list2))

#################################################

header = f"""
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Password</th>
        <th>Mail</th>
    </tr>
"""

str_ren = header.join(render_list2) # iterator to str

str_ren = "\n<table>\n" + str_ren + "\n</table>\n"
print(str_ren)

# file = create, write, close 
h = open("user_table.html", "w")
h.write(str_ren)
h.close()

'''
#################################################

*users

('user0001', '1xxxxx', 'user0001@gmail.com'), ('user0002', '2xxxxx', 'user0002@gmail.com'), ('user0003', '3xxxxx', 'user0003@gmail.com'), ('user0004', '4xxxxx', 'user0004@gmail.com'), ('user0005', '5xxxxx', 'user0005@gmail.com'), ('user0006', '6xxxxx', 'user0006@gmail.com'), ('user0007', '7xxxxx', 'user0007@gmail.com'), ('user0008', '8xxxxx', 'user0008@gmail.com'), ('user0009', '9xxxxx', 'user0009@gmail.com'), ('user0010', '10xxxx', 'user0010@gmail.com')

#################################################

#print(*zip(*users))

* zip

('user0001', 'user0002', 'user0003', 'user0004', 'user0005', 'user0006', 'user0007', 'user0008', 'user0009', 'user0010')

('1xxxxx', '2xxxxx', '3xxxxx', '4xxxxx', '5xxxxx', '6xxxxx', '7xxxxx', '8xxxxx', '9xxxxx', '10xxxx')

('user0001@gmail.com', 'user0002@gmail.com', 'user0003@gmail.com', 'user0004@gmail.com', 'user0005@gmail.com', 'user0006@gmail.com', 'user0007@gmail.com', 'user0008@gmail.com', 'user0009@gmail.com', 'user0010@gmail.com)

#################################################
#################################################
'''

