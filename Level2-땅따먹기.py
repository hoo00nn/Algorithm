# 처음 접해본 DP 문제.
# 어려웠다

def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            check = set(range(4)) - {j}
            land[i][j] += max(land[i - 1][k] for k in check)

    answer = max(land[-1])

    return answer