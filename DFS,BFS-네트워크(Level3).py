from collections import deque


def bfs__search(n, visited, i, computers):
    dq = deque()
    dq.append(i)

    while len(dq) > 0:
        item = dq.pop()
        visited[item] = True

        for j, k in enumerate(computers[item]):
            if k == 1 and visited[j] == False:
                dq.append(j)


def solution(n, computers):
    answer = 0
    visited = [False for k in range(n)]

    for i in range(n):
        if not visited[i]:
            bfs__search(n, visited, i, computers)
            answer += 1

    return answer


solution(4, [[1, 0, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1]])