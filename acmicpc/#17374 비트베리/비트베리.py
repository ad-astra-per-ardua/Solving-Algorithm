import sys
input = sys.stdin.readline

loop = int(input())
for _ in range(loop):
    p, q, a, b, c, d = map(int, input().split())
# In Pekaz's p = bit, q = berry
# In Vincent's a = bit, b = coin, c = berry , d = coin
    coin = (q // c) * d     # Convert berry to coin
    p += (coin // b) * a    # Convert coin to bit
    coin %= b               # Remaining coin after converted to bits

    x = (p - coin) // (a + b)

    ans = max(min(coin + (b * x), p - (a * x)), min(coin + (b * (x + 1)), p - (a * (x + 1))))

    print(ans)