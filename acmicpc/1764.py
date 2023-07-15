r, f = map(int,input().split())
angle = (f / r) * 180 % 360
if 180 < angle < 360:
    print("down")
else:
    print("up")
