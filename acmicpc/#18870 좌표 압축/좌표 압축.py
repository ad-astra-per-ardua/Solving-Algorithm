import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
sorted_array = sorted(list(set(array)))

dict = {sorted_array[i] : i for i in range(len(sorted_array))}

for i in array:
    print(dict[i], end=' ')
