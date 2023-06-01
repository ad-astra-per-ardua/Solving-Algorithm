a = int(input())
b = int(input())
c = int(input())

multiple = a * b * c
list_multiple = list(str(multiple))
for i in range(10):
    print(list_multiple.count(str(i)))