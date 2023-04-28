import math


def find_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def find_factors(n, primes):
    factors = []
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
            while n % prime == 0:
                n //= prime
    if n != 1:
        factors.append(n)
    return factors


def solve(N, L, values):
    global prime, next_value
    primes = find_primes(N)
    sorted_primes = sorted(set(prime for value in values for prime in find_factors(value, primes)))
    prime_to_letter = {prime: chr(ord('A') + i) for i, prime in enumerate(sorted_primes)}

    plaintext = ''
    for i in range(L - 1):
        value = values[i]
        next_value = values[i + 1]
        for prime in sorted_primes:
            if value % prime == 0 and next_value % prime == 0:
                break
        letter = prime_to_letter[prime]
        plaintext += letter
    plaintext += prime_to_letter[next_value // prime]

    return plaintext


T = int(input())
for i in range(1, T + 1):
    N, L = map(int, input().split())
    values = list(map(int, input().split()))
    result = solve(N, L, values)
    print(f"Case #{i}: {result}")
