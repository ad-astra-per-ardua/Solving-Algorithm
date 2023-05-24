import sys
input = sys.stdin.readline

m = int(input().rstrip())
n = int(input().rstrip())


prime = []
for i in range(m,n+1):
    if i == 1:
        continue
    else:
        for e in range(2, int(i ** 0.5) + 1):
            if i % e == 0:
                break
        else:
            prime.append(i)

if len(prime) <= 0:
    print('-1')
else:
    print(sum(prime))
    print(min(prime))