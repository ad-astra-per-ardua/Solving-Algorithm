import sys
input=sys.stdin.readline
mod = 1000000007
def solve(A):
    if len(A) <= 1:
        return (0, A)

    countl, L = solve(A[:len(A) // 2])
    countr, R = solve(A[len(A) // 2:])

    cnt = (countl + countr) % mod
    rzs = Lit = Rit = 0
    ret = []

    while Lit != len(L) or Rit != len(R):
        if Lit == len(L):
            fromL = False
        elif Rit == len(R):
            fromL = True
        else:
            fromL = L[Lit][0] <= R[Rit][0]

        if fromL:
            if not ret or ret[-1][0] != L[Lit][0]:
                ret.append((L[Lit][0], 0))
            cnt = (cnt + rzs * L[Lit][1]) % mod
            ret[-1] = (ret[-1][0], (ret[-1][1] + L[Lit][1]) % mod)
            Lit += 1
        else:
            if not ret or ret[-1][0] != R[Rit][0]:
                ret.append((R[Rit][0], 0))
            rzs = (rzs + R[Rit][1]) % mod
            ret[-1] = (ret[-1][0], (ret[-1][1] + R[Rit][1]) % mod)
            Rit += 1
    return (cnt, ret)

def main():
    M = int(input())
    ans = 0
    A = []
    for _ in range(M):
        K, N = map(int, input().split())
        *B, = map(lambda b: (int(b), 1), input().split())

        count, sortedb = solve(B)
        rep_count = N * (N - 1) // 2
        for b, c in sortedb:
            rep_count -= c * (c - 1) // 2
        ans = (ans + K * count + K * (K - 1) // 2 * rep_count) % mod

        for b, c in sortedb:
            A.append((b, c * K % mod))

    ans = (ans + solve(A)[0]) % mod
    print(ans)

if __name__ == "__main__":
    main()