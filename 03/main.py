from sys import argv
from time import perf_counter

start = perf_counter()

with open(argv[1], encoding="ascii") as file:
    banks = [list(map(int, line.strip())) for line in file]


def calc(nums: list[int], power: int) -> int:
    prefix = nums[: -1 * power] if power > 0 else nums
    i, val = max(enumerate(prefix), key=lambda x: x[1])
    rest = calc(nums[i + 1 :], power - 1) if power > 0 else 0
    return val * 10**power + rest


p1 = sum(calc(bank, 1) for bank in banks)
p2 = sum(calc(bank, 11) for bank in banks)

print(p1, p2)

exec_time = (perf_counter() - start) * 1000
print(f"{exec_time:.1f}ms")
