import sys

n = int(sys.stdin.readline().strip())
list1 = list(map(int,sys.stdin.readline().split()))
list1.sort()
n2 = int(sys.stdin.readline().strip())
list2 = list(map(int,sys.stdin.readline().split()))
#
#
# for i in list2:
#     if i in list1:
#         print('1')
#     else:
#         print('0')


def b_search(arr ,value):
    first , last = 0, len(arr)-1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            last = mid - 1
        else:
            first = mid + 1

for i in list2:
    result = b_search(list1, i)
    if result is None:
        print('0')
    else:
        print('1')