# filter() 리턴값이 참인 것만 묶어서 돌려준다
li = [-2, -3, 5, 6]

print(list(filter(lambda x: x > 0, li)))  # [5, 6]

# map(함수, iterable) 입력받은 자료형의 각 요소가 함수에 의해서 실행된 결과를 묶어서 map iterator객체로 반환
li = [1, 2, 3]

result = list(map(lambda x: x ** 2, li))  # [1, 4, 9]

# reduce(집계 함수(누적자, 현재값), iterator[, 초기값])
# reduce함수는 내장 함수가 아니기 때문에 import functools from reduce를 해줘야 한다.
from functools import reduce
result = reduce(lambda x,y: x+y, [1,2,3,4,5], 100) # (100+1)+2)+3)+4)+5 = 115

# gcd(num1, num2) 최대공약수 구하는 함수 from math import gcd 사용.
from math import gcd
print(gcd(8, 16))
# 최대공배수 x*y//gcd(x,y)
print(8*16//gcd(8,16))

# 순열, 조합, 곱집합을 제공 (import itertools)
from itertools import permutations
a = [1,2,3]
k = list(permutations(a, 2)) #[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import combinations
b = list(combinations(a, 2)) #[(1,2), (1, 3), (2, 3)]

from itertools import product
x = ['A', 'B', 'C']
c = list(product(a, x))

# zfill(개수) [현재 문자열 길이 - 개수] 만큼 0으로 채울 수 있음.
s = 'sh'
s = s.zfill(4)

# rjust(개수, 채울 문자) 채울 문자는 무조건 1글자이여야 한다.
z = 'kk'
z = z.rjust(4, 'a')

