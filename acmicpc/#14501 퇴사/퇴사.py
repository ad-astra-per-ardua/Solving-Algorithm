import sys
input = sys.stdin.readline
n = int(input())
reserve = []
for _ in range(n):
    a, b = map(int,input().split())
    reserve.append((a,b))

max_income = [0] * (n + 1)  # 각 날짜까지의 최대 이익을 저장할 리스트

for i in range(n):
    if i + reserve[i][0] <= n:  # 상담이 끝나는 날이 퇴사일 이후가 아니라면
        # 이 날에 상담을 받는 경우와 받지 않는 경우 중 이익이 더 큰 경우를 선택
        max_income[i + reserve[i][0]] = max(max_income[i + reserve[i][0]], max_income[i] + reserve[i][1])
    # 이 날에 상담을 받지 않는 경우를 고려하여, 다음날의 최대 이익을 업데이트
    if i + 1 <= n:
        max_income[i + 1] = max(max_income[i + 1], max_income[i])

print(max(max_income))
