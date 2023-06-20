from enum import Enum

class State(Enum):
  kInit = 0
  kVisiting = 1
  kVisited = 2

class Solution:
  def maximumInvitations(self, favorite: List[int]) -> int:
    n = len(favorite)
    sumComponentsLength = 0
    graph = [[] for _ in range(n)]
    inDegree = [0] * n
    maxChainLength = [1] * n

    for i, f in enumerate(favorite):
      graph[i].append(f)
      inDegree[f] += 1

    q = collections.deque([i for i, d in enumerate(inDegree) if d == 0])

    while q:
      u = q.popleft()
      for v in graph[u]:
        inDegree[v] -= 1
        if inDegree[v] == 0:
          q.append(v)
        maxChainLength[v] = max(maxChainLength[v], 1 + maxChainLength[u])

    for i in range(n):
      if favorite[favorite[i]] == i:
        sumComponentsLength += maxChainLength[i] + maxChainLength[favorite[i]]

    maxCycleLength = 0
    parent = [-1] * n
    seen = set()
    states = [State.kInit] * n

    def findCycle(u: int) -> None:
      nonlocal maxCycleLength
      seen.add(u)
      states[u] = State.kVisiting
      for v in graph[u]:
        if v not in seen:
          parent[v] = u
          findCycle(v)
        elif states[v] == State.kVisiting:
          curr = u
          cycleLength = 1
          while curr != v:
            curr = parent[curr]
            cycleLength += 1
          maxCycleLength = max(maxCycleLength, cycleLength)
      states[u] = State.kVisited

    for i in range(n):
      if i not in seen:
        findCycle(i)

    return max(sumComponentsLength // 2, maxCycleLength)
