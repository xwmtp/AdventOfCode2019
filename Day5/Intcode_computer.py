class Intcode_computer:

    def __init__(self):
        self.outputs = []

    def parse_instruction_number(self, num):
        num = str(num)
        num = '0' * (5 - len(num)) + num

        opcode = int(num[-2:])
        param_modes = [int(n) for n in num[:-2]]
        param_modes.reverse()
        return param_modes, opcode

    # get arg AND check mode
    def get_arg(self, i):
        # pos mode
        arg = self.args[i]
        if not self.modes[i]:
            arg = self.code[arg]
        return arg

    def read_args(self):
        args = []
        for i in range(len(self.modes)):
            index = self.pos + 1 + i
            if index >= len(self.code):
                break
            args.append(self.code[index])
        self.args = args


    def compute(self, intcode, input_val):
        self.code = intcode.copy()
        self.pos = 0

        while self.pos < len(self.code):
            self.modes, opcode = self.parse_instruction_number(self.code[self.pos])
            self.read_args()

            if opcode == 1:
                self.code[self.args[2]] = self.get_arg(0) + self.get_arg(1)
                self.pos = self.pos + 4
            elif opcode == 2:
                self.code[self.args[2]] = self.get_arg(0) * self.get_arg(1)
                self.pos = self.pos + 4
            elif opcode == 3:
                self.code[self.args[0]] = input_val
                self.pos = self.pos + 2
            elif opcode == 4:
                self.outputs.append(self.get_arg(0))
                self.pos = self.pos + 2
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
                return self.outputs
            else:
                raise IndexError(f'Opcode {opcode} is not a valid number!')

