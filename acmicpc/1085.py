a, b, c ,d = map(int, input().split())  # x, y = 사람 좌표 , c,d = 사각형 좌표

x = abs(a - c)
y = abs(b - d)
z = abs(a - 0)
w = abs(b - 0)
print(min(x,y,z,w))