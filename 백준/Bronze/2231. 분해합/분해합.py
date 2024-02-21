ans = int(input())

for i in range(1, ans+1):
    decom = i + sum(map(int,str(i)))
    if decom == ans:
        print(i)
        break
    if i == ans:
        print(0)
