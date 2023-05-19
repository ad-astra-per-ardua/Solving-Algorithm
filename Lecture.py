a,b = map(int, input().split())

temp1 = int(str(a),2)
temp2 = int(str(b),2)

ans_temp = temp1 + temp2
if bin(ans_temp)[2] == 0:
    ans = bin(ans_temp)[3:]
else:
    ans = bin(ans_temp)[2:]

print(ans)