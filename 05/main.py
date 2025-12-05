from sys import argv
from time import perf_counter

start = perf_counter()

with open(argv[1], encoding="ascii") as file:
    [ranges_str, ids] = file.read().strip().split("\n\n")

    ranges_list = [list(map(int, r.split('-'))) for r in ranges_str.split("\n")]
    ranges = [(r[0], r[1]) for r in ranges_list]
    ids = list(map(int, ids.split("\n")))

ranges.sort(key=lambda x: x[0])

good_ids = 0
for i in ids:
    for low, high in ranges:
        if low <= i <= high:
            good_ids += 1
            break
print("part 1:", good_ids)

top = 0
total = 0
for lo, hi in ranges:
    if lo > top:
        total += hi - lo + 1
        top = hi
    elif hi > top:
        total += hi - top
        top = hi


print("part 2:", total)

exec_time = (perf_counter() - start) * 1000
print(f"{exec_time:.1f}ms")
