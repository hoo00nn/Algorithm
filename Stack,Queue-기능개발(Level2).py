import math


def solution(progresses, speeds):
    answer = []
    doneWorked = dict()
    curWorked = 0
    count = 1

    for i in range(0, len(progresses)):
        doneWorked[i] = math.ceil((100 - progresses[i]) / speeds[i])

    while curWorked <= len(progresses) - 1:
        if curWorked + count == len(progresses):
            answer.append(count)
            break
        else:
            if doneWorked[curWorked] >= doneWorked[curWorked + count]:
                count += 1
            else:
                answer.append(count)
                curWorked += count
                count = 1

    return answer


solution([93, 30, 55], [1, 30, 5])
