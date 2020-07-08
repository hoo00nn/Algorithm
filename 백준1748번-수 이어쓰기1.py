# int형으로 주어진 수의 자릿 수 구하는 방법을 알게 되었다.

def num_len(n):
    count = 0

    while n > 0:
        n = int(n/10)
        count += 1

    return count


n = int(input())
answer = 0
num_length = num_len(n)
answer += (n - 10**(num_length-1) + 1) * num_length
for i in range(num_length - 1, 0, -1):
    answer += (10**(i) - 10**(i-1)) * i

print(answer)
