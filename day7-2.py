from helpers import *
import itertools
from copy import deepcopy

data = get_input(7)
for line in data:
    opcode = line.split(',')

sequences = list(itertools.permutations([9, 8, 7, 6, 5], 5))

def run_sequence(opcode, sequence):
    #make each amp, and run it's first pass to get the next input to create the next amp
    a = Amp(deepcopy(opcode), sequence[0], 0)
    a.run()
    b = Amp(deepcopy(opcode), sequence[1], a.output)
    b.run()
    c = Amp(deepcopy(opcode), sequence[2], b.output)
    c.run()
    d = Amp(deepcopy(opcode), sequence[3], c.output)
    d.run()
    e = Amp(deepcopy(opcode), sequence[4], d.output)
    e.run()

    while e.halted is False:
        #setup feed back loop and reset command_used to False so it'll continue
        a.command = e.output
        a.command_used = False
        a.run()
        b.command = a.output
        b.command_used = False
        b.run()
        c.command = b.output
        c.command_used = False
        c.run()
        d.command = c.output
        d.command_used = False
        d.run()
        e.command = d.output
        e.command_used = False
        e.run()
    return e.output


def find_max_output(sequences):
    m = 0
    for s in sequences:
        o = int(run_sequence(opcode, s))
        if o > m:
            m = o
    return m


print(find_max_output(sequences))

