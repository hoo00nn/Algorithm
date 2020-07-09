def solution(s):
    answer = []
    stack = []
    ret = []
    openBracket = 0
    closeBracket = 0
    s = s[1:-1]
    for i, item in enumerate(s):
        if item == '{':
            openBracket = i
            stack.append(item)
        elif item == '}':
            closeBracket = i
            stack.pop()

        if len(stack) == 0 and item != ',':
            ret.append(s[openBracket + 1:closeBracket].split(','))

    ret = sorted(ret, key=lambda x: len(x))

    for i in ret:
        for j in i:
            if j not in answer:
                answer.append(j)
    answer = list(map(int, answer))
    return answer