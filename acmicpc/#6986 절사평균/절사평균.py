import sys
input = sys.stdin.readline


def trimmed(n, k, lists):
    lists = [score * 10 for score in lists]
    lists.sort()
    ret1 = sum(lists[k:n-k]) / (n-2*k) / 10
    return "%.2f" % (ret1 + 1e-8)


def adjusted(n, k, lists):
    lists = [score * 10 for score in lists]
    lists.sort()
    lists[:k] = [lists[k]] * k
    lists[n-k:] = [lists[n-k-1]] * k
    ret2 = sum(lists) / n / 10
    return "%.2f" % (ret2 + 1e-8)


n,k = map(int,input().split())
lists = [float(input()) for _ in range(n)]

print(trimmed(n,k,lists))
print(adjusted(n,k,lists))
