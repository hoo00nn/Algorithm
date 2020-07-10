# 2번 런타임 초과하고 완성
# 아직도 뭐가 차이가 있는지 모르겠다
# 시간복잡도 공부해야겠다

def solution(s):
    answer = s.split(' ')

    for i in range(0, len(answer)):
        answer[i] = answer[i].capitalize()

    return ' '.join(answer)

# 실패 케이스
# isalpha()로 한번 더 비교하는 연산 때문인가?

def solution(s):
    answer = s.split(' ')

    for i in range(0, len(answer)):
        if answer[i][0].isalpha():
            answer[i] = answer[i].title()

    return ' '.join(answer)

# 실패 케이스
# 이유를 모르겠다.

import string


def solution(s):
    answer = string.capwords(s)

    return answer


# 위에 실패이유를 알아냈다.
# capwords(s[, seq])로 정의 가능한데 처음에 구분자를 안넣어줘서 공백 한칸만 인식했다
# capwords(s, ' ') 넣어주니까 모든공백을 인식하여 통과

import string

def solution(s):
    answer = string.capwords(s, ' ')

    return answer