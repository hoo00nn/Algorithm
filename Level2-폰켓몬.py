# 첫 번째 시도 정확성 30.0 나머지 시간초과..

from itertools import combinations


def solution(nums):
    answer = list(map(lambda x: len(set(x)), combinations(nums, len(nums) // 2)))

    return max(answer)

# 두 번째 시도 정확성 80.0 나머지 시간초과..

from itertools import combinations


def solution(nums):
    if len(nums) // 2 >= len(set(nums)):
        return len(set(nums))

    answer = list(map(lambda x: len(set(x)), combinations(nums, len(nums) // 2)))

    return max(answer)

# 세 번째 시도 통과
# 조금만 생각해보면 되게 간단한 문제였는데,,
# 문제 잘 읽고 입출력 예시에서 힌트를 찾자!


def solution(nums):
    if len(nums) // 2 >= len(set(nums)):
        return len(set(nums))

    return len(nums) // 2