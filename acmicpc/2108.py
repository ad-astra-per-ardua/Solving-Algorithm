import statistics,sys
lists = []
loop = int(input())
for _ in range(loop):
    lists.append(int(sys.stdin.readline().strip()))

avg = int(round(sum(lists) / len(lists), 0))
if avg == -0:   # deal with -0
    avg = 0
modes = statistics.multimode(lists)
if len(modes) > 1:
    mode = sorted(modes)[1]
else:
    mode = modes[0]

print(avg)
print(statistics.median(lists))
print(mode)
print(max(lists) - min(lists))
