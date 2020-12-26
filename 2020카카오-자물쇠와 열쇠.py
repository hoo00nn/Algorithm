# 문제 해결 전략
# 키는 회전, 이동 모두 가능
# 완전탐색으로 풀기위해선 모든 경우의 수 계산
# 회전은 4가지 경우의 수 (0도, 90도, 180도 270도)
# lock 배열을 모두 순회하면서 각 자리마다 회전 4가지 경우의 수 추가
# lock 배열을 모두 순회 -> 이동 경우의 수 체크됨
# lock 배열의 각 자리에서 4가지 경우의 수 추가 -> 회전하는 경우의 수까지 체크됨
# 한 가지 문제 lock범위에서만 key가 유효! lock범위 밖에선 어떤 형태든 상관 X -> lock 배열을 확장한 배열을 만들자

# 문제 해결
# 1. rotate90 함수 구현 -> 90도 회전한 결과값 리턴하는 함수
# 2. getExpendList 함수 구현 -> 배열을 확장한 결과값 리턴
# 3. isUnlocked 함수 구현 -> 자물쇠가 풀리는지 체크하는 함수

import copy

def rotate90(M, key):
    rotate = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            rotate[j][M-1-i] = key[i][j]

    return rotate

def getExpendList(M, N, lock):
    expend = [[0] * (2 * (M-1) + N) for _ in range(2 * (M-1) + N)]

    for i in range(N):
        for j in range(N):
            expend[M-1+i][M-1+j] = lock[i][j]

    return expend


def isUnlocked(M, N, startX, startY, key, lock):

    for i in range(M):
        for j in range(M):
            lock[startX + i][startY + j] += key[i][j]

    for i in range(M-1, M-1+N):
        for j in range(M-1, M-1+N):
            if lock[i][j] != 1:
                return False

    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)
    expend = getExpendList(M, N, lock)

    for i in range(4):
        key = rotate90(M, key)

        for j in range(M - 1 + N):
            for k in range(M - 1 + N):
                copyExpend = copy.deepcopy(expend)
                print(copyExpend)

                if isUnlocked(M, N, j, k, key, copyExpend):
                    return True

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))

