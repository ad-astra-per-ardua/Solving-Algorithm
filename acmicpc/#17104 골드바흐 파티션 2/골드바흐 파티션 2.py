import sys
import math

def fft(a, inv=False):
    n = len(a)
    j = 0

    # --- Bit Reversal ---
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    # -------------------

    length = 2
    while length <= n:
        angle = 2 * math.pi / length * (-1 if inv else 1)
        wlen = complex(math.cos(angle), math.sin(angle))

        for i in range(0, n, length):
            w = 1 + 0j
            half = length >> 1
            for k in range(i, i + half):
                u = a[k]
                t = w * a[k + half]
                a[k] = u + t      
                a[k + half] = u - t  
                w *= wlen
        length <<= 1

    if inv:
        for i in range(n):
            a[i] /= n

def polymul(a, b):
    n = 1
    while n < len(a) + len(b) - 1:
        n <<= 1

    fa = [complex(x, 0) for x in a] + [0] * (n - len(a))
    fb = [complex(x, 0) for x in b] + [0] * (n - len(b))

    fft(fa, inv=False)
    fft(fb, inv=False)

    for i in range(n):
        fa[i] *= fb[i]

    fft(fa, inv=True)

    res_size = len(a) + len(b) - 1
    res = [0] * res_size
    for i in range(res_size):
        val = round(fa[i].real)
        res[i] = val if val > 0 else 0

    return res

def solve():
    input = sys.stdin.readline
    T = int(input())

    MAX_N = 1_000_000

    is_prime = [True] * (MAX_N + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(MAX_N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, MAX_N + 1, i):
                is_prime[j] = False

    N2 = 500_000 
    A = [0]*(N2 + 1)
    for num in range(3, MAX_N+1, 2):
        if is_prime[num]:
            A[num >> 1] = 1 
    ConvA = polymul(A, A) 


    outputs = []
    for _ in range(T):
        n = int(input())
        val = 0
        if n//2 - 1 >= 0:
            val = ConvA[n//2 - 1] // 2
        if is_prime[n//2]:
            val += 1
        outputs.append(val)

    print("\n".join(map(str, outputs)))


if __name__ == "__main__":
    solve()
