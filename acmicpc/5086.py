while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
    if max(a,b) % min(a,b) == 0 and a < b:
        print('factor')
    elif max(a,b) % min(a,b) == 0 and a > b:
        print('multiple')
    else:
        print('neither')