import sys

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

def insert(num):
    curr_node = trie
    for char in num:
        if char not in curr_node:
            curr_node[char] = {}
        if 'isEnd' in curr_node:
            return False
        curr_node = curr_node[char]
    curr_node['isEnd'] = True
    if len(curr_node) > 1:
        return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    trie = {}
    flag = True
    nums = [sys.stdin.readline().strip() for _ in range(n)]
    nums.sort()
    for num in nums:
        if not insert(num):
            flag = False
            break
    print('YES' if flag else 'NO')
