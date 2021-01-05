def solution(s):
    answer = True
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack) == 0:
            return False
        else:
            stack.pop()

    return len(stack) == 0