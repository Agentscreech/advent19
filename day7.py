from helpers import *
import itertools

data = get_input(7)
for line in data:
    opcode = line.split(',')

sequences = list(itertools.permutations([0,1,2,3,4], 5))

def run_sequence(opcode, sequence):
    a = intcode(opcode, [sequence[0],0])
    b = intcode(opcode, [sequence[1], a[0]])
    c = intcode(opcode, [sequence[2], b[0]])
    d = intcode(opcode, [sequence[3], c[0]])
    return intcode(opcode, [sequence[4], d[0]])

def find_max_output(sequences):
    m = 0
    for s in sequences:
        o = int(run_sequence(opcode, s)[0])
        if o > m:
            m = o
    return m

print(find_max_output(sequences))
