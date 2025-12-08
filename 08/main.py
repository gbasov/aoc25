from itertools import combinations
from math import dist, prod
from operator import itemgetter
from sys import argv
from time import perf_counter

start = perf_counter()

TEST = argv[1] == "test.txt"
with open(argv[1], encoding="ascii") as file:
    boxes = [tuple(map(int, line.strip().split(","))) for line in file]

pairs = [
    (a, b, dist(boxes[a], boxes[b])) for a, b in combinations(range(len(boxes)), 2)
]
pairs.sort(key=itemgetter(2))

sets: list[set[int]] = []
limit = 10 if TEST else 1000

for i, (a, b, _) in enumerate(pairs):
    if i == limit:
        sets.sort(reverse=True, key=len)
        print("part 1:", prod(len(s) for s in sets[:3]))

    merging = [s for s in sets if a in s or b in s]

    for s in merging:
        sets.remove(s)

    sets.append({a, b}.union(*merging))

    if len(sets) == 1 and len(sets[0]) == len(boxes):
        print("part 2:", boxes[a][0] * boxes[b][0])
        break

print(f"{(perf_counter() - start) * 1000:.1f}ms")
