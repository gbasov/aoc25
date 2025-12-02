from sys import argv
from time import perf_counter

start = perf_counter()

with open(argv[1], encoding="ascii") as file:
    input = [
        list(map(int, pair.split("-"))) for pair in file.readline().strip().split(",")
    ]

sum1 = 0
sum2 = 0

for min, max in input:
    found_ids: set[int] = set()
    for num_len in range(len(str(min)), len(str(max)) + 1):
        for chunk_len in range(1, num_len // 2 + 1):
            n_chunks, remainder = divmod(num_len, chunk_len)
            if remainder > 0:
                continue
            chunk_start = 10 ** (chunk_len - 1)
            chunk_end = 10**chunk_len - 1
            for chunk in range(chunk_start, chunk_end + 1):
                id = int(str(chunk) * n_chunks)
                if min <= id <= max:
                    if n_chunks == 2:
                        sum1 += id
                    if id not in found_ids:
                        sum2 += id
                        found_ids.add(id)

print(sum1, sum2)

exec_time = (perf_counter() - start) * 1000
print(f"{exec_time:.1f}ms")
