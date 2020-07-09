# 너무 쉬웠다 5분 컷.

def solution(s):
    answer = ''
    ret = list(map(int, s.split(' ')))
    answer = ' '.join(list(map(str, [min(ret), max(ret)])))
    return answer