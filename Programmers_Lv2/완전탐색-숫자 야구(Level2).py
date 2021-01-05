from itertools import permutations


def solution(baseball):
    answer = 0
    permu = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    permu = list(map(''.join, permutations(permu, 3)))

    for i in permu:
        count = 0
        for j in baseball:
            n = list(str(j[0]))
            strike = 0
            ball = 0
            for k in range(0,3):
                if list(i)[k] == n[k]:
                    strike += 1
                elif list(i)[k] in n:
                    ball += 1
            if strike == j[1] and ball == j[2]:
                count += 1
                continue
            else:
                break
        if count == len(baseball):
            answer += 1
    return answer


solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])