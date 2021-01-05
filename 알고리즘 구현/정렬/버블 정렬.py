# 시간복잡도는 O(n^2)이 보장된다.
# 공간복잡도는 O(n)
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort([3,1,2,8,5,9]))