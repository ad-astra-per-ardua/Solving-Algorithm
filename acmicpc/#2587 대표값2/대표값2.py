import statistics,sys
input = sys.stdin.readline
temp = []
for _ in range(5):
    a = int(input())
    temp.append(a)
temp.sort()
print(sum(temp)//len(temp))
print(statistics.median(temp))