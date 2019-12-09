# https://adventofcode.com/2019/day/9
from Intcode_computer import Intcode_computer


f = open("Input9.txt")

input_string = f.read()
f.close()

code = [int(i) for i in input_string.split(',')]


# --- Part 1 ---
computer = Intcode_computer(code)
test_output = computer.compute([1], False)
print(test_output[0])

# --- Part 2 ---
computer = Intcode_computer(code)
output = computer.compute([2], False)
print(output[0])
