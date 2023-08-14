import sys

n = int(input())
a = list(map(int,input().split()))
total_sum = sum(a)
a = [-1] + a + [-1]
for i in range(1, n+1):
    try:
        a[i]=int(input().rstrip())
        total_sum += a[i]
    except EOFError:
        break
I = [i for i in range(n+2) if a[i] != 1]

answer = n
k = len(I)-2
for l in range(1,k+1):
    multi, summation = 1,0
    for r in range(l,k+1):
        multi *=a[I[r]]
        summation+=a[I[r]]-1
        if multi > total_sum:
            break
        if l!=r:
            u=I[l]-I[l-1]-1
            v=I[r+1]-I[r]-1
            z=multi-(summation+I[r]-I[l]+1)
            if 0<=z<=u+v:
                answer+=min(z,u+v-z,u,v)+1
print(answer)