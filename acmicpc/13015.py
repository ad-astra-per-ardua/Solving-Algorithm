n = int(input())

a = 0
b = n - 1
c = 3 * n - 3
d = 4 * n - 4

for i in range(1, 2 * n):
    if i == 1 or i == (2 * n) - 1:
        print("*" * (b - a + 1), end="")
        print(" " * (c - b - 1), end="")
        print("*" * (d - c + 1), end="")
    else:
        print(" " * a, end="")
        print("*", end="")
        print(" " * (b - a - 1), end="")
        print("*", end="")
        print(" " * (c - b - 1), end="")
        if b != c:
            print("*", end="")
        print(" " * (d - c - 1), end="")
        print("*", end="")
    print()

    if i < n:
        a += 1
        b += 1
        c -= 1
        d -= 1
    else:
        a -= 1
        b -= 1
        c += 1
        d += 1
