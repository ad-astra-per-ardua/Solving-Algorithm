from sys import stdin

def evaluate_expression(x, y, expr):
    global max_val, min_val
    if x == y == n - 1:
        max_val = max(max_val, eval(expr))
        min_val = min(min_val, eval(expr))
        return

    if x + 1 < n:
        next_expr = expr + arr[x + 1][y] if (x + y) % 2 == 0 else str(eval(expr + arr[x + 1][y]))
        evaluate_expression(x + 1, y, next_expr)

    if y + 1 < n:
        next_expr = expr + arr[x][y + 1] if (x + y) % 2 == 0 else str(eval(expr + arr[x][y + 1]))
        evaluate_expression(x, y + 1, next_expr)


n = int(stdin.readline())
max_val = -float('inf')
min_val = float('inf')

arr = [list(stdin.readline().rstrip().split()) for _ in range(n)]

evaluate_expression(0, 0, arr[0][0])
print(max_val, min_val)
