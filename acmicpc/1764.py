from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

hear = set() # 듣도 못한 사람
see = set() # 보도 못한 사람
for _ in range(N):
    hear.add(input().rstrip())
for _ in range(M):
    see.add(input().rstrip())

result = sorted(list(hear & see)) # 교집합 구하기
print(len(result))
for name in result:
    print(name)
