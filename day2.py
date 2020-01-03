from helpers import *
data = get_input(2)
for line in data:
    opcode = line.split(',')
    opcode = [int(i) for i in opcode]
opcode[1], opcode[2] = 12, 2

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


print(opcode[0])
