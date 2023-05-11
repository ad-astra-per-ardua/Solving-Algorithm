import math

a ,b = map(int, input().split())
Acol = (math.ceil(a / 4) * 4)
Bcol = (math.ceil(b / 4) * 4)
AnsCol = int(abs(Bcol - Acol) / 4)
temp = a + (AnsCol * 4)
AnsRow = ((b-a) % 10) % 4
if a % 4 == 0 and b % 4 == 1:
    AnsRow = 3
elif abs(a - b) == 3:
    AnsRow = 3
ans = AnsRow + AnsCol
print(AnsCol)
print(AnsRow)
print(ans)