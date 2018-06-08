import os

def fact(n):

    if n <= 1:
        return 1
    else:
        return fact(n-1) * n



print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))