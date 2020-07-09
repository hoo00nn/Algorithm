# lstrip, rstrip, split 함수 사용 했으면 훨씬 간결했다
# 문자열 함수 자주 사용해보기
# 간결하게 수정한 코드


def solution(s):
    answer = []
    ret = []
    s = sorted(s.lstrip('{').rstrip('}').split('},{'), key=lambda x: len(x))

    for i in s:
        answer.append(i.split(','))

    for i in answer:
        for j in i:
            if int(j) not in ret:
                ret.append(int(j))

    return ret


# 밑에서부턴 처음 내가 짠 코

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