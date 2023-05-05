while True:
    a = list(input())
    if a == ['0']:
        break;
    ans = list(reversed(a))
    if a == ans:
        print("yes")
    else:
        print("no")
