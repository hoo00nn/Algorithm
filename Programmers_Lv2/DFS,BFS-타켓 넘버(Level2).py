# 두 개 이상 리스트의 모든 조합 구하기
# product(*listName) --> * 붙이는 거 잊지 말자.

from itertools import product

def solution(numbers, target):
    answer = 0
    noc = [[x, -x] for x in numbers]
    noc = list(map(sum, product(*noc)))
    answer = noc.count(target)
    return answer