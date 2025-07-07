import math


def square(n):
    sq = n*n
    return math.ceil(sq)


n = float(input("Введите сторону квадрата: "))
result = square(n)
print(result)
