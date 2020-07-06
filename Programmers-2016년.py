# 나만 이해할 수 있는 코드로 짠 것 같다..

def solution(a, b):
    answer = ''
    WEEK = 7
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    monthDate = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = b - 1

    for i in monthDate[0:a - 1]:
        date += i

    answer = day[date % WEEK]

    return answer