from helpers import *
data = get_input(5)
for line in data:
    opcode = line.split(',')


def set_mode(mode, i):
    if mode == "1":
        return int(opcode[i])
    if mode == "0":
        return int(opcode[int(opcode[i])])

def get_modes(opcode):
    if len(opcode) == 1:
        return int(opcode), "0", "0"
    if len(opcode) == 3:
        return int(opcode[-1]), opcode[-3], "0"
    if len(opcode) == 4:
        return int(opcode[-1]), opcode[-3], opcode[-4]

i = 0
while i < len(opcode):
    if int(opcode[i]) == 99:
        break
    code, p1, p2 = get_modes(opcode[i])
    if code == 1:
        #add i+1 (either value or refval) ot i+2 (either value or refval) to the index value at i+3
        opcode[int(opcode[i+3])] = str(set_mode(p1, i+1) + set_mode(p2, i+2))
        i += 4
        continue
    if code == 2:
        #mulitply i+1 (either value or refval) ot i+2 (either value or refval) to the index value at i+3
        opcode[int(opcode[i+3])] = str(set_mode(p1, i+1) * set_mode(p2, i+2))
        i += 4
        continue
    if code == 3:
        #set index i+1 to an input
        opcode[int(opcode[i+1])] = input("Press 1: ")
        i += 2
        continue
    if code == 4:
        print(set_mode(p1, i+1))
        i += 2
        continue
