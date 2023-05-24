a = int(input())
start = 2
base = 2
for i in range(0,a):
    ans = start + (base ** i)
    start += (base ** i)
print(ans**2)