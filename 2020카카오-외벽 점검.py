# 완전 탐색 문제
# circle을 선형으로 생각하면 방향 문제(시계? 반시계?)는 해결할 수 있다.
# 선형으로 변경 방법 각 취약점에 원 둘레를 더해준다. ex) [1, 5, 6, 10] -> [1, 5, 6, 10, 13, 17, 18, 22]
# 취약점 개수를 두 배로 늘리면 취약점 비교 범위를 어떻게 잡아야할까? -> 오름차순으로 정렬되어 있기 때문에 기존의 취약점 기준을 시작점으로 검사.
# 즉, 1, 5, 6, 10을 시작점으로하여 기존의 취약점 개수(4개)만큼 검사를 하면된다.
# 위의 문장을 표현하면 [1, 5, 6, 10], [5, 6, 10, 13], [6, 10, 13, 17], [10, 13, 17, 18]으로 모든 취약점을 방향 문제없이 체크가능.
# 문제의 핵심은 투입되는 친구의 이동거리 배열(dist)는 정렬되어 있다는 문장이 없다. -> 조합을 이용해 모든 경우의 수를 체크
# 파이썬에서 조합은 itertools의 permutations를 이용해 구할 수 있다.
from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    weakLength = len(weak)
    weak.extend([i + n for i in weak])

    for i in range(weakLength):
        compare = weak[i:i + weakLength]
        friends = permutations(dist)

        for friend in friends:
            friendIdx, friendCount = 0, 1
            possibleDist = compare[0] + friend[friendIdx]

            for k in range(weakLength):
                if possibleDist < compare[k]:
                    friendCount += 1

                    if friendCount > len(dist):
                        break

                    friendIdx += 1
                    possibleDist = friend[friendIdx] + compare[k]

            answer = min(answer, friendCount)

    return -1 if answer > len(dist) else answer


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])

