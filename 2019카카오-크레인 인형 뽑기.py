# 주어진 리스트가 세로를 의미하는 줄 알고 접근했다가 2시간 삽질..
# 가로를 의미하고 있었다,, 문제에 명시 해줬으면 쉽게 풀었을텐데

def solution(board, moves):
    answer = 0
    bucket = []

    while len(moves) > 0:
        k = moves.pop(0) - 1

        for i in range(0, len(board)):
            if board[i][k] == 0:
                continue
            else:
                bucket.append(board[i][k])
                board[i][k] = 0
                break

        if len(bucket) > 1:
            if bucket[-1] == bucket[-2]:
                bucket = bucket[0:-2]
                answer += 2

    return answer


solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])
