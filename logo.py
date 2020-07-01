from dataclasses import dataclass
import math


@dataclass
class Color:
    r: float
    g: float
    b: float


@dataclass
class Circle:
    x: float
    y: float
    radius: float
    color: Color


def print_svg(circles):

    x_max = 0.0
    y_max = 0.0
    for circle in circles:
        x_max = max(x_max, circle.x + circle.radius)
        y_max = max(y_max, circle.y + circle.radius)
    xy_max = max(x_max, y_max)

    print(f"<svg height='{xy_max}' width='{xy_max}'>")

    for circle in circles:
        print(
            f"  <circle cx='{circle.x}' cy='{circle.y}' r='{circle.radius}' fill='rgb({circle.color.r*100.0}%, {circle.color.g*100.0}%, {circle.color.b*100.0}%)' />"
        )

    print("</svg>")


def centers(x, y, radius):
    r = radius / 3.0
    xt = 2.0 * r * math.sin(2.0 * math.pi / 6.0)
    yt = 2.0 * r * math.cos(2.0 * math.pi / 6.0)

    return [
        (x, y - 2.0 * r),
        (x + xt, y - yt),
        (x + xt, y + yt),
        (x, y + 2.0 * r),
        (x - xt, y + yt),
        (x - xt, y - yt),
    ]


def six_circles(x, y, radius, level):

    circles = []

    if level > 2:
        return circles

    f = 0.05
    cr = radius / 3.0
    for (cx, cy) in centers(x, y, radius):
        circles += [Circle(cx, cy, cr, color=Color(f, f, 1.00))]
        circles += six_circles(cx, cy, cr, level + 1)
        f += 0.15
    return circles


circles = six_circles(100.0, 100.0, 100.0, 1)
print_svg(circles)
