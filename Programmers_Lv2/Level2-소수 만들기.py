# Solving 1 -> isPrime함수 구현해서 해결
# Solving 2 -> 에라토테네스의 체 이용해서 해

from itertools import combinations
from math import sqrt


def isPrime(num):
    end = int(sqrt(num)) + 1

    for i in range(2, end):
        if num % i == 0: return False
    return True


def solution(nums):
    answer = 0
    ret = list(map(lambda x: x[0] + x[1] + x[2], combinations(nums, 3)))
    print(ret)
    for i in ret:
        if isPrime(i):
            answer += 1

    return answer

# 밑에는 에라토스테네스의 체 이용한 풀이

def isPrime2(num):
    check = [True for i in range(num + 1)]
    end = int(sqrt(num)) + 1
    for i in range(2, end):
        if check[i]:
            for j in range(i + i, num + 1, i):
                check[j] = False
    return check


def solution(nums):
    answer = 0
    ret = list(map(lambda x: x[0] + x[1] + x[2], combinations(nums, 3)))
    check = isPrime2(max(ret))
    for i in ret:
        if check[i]:
            answer += 1
    return answer