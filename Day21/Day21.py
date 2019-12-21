# https://adventofcode.com/2019/day/20

from Intcode_computer import Intcode_computer

f = open("Input21.txt")
inputs = f.read()
f.close()

code = [int(i) for i in inputs.split(',')]


def nums_to_string(outputs):
    string = ''
    for c in outputs:
        try:
            string += chr(c)
        except ValueError:
            string += str(c)
    return string

def string_to_nums(string):
    return [ord(c) for c in string]


def execute_program(program):
    computer = Intcode_computer(code)
    computer.compute([])
    for instruction in program:
        nums = string_to_nums(instruction + '\n')
        computer.compute(nums)
        print(nums_to_string(computer.outputs))

def parse_program(program, bools_dict):
    """Debugger which prints the result of each program step, given start parameters."""
    bools = {'A':True,'B':True,'C':True,'D':True,'T':False,'J':False}
    bools.update(bools_dict)
    print(bools)
    for instruction in program:
        parts = instruction.split(' ')
        if parts[0] == 'WALK':
            return
        instr, arg0, arg1 = parts[0], parts[1], parts[2]
        if instr == 'NOT':
            new_bool = not bools[arg0]
            print(f'{instruction}: {arg1}={new_bool}')
        elif instr == 'OR':
            new_bool = bools[arg0] or bools[arg1]
            print(f'{instruction} : {arg1}={new_bool}')
        elif instr == 'AND':
            new_bool = bools[arg0] and bools[arg1]
            print(f'{instruction}: {arg1}={new_bool}')
        bools[arg1] = new_bool

# --- Part 1 ---

program = [
    'NOT A T',
    'NOT B J',
    'OR T J',
    'NOT C T',
    'OR T J',
    'AND D J',
    'WALK'
]

execute_program(program)



# --- Part 2 ---

program_2 = [
    'NOT A T',
    'NOT B J',
    'OR T J',
    'NOT C T',
    'OR T J',
    'AND D J',
    'NOT E T',
    'NOT T T',
    'OR H T',
    'AND T J',
    'RUN'
]

execute_program(program_2)








