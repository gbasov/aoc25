from sys import argv
from time import time

start = time()

with open(argv[1], encoding="ascii") as file:
    input = [
        list(map(int, pair.split("-"))) for pair in file.readline().strip().split(",")
    ]

sum1 = 0
sum2 = 0

for min, max in input:
    found_ids = set()
    for num_len in range(len(str(min)), len(str(max)) + 1):
        for chunk_len in range(1, int(num_len / 2) + 1):
            if num_len % chunk_len > 0:
                continue
            num_chunks = int(num_len / chunk_len)
            chunk_start = int("1" + "0" * (chunk_len - 1))
            chunk_end = int("9" * chunk_len)
            for chunk in range(chunk_start, chunk_end + 1):
                id = int(str(chunk) * num_chunks)
                if min <= id <= max:
                    if num_chunks == 2:
                        sum1 += id
                    if id not in found_ids:
                        sum2 += id
                        found_ids.add(id)

print(sum1, sum2)

exec_time = (time() - start) * 1000
print(f"{exec_time:.1f}ms")
