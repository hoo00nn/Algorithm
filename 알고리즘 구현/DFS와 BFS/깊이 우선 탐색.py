def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += set(graph[n]) - set(visited)
            print(n)
    return visited


graph_list = {1: [2, 3, 4],
              2: [1, 4],
              3: [1, 4],
              4: [1, 2, 3]
              }
root_node = 1

dfs(graph_list, root_node)
