from math import prod, sqrt
from operator import itemgetter
from sys import argv
from time import perf_counter

start = perf_counter()

with open(argv[1], encoding="ascii") as file:
    boxes = [tuple(map(int, line.strip().split(","))) for line in file]

LIMIT = 10 if argv[1] == "test.txt" else 1000

distances: dict[tuple[int, int], float] = {}


def calc_distance(a: tuple[int, ...], b: tuple[int, ...]) -> float:
    return sqrt(sum([pow(a[i] - b[i], 2) for i in range(3)]))


for i, a in enumerate(boxes):
    for j, b in enumerate(boxes):
        key = sorted([i, j])
        key = (key[0], key[1])

        if i == j or key in distances:
            continue
        distances[key] = calc_distance(a, b)

sorted_distances = sorted(distances.items(), key=itemgetter(1))


def calc_product(circuits: list[set[int]]) -> int:
    circuits = sorted(circuits, reverse=True, key=lambda c: len(c))
    return prod([len(c) for c in circuits[:3]])


circuits: list[set[int]] = []

for i, ((a, b), _) in enumerate(sorted_distances):
    if i == LIMIT:
        print("part 1:", calc_product(circuits))

    added = False
    merging: list[int] = []
    for i, circuit in enumerate(circuits):
        if a in circuit or b in circuit:
            circuit.update({a, b})
            added = True
            merging.append(i)
    if not added:
        circuits.append({a, b})
        continue

    if len(merging) > 1:
        new_circuit: set[int] = set()
        new_circuit = new_circuit.union(*[circuits[i] for i in merging])
        circuits.append(new_circuit)
        removing: list[set[int]] = []
        for i in merging:
            removing.append(circuits[i])
        for circuit in removing:
            circuits.remove(circuit)

    if len(circuits) == 1 and len(circuits[0]) == len(boxes):
        print("part 2:", boxes[a][0] * boxes[b][0])
        break


print(f"{(perf_counter() - start) * 1000:.1f}ms")
