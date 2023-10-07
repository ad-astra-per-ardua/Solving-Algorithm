import sys
input = sys.stdin.readline
def insertion_sort(A, B):
    N = len(A)

    for i in range(1, N):
        loc = i - 1
        newItem = A[i]

        while loc >= 0 and newItem < A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1
            if A == B:
                return 1

        if loc + 1 != i:
            A[loc + 1] = newItem
        if A == B:
            return 1

    return 0


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(insertion_sort(A, B))
