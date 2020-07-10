def check(n):
    ret = 0

    while n > 0:
        if n % 2 == 1: ret += 1
        ret = ret + check(n // 2)
        return ret

    return 0


def solution(n):
    return check(n)