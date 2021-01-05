# 이미 정렬되어 있는 경우는 한 번씩 밖에 비교를 하지 않아 시간복잡도는 O(n)
# Big-O는 최악의 경우를 나타내므로 시간복잡도는 O(n^2)
# 하나의 배열로 정렬을 하므로 공간복잡도는 O(n)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        N = i
        idx = i - 1

        while idx >= 0:
            if arr[idx] > arr[N]:
                arr[N], arr[idx] = arr[idx], arr[N]
                N = idx
                idx -= 1
            else:
                break

    return arr


print(insertion_sort([4, 2, 1, 6, 5, 7]))
