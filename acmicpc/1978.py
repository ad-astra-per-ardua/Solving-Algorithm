def prime_num(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

b = int(input())
a = list(map(int, input().split()))

prime_count = 0
for num in a:
    if prime_num(num):
        prime_count += 1

print(prime_count)
