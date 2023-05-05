t=int(input())
for _ in range(t):
  n=int(input())
  s=input()
  a=set()
  b=set()
  for i in range(n):
    if i%2==0:
      a.add(s[i])
    else:b.add(s[i])
  if len(a.intersection(b))==0:print('YES')
  else:print('NO')
