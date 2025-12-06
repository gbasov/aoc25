from math import prod
from sys import argv
from time import perf_counter

start = perf_counter()

with open(argv[1], encoding="ascii") as file:
    lines = [list(line.rstrip("\n")) for line in file]

W = max(len(line) for line in lines)

for line in lines:
    line.extend(" " * (W - len(line)))

*num_lines, op_line = lines
ops = {"*": prod, "+": sum}
stack: list[int] = []
total = 0

for j in range(W - 1, -1, -1):
    num = "".join(line[j] for line in num_lines).strip()

    if num:
        stack.append(int(num))

    if (op := op_line[j]) in ops:
        total += ops[op](stack)
        stack.clear()

print(total)

print(f"{(perf_counter() - start) * 1000:.1f}ms")
