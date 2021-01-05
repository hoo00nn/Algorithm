def Fibonacci(n):
    ret = [0, 1]

    for i in range(2, n + 1):
        ret.append(ret[i - 2] + ret[i - 1])

    return ret


def solution(n):
    answer = 0
    answer = Fibonacci(n)[-1] % 1234567
    return answer