import math,sys
input = sys.stdin.readline

dic = {}
loop = int(input())

for _ in range(loop):
    name, logged = input().split()
    dic[name] = logged
    if logged == 'leave':
        del dic[name]
temp = sorted(dic.items(),reverse=True)
dic2 = dict(temp)

for key in dic2.keys():
    print(key)