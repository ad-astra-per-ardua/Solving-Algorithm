
while True:
    appendix = []
    n = int(input())
    if n == -1:
        break
    for i in range(1,n):
        if n % i == 0:
            appendix.append(i)
    if sum(appendix) == n:
        print("{} =".format(n), end='')
        for i in range(len(appendix)):
            if i == len(appendix) - 1:
                print(" {}".format(appendix[i]))
            else:
                print(" {} +".format(appendix[i]), end='')
    else:
        print(f"{n} is NOT perfect.")