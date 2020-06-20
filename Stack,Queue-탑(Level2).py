def solution(heights):
    answer = []
    for i in range(len(heights)-1, -1, -1):
        if i != 0:
            count = 0
            for j in range(i-1,-1, -1):
                if heights[i] < heights[j]:
                    answer.insert(0,j+1)
                    break
                else:
                    count += 1
            if count == i:
                answer.insert(0,0)
        else:
            answer.insert(0,0)
    return answer

solution([10, 8, 6, 9])