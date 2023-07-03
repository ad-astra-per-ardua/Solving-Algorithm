import sys
from math import sqrt

input = sys.stdin.readline

def point_in_circle(cx, cy, r, px, py):
    return sqrt((cx-px)**2 + (cy-py)**2) <= r

w, h, x, y, p = map(int, input().split())
player_positions = [list(map(int, input().split())) for _ in range(p)]

players_in_arena = 0
for px, py in player_positions:
    if x <= px <= x+w and y <= py <= y+h:
        players_in_arena += 1
    elif point_in_circle(x, y+h/2, h/2, px, py) or point_in_circle(x+w, y+h/2, h/2, px, py):
        players_in_arena += 1

print(players_in_arena)
