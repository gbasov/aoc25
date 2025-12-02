from sys import argv
from time import perf_counter

start = perf_counter()

with open(argv[1], encoding="ascii") as file:
    input = [(line[0], int(line[1:])) for line in file]

pos = 50
max = 100
stops = 0
passes = 0
prev = "R"

for dir, diff in input:
    if dir != prev:
        pos = 0 if pos == 0 else max - pos

    incr, pos = divmod(pos + diff, max)
    passes += incr

    prev = dir

    if pos == 0:
        stops += 1

print("stops", stops)
print("passes", passes)

exec_time = (perf_counter() - start) * 1000
print(f"{exec_time:.1f}ms")
