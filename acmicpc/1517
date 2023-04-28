def merge(left, right):
    global cnt

    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            cnt += len(left) - i

    result += left[i:]
    result += right[j:]

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


n = int(input())
arr = list(map(int, input().split()))

cnt = 0
merge_sort(arr)

print(cnt)
