n, k  = map(int, input().split())
multi = []
 
for i in range(1, k+1):
    multi.append(int(str(n * i)[::-1]))
 
print(max(multi))