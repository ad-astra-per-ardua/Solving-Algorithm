import sys

input = sys.stdin.readline

def slope(p1, p2):
    return (p2[1]-p1[1]) / (p2[0]-p1[0]) if p2[0]-p1[0] != 0 else float('inf')

p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

if slope(p1, p2) == slope(p2, p3):
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")
