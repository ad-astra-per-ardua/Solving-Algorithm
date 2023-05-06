def difference(s: str) -> int:
    tg = "codeforces"
    return sum(1 for i in range(len(s)) if s[i] != tg[i])


a = int(input())
for _ in range(a):
    s = input().strip()
    result = difference(s)
    print(result)