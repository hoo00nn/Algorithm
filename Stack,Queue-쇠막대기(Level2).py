def solution(arrangement):
    answer = 0
    arrangement = arrangement.replace("()", "L")
    openBracket = []
    for i in arrangement:
        if i == "(":
            openBracket.append(i)
            answer += 1
        elif i == ")":
            openBracket.pop()
        else:
            answer += len(openBracket)

    return answer
