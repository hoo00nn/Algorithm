# 2시간 삽질하다 결국 검색,,
# 간단한 문제 왜 이렇게 복잡하게 생각한거지?

def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(0, len(A)):
        answer += A[i] * B[i]

    return answer