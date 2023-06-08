from collections import deque
import sys,itertools
input = sys.stdin.readline

k = int(input().rstrip())
student = []
for j in range(1,k+1):
    student = list(map(int,input().split()))
    student = student[1:]
    s_student = sorted(student)
    lg = 0
    for i in range(0,len(s_student)-1):
        if s_student[i+1] - s_student[i]>lg:
            lg = s_student[i+1] - s_student[i]
    print(f'Class {j}')
    print(f'Max {max(s_student)}, Min {min(s_student)}, Largest gap {lg}')