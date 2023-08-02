import heapq
from collections import defaultdict

INF = 100000000

def solution(n, start, end, roads, traps):
    def check_is_right(curv, nextv, cur_status, trap_map):
        if curv not in trap_map and nextv not in trap_map:
            return True
        if curv in trap_map and nextv in trap_map:
            is_curv_active = bool(cur_status & (1 << trap_map[curv]))
            is_nextv_active = bool(cur_status & (1 << trap_map[nextv]))
            return is_curv_active == is_nextv_active
        if curv in trap_map:
            is_curv_active = bool(cur_status & (1 << trap_map[curv]))
            return not is_curv_active
        if nextv in trap_map:
            is_nextv_active = bool(cur_status & (1 << trap_map[nextv]))
            return not is_nextv_active
        return True

    trap_map = {trap: i for i, trap in enumerate(traps)}
    graph = defaultdict(list)
    for u, v, w in roads:
        graph[u].append((v, w, False))
        graph[v].append((u, w, True))

    dist = [[INF] * (1 << len(traps)) for _ in range(n + 1)]
    queue = [(0, start, 0)]
    answer = INF

    while queue:
        curw, curv, cur_status = heapq.heappop(queue)
        if curv == end:
            answer = min(answer, curw)
            continue
        if curw > dist[curv][cur_status]:
            continue
        if curv in trap_map:
            cur_status ^= (1 << trap_map[curv])
        for nextv, nextw, is_reverse_edge in graph[curv]:
            is_right = check_is_right(curv, nextv, cur_status, trap_map)
            if (is_right and is_reverse_edge) or (not is_right and not is_reverse_edge):
                continue
            if dist[nextv][cur_status] > nextw + curw:
                dist[nextv][cur_status] = nextw + curw
                heapq.heappush(queue, (nextw + curw, nextv, cur_status))
    return answer
