import sys
input = sys.stdin.readline
def changes(a):     # a의 단위는 cent case1 : 124 cent
    quarter = 0     # 25
    dime = 0        # 10
    nickel = 0      # 5
    penny = 0       # 1
    while a > 0:
        if a >= 25:
            quarter += a // 25
            a -= quarter * 25
        elif a >= 10:
            dime += a // 10
            a -= dime * 10
        elif a >= 5:
            nickel += a // 5
            a -= nickel * 5
        elif a >= 1:
            penny += a // 1
            a -= penny * 1
    return quarter, dime, nickel, penny

loop = int(input())

for _ in range(loop):
    price = int(input())
    ans = changes(price)
    print(' '.join(map(str, ans)))
