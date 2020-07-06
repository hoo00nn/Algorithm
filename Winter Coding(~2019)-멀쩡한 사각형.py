# 격자점을 통해 구하는 방법을 생각하기 어려웠다..
# 결국 격자점 개수 구하는 방법 구글링해서 풀었다..

def getGcf(n, k):
    if n % k == 0:
        return k
    else:
        return getGcf(k, n % k)


def solution(w, h):
    answer = 1
    if w <= h:
        temp = w
        w = h
        h = temp

    GCF = getGcf(w, h)

    if GCF == 1:
        answer = (w * h) - (w + h - 1)
    else:
        answer = (w * h) - (w + h - GCF)

    return answer