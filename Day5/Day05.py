# https://adventofcode.com/2019/day/5

from Intcode_computer import Intcode_computer


f = open("Input05.txt")

program_string = f.read()
f.close()

code_chars = program_string.split(',')
code = [int(i) for i in code_chars]


# --- Part 1 ---

computer = Intcode_computer()
output = computer.compute(code, 1)
print(output[-1])

# --- Part 2 ---

computer = Intcode_computer()
output = computer.compute(code, 5)
print(output[-1])