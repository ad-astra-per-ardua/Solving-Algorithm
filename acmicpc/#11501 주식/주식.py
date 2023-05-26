import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    earn = 0
    day = int(input())
    stock = list(map(int,input().split()))

    max_price = stock[-1]   # Start from final day's stock price.

    for i in range(day - 2, -1, -1):    # Check prices by reverse
        if stock[i] > max_price:        # If found new highest stock price
            max_price = stock[i]        # Update it.
        else:
            earn += max_price - stock[i] # Calculate earn by max price - stock's now price.

    print(earn)
