# 중간에 중복되는 문자열 제거하고 이어 붙인다..
# 제거하고 다시 처음부터 반복문 돌면 효율성면에서 안좋다
# 제일 밑에서부터 쌓이면 중간에 제거되도 알아서 이어 붙여진다. --> STACK 개념 생각
def ck_str(s, stack):
    if len(stack) == 0:
        stack.append(s)
    elif stack[-1] == s:
        stack.pop()
    else:
        stack.append(s)


def solution(s):
    stack = []

    for i in s:
        ck_str(i, stack)

    return len(stack) == 0

# 재귀 이용한 방법보다 조금 더 빠른 방법

def solution(s):
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return len(stack) == 0