# 문자를 ASCII 코드로 변환하는 함수 ord() 함수
# ASCII 코드를 문자로 변환하는 함수 chr() 함수


def solution(s, n):
    answer = ''
    ALPHA = 26
    ALPHA_LOWER = 97
    ALPHA_UPPER = 65

    for i in s:
        if i == ' ':
            answer += ' '
        else:
            if i.isupper():
                answer += chr(ALPHA_UPPER + (ord(i) + n - ALPHA_UPPER) % ALPHA)
            else:
                answer += chr(ALPHA_LOWER + (ord(i) + n - ALPHA_LOWER) % ALPHA)

    return answer