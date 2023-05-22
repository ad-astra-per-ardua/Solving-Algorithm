import sys
input = sys.stdin.readline
grade_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
a = []
b = []
for _ in range(20):
    trash, a_val, b_val = input().split()
    if b_val == 'P':
        continue
    a.append(float(a_val))
    b.append(b_val)
temp = []
for i in range(len(a)):
    temp2 = a[i] * grade_dict[b[i]]
    temp.append(temp2)
fin_sum = sum(temp)
avg_for = sum(a)
ans = round(fin_sum / avg_for,6)

print(f"{ans:.6f}")