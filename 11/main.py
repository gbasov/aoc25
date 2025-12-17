from sys import argv
from time import perf_counter

start_time = perf_counter()

nodes: dict[str, set[str]] = {}
DAC, FFT, OUT, SVR, YOU = "dac", "fft", "out", "svr", "you"

with open(argv[1]) as file:
    for line in file:
        node, links_str = line.strip().split(":")
        nodes[node] = set(links_str.strip().split(" "))

mem: dict[tuple[str, str], int] = {}


def traverse(node: str, final: str) -> int:
    if node == final:
        return 1
    if node == OUT:
        return 0

    if (node, final) in mem:
        return mem[(node, final)]

    result = sum(traverse(n, final) for n in nodes[node])
    mem[(node, final)] = result
    return result


if YOU in nodes:
    print("part 1:", traverse(YOU, OUT))

if SVR in nodes:
    path1 = traverse(SVR, DAC) * traverse(DAC, FFT) * traverse(FFT, OUT)
    path2 = traverse(SVR, FFT) * traverse(FFT, DAC) * traverse(DAC, OUT)
    print("part 2:", path1 + path2)

print(f"{(perf_counter() - start_time) * 1000:.1f}ms")
