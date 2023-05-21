import sys
from collections import deque
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
score = deque()
grade = deque()

for _ in range(20):
    a = input().split()
    score.append(float(a[1]))
    grade.append(a[2])
temp = deque()
for i in range(len(grade)):
    if grade[i] == 'P':
        temp.append(i)

grade_point_notP = deque()
score_point_notP = deque()
for e in range(len(score)):
    if e not in temp:
        grade_point_notP.append(grade[e])
        score_point_notP.append(score[e])

tot_grade = deque()
for j in range(len(grade_point_notP)):
    tot_grade.append(grade_dict[grade_point_notP[j]] * score_point_notP[j])

total_fin_grade = sum(tot_grade)
dis = sum(score_point_notP)

ans = total_fin_grade / dis

print(f"{round(ans,6):.6f}")