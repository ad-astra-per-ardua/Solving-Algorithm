from collections import Counter
a = input()
a = a.lower()
temp = list(a)
temp.sort()
if len(temp) == 1:
    print((temp[0]).upper())
    exit()
counter = Counter(temp)
most = counter.most_common(2)
if most[0][1] == most[1][1]:
    print('?')
else:
    print((most[0][0]).upper())
