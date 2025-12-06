from math import prod
from sys import argv
from time import perf_counter

start = perf_counter()

with open(argv[1], encoding="ascii") as file:
    *num_lines, ops_line = file.read().splitlines()

ops = ops_line.split()
nums = [list(map(int, line.split())) for line in num_lines]

nums = list(zip(*nums))

ops_map = {"+": sum, "*": prod}
total = sum(ops_map[op](col) for col, op in zip(nums, ops))

print(total)

print(f"{(perf_counter() - start) * 1000:.1f}ms")
