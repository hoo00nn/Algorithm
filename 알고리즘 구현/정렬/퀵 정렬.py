# 시간복잡도는 O(NlogN), 하지만 정렬이 되어있는 경우 분할이 N만큼 일어나므로 O(n^2)이 된다.
# 최악의 경우 때문에 합병정렬보다 느리다고 생각할 수 있지만, 발생하기 쉽지 않은 경우이고,
# 일반적으로 퀵 정렬이 합병정렬보다 20% 빠르다고 한다.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

print(quick_sort([5,1,2,8,4,9]))