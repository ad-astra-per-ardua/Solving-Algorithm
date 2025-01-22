import sys
import heapq

input = sys.stdin.readline

def calculate_range(prefix_sum, i1, i2, j1, j2):
    return (prefix_sum[i2][j2]
            - prefix_sum[i1-1][j2]
            - prefix_sum[i2][j1-1]
            + prefix_sum[i1-1][j1-1])

def main():
    h, w = map(int, input().split())
    h1, h2, w1, w2 = map(int, input().split())
    
    grid = [[0]*(w+1) for _ in range(h+1)]
    for i in range(1, h+1):
        row = list(map(int, input().split()))
        for j in range(1, w+1):
            grid[i][j] = row[j-1]
    
    if h <= h1 or w <= w1:
        print("No")
        return
    
    prefix_sum = [[0]*(w+1) for _ in range(h+1)]
    for i in range(1, h+1):
        for j in range(1, w+1):
            prefix_sum[i][j] = (prefix_sum[i-1][j]
                                + prefix_sum[i][j-1]
                                - prefix_sum[i-1][j-1]
                                + grid[i][j])
    
    h2 = min(h2, h-1)
    w2 = min(w2, w-1)
    
    INF = 10**18
    ret = INF
    
    for i in range(h1+1, h2+2):
        pq = []
        
        for j in range(w1+1, w+1):
            while pq and pq[0][1] < (j - w2):
                heapq.heappop(pq)
            
            c1 = calculate_range(prefix_sum, 1, i, j-w1, w)
            c2 = calculate_range(prefix_sum, 2, i-1, (j-w1)+1, w) if i>1 else 0
            val_push = c1 - c2
            heapq.heappush(pq, (val_push, j-w1))
            
            if j < w:
                val_part1 = calculate_range(prefix_sum, 1, 1, j+1, w)
                val_part2 = calculate_range(prefix_sum, i, i, j+1, w)
                val = val_part1 + val_part2
            else:
                val = 0
            
            top_val, _ = pq[0]
            c3 = calculate_range(prefix_sum, 2, i-1, j, j) if i>1 else 0
            candidate = top_val - val + c3
            if candidate < ret:
                ret = candidate
    
    print(ret)

if __name__ == "__main__":
    main()
