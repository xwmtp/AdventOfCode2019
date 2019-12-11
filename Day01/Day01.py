# https://adventofcode.com/2019/day/1

import math

def fuel(mass):
    fuel = 0
    while mass > 0:
        mass = math.floor(mass / 3) - 2
        if mass > 0:
            fuel += mass
    return fuel



f = open("Input01.txt")

fuels = []
for l in f.readlines():
    fuels.append(fuel(int(l)))
f.close()


print('SUM:', sum(fuels))