# 최적화X 그냥 냅다때려박은버전
n, m, k = map(int,input().split())
if m < k:
    exit()
num_list = tuple(map(int,input().split()))
temp_num = list(num_list)
summation = 0
attempt = 0
def sum_tool(*arg):
    for _ in range(k):
        global summation
        global attempt
        summation += max(temp_num)
        attempt += 1
        if attempt == m:
            break
    return arg

while attempt < m:
    sum_tool(temp_num)
    a = temp_num.index(max(temp_num))
    max1 = temp_num.pop(a)
    summation += max(temp_num)
    attempt += 1
    if attempt == m:
        break
    temp_num.append(max1)
print(summation)

