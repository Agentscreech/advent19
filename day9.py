from helpers import intcode, get_input

opcodes = []
data = get_input(9)
for line in data:
    opcodes = line.split(',')
opcodes = list(map(lambda x: int(x), opcodes))

p1 = intcode(opcodes, [1])
p2 = intcode(opcodes, [2])
print(p1[0], p2[0])
