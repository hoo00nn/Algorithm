# pop() 사용해서 문제를 풀어보니 효율성에서 한 문제가 실패했다.
# pop() 사용하지 않고 인덱스를 직접 조종해서 풀었다.


def solution(people, limit):
    answer = 0
    people.sort()

    while len(people) > 0:
        check = people.pop()

        if len(people) == 0:
            answer += 1
            return answer

        while check + people[0] <= limit:
            check += people.pop(0)

            if len(people) == 0:
                answer += 1
                return answer

        answer += 1

    return answer

# 최종 코

def solution(people, limit):
    answer = 0
    start = 0
    end = len(people) - 1
    people.sort()

    while start <= end:
        if people[start] + people[end] <= limit:
            answer += 1
            start += 1
            end -= 1
            continue
        end -= 1
        answer += 1

    return answer