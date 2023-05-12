leng = int(input())

for i in range(leng):

    a, b = input().split()
    a = int(a)
    lists = list(b)
    for s in range(0,len(b)):
        print(lists[s] * a,end='')
    print()
