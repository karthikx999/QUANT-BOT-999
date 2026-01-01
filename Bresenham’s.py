import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        p = 2 * dy - dx
        while x != x2:
            points.append((x, y))
            if p >= 0:
                y += sy
                p -= 2 * dx
            x += sx
            p += 2 * dy
    else:
        p = 2 * dx - dy
        while y != y2:
            points.append((x, y))
            if p >= 0:
                x += sx
                p -= 2 * dy
            y += sy
            p += 2 * dx

    points.append((x2, y2))
    return points

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

pts = bresenham(x1, y1, x2, y2)

xs = [p[0] for p in pts]
ys = [p[1] for p in pts]

plt.scatter(xs, ys)
plt.plot(xs, ys)
plt.grid(True)
plt.show()
