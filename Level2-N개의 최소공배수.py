# 두 가지 방식으로 풀 수 있다
# 1. gcd함수 이용 2. 유클리드 호제법 구현

from math import gcd


def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        answer = answer * arr[i] // gcd(answer, arr[i])

    return answer

# 유클리드 호제법 직접 구현 풀이

def getGCD(x, y):
    if x == y: return x
    if x > y:
        while True:
            x, y = y, x % y
            if y == 0: return x
    while True:
        y, x = x, y % x
        if x == 0: return y


def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        answer = answer * arr[i] // getGCD(answer, arr[i])

    return answer