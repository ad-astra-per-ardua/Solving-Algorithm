import sys
input = sys.stdin.readline
class Trie:
    def __init__(self):
        self.root = {}

    def add(self,foods):
        current = self.root
        for food in foods:
            if food not in current:
                current[food]={}
            current = current[food]
        current[0] = True

    def dfs(self,level,temp):
        if 0 in temp:
            return
        current_child = sorted(temp)
        for i in current_child:
            print("--"*level+i)
            self.dfs(level+1,temp[i])

N = int(input())
trie = Trie()
for e in range(N):
    dt = list(input().split())
    trie.add(dt[1:])
trie.dfs(0,trie.root)