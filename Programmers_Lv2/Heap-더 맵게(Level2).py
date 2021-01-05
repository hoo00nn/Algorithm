import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while (True):
        if scoville[0] < K:
            if len(scoville) == 1:
                return -1
            else:
                heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
                answer += 1
        else:
            break
    return answer


