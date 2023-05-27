n = int(input())
if n == 1 or n == 3:
    print(-1)
    exit(0)
big = 5
small = 2
count = 0

if n >= 5:
    count += n // big
    n %= big
    if n % 2 == 0:
        count += n // small
    else:
        count -= 1
        n += big
        count += n // small
else:
    count += n // small
print(count)