a = int(input())
sum = 0
i = 1
if a == 1:
    print('1')
else:
    while True:
        sum += i

        if sum >= a:
            break
        i += 1

    if sum == a:
        print(i)
    elif sum >= a:
        print(i-1)
