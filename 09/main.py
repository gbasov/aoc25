from itertools import combinations
from operator import itemgetter
from sys import argv
from time import perf_counter

start_time = perf_counter()

type point = tuple[int, int]

points: list[point] = []
with open(argv[1], encoding="ascii") as file:
    for line in file:
        x, y = tuple(map(int, line.strip().split(",")))
        points.append((x, y))


def points_to_svg(points: list[point], rect: tuple[point, point] | None):
    w = max([x for x, _ in points]) + 1
    h = max([y for _, y in points]) + 1
    points_attr = " ".join(f"{x},{y}" for x, y in points)
    p = int(w / 20)
    s = 300 if w > 1000 else 1

    rect_str = ""
    if rect is not None:
        rect_x = min([x for x, _ in rect])
        rect_y = min([y for _, y in rect])
        rect_w = abs(rect[0][0] - rect[1][0])
        rect_h = abs(rect[0][1] - rect[1][1])
        rect_str = f"""<rect x="{rect_x}" y="{rect_y}" width="{rect_w}" height="{rect_h}" stroke-width="{s / 3}" fill="none" stroke="red" />"""

    with open("out.svg", "w") as file:
        file.write(
            f"""<svg xmlns="http://www.w3.org/2000/svg"
    viewBox="{-p} {-p} {w + p * 2} {h + p * 2}"
    style="background: #222">
    <polygon points="{points_attr}" stroke="green" stroke-width="{s}" fill="none" />
    {rect_str}
</svg>"""
        )


def area(a: point, b: point) -> int:
    (xa, ya), (xb, yb) = a, b
    return (abs(xa - xb) + 1) * (abs(ya - yb) + 1)


rects = [
    (points[i], points[j], area(points[i], points[j]))
    for i, j in combinations(range(len(points)), 2)
]
rects.sort(reverse=True, key=itemgetter(2))

print("part 1:", rects[0][2])


shape: set[point] = set(points)
for i, a in enumerate(points):
    b = points[i + 1] if i < len(points) - 1 else points[0]

    axis = 1 if a[0] == b[0] else 0
    start, end = sorted((a, b), key=itemgetter(axis))

    for k in range(start[axis] + 1, end[axis]):
        shape.add((start[0], k) if axis == 1 else (k, start[1]))

valid_rect = None
for r1, r2, r_area in rects:
    xs, ys = ([x for x, _ in (r1, r2)], [y for _, y in (r1, r2)])
    xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)

    is_valid = True
    for px, py in shape:
        if xmin < px < xmax and ymin < py < ymax:
            is_valid = False
            break

    if is_valid:
        # it doesn't check whether a rectangle is placed within the shape.
        # thus, it finds an incorrect rectangle for the test input.
        print("part 2", r_area)
        valid_rect = (r1, r2)
        break

points_to_svg(points, valid_rect)

print(f"{(perf_counter() - start_time) * 1000:.1f}ms")
