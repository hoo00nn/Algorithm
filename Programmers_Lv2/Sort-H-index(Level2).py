# 1시간30분 삽질하고 구글링하여 참고...

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


solution([10,9,4,1,1])