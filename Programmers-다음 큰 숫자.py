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