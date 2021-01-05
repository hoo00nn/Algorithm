# 시간복잡도는 O(NlogN)
# 공간복잡도는 O(2N)
def merge_sort(arr):
즘    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[h])
            h += 1
    merged_arr += left[l:]
    merged_arr += right[h:]

    return merged_arr

print(merge_sort([2,3,7,5,9,1]))