def count_subsequences():
    MOD = 1000000007

    t = int(input())

    results = []

    for _ in range(t):
        n, k = map(int, input().split())

        a = list(map(int, input().split()))

        freq = [0] * 64
        for num in a:
            freq[num] += 1

        dp = [[0] * 64 for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(64):
                dp[i][j] = (dp[i - 1][j] * (1 + freq[j])) % MOD

        ans = sum(dp[i][k] for i in range(1, n + 1)) % MOD
        results.append(ans)

    for res in results:
        print(res)

count_subsequences()
