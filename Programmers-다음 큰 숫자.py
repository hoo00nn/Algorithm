# 풀고 나서 다른 사람의 풀이를 보니 bin이라는 함수가 존재 했다.
# bin 함수는 10진수 숫자를 2진수 문자열로 바꿔주는 함수.
# 맨 밑에 bin()을 이용한 풀

def binaryConversion(k):
    num = ''

    while k > 0:
        if k % 2 == 1:
            num += '1'
        else:
            num += '0'

        k = int(k / 2)

    return num


def solution(n):
    answer = binaryConversion(n)
    k = n + 1

    while True:
        if answer.count('1') == binaryConversion(k).count('1'):
            answer = int(k)
            break
        else:
            k += 1

    return answer


# 여기서부터 bin()을 이용한 풀이
# 너무 간단하게 구현 가능했다.

def solution(n):
    answer = bin(n).count('1')

    while True:
        n += 1
        if answer == bin(n).count('1'):
            return n

    return answer

