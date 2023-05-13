list1 = []
list2 = []
loop = int(input())
for i in range(loop):
    vote = int(input())
    if vote == 1:
        list1.append(vote)
    elif vote == 0:
        list2.append(vote)
if len(list1) < len(list2):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')