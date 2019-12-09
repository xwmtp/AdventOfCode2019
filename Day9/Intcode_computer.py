class Intcode_computer:

    def __init__(self, intcode=None, extra_memory=1e4):
        self.outputs = []
        if not intcode:
            intcode = []
        self.code = intcode + [0] * int(extra_memory)
        self.pos = 0
        self.rel_base = 0
        self.mode_dict = {
            0: 'pos',
            1: 'imm',
            2: 'rel'
        }

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
        if self.debug: print(f'Wrote {value} to position {arg}.')




    def compute(self, inputs, debug=False, return_outputs=False):
        self.debug = debug

        while self.pos < len(self.code):
            self.modes, opcode = self.parse_instruction_number(self.code[self.pos])

            # read in args on next
            self.read_args()

            if debug:
                print('')
                print(self.code[:30])
                print(self.code[self.pos:self.pos + 30])
                print(f'OPCODE {opcode} at pos {self.pos}, rel base {self.rel_base}')
                print('modes', [self.mode_dict[m] for m in self.modes])
                print('args', self.args)

            if opcode == 1:
                if debug: print(f'Added {self.get_arg(0)} and {self.get_arg(1)}.')
                self.write_to_arg(2, self.get_arg(0) + self.get_arg(1))
                self.pos = self.pos + 4

            elif opcode == 2:
                if debug: print(f'Multiplied {self.get_arg(0)} and {self.get_arg(1)}.')
                self.write_to_arg(2, self.get_arg(0) * self.get_arg(1))
                self.pos = self.pos + 4

            elif opcode == 3:
                val = inputs.pop(0)
                self.write_to_arg(0, val)
                self.pos = self.pos + 2

            elif opcode == 4:
                if debug: print(f'Outputted {self.get_arg(0)}.')
                self.outputs.append(self.get_arg(0))
                self.pos = self.pos + 2
                if return_outputs:
                    return self.get_arg(0)

            elif opcode == 5:
                if self.get_arg(0) != 0:
                    if debug: print(
                        f'{self.get_arg(0)} is indeed non-0, so changed position pointer to {self.get_arg(1)}.')
                    self.pos = self.get_arg(1)
                else:
                    if debug: print(f'{self.get_arg(0)} is 0, nothing happens.')
                    self.pos = self.pos + 3

            elif opcode == 6:
                if self.get_arg(0) == 0:
                    if debug: print(
                        f'{self.get_arg(0)} is indeed equal to 0, so changed position pointer to {self.get_arg(1)}.')
                    self.pos = self.get_arg(1)
                else:
                    if debug: print(f'{self.get_arg(0)} is not not 0, nothing happens.')
                    self.pos = self.pos + 3

            elif opcode == 7:
                if debug: print(f'If {self.get_arg(0)} < {self.get_arg(1)}, put 1 at position {self.args[2]}. Else, 0.')
                self.write_to_arg(2, 1 if self.get_arg(0) < self.get_arg(1) else 0)
                self.pos = self.pos + 4

            elif opcode == 8:
                if debug: print(
                    f'If {self.get_arg(0)} == {self.get_arg(1)}, put 1 at position {self.args[2]}. Else, 0.')
                self.write_to_arg(2, 1 if self.get_arg(0) == self.get_arg(1) else 0)
                self.pos = self.pos + 4

            elif opcode == 9:
                if debug: print(f'Added {self.get_arg(0)} to relative base.')
                self.rel_base += self.get_arg(0)
                if debug: print(f'Relative base is now {self.rel_base}.')
                self.pos = self.pos + 2

            elif opcode == 99:
                if debug: print(f'Reached end of program.')
                return self.outputs

            else:
                raise IndexError(f'Opcode {opcode} is not a valid number!')

