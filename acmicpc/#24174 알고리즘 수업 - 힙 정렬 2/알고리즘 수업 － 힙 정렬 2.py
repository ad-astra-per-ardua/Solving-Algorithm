import cmath
import random
import math
from collections import defaultdict, Counter, deque, OrderedDict
# from heapq import heapify, heappush, heappop
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
def heap_sort(arr, length):
    global swap_count
    build_min_heap(arr, length)
    for i in range(length, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        swap_count += 1
        if swap_count == max_swaps:
            print(*arr[1:])
            exit()
        sift_down(arr, 1, i - 1)

def build_min_heap(arr, length):
    for i in range(length // 2, 0, -1):
        sift_down(arr, i, length)

def sift_down(arr, idx, length):
    global swap_count
    left_child, right_child = 2 * idx, 2 * idx + 1
    if right_child <= length:
        smallest = left_child if arr[left_child] < arr[right_child] else right_child
    elif left_child <= length:
        smallest = left_child
    else:
        return

    if arr[smallest] < arr[idx]:
        arr[idx], arr[smallest] = arr[smallest], arr[idx]
        swap_count += 1
        if swap_count == max_swaps:
            print(*arr[1:])
            exit()
        sift_down(arr, smallest, length)

total_numbers, max_swaps = map(int, input().split())
arr = [0] + list(map(int, input().split()))
swap_count = 0
heap_sort(arr, total_numbers)
print(-1)
