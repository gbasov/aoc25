from sys import argv
from time import perf_counter

start = perf_counter()

with open(argv[1], encoding="ascii") as file:
    lines = [list(line.strip()) for line in file]

START, SPLIT = "S", "^"

beams = {lines[0].index(START): 1}
splits = 0

for line in lines[1:]:
    for i, char in enumerate(line):
        if char == SPLIT and i in beams:
            splits += 1
            val = beams.pop(i)
            for j in (i - 1, i + 1):
                beams[j] = beams.get(j, 0) + val


print("part 1:", splits)
print("part 2:", sum(beams.values()))

print(f"{(perf_counter() - start) * 1000:.1f}ms")
