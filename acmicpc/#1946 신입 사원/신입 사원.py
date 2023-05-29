import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    loop = int(input())
    result = []
    for _ in range(loop):
        a, b = map(int, input().split())
        result.append((a,b))
    result.sort(key=lambda x:(x[0]))
    count = 1
    first_rank = result[0][1]
    for i in range(1, len(result)):
        if result[i][1] < first_rank:
            count += 1
            first_rank = result[i][1]
    print(count)