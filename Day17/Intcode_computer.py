class Intcode_computer:

    def __init__(self, intcode=None, extra_memory=1e4):
        self.outputs = []
        self.halted = False
        if not intcode:
            intcode = []
        self.code = intcode.copy() + ([0] * int(extra_memory))
        self.pos = 0
        self.rel_base = 0
        self.mode_dict = {
            0: 'pos',
            1: 'imm',
            2: 'rel'
        }

    def __copy__(self):
        comp_copy = Intcode_computer(self.code.copy())
        comp_copy.outputs = self.outputs
        comp_copy.halted = self.halted
        comp_copy.pos, comp_copy.rel_base = self.pos, self.rel_base
        return comp_copy


    def parse_instruction_number(self, num):
        num = str(num)
        num = '0' * (5 - len(num)) + num

        opcode = int(num[-2:])
        param_modes = [int(n) for n in num[:-2]]
        param_modes.reverse()
        return param_modes, opcode

    def read_args(self):
        args = []
        for i in range(len(self.modes)):
            index = self.pos + 1 + i
            if index >= len(self.code):
                break
            args.append(self.code[index])
        self.args = args

    # retrieve ith argument and convert it according to current mode
    def get_arg(self, i):
        mode = self.modes[i]
        arg = self.args[i]
        # relative mode
        if mode == 2:
            arg = arg + self.rel_base
        # position/relative mode
        if mode != 1:
            arg = self.code[arg]
        return arg

    # retrieve ith argument, and write to the corresponding address in the code (according to current mode)
    def write_to_arg(self, i, value):
        arg = self.args[i]
        # relative mode
        if self.modes[i] == 2:
            arg = arg + self.rel_base
        self.code[arg] = value



    def compute(self, inputs, return_outputs=False):
        self.outputs = []

        while self.pos < len(self.code):
            self.modes, opcode = self.parse_instruction_number(self.code[self.pos])

            # read in args on next
            self.read_args()


            if opcode == 1:
                self.write_to_arg(2, self.get_arg(0) + self.get_arg(1))
                self.pos = self.pos + 4

            elif opcode == 2:
                self.write_to_arg(2, self.get_arg(0) * self.get_arg(1))
                self.pos = self.pos + 4

            elif opcode == 3:
                if inputs == []:
                    return
                val = inputs.pop(0)
                self.write_to_arg(0, val)
                self.pos = self.pos + 2

            elif opcode == 4:
                #print(f'Outputted {self.get_arg(0)}')
                self.outputs.append(self.get_arg(0))
                self.pos = self.pos + 2
                if return_outputs:
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
                self.write_to_arg(2, 1 if self.get_arg(0) < self.get_arg(1) else 0)
                self.pos = self.pos + 4

            elif opcode == 8:
                self.write_to_arg(2, 1 if self.get_arg(0) == self.get_arg(1) else 0)
                self.pos = self.pos + 4

            elif opcode == 9:
                self.rel_base += self.get_arg(0)
                self.pos = self.pos + 2

            elif opcode == 99:
                self.halted = True
                return

            else:
                raise IndexError(f'Opcode {opcode} is not a valid number!')
