import re
from itertools import combinations_with_replacement
from sys import argv
from time import perf_counter
from typing import NamedTuple

from z3 import Int, Optimize, Sum, sat

start_time = perf_counter()


class Machine(NamedTuple):
    lights: list[bool]
    btns: list[list[int]]
    jolts: list[int]


machines: list[Machine] = []
with open(argv[1], encoding="ascii") as file:
    for line in file:
        [lights_str] = re.findall(r"\[(.+)\]", line)
        lights = [c == "#" for c in lights_str]

        btns_strs = re.findall(r"\((.*?)\)", line)
        btns = [list(map(int, s.split(","))) for s in btns_strs]

        [jolt_str] = re.findall(r"{(.+)}", line)
        jolts = list(map(int, jolt_str.split(",")))

        machines.append(Machine(lights, btns, jolts))


total_init = 0
for lights, btns, _ in machines:
    n_btns = len(btns)
    found_init = False
    n = 0
    while not found_init:
        n += 1
        for combo in combinations_with_replacement(btns, n):
            state_init = [False] * len(lights)
            state_jolt = [0] * len(lights)

            for btn in combo:
                for i in btn:
                    state_init[i] = not state_init[i]
            if state_init == lights:
                total_init += n
                found_init = True
                break
print("part 1:", total_init)

total_jolt = 0
for _, btns, jolts in machines:
    n_btns = len(btns)
    b_vars = [Int(f"b{i}") for i in range(n_btns)]
    eqs: list[tuple[list[int], int]] = []
    for light_idx, jolt in enumerate(jolts):
        eq_parts: list[int] = []
        for btn_idx, btn_lights in enumerate(btns):
            if light_idx in btn_lights:
                eq_parts.append(btn_idx)
        eqs.append((eq_parts, jolt))

    opt = Optimize()
    for parts, res in eqs:
        opt.add(Sum([b_vars[b_idx] for b_idx in parts]) == res)
    for b_var in b_vars:
        opt.add(b_var >= 0)
    opt.minimize(Sum(b_vars))
    if opt.check() == sat:
        m = opt.model()
        b_sum = int(str(m.eval(Sum(b_vars))))
        total_jolt += b_sum

print("part 2:", total_jolt)


print(f"{(perf_counter() - start_time) * 1000:.1f}ms")
