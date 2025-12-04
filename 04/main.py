from sys import argv
from time import perf_counter

start = perf_counter()

with open(argv[1], encoding="ascii") as file:
    grid = [list(line.strip()) for line in file]

EMPTY, ROLL = ".", "@"
ADJ = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
H, W = len(grid), len(grid[0])
ADJ_LIMIT = 3


def count_adj(i: int, j: int) -> int:
    adj_rolls = 0
    for di, dj in ADJ:
        i1, j1 = i + di, j + dj
        if not (0 <= i1 < H and 0 <= j1 < W):
            continue
        adj_rolls += 1 if grid[i1][j1] == ROLL else 0
        if adj_rolls > ADJ_LIMIT:
            break
    return adj_rolls


def process(clearing: bool) -> int:
    cnt = 0
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char != ROLL:
                continue
            adj_rolls = count_adj(i, j)
            if adj_rolls <= ADJ_LIMIT:
                cnt += 1
                if clearing:
                    grid[i][j] = EMPTY
    return cnt


p1 = process(False)
print(p1)

p2 = 0
while (cnt := process(True)) > 0:
    p2 += cnt

print(p2)

exec_time = (perf_counter() - start) * 1000
print(f"{exec_time:.1f}ms")
