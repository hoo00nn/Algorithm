# 절대값, 등차수열의 합을 이용하면 더 쉽게 구할 수 있었을 것 같다.
# abs 함수 생각하기

def solution(a, b):
    answer = 0
    if(a>b):
        temp=b
        b=a
        a=temp
    for i in range(a,b+1):
        answer+=i
    return answer