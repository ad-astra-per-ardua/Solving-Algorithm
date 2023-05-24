
x = []
y = []

for _ in range(3):
    xi, yi = map(int, input().split())
    if xi in x:
        x.remove(xi)
    else:
        x.append(xi)
    if yi in y:
        y.remove(yi)
    else:
        y.append(yi)
print(x[0],y[0])