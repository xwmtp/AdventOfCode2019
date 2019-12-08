# https://adventofcode.com/2019/day/2

def run_program(noun, verb, program):
    intcode = program.copy()
    intcode[1] = noun
    intcode[2] = verb
    return compute(intcode)[0]


def compute(intcode):
    pos = 0

    while pos < len(intcode):

        num = intcode[pos]
        if num == 1:
            intcode[intcode[pos + 3]] = intcode[intcode[pos + 1]] + intcode[intcode[pos + 2]]
        if num == 2:
            intcode[intcode[pos + 3]] = intcode[intcode[pos + 1]] * intcode[intcode[pos + 2]]
        if num == 99:
            return intcode

        pos = pos + 4

def find_inputs_for_value(value):
    for noun in range(0, 100):
        for verb in range(0, 100):
            output = run_program(noun, verb, intcode)
            if output == value:
                return noun, verb


f = open("Input2.txt")

input_string = f.read()
f.close()

intcode = [int(i) for i in input_string.split(',')]

noun, verb = find_inputs_for_value(19690720)

print(100 * noun + verb)
