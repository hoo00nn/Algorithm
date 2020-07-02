def solution(numbers):
    answer = ''
    if max(numbers) == 0:
        return '0'
    else:
        isSorted = list(map(str, numbers))
        isSorted.sort(key=lambda x: x * 4, reverse=True)
        answer = ''.join(isSorted)
    return answer
