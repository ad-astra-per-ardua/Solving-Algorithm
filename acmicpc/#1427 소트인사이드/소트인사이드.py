import sys
input = sys.stdin.readline
n = list(map(str,(input())))
n = sorted(n, reverse=True)
print(''.join(map(str,n)))