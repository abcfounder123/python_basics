
from Test import FunctionTester
#  2, 3, 4
def max_of_three(n1, n2, n3):
    max = n1
    if n2 > max:
        max = n2
    elif n3 > max:
        max = n3
    return max

# 1, 2, 3, 4, 5, 6, 2, 5
def maxfun(l):
    max = l[0]
    for n in l:
        if n > max:
            max = n
    return max

def sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

def test():
    t = FunctionTester()

    t.check("max_of_three test #1", 4, max_of_three, 2, 3, 4)
    t.check("max_of_three test #2", 4, max_of_three, 4, 3, 2)
    t.check("max_of_three test #3", 4, max_of_three, 3, 2, 4)

    t.check("max function test #1", 10, max, range(11))
    t.check("max function test #1", 9, max, [8, 5, 2, 9, 6, 3, 1, 4, 7])

    t.check("sum function test #1", 10, sum, range(5))
    t.check("sum function test #2", 45, sum, range(10))

    t.report_results()


if __name__ == "__main__":
    test()