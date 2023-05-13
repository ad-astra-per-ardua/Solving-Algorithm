loop = int(input())
lists = []
list2 = []

for _ in range(loop):
    lists.append(input())

length = 1
lists = sorted(set(lists))
list3 = lists.copy()

while list3:
    for i in list3[:]:
        if len(i) == length:
            list2.append(i)
            list3.remove(i)
    length =+ 1