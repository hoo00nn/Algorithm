# 쉬운 문제. 소요 시간 20분

def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees:
        orderOfSkill = 0
        answer += 1
        for i in st:
            if skill[orderOfSkill] == i:
                orderOfSkill += 1
            elif i not in skill:
                continue
            else:
                answer -= 1
                break

            if len(skill) == orderOfSkill:
                break

    return answer