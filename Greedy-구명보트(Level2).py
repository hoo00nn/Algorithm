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