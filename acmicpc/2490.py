for i in range(3):
    res = []
    a,b,c,d = map(int,input().split())
    res += [a,b,c,d]
    res.sort()

    if res[0] == 1:
        print('E')
    elif res[0] == 0 and res[1] == 1:
        print('A')
    elif res[1] == 0 and res[2] == 1:
        print('B')
    elif res[2] == 0 and res[3] == 1:
        print('C')
    elif res[3] == 0:
        print('D')