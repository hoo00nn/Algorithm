# 3시간 고민 후 https://gurumee92.tistory.com/172 참조


def solution(stock, dates, supplies, k):
    import heapq as hp

    pq = []
    answer = 0
    idx = 0

    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            hp.heappush(pq, -supplies[i])
            idx = i + 1

        stock += -hp.heappop(pq)
        answer += 1

    return answer
