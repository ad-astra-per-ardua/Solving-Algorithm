import heapq as h
N=int(input());Q=[];A=list(map(int,input().split()));mx=max(A);[h.heappush(Q,a) for a in A];curmx=mx;ans=curmx-Q[0]
while Q[0]<mx:
    v=h.heappop(Q);ans=min(ans,curmx-v);curmx=max(curmx,2*v);h.heappush(Q,2*v)
print(min(ans,curmx-Q[0]))
