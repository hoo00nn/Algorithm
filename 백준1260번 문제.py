from collections import deque


def dfs(graph, root):
    visited = []
    stack = [root]

    while len(stack) > 0:
        item = stack.pop()

        if item not in visited:
            visited.append(item)
            sortList = list(set(graph[item]) - set(visited))
            stack += sorted(sortList, reverse=True)

    return visited


def bfs(graph, root):
    visited = []
    dq = deque([root])

    while len(dq) > 0:
        item = dq.popleft()

        if item not in visited:
            visited.append(item)
            sortList = list(set(graph[item]) - set(visited))
            sorted(sortList)
            dq += sortList
    return visited


n, m, v = list(map(int, input().split()))
graph_list = dict()

for i in range(m):
    link = list(map(int, input().split()))
    if link[0] in graph_list:
        graph_list[link[0]].append(link[1])
    else:
        graph_list[link[0]] = [link[1]]

    if link[1] in graph_list:
        graph_list[link[1]].append(link[0])
    else:
        graph_list[link[1]] = [link[0]]

print(' '.join(str(i) for i in dfs(graph_list, v)))
print(' '.join(str(i) for i in bfs(graph_list, v)))

