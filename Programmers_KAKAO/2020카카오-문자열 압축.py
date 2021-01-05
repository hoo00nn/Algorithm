# 생각보다 쉬웠다..
# 소요시간 40분정도 걸린 것 같다.

def getStringZip(n, s):
    count = 1
    zipChar = ''
    check = False
    for i in range(0, len(s), n):
        if s[i:i + n] == s[i + n:i + 2 * n]:
            count += 1
        else:
            if count == 1:
                zipChar += s[i:i + n]
            else:
                zipChar += str(count) + s[i:i + n]
                count = 1
    return len(zipChar)


def solution(s):
    answer = 0
    zipList = []

    for i in range(1, len(s) + 1):
        zipList.append(getStringZip(i, s))

    answer = min(zipList)

    return answer