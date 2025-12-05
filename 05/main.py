from operator import itemgetter
from sys import argv
from time import perf_counter

start = perf_counter()

with open(argv[1], encoding="ascii") as file:
    ranges_str, ids_str = file.read().strip().split("\n\n")
    ranges = [
        (int(lo), int(hi)) for lo, hi in (r.split("-") for r in ranges_str.splitlines())
    ]
    ids = [int(x) for x in ids_str.splitlines()]


def part1():
    return sum(any(lo <= i <= hi for lo, hi in ranges) for i in ids)


def part2():
    ranges.sort(key=itemgetter(0))
    top = 0
    total = 0
    for lo, hi in ranges:
        if lo > top:
            total += hi - lo + 1
            top = hi
        elif hi > top:
            total += hi - top
            top = hi
    return total


print("part 1:", part1())
print(f"{(perf_counter() - start) * 1000:.1f}ms")
start = perf_counter()

print("part 2:", part2())
print(f"{(perf_counter() - start) * 1000:.3f}ms")
