def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first_count = 0
    second_count = 0
    third_count = 0

    for i in range(0, len(answers)):
        if first[i % len(first)] == answers[i]:
            first_count += 1
        if second[i % len(second)] == answers[i]:
            second_count += 1
        if third[i % len(third)] == answers[i]:
            third_count += 1

    result = [first_count, second_count, third_count]

    for i in range(0, len(result)):
        if result[i] == max(result):
            answer.append(i + 1)

    return answer


# 다른 사람 풀이를 보고 좀 더 깔끔하게 코드 구성을 할 수 있었다.
# enumerate 사용
# idx 와 해당하는 값을 모두 사용해야 할 경우 enumerate!!

def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0, 0, 0]

    for idx, item in enumerate(answers):
        if item == first[idx % len(first)]:
            result[0] += 1
        if item == second[idx % len(second)]:
            result[1] += 1
        if item == third[idx % len(third)]:
            result[2] += 1

    for idx, item in enumerate(result):
        if max(result) == item:
            answer.append(idx + 1)

    return answer
