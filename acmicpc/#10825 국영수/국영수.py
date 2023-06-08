import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    students.append(sys.stdin.readline().split())

students.sort(key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in students:
    print(i[0])