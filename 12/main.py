from math import prod
from sys import argv
from time import perf_counter

start_time = perf_counter()

SHAPE_AREA = 9
total = 0

*_, regions = open(argv[1]).read().strip().split("\n\n")

for region in regions.split("\n"):
    region_area, shape_nums = region.split(": ")

    region_area = prod(map(int, region_area.split("x")))
    shapes = sum(map(int, shape_nums.split(" ")))

    if shapes * SHAPE_AREA <= region_area:
        total += 1

print(total)

print(f"{(perf_counter() - start_time) * 1000:.1f}ms")
