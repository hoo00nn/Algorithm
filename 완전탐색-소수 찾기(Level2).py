# 3시간 만에 풀었다. 어려웠다
# 구하려는 수의 제곱근까지만 확인해도 구할 수 있다는 것을 알고난 후 시간을 절반이상 단축했는데,,
# 완성하고 다른 사람의 소스를 보니 내 시간복잡도 보다 5배이상 단축시킨 코드가 있었다,,

from itertools import permutations

def solution(numbers):
    answer = 0
    maximum = 10000000
    seive = [False, False] + [True] * (maximum-1)
    l = round(maximum ** 0.5) + 1
    result = []

    for i in range(2, l):
        if seive[i]:
            k = i * 2
            while k <= maximum:
                seive[k] = False
                k += i

    for i in range(0, len(numbers)):
        result += list(map(int, map(''.join, permutations(list(numbers), i+1))))

    result = list(set(result))

    for i in result:
        if seive[i]:
            answer += 1

    return answer

