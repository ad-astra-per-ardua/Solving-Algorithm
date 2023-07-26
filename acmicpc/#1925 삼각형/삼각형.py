import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def check_line(a, b, c):
    dxAB = b.x - a.x
    dyAB = b.y - a.y
    dxAC = c.x - a.x
    dyAC = c.y - a.y

    if dxAB * dyAC == dyAB * dxAC:
        return True
    return False

def check_jung_triangle(a, b, c):
    ab = (a.x - b.x) ** 2 + (a.y - b.y) ** 2
    ac = (a.x - c.x) ** 2 + (a.y - c.y) ** 2
    bc = (b.x - c.x) ** 2 + (b.y - c.y) ** 2

    if ab == ac == bc:
        return True
    return False

def check_two_length(a, b, c):
    ab = (a.x - b.x) ** 2 + (a.y - b.y) ** 2
    ac = (a.x - c.x) ** 2 + (a.y - c.y) ** 2
    bc = (b.x - c.x) ** 2 + (b.y - c.y) ** 2

    if ab == ac or ab == bc or ac == bc:
        return True
    return False

def dot(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2

def main():
    a = Point(*map(int, input().split()))
    b = Point(*map(int, input().split()))
    c = Point(*map(int, input().split()))

    if check_line(a, b, c):
        print("X")
    elif check_jung_triangle(a, b, c):
        print("JungTriangle")
    elif check_two_length(a, b, c):
        if dot(b.x-a.x, b.y-a.y, c.x-a.x, c.y-c.y) < 0:
            print("Dunkak2Triangle")
        elif dot(a.x-b.x, a.y-b.y, c.x-b.x, c.y-b.y) < 0:
            print("Dunkak2Triangle")
        elif dot(a.x-c.x, a.y-c.y, b.x-c.x, b.y-c.y) < 0:
            print("Dunkak2Triangle")
        elif dot(b.x-a.x, b.y-a.y, c.x-a.x, c.y-c.y) == 0:
            print("Jikkak2Triangle")
        elif dot(a.x-b.x, a.y-b.y, c.x-b.x, c.y-b.y) == 0:
            print("Jikkak2Triangle")
        elif dot(a.x-c.x, a.y-c.y, b.x-c.x, b.y-c.y) == 0:
            print("Jikkak2Triangle")
        else:
            print("Yeahkak2Triangle")
    else:
        if dot(b.x-a.x, b.y-a.y, c.x-a.x, c.y-c.y) < 0:
            print("DunkakTriangle")
        elif dot(a.x-b.x, a.y-b.y, c.x-b.x, c.y-b.y) < 0:
            print("DunkakTriangle")
        elif dot(a.x-c.x, a.y-c.y, b.x-c.x, b.y-c.y) < 0:
            print("DunkakTriangle")
        elif dot(b.x-a.x, b.y-a.y, c.x-a.x, c.y-c.y) == 0:
            print("JikkakTriangle")
        elif dot(a.x-b.x, a.y-b.y, c.x-b.x, c.y-b.y) == 0:
            print("JikkakTriangle")
        elif dot(a.x-c.x, a.y-c.y, b.x-c.x, b.y-c.y) == 0:
            print("JikkakTriangle")
        else:
            print("YeahkakTriangle")

if __name__ == "__main__":
    main()
