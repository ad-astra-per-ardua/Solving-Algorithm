T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    idx = S.rfind('a')
    if idx != -1 and S[idx:] > S[:idx]:
        print("Yes")
    else:
        print("No")
