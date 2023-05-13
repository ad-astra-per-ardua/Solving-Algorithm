import sys,time

start_time = time.time()

a, b = map(int,sys.stdin.readline().split())
lists = []

for i in range(a, b+1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        lists.append(i)
if 1 in lists:
    lists.remove(1)
end_time = time.time()
for i in range(len(lists)):
    print(lists[i])
print(end_time - start_time)
