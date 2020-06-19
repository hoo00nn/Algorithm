def solution(priorities, location):
    answer = 1
    copyList = []
    for i in range(0, len(priorities)):
        copyObj = dict()
        copyObj[i] = priorities[i]
        copyList.append(copyObj)

    while True:
        if list(copyList[0].values())[0] >= max(priorities):
            if list(copyList[0].keys())[0] == location:
                break
            else:
                priorities.remove(max(priorities))
                del copyList[0]
                answer += 1
        else:
            temp = copyList.pop(0)
            copyList.append(temp)
    return answer


solution([1, 1, 9, 1, 1, 1], 0)
