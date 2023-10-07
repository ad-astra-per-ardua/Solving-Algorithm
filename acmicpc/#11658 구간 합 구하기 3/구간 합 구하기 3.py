import sys
input = sys.stdin.readline

def sum(r, c):
    result = 0
    row = r
    while row > 0:
        col = c
        while col > 0:
            result += tree[row][col]
            col -= (col & -col)
        row -= (row & -row)
    return result

def update(r, c, num):
    row = r
    while row <= table_size:
        col = c
        while col <= table_size:
            tree[row][col] += num
            col += (col & -col)
        row += (row & -row)

table_size, operation_num = map(int, input().split())
tree = [[0] * (table_size + 1) for _ in range(table_size + 1)]
table = [[0] * (table_size + 1) for _ in range(table_size + 1)]

for r in range(1, table_size + 1):
    row_vals = list(map(int, input().split()))
    for c in range(1, table_size + 1):
        table[r][c] = row_vals[c-1]
        update(r, c, table[r][c])

for _ in range(operation_num):
    operations = list(map(int, input().split()))
    w = operations[0]
    
    if w == 0:
        r1, c1, num = operations[1], operations[2], operations[3]
        update(r1, c1, num - table[r1][c1])
        table[r1][c1] = num
    else:
        r1, c1, r2, c2 = operations[1], operations[2], operations[3], operations[4]
        print(sum(r2, c2) - sum(r2, c1-1) - sum(r1-1, c2) + sum(r1-1, c1-1))
