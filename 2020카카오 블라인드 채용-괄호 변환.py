# 천천히 생각하면 풀 수 있었던 문제.
# 머리로 디버깅하는걸 연습해야겠다.

def checkBracket(n):
    stack = []

    for i in n:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack) == 0:
            return False
        else:
            stack.pop()

    return len(stack) == 0


def getBracket(k):
    openBracket = 0
    closeBracket = 0
    u = ''
    v = ''

    if len(k) == 0:
        return ''
    else:
        for i in k:
            if i == '(':
                openBracket += 1
            else:
                closeBracket += 1

            if openBracket == closeBracket:
                u = k[0:openBracket + closeBracket]
                v = k[openBracket + closeBracket:]
                break

        if checkBracket(u):
            u += getBracket(v)
            return u
        else:
            s = ''
            s += '('
            s += getBracket(v)
            s += ')'
            u = list(u[1:-1])
            for i in range(0, len(u)):
                if u[i] == '(':
                    u[i] = ')'
                else:
                    u[i] = '('
            u = ''.join(u)
            s += u
            return s


def solution(p):
    if checkBracket(p):
        return p
    else:
        return getBracket(p)
