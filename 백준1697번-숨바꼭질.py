from collections import deque

def dfs(n,k,visited):
    dq = deque()
    dq.append(n)

    while dq:
        item = dq.popleft()

        if item == k: return visited[item]

        for i in (item+1, item-1, item*2):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[item] + 1
                dq.append(i)

n,k = map(int, input().split())
visited = [0 for i in range(100001)]

print(dfs(n,k,visited))

