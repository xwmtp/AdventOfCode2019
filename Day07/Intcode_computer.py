class Intcode_computer:

    def __init__(self, intcode):
        self.outputs = []
        self.code = intcode
        self.pos = 0
        self.halted = False

    def parse_instruction_number(self, num):
        num = str(num)
        num = '0' * (5 - len(num)) + num

        opcode = int(num[-2:])
        param_modes = [int(n) for n in num[:-2]]
        param_modes.reverse()
        return param_modes, opcode

    def mode(self, val, bool):
        # self.pos mode
        if not bool:
            val = self.code[val]
        return val

    # get arg AND check mode
    def get_arg(self, i):
        # pos mode
        arg = self.args[i]
        if not self.modes[i]:
            arg = self.code[arg]
        return arg

    def compute(self, inputs):

        while self.pos < len(self.code):
            num = self.code[self.pos]
            self.modes, opcode = self.parse_instruction_number(num)

            self.args = [self.code[self.pos + 1 + i] if self.pos + 1 + i < len(self.code) - 1 else 'Z' for i in
                         range(len(self.modes))]

            if opcode == 1:
                self.code[self.args[2]] = self.get_arg(0) + self.get_arg(1)
                self.pos = self.pos + 4
            elif opcode == 2:
                self.code[self.args[2]] = self.get_arg(0) * self.get_arg(1)
                self.pos = self.pos + 4
            elif opcode == 3:
                val = inputs.pop(0)
                self.code[self.args[0]] = val
                self.pos = self.pos + 2
            elif opcode == 4:
                self.outputs.append(self.get_arg(0))
                self.pos = self.pos + 2
                return self.get_arg(0)
            elif opcode == 5:
                if self.get_arg(0) != 0:
                    self.pos = self.get_arg(1)
                else:
                    self.pos = self.pos + 3
            elif opcode == 6:
                if self.get_arg(0) == 0:
                    self.pos = self.get_arg(1)
                else:
                    self.pos = self.pos + 3
            elif opcode == 7:
                self.code[self.args[2]] = 1 if self.get_arg(0) < self.get_arg(1) else 0
                self.pos = self.pos + 4
            elif opcode == 8:
                self.code[self.args[2]] = 1 if self.get_arg(0) == self.get_arg(1) else 0
                self.pos = self.pos + 4
            elif opcode == 99:
                self.halted = True
                return self.outputs
            else:
                raise IndexError(f'Opcode {opcode} is not a valid number!')

