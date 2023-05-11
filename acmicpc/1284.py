while True:
    a = list(map(int, str(input())))
    if a[0] == 0:
        break
    l = len(a)
    ans = 0
    for i in range(l):
        if a[i] == 1:
            ans += 2
        elif a[i] == 0:
            ans += 4
        else:
            ans += 3
    print(ans + (l + 1))
