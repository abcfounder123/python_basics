"""


Function Annotations မှတ်ချက်
annotations are stored in __annotations__


def f(x:str, y:str) -> str:
    return f"Hello {x} {y}"

"""

def add(x:int, y:int) -> int:
    return x / y

print(add.__annotations__)
import m
ans = m.mul(1, 2)
print(ans)