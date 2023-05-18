from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
mat_A = deque()
mat_B = deque()
sum_c = deque()

for _ in range(a):
    mat_A.append(list(map(int, input().split())))

for _ in range(a):
    mat_B.append(list(map(int, input().split())))

for i in range(a):
    temp = deque()
    for j in range(b):
        temp.append(mat_A[i][j] + mat_B[i][j])
    sum_c.append(temp)

for row in sum_c:
    print(' '.join(map(str, row)))
