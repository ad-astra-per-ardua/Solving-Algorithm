import heapq
from collections import deque


class Val:
    ide = 0
    u = 0
    v = 0
    low = 0
    base = 0
    mul = 0
    num = 0
    den = 0

    def contains(self, b):
        return self.u <= b.u and self.v >= b.v

    def support(self):
        return self.num // self.den

    def __gt__(self, other):
        return self.support() < other.support()

    def __ge__(self, other):
        return self.support() <= other.support()

    def __lt__(self, other):
        return self.support() > other.support()

    def __le__(self, other):
        return self.support() >= other.support()

    def __eq__(self, other):
        return self.support() == other.support()

    def __str__(self) -> str:
        return str(self.support())


class HuShing:
    def __init__(self, array) -> None:
        self.n = len(array)
        self.n_pqs = 0
        self.w = [0 for _ in range(self.n + 10)]
        self.cp = [0 for _ in range(self.n + 10)]

        self.sub = [0 for _ in range(self.n + 10)]
        self.qid = [0 for _ in range(self.n + 10)]
        self.pqs = [[] for _ in range(self.n + 10)]

        self.con = [deque() for _ in range(self.n + 10)]
        self.child = [deque() for _ in range(self.n + 10)]
        self.n_arcs = 0
        self.arcs = [Val() for _ in range(self.n + 10)]

        for i in range(self.n):
            self.w[i + 1] = array[i]

    def new_arc(self, u, v):
        self.n_arcs += 1
        self.arcs[self.n_arcs].ide = self.n_arcs
        self.arcs[self.n_arcs].u = u
        self.arcs[self.n_arcs].v = v
        self.arcs[self.n_arcs].low = u if self.w[u] < self.w[v] else v
        self.arcs[self.n_arcs].mul = self.w[u] * self.w[v]
        self.arcs[self.n_arcs].base = self.cp[v] - self.cp[u] - self.arcs[self.n_arcs].mul

    def build_tree(self, lst):
        stack = deque()
        self.new_arc(1, self.n + 1)
        for it in lst:
            self.new_arc(it[0], it[1])
            while stack and self.arcs[self.n_arcs].contains(self.arcs[stack[-1]]):
                self.child[self.n_arcs].append(stack[-1])
                stack.pop()
            stack.append(self.n_arcs)
        while stack:
            self.child[1].append(stack[-1])
            stack.pop()

    def one_sweep(self):
        stack = deque()
        tmp = deque()
        lst = deque()
        for i in range(1, self.n + 1):
            while len(stack) >= 2 and self.w[stack[-1]] > self.w[i]:
                tmp.append((stack[len(stack) - 2], i))
                stack.pop()
            stack.append(i)
        while len(stack) >= 4:
            vt1 = stack[-2]
            tmp.append((1, vt1))
            stack.pop()
        for it in tmp:
            if it[0] == 1 or it[1] == 1:
                continue
            lst.append(it)
        self.build_tree(lst)

    def prepare(self):
        V1 = min(range(1, self.n + 1), key=self.w.__getitem__)
        self.w = [0] + self.w[V1:self.n + 1] + self.w[1:V1] + [0]
        self.w[self.n + 1] = self.w[1]
        for i in range(1, self.n + 2):
            self.cp[i] = self.w[i] * self.w[i - 1]
            self.cp[i] += self.cp[i - 1]

    def mnmul(self, node):
        if node == 1:
            return self.w[1] * self.w[2] + self.w[1] * self.w[self.n]
        cur = self.arcs[node]
        if cur.u == cur.low:
            if (not self.con[cur.u]) or (not cur.contains(self.con[cur.u][-1])):
                return self.w[cur.u] * self.w[cur.u + 1]
            else:
                return self.con[cur.u][-1].mul
        else:
            if (not self.con[cur.v]) or (not cur.contains(self.con[cur.v][-1])):
                return self.w[cur.v] * self.w[cur.v - 1]
            else:
                return self.con[cur.v][-1].mul

    def add_arc(self, cur_node, arc):
        heapq.heappush(self.pqs[self.qid[cur_node]], arc)
        self.con[arc.u].append(arc)
        self.con[arc.v].append(arc)

    def remove_arc(self, cur_node):
        hm = self.pqs[self.qid[cur_node]][0]
        self.con[hm.u].pop()
        self.con[hm.v].pop()
        heapq.heappop(self.pqs[self.qid[cur_node]])

    def merge_pq(self, node):
        maxi = -1
        for it in self.child[node]:
            if maxi == -1 or self.sub[maxi] < self.sub[it]:
                maxi = it
        self.qid[node] = self.qid[maxi]
        cur_pq = self.pqs[self.qid[node]]
        for it in self.child[node]:
            if it == maxi:
                continue
            child_pq = self.pqs[self.qid[it]]
            while child_pq:
                heapq.heappush(cur_pq, heapq.heappop(child_pq))

    def dfs(self, node):
        cur = self.arcs[node]
        self.sub[node] = 1
        if not self.child[node]:
            self.n_pqs += 1
            self.qid[node] = self.n_pqs
            cur.den = cur.base
            cur.num = self.w[cur.low] * (cur.den + cur.mul - self.mnmul(node))
            self.add_arc(node, cur)
            return
        cur.den = cur.base
        for it in self.child[node]:
            self.dfs(it)
            self.sub[node] += self.sub[it]
            cur.den -= self.arcs[it].base
        cur.num = self.w[cur.low] * (cur.den + cur.mul - self.mnmul(node))
        self.merge_pq(node)
        cur_pq = self.pqs[self.qid[node]]
        while cur_pq and cur_pq[0].support() >= self.w[cur.low]:
            hm = cur_pq[0]
            cur.den += hm.den
            self.remove_arc(node)
            cur.num = self.w[cur.low] * (cur.den + cur.mul - self.mnmul(node))

        while cur_pq and cur >= cur_pq[0]:
            hm = cur_pq[0]
            cur.den += hm.den
            self.remove_arc(node)
            cur.num += hm.num
        self.add_arc(node, cur)

    def answer(self):
        self.dfs(1)
        ans = 0
        cur_pq = self.pqs[self.qid[1]]
        while cur_pq:
            ans += heapq.heappop(cur_pq).num
        return ans

    def solve(self):
        if self.n == 2:
            return self.w[1] * self.w[2]
        self.prepare()
        self.one_sweep()
        return self.answer()


n = int(input())
arr = []
for i in list(map(int, input().split())):
    arr.append(i)
for _ in range(1, n):
    a, tmp = map(int, input().split())
    arr.append(tmp)
hsing = HuShing(arr)
print(hsing.solve())
