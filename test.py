# 중복 제거 함수
def getSet(item):
    ret = []

    for i in item:
        if i not in ret:
            ret.append(i)

    return ret


# 차집합 함수
def getDiff(item, compareItem):
    ret = []

    for i in item:
        if i not in compareItem:
            ret.append(i)

    return ret


# 출발 지점에서 도착 지점까지 경로 구하는 함수
def bfs(graph, origin, dest):
    ret = []
    queue = [(origin, [origin])]

    while queue:
        item, path = queue.pop(0)

        if item == dest:
            ret.append(path)
        else:
            for i in getDiff(getSet(graph[item]),getSet(path)):
                queue.append((i, path+[i]))

    return ret


# 출발 지점부터 도착 지점까지 가중치 구하는 함수
def price(path, price_list):
    ret = []

    for i in path:
        price = 0

        for j in range(0, len(i)-1):
            price += price_list[i[j:j+2]]
        ret.append(price)

    return ret


# 경로 정렬 함수
def path_sorted(path):
    ret = []

    for i in path:
        ret.append(''.join(i))

    for i in range(0, len(ret)-1):
        for j in range(0, len(ret)-1-i):
            if ret[j] > ret[j+1]:
                temp = ret[j]
                ret[j] = ret[j+1]
                ret[j+1] = temp

    return ret


def  solution(origin, dest):
    answer = []
    graph_list = {'A': getSet(['B', 'C', 'F'])
                 ,'B': getSet(['D', 'E'])
                 ,'C': getSet(['D'])
                 ,'D': getSet(['K', 'G'])
                 ,'E': getSet(['H'])
                 ,'F': getSet(['G'])
                 ,'G': getSet(['H', 'J', 'I'])
                 ,'H': getSet(['K', 'J'])
                 ,'I': getSet(['J'])
                 ,'J': []
                 ,'K': []}

    price_list = {'AB': 1,'AC': 2,'AF': 4,'BD': 2,'BE': 1,'CD': 2,'DG': 1,
                 'DK': 2,'EH': 1,'FG': 3,'GH': 1,'GJ': 3,'GI': 2,'HK': 2,
                 'HJ': 1,'IJ': 2,}

    path = path_sorted(bfs(graph_list, origin, dest))
    # 갈 수 있는 경로가 없을 때
    if len(path) == 0: return [-1]
    # 출발지와 도착지가 같을 때
    elif origin == dest: return [0]

    answer = price(path, price_list)

    return answer
