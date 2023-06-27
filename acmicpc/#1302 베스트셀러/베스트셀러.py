import statistics,sys
input = sys.stdin.readline

loop = int(input())
lists = []
for _ in range(loop):
    element = input()
    lists.append(element)
lists = sorted(lists)
lists = statistics.mode(lists)
print(lists)
