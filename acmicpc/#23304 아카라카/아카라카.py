import sys

def is_akaraka(s):
    if len(s) <= 1:
        return True
    n = len(s) // 2
    if s != s[::-1]:
        return False
    if is_akaraka(s[:n]) and is_akaraka(s[-n:]):
        return True
    return False

s = sys.stdin.readline().rstrip()

if is_akaraka(s):
    print('AKARAKA')
else:
    print('IPSELENTI')
