"""
Defining Functions


def name(par):
    '''doc-strings'''
    statements   
    return value


def  = keyword for standard function definition (keyword)
name = function name ( identifier for function object )
()   = parenthesized list of formal parameters
:    = code block
____ = indent ( function body)

'''doc'''  = str value for function's documentation
statements = code section in function body
return     = used to exit a function and return a value (keyword)  ( default value ---> None )

################################################

1. invoke, call
2. more than one place, decomposition,
3. where?
   --->  built-in function,
   --->  preinstalled module, external module,
   --->  directly from our code
4. def, name, (), :, body
5. same name of function

################################################

6. parameterized function

# parameter

# 1. standard / normal parameter    ---> (x, y)
# positional arguments              ---> (2, 3)
# keyword arguments                 ---> (x=2, y=3)
# mixed                             ---> (2, y=3)

# 2. special parameter              ---> /, *
# positional only parameter         ---> (x, y, /)
# keyword only parameter            ---> (*, x, y)

################################################


def f_z(x, y):
    z = x ** 2 + 2 * x * y + y ** 2
    return z


z = f_z(2, 3)
print(z)

################################################


def add(x, y, /):
    return x + y


add(1, 2)

################################################


def info(*, name, age, phone_no):
    print(f"name = {name}")
    print(f"age = {age}")
    print(f"phone No = {phone_no}")


info(phone_no="09953212", name="Mg Mg", age=20)

################################################

"""