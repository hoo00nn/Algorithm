# N부터 N-1, N-2 ... 1까지 모두 탐색하므로 시간 복잡도는 O(n^2)
# 하나의 배열에서 정렬하기 때문에 공간 복잡도는 O(n)
def selection_sort(arr):
    for i in range(len(arr)):
        N = i

        for j in range(i, len(arr)):
            if arr[N] > arr[j]:
                N = j

        arr[i], arr[N] = arr[N], arr[i]

    return arr


print(selection_sort([3,6,2,1,8,5]))
