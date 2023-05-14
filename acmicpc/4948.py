import math

maximum = 123456 * 2
prime = [False, False] + [True] * (maximum - 1)
for i in range(2, int(math.sqrt(maximum)) + 1):
    if prime[i]:
        for j in range(2*i, maximum+1, i):
            prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    print(sum(prime[n+1:2*n+1]))