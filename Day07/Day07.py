# https://adventofcode.com/2019/day/7

from Intcode_computer import Intcode_computer
import itertools

f = open("Input07.txt")
program_string = f.read()
f.close()

code = [int(i) for i in program_string.split(',')]

# --- Part 1 ---
max_output = 0

for phase in itertools.permutations(range(5)):

    output = 0
    for i in range(5):
        amp = Intcode_computer(code)
        output = amp.compute([phase[i], output])
    if output > max_output:
        max_output = output

print(max_output)


# --- Part 2 ---

def loop_amps(amps, output):
    thruster_output = output
    while True:
        for i in range(5):
            amp_comp = amps[i]
            output = amp_comp.compute([output])
            if amp_comp.halted:
                return thruster_output
        thruster_output = output

max_output = 0
for phase in itertools.permutations(range(5,10)):
    thruster_output = 0
    output = 0

    # initialize amps
    amps = []
    for i in range(5):
        amp = Intcode_computer(code)
        amps.append(amp)
        output = amp.compute([phase[i], output])

    # loop amps
    thruster_output = loop_amps(amps, output)
    if thruster_output > max_output:
        max_output = thruster_output

print(max_output)
