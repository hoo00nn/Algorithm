from collections import deque


def bfs(graph, root):
    visited = []
    dq = deque([root])


    while len(dq) > 0:
        item = dq.popleft()

        if item not in visited:
                visited.append(item)
                dq += set(graph[item]) - set(visited)
                print(item)

    return visited



graph_list = {1: [3, 4],
              2: [3, 4, 5],
              3: [1, 5],
              4: [1],
              5: [2, 6],
              6: [3, 5]}
root_node = 1

bfs(graph_list, root_node)
