import sys
input = sys.stdin.readline
loop = int(input())
expect = []
actual = []
count = 0
for i in range(1,loop+1):
    a = int(input())
    expect.append(a)
    actual.append(i)
expect.sort()
for e in range(len(expect)):
    count += abs(expect[e] - actual[e])
print(count)
