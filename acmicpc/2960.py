from collections import deque
a,b = map(int,input().split())
temp = deque([])
array = [True for i in range(a + 1)]

for i in range(2, a+1):
    if array[i] == True:
        j = 2
        temp.append(i)
        while i * j <= a:
            array[i * j] = False
            if i * j not in temp:
                temp.append(i * j)
            j += 1

ans = list(temp)
print(ans[b-1])
