import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb, sqrt
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_007
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########


N = 0
M = 0
S = 0
A = []
Query = []
Value = 0
Left = 0
Right = 0
Count = [0] * 100001
Count_Count = [0] * 100001
Answer = [0] * 100001


class QUERY:
    def __init__(self, Left, Right, Index):
        self.Left = Left
        self.Right = Right
        self.Index = Index


def input_values():
    global N, M, A, Query
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    for _ in range(M):
        I, J = map(int, input().split())
        Query.append(QUERY(I - 1, J - 1, len(Query)))


def Comp(A, B):
    global S
    if A.Left // S != B.Left // S:
        return A.Left // S < B.Left // S
    return A.Right < B.Right


def settings():
    global N, M, S, A, Query, Value, Left, Right, Count, Count_Count, Answer
    S = int(sqrt(N))
    Query.sort(key=lambda x: (x.Left // S, x.Right))
    Left = Query[0].Left
    Right = Query[0].Right
    for i in range(Left, Right + 1):
        Now = A[i]
        Count_Count[Count[Now]] -= 1
        Count[Now] += 1
        Value = max(Value, Count[Now])
        Count_Count[Count[Now]] += 1
    Answer[Query[0].Index] = Value
    for i in range(1, M):
        while Query[i].Left < Left:
            Left -= 1
            Now = A[Left]
            Count_Count[Count[Now]] -= 1
            Count[Now] += 1
            Value = max(Value, Count[Now])
            Count_Count[Count[Now]] += 1

        while Query[i].Left > Left:
            Now = A[Left]
            Count_Count[Count[Now]] -= 1
            if Count_Count[Count[Now]] == 0 and Value == Count[Now]:
                Value -= 1
            Count[Now] -= 1
            Count_Count[Count[Now]] += 1
            Left += 1

        while Query[i].Right > Right:
            Right += 1
            Now = A[Right]
            Count_Count[Count[Now]] -= 1
            Count[Now] += 1
            Value = max(Value, Count[Now])
            Count_Count[Count[Now]] += 1

        while Query[i].Right < Right:
            Now = A[Right]
            Count_Count[Count[Now]] -= 1
            if Count_Count[Count[Now]] == 0 and Value == Count[Now]:
                Value -= 1
            Count[Now] -= 1
            Count_Count[Count[Now]] += 1
            Right -= 1

        Answer[Query[i].Index] = Value


def find_Answer():
    for i in range(M):
        print(Answer[i])


def main():
    input_values()
    settings()
    find_Answer()


if __name__ == "__main__":
    main()
