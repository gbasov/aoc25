from sys import argv
from time import time
start = time()

with open(argv[1], encoding='ascii') as file:
    input = [[line[:1], int(line[1:])] for line in file]
    
pos = 50
max = 100
stops = 0
passes = 0
prev = 'R'

for [dir, diff] in input:
    if dir != prev:
        pos = (max - pos) % max
    
    passes += int((pos + diff) / max)
    pos = (pos + diff) % max
    
    prev = dir
    
    if pos == 0:
        stops += 1
        
print('stops', stops)
print('passes', passes)

exec_time = (time() - start) * 1000
print(f'{exec_time:.1f}ms')
