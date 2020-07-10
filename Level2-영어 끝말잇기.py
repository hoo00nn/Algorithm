# 순서 셀 때 생각 잘하자
# 예외 생각 잘하기

def solution(n, words):
    answer = [words[0]]
    check = 1
    count = 1

    for i in range(1, len(words)):
        check = (i + 1) % n
        if check == 1: count += 1
        if words[i][0] != answer[-1][-1] or words[i] in answer:
            if check == 0: return [n, count]
            return [check, count]
        answer.append(words[i])

    return [0, 0]