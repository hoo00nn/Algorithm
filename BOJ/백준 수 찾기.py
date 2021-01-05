from collections import Counter

def solution():
    N = int(input())
    N_List = input().split(' ')
    M = int(input())
    M_List = input().split(' ')
    result = []

    NM_List_Count = Counter(N_List + M_List)
    dup = list(map(lambda x : x[0], (filter(lambda x: x[1] > 1, NM_List_Count.items()))))

    for i in M_List:
        if i in dup:
            result.append(1)
        else:
            result.append(0)

    for i in result:
        print(i)

solution()
