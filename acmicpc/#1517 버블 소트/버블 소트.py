import sys
input = sys.stdin.readline
def merge_sort(arr, start, end, temp):
    if start >= end:
        return 0
    mid = (start + end) // 2
    cnt = merge_sort(arr, start, mid, temp) + merge_sort(arr, mid + 1, end, temp)

    i, j, k = start, mid + 1, start
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            cnt += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= end:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(start, end + 1):
        arr[i] = temp[i]

    return cnt


n = int(input())
arr = list(map(int, input().split()))
temp = [0] * n
print(merge_sort(arr, 0, n - 1, temp))
