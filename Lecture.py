import sys

input = sys.stdin.readline

loop = int(input())
paper = []
temp = []
overlap = []


for _ in range(loop):
    a, b = map(int, input().split())
    paper.append((a, b))
    for _ in range(1):
        paper.append((a + 10, b + 10))


for i in range(len(paper)):
    a, b = paper[i // 2 - 1]
    if


print(paper)
print(len(paper))
print(a,b)
