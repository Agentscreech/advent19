def get_input(day):
    return open(f"inputs/day{day}.txt", "r")
    

class Amp():
    def __init__(self, opcode, sequence, command):
        self.opcode = opcode
        self.sequence = sequence
        self.pointer = 0
        self.command = command
        self.halted = False
        self.output = 0
        self.sequence_set = False
        self.command_used = False

    def set_mode(self, mode, i):
            if mode == "1":
                return int(self.opcode[i])
            if mode == "0":
                return int(self.opcode[int(self.opcode[i])])

    def get_modes(self, opcode):
        if len(opcode) == 1:
            return int(opcode), "0", "0", "0"
        if len(opcode) == 3:
            return int(opcode[-1]), opcode[-3], "0", "0"
        if len(opcode) == 4:
            return int(opcode[-1]), opcode[-3], opcode[-4], "0"
        if len(opcode) == 5:
            return int(opcode[-1]), opcode[-3], opcode[-4], opcode[-5]

    def run(self):
        while self.pointer < len(self.opcode):
            if int(self.opcode[self.pointer]) == 99:
                self.halted = True
                break
            code, p1, p2, p3 = self.get_modes(self.opcode[self.pointer])
            if code == 1:
                #add self.pointer+1 (either value or refval) ot self.pointer+2 (either value or refval) to the index value at self.pointer+3
                self.opcode[int(self.opcode[self.pointer+3])] = str(self.set_mode(p1, self.pointer+1) + self.set_mode(p2, self.pointer+2))
                self.pointer += 4
                continue
            if code == 2:
                #mulitply self.pointer+1 (either value or refval) ot self.pointer+2 (either value or refval) to the index value at self.pointer+3
                self.opcode[int(self.opcode[self.pointer+3])] = str(self.set_mode(p1, self.pointer+1) * self.set_mode(p2, self.pointer+2))
                self.pointer += 4
                continue
            if code == 3:
                #set index self.pointer+1 to an input
                if self.command_used:
                    #we used the current command, and we need to wait for another 
                    break
                if self.sequence_set:
                    self.opcode[int(self.opcode[self.pointer+1])] = self.command
                    self.command_used = True
                else:
                    self.opcode[int(self.opcode[self.pointer+1])] = self.sequence
                    self.sequence_set = True
                self.pointer += 2
                continue
            if code == 4:
                self.output = self.set_mode(p1, self.pointer+1)
                self.pointer += 2
                continue
            if code == 5:
                if self.set_mode(p1, self.pointer+1) != 0:
                    self.pointer = self.set_mode(p2, self.pointer+2)
                    continue
                self.pointer += 3
                continue
            if code == 6:
                if self.set_mode(p1, self.pointer+1) == 0:
                    self.pointer = self.set_mode(p2, self.pointer+2)
                    continue
                self.pointer += 3
                continue
            if code == 7:
                if self.set_mode(p1, self.pointer+1) < self.set_mode(p2, self.pointer+2):
                    self.opcode[int(self.opcode[self.pointer+3])] = "1"
                else:
                    self.opcode[int(self.opcode[self.pointer+3])] = "0"
                self.pointer += 4
                continue
            if code == 8:
                if self.set_mode(p1, self.pointer+1) == self.set_mode(p2, self.pointer+2):
                    self.opcode[int(self.opcode[self.pointer+3])] = "1"
                else:
                    self.opcode[int(self.opcode[self.pointer+3])] = "0"
                self.pointer += 4
                continue
            else:
                raise ValueError(f"bad opcode: {code}")

#classic mode
def intcode(opcode, command):
    def set_mode(mode, i):
        if mode == "1":
            return int(opcode[i])
        if mode == "0":
            return int(opcode[int(opcode[i])])

    def get_modes(opcode):
        if len(opcode) == 1:
            return int(opcode), "0", "0", "0"
        if len(opcode) == 3:
            return int(opcode[-1]), opcode[-3], "0", "0"
        if len(opcode) == 4:
            return int(opcode[-1]), opcode[-3], opcode[-4], "0"
        if len(opcode) == 5:
            return int(opcode[-1]), opcode[-3], opcode[-4], opcode[-5]
    input_used = 0
    i = 0
    output = []
    while i < len(opcode):
        if int(opcode[i]) == 99:
            break
        code, p1, p2, p3 = get_modes(opcode[i])
        if code == 1:
            #add i+1 (either value or refval) ot i+2 (either value or refval) to the index value at i+3
            opcode[int(opcode[i+3])] = str(set_mode(p1, i+1) +
                                           set_mode(p2, i+2))
            i += 4
            continue
        if code == 2:
            #mulitply i+1 (either value or refval) ot i+2 (either value or refval) to the index value at i+3
            opcode[int(opcode[i+3])] = str(set_mode(p1, i+1)
                                           * set_mode(p2, i+2))
            i += 4
            continue
        if code == 3:
            #set index i+1 to an input
            opcode[int(opcode[i+1])] = command[input_used]
            input_used += 1
            i += 2
            continue
        if code == 4:
            # print(set_mode(p1, i+1))
            output.append(set_mode(p1, i+1))
            i += 2
            continue
        if code == 5:
            if set_mode(p1, i+1) != 0:
                i = set_mode(p2, i+2)
                continue
            i += 3
            continue
        if code == 6:
            if set_mode(p1, i+1) == 0:
                i = set_mode(p2, i+2)
                continue
            i += 3
            continue
        if code == 7:
            if set_mode(p1, i+1) < set_mode(p2, i+2):
                opcode[int(opcode[i+3])] = "1"
            else:
                opcode[int(opcode[i+3])] = "0"
            i += 4
            continue
        if code == 8:
            if set_mode(p1, i+1) == set_mode(p2, i+2):
                opcode[int(opcode[i+3])] = "1"
            else:
                opcode[int(opcode[i+3])] = "0"
            i += 4
            continue
        else:
            raise ValueError(f"bad opcode: {code}")
    return output
