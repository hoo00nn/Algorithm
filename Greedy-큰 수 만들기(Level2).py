def solution(number, k):
    answer = []
    for i in range(0, len(number)):
        answer.append(number[i])
        n = len(answer)

        if n < 2:
            continue
        else:
            while k > 0 and answer[-1] > answer[-2]:
                del answer[-2]
                k -= 1
                if len(answer) == 1:
                    break
    while k > 0:
        answer.remove(min(answer))
        k -= 1

    answer = ''.join(answer)
    return answer


solution("4177252841", 4)