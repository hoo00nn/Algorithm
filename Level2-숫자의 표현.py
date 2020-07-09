# 소요시간 5분

def solution(n):
    answer = 1

    check_num = n // 2 if n % 2 == 0 else n // 2 + 2

    for i in range(1, check_num):
        sum = 0
        while True:
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
            else:
                sum += i
            i += 1

    return answer