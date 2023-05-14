from collections import deque
import sys,time

n = int(sys.stdin.readline().strip())
start_time = time.time()
lists = deque()
for i in range(1, n+1):
    lists.append(i)

while len(lists) > 1:
    lists.remove(lists[0])
    lists.append(lists.popleft())
print(lists[0])
end_time = time.time() # 측정 종료
print((end_time - start_time)*1000,"ms")
print((end_time - start_time),"sec")