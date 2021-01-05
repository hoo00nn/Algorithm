# 제곱근 함수 사용하기 위해 math 라이브러리 추가
import math

# 특정 숫자가 소수 인지 판별하는 함수 구현, 제곱근 까지만 판단하면 됨
def isPrimeOne(num):
    end = int(math.sqrt(num))

    for i in range(2, end):
        if num % i == 0: return False

    return True

# 특정 정수 범위의 소수 개수 구하기 (에라토스테네스의 체 이용)
def getPrimeNum(num):
    check = [False, False] + [True for i in range(num - 1)] # 0과 1을 제외하고 num-1만큼 나머지를 True로 변경
    end = math.ceil(math.sqrt(num)) # 소수구할 때 제곱근까지만 비교하면 됨

    for i in range(2, end):
        if check[i]:
            for j in range(i*2, num+1, i): # i가 True이면 i를 제외한 i의 배수들을 False로 변경
                check[j] = False

    return check.count(True)




