loop = int(input())
paper = []
temp = []
overlap = []

for _ in range(loop):
    a, b = map(int, input().split())
    paper.append((a, b))
    paper.append((a + 10, b + 10))

for i in range(1,len(paper),2):
        a, b = paper[i-1]
        c, d = paper[i]
        for e in range(a, c):
            for j in range(b,d):
                overlap.append((e,j))
area = set(overlap)
print(len(area))