import sys
input = sys.stdin.readline

loop = int(input().rstrip())

for _ in range(loop):
    sequence = [1,1,1]
    case = int(input().rstrip())
    if case < 4:
        print(1)
    i = 0

    while i < case-1:
        sequence.append(sequence[i] + sequence[i+1])
        i += 1
        if i + 3 == case:
            print(sequence.pop())
            break