def solution(brown, yellow):
    answer = []
    start = int(brown / 2 - 1)
    end = 0
    for i in range(start, end, -1):
        hor = i * 2
        ver = (brown - hor) / 2
        if yellow / ver + 2 == i and i >= ver + 2:
            answer.append(i)
            answer.append(ver + 2)
            return answer
    return answer


solution(24, 24)
