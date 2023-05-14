n,k = map(int,input().split())


bt_n = 1
bt_k = 1
third = 1
for i in range(1,n+1):
    bt_n *= i
for e in range(1,k+1):
    bt_k *= e
for f in range(1,n-k+1):
    third *= f
ans = bt_n /(bt_k * third)
print(int(ans))