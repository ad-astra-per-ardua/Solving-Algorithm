a = int(input())
temp = a

for i in range(2,a+1):
        while True:
            if temp % i != 0:
                break
            temp /= i
            print(i)