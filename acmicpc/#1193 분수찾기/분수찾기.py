line = int(input())
i = 1
while True:
    line -= i
    if line <= 0:
        break
    i += 1

appendix = []
for e in range(1,i+1):
    res = e,'/',i+1-e
    appendix.append(res)
if i % 2 == 1:
    appendix.reverse()
ans = appendix[line-1]
print("".join(map(str,ans)))