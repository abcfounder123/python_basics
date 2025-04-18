"""
#################################################

" slope (m) "

increase ( 2x )  -->  /

1 2 3 4 5         -->  x       <---  input data
2 4 6 8 10        -->  y       <---  output data

function, model, linear relations   --->  "y = 2x" 

decrease ( -2x )  -->  \\

1    2    3    4    5
-2  -4   -6   -8   -10

" linear relations "

correlation coefficient  -->  2
correlation coefficient  --> -2

#################################################

linear Regression

m = (y2 - y1) / (x2 - x1)

10         .
9
8       .
7
6     .
5
4   . (2, 4)
3
2 . (1, 2)
1
0 1 2 3 4 5

10
9
8
7 .
6 .
5 .
4 .
3 . . . . .
2
1
0 1 2 3 4 5
1
2 .
3
4   .
5
6     .
7
8       .
9

#################################################

difference of y   = 4 - 2 = 2     ( rise ) ( vertical )   (height)
difference of x   = 2 - 1 = 1     ( run )  ( horizontal ) (base)
correlation coefficient = slope = m = 2 / 1 = 2     ( + up / , - down  \\ , 0 horizontal, undefined vertical )
linear relations --->  y = mx + b = 2x + 0 = 2x

#################################################

" y intercept (b) "
- value of y when x = 0

" linear relations / function / model "
y = mx + b

2x + 0
0 1 2 3 4 5
0 2 4 6 8 10

2x + 1
0 1 2 3 4  5
1 3 5 7 9  11

dy = 5 - 3 = 2
dx = 2 - 1 = 1
correlation coefficient = slope = m = dy / dx = 2 / 1 = 2
y intercept = b = 1
linear relations --->  y = mx + b = 2x + 1

#################################################

linear function / formula ( mathematics model )
mx + b
mx**2 + x + b
mx**3 + x**2 + b

#################################################

Regression
- linear
- non linear

#################################################

linregress(x, y)   -->  (m, b, rvalue, pvalue, stderr)
1. slope ( m )
2. y intercept ( b )
3. Regression value ( rvalue ) ( 1 = 100%, 0.1 = 10% )
4. paired value ( pvalue )
5. standard error ( stderr )

#################################################

simple linear function
mx + b

" machine learning "
- finding complex function for Regression

#################################################

map, reduce, filter ( functional programming concept ) ( declarative paradigm )

#################################################

" prediction "
- machine learning model or
- custom model/ function

def model(x):
    return mx + b

#################################################

" loop "

input_data = [1, 2, 3, 4, 5]

print(1)
print(2)
print(3)
print(4)
print(5)

print('- ' * 21)

#################################################

for n in input_data:
    print(n)

print('- ' * 21)

map(print, input_data)

#################################################
#################################################

" loop Vs map "

# mx + b
# 2x + 1
m = 2
b = 1

def model(x):
    return m * x + b


input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_data = []

for i in input_data:
    output_data.append(model(i))

print(output_data)

input_data = [1, 2, 3, 4, 5]
output_data = list(map(model, input_data))
#print(output_data)

#################################################

Machine Learning

# 1 2 3 4 5  6  7  8  9  10
# 3 5 7 9 11 13 15 17 19 21
# train(linear model) 80%, check 20%

# train data
# input data  --> 1 2 3 5  6  7  8  10,
# output data --> 3 5 7 11 13 15 17 21

# test data
# input data  --> 4, 9
# actual output data --> 9, 19


def model(x):
    return 2 * x + 1


test_input_data = [4, 9]
actual_output_data = [9, 19]

predict_output_data = list(map(model, test_input_data))
print(predict_output_data == actual_output_data)

predict_data = model(-2)
print(predict_data)

#################################################
#################################################

"""
