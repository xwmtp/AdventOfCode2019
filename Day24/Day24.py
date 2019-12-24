# https://adventofcode.com/2019/day/24

from Bug_simulator import Bug_simulator
from Recursive_bug_simulator import Recursive_bug_simulator

f = open("Input24.txt")
inputs = f.read()
f.close()


example = '....#\n#..#.\n#..##\n..#..\n#....'


# --- Part 1 ---

simulator = Bug_simulator(inputs)

while True:
    out = simulator.step()
    if out:
        print(simulator.biodiversity())
        break


# --- Part 2 ---

simulator = Recursive_bug_simulator(inputs)

for i in range(200):
    simulator.step()
print(simulator.count_bugs())