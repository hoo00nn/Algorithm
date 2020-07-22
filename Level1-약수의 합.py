import math


def divisor(n):
    k = int(math.sqrt(n))
    check = []

    for i in range(1, k + 1):
        if n % i == 0:
            check += [i]
            check += [int(n / i)]

    return set(check)


def solution(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    return sum(divisor(n))