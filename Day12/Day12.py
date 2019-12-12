# https://adventofcode.com/2019/day/12

from Universe import Universe
from Moon import Moon
import math
import re
from copy import copy



f = open("Input12.txt")

inputs = f.read().splitlines()
f.close()

def parse_moon(string):
    m = re.search(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', string)
    x, y, z = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return Moon(x, y, z)


# --- Part 1 ---

moons = [parse_moon(str) for str in inputs]
universe = Universe(moons)

for _ in range(1000):
    universe.step()
print(universe.total_energy())


# --- Part 2 ---

def lowest_common_multiple(nums):
    lcm = nums[0]
    for i in nums[1:]:
        lcm = int(lcm*i/math.gcd(lcm, i))
    return lcm

def steps_to_repeat_per_axis(universe):
    initial_universe = copy(universe)
    steps_to_repeat = []
    for axis in ['x', 'y', 'z']:
        moons = [parse_moon(str) for str in inputs]
        universe = Universe(moons)
        universe.step()

        while not universe.equal_on_axis(axis, initial_universe):
            universe.step()
        steps_to_repeat.append(universe.steps)
    return steps_to_repeat


moons = [parse_moon(str) for str in inputs]
universe = Universe(moons)

steps_to_repeat = steps_to_repeat_per_axis(universe)

print(lowest_common_multiple(steps_to_repeat))



