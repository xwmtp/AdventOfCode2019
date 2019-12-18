# https://adventofcode.com/2019/day/14

from Chem_calculator import Chem_calculator
import sys

f = open("Input14.txt")

inputs = f.read().splitlines()
f.close()


def chem_tuple(string):
    num, chem = string.split(' ')
    return (chem, int(num))

rules = dict()
for rule in inputs:
    chem_inputs, chem_output = rule.split(' => ')
    chem_inputs = [chem_tuple(chem) for chem in chem_inputs.split(', ')]
    chem_output, chem_output_num = chem_tuple(chem_output)
    rules[chem_output] = (chem_output_num, dict(chem_inputs))





# --- Part 1 ---

calculator = Chem_calculator(rules)
ores = Chem_calculator.ore_required(calculator)
print(ores)



# --- Part 2 ---

def binary_search(func, l, r, x):
    """Find a value 'mid' for which func(mid) is closest to x, but still smaller than x."""
    min_diff = sys.maxsize
    min_mid = 0

    while l <= r:
        mid = l + (r-l)//2

        found = func(mid)
        diff = abs(found - x)
        if found < x and diff < min_diff:
            min_diff = diff
            min_mid = mid

        if found == x:
            return mid
        elif found < x:
            l = mid + 1
        else:
            r = mid - 1

    return min_mid

def max_fuel(calculator, ores = int(1e12)):
    return binary_search(calculator.ore_required, 0, int(1e10), ores)


ores = calculator.ore_required(fuel = 100)
print(max_fuel(calculator))



