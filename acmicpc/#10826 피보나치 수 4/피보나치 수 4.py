import sys
input = sys.stdin.readline
count = 0
def dp(n):
    global count
    count += 1
    memory = [1,1]
    if n < 0:
        return 0
    elif n < 2:
        return memory[n]
    else:
        for i in range(2, n+1):
            memory.append(memory[i-1] + memory[i-2])
            count += 1
        return memory[n]
res = dp(int(input())-1)
print(res)
