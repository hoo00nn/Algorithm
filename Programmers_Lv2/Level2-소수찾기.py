import math


def isPrime(n):
    check = [False, False] + [True for i in range(n - 1)]
    k = math.ceil(math.sqrt(n))

    for i in range(2, k):
        if check[i]:
            for j in range(i + i, n + 1, i):
                check[j] = False

    return check

def solution(n):
    answer = isPrime(n).count(True)
    return answer