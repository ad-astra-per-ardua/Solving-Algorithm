import sys
sys.setrecursionlimit(10**5)

search = dict()
search[10] = 3
def scanning(num):
    if num in search.keys():
        return search[num]
    if num == 1:
        return 0
    ans = scanning(num-1)+1
    if num % 3 == 0:
        ans = min(ans,scanning(num/3) + 1)
    if num % 2 == 0:
        ans = min(ans,scanning(num/2) + 1)
    search[num] = ans
    return ans

N = int(input())
for i in range(1,N):
    scanning(i)
print(scanning(N))