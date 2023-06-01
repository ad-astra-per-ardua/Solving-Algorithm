import math,sys
input = sys.stdin.readline


def eratosthenes(n):
    lists = [True] * n
    for i in range(2, int(math.sqrt(n)) + 1):
        if lists[i]:
            for j in range(i+i, n, i):
                lists[j] = False
    return lists


max_num = 10000
prime_list = eratosthenes(max_num + 1)

for _ in range(int(input())):
    num = int(input())
    a, b = num//2, num//2
    while a > 0:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1