import matplotlib.pyplot as plt

xc = 0
yc = 0
r = 10

x = 0
y = r
p = 1 - r

X = []
Y = []

while x <= y:
    X.append(xc + x)
    Y.append(yc + y)

    X.append(xc - x)
    Y.append(yc + y)

    X.append(xc + x)
    Y.append(yc - y)

    X.append(xc - x)
    Y.append(yc - y)

    X.append(xc + y)
    Y.append(yc + x)

    X.append(xc - y)
    Y.append(yc + x)

    X.append(xc + y)
    Y.append(yc - x)

    X.append(xc - y)
    Y.append(yc - x)

    x = x + 1

    if p < 0:
        p = p + 2 * x + 1
    else:
        y = y - 1
        p = p + 2 * x - 2 * y + 1

plt.scatter(X, Y)
plt.gca().set_aspect("equal")
plt.show()
