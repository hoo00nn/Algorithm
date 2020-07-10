# 순서 셀 때 생각 잘하자
# 예외 생각 잘하

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

# 효율적인 코드
# 좀 더 생각하면 충분히 할 수 있었는데,, 집중력 문제

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]