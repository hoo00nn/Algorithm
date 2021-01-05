def solution(clothes):
    answer = 1
    test = {}
    for i in dict(clothes).values():
        if i in test.keys():
            test[i] += 1
        else:
            test[i] = 1
    for i in test.keys():
        test[i] += 1
        answer *= test[i]
    return answer-1


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
