def getSet(arr):
    visited = []
    compareNum = arr[0]

    for i in arr:
        if i == compareNum:
            continue
        else:
            visited.append(compareNum)
            compareNum = i

    visited.append(compareNum)

    return visited


def solution(arr):
    answer = getSet(arr)

    return answer