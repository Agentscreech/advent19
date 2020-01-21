from helpers import intcode, get_input

# t1 = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
# t2 = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
# t3 = [104, 1125899906842624, 99]
# opcodes = list(map(lambda x: str(x), t3))
opcodes = []
data = get_input(9)
for line in data:
    opcodes = line.split(',')

o = intcode(opcodes, [1])
print(o)
