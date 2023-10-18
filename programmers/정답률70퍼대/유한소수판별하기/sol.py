import math


def solution(a, b):
    gcd = math.gcd(a, b)
    b //= gcd

    d = 2

    num = []

    while d <= b:
        if b % d == 0:
            b //= d

            num.append(d)

        else:
            d += 1

    if all(i in [2,5] for i in num):
        return 1
    else:
        return 2


print(solution(7, 20))