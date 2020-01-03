from helpers import *
import copy
data = get_input(2)
for line in data:
    opcode = line.split(',')
    base_input = [int(i) for i in opcode]

def get_output(noun, verb, opcode):
    opcode[1], opcode[2] = noun, verb
    i = 0
    while i < len(opcode):
        if opcode[i] == 99:
            break
        if opcode[i] == 1:
            #add i+1 and i+2, set to i+3
            opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
            i += 4
            continue
        if opcode[i] == 2:
            #mult i+1 and i+2, set to i+3
            opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]
            i += 4
            continue
        else:
            print(f"error: opcode is {opcode[i]}")
            return -1
    return opcode[0]

target = 19690720
output = 0
for i in range(100):
    for j in range(100):
        if target == get_output(i, j, copy.deepcopy(base_input)):
            print(i,j)
            break

