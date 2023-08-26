import cmath
import random
from math import *
from collections import defaultdict, Counter, deque, OrderedDict
from heapq import heapify, heappush, heappop
from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
from types import GeneratorType
import sys

input = lambda: sys.stdin.readline().strip()

# class SegmentTree:
#    def __init__(self, arr, func = lambda x, y : x + y, defaultvalue = 0) :
#        self.n = len(arr)
#        self.segmentTree = [0]*self.n + arr
#        self.func = func
#        self.defaultvalue = defaultvalue
#        self.buildSegmentTree(arr)
#
#    def buildSegmentTree(self, arr) :
#        for i in range(self.n -1, 0, -1) :
#            self.segmentTree[i] = self.func(self.segmentTree[2*i] , self.segmentTree[2*i+1])
#
#    def query(self, l, r) :
#        l += self.n
#        r += self.n
#        res = self.defaultvalue
#        while l < r :
#            if l & 1 :
#                res = self.func(res, self.segmentTree[l])
#                l += 1
#            l >>= 1
#            if r & 1 :
#                r -= 1
#                res = self.func(res, self.segmentTree[r])
#            r >>= 1
#        return res
#
#    def update(self, i, value) :
#        i += self.n
#        self.segmentTree[i] = value
#        while i > 1 :
#            i >>= 1
#            self.segmentTree[i] = self.func(self.segmentTree[2*i] , self.segmentTree[2*i+1])
#
#
# class UnionFind:
#    def __init__(self, n):
#        self.n = n
#        self.parents = list(range(n))
#        self.count = [1]*n
#    def find(self, x):
#        if self.parents[x] == x:
#            return x
#        else:
#            self.parents[x] = self.find(self.parents[x])
#            return self.parents[x]
#    def union(self, x, y):
#        x = self.find(x)
#        y = self.find(y)
#        if x != y:
#            self.parents[x] = y
#            self.count[y] += self.count[x]
#
# dire = [0,1,0,-1,0]

# def is_prime(n):
#     if n==1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# def ncr(n, r, p):
#     num = den = 1
#     for i in range(r):
#         num = (num * (n - i)) % p
#         den = (den * (i + 1)) % p
#     return (num * pow(den,
#             p - 2, p)) % p
#
# def case(t):
#     print("Case #{}:".format(t), end=" ")
#
# RANDOM = random.randrange(2**62)
# def mapping_wrapper(x):
#   return x ^ RANDOM
#
# class HashMap(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(mapping_wrapper(key), value)
#     def __getitem__(self, key):
#         return super().__getitem__(mapping_wrapper(key))
#     def __contains__(self, key):
#         return super().__contains__(mapping_wrapper(key))


# MOD = 1
#
# def binpow(a, b):
#     if b==0:
#         return 1
#     res = binpow(a,b//2)
#     res = pow(res,2,MOD)
#     if b%2:
#         return (res*a)%MOD
#     return res
#
# def mod_inverse(a):
#     return binpow(a,MOD-2)
#
# MAX = 2*(10**5)+5

# def factors(n):
#     if n==0:
#         return set()
#     return set(reduce(list.__add__,
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
#
# factors = [factors(i) for i in range(MAX)]
#
#
# fact = [1]*MAX
# invfact = [1]*MAX
# for i in range(1,MAX):
#     fact[i] = (fact[i-1]*i)%MOD
#     invfact[i] = (invfact[i-1]*mod_inverse(i))%MOD

# def bootstrap(f):
#     stack = []
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#     return wrappedfunc


def power(x, y, mod):
    x %= mod
    ret = 1
    while y > 0:
        if y % 2 == 1:
            ret = (ret * x) % mod
        x = (x * x) % mod
        y //= 2
    return ret

def check_prime(n, a):
    if a % n == 0:
        return True
    k = n - 1
    while True:
        temp = power(a, k, n)
        if temp == n - 1:
            return True
        if k % 2 == 1:
            return temp == 1 or temp == n - 1
        k //= 2

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i in a:
        if not check_prime(n, i):
            return False
    return True

def find_div(n):
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n

    x = random.randint(2, n-2)
    y = x
    c = random.randint(1, 10)
    g = 1
    while g == 1:
        x = (x*x + c) % n
        y = (y*y + c) % n
        y = (y*y + c) % n
        g = gcd(abs(x-y), n)
        if g == n:
            return find_div(n)
    if is_prime(g):
        return g
    else:
        return find_div(g)

if __name__ == "__main__":
    N = int(input())
    temp = N
    if N == 1:
        print(1)
        exit(0)

    List = []
    while N > 1:
        div = find_div(N)
        List.append(div)
        N //= div

    List.sort()
    Ans = temp
    Ans = (Ans // List[0]) * (List[0] - 1)
    for i in range(1, len(List)):
        if List[i] != List[i-1]:
            Ans = (Ans // List[i]) * (List[i] - 1)
    print(Ans)
