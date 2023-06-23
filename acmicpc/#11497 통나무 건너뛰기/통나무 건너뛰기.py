import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    m = int(input())
    array = sorted(list(map(int,input().split())))
    max = 0
    for j in range(2,len(array)):
        if array[j] - array[j-2] > max:
            max = array[j] - array[j-2]
    print(max)