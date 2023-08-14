import math,sys
input = sys.stdin.readline

def count_perms(nums, k):
    n = len(nums)
    mod_values = [int(num) % k for num in nums]
    lengths = [len(num) for num in nums]
    dp = [[0 for _ in range(k)] for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][mod_values[i]] = 1

    for mask in range(1 << n):
        for mod in range(k):
            for j in range(n):
                if not (mask & (1 << j)):
                    new_mod = (mod * pow(10, lengths[j], k) + mod_values[j]) % k
                    dp[mask | (1 << j)][new_mod] += dp[mask][mod]

    return dp[(1 << n) - 1][0]


n = int(input())
nums = [input().strip() for _ in range(n)]
k = int(input())

total_perms = math.factorial(n)
valid_perms = count_perms(nums, k)

gcd_value = math.gcd(valid_perms, total_perms)
print("{}/{}".format(valid_perms // gcd_value, total_perms // gcd_value))
