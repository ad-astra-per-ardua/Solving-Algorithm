import sys
input = sys.stdin.readline

def check_time_limit(complexity: str, N: int, T: int, L: int) -> str:
    MAX_OPERATION = 100000000
    if complexity == "O(N)":
        operations = N
    elif complexity == "O(N^2)":
        operations = N * N
    elif complexity == "O(N^3)":
        operations = N * N * N
    elif complexity == "O(2^N)":
        operations = 2 ** N
    elif complexity == "O(N!)":
        operations = 1
        for i in range(1, N + 1):
            operations *= i
            if operations > MAX_OPERATION * L * T:
                break
    else:
        return "Invalid Complexity"
    total_operations = operations * T
    if total_operations > MAX_OPERATION * L:
        return "TLE!"
    else:
        return "May Pass."

def main():
    C = int(input().strip())

    for _ in range(C):
        complexity, N, T, L = input().strip().split()
        N, T, L = int(N), int(T), int(L)

        result = check_time_limit(complexity, N, T, L)
        print(result)

main()
