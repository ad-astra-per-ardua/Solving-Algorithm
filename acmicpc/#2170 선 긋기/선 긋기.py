import sys
input = sys.stdin.readline
loop = int(input())

line = []
final = []
fin_a = 0
fin_b = 0
for _ in range(loop):
    a,b = map(int,input().split())
    line.append((a,b))
line.sort()
comp_a, comp_b = line[0]
for i in range(1,len(line)):
    temp_a, temp_b = line[i]
    if comp_b >= temp_a:
        if comp_b < temp_b:
            comp_b = temp_b
        else:
            continue
    else:
        final.append([comp_a,comp_b])
        comp_a = temp_a
        comp_b = temp_b

final.append([comp_a,comp_b])
answer = 0
for i in final:
    answer += (max(i) - min(i))
print(answer)