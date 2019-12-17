# https://adventofcode.com/2019/day/14

f = open("Input14.txt")

inputs = f.read().splitlines()
f.close()

print(inputs)


#inputs = ['157 ORE => 5 NZVS', '165 ORE => 6 DCFZ', '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL', '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ', '179 ORE => 7 PSHF', '177 ORE => 5 HKGWZ', '7 DCFZ, 7 PSHF => 2 XJWVT', '165 ORE => 2 GPVTF', '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT']

def chem_tuple(string):
    num, chem = string.split(' ')
    return (chem, int(num))

rules = dict()
for rule in inputs:
    chem_inputs, chem_output = rule.split(' => ')
    chem_inputs = [chem_tuple(chem) for chem in chem_inputs.split(', ')]
    chem_output, chem_output_num = chem_tuple(chem_output)
    rules[chem_output] = (chem_output_num, chem_inputs)

print(rules)


class Chem_calculator:

    def __init__(self, rules):
        self.rules = rules

    def ore_required(self):
        list = self.rules['FUEL']


        self.fulfill_requirements(inputs, dict())



    def fulfill_requirements(self, chem_tuples_needed, chem_tuples_own):
        for needed, chem in chem_tuples_needed:
            amount, inputs = self.rules[chem]
            if 




    def tuple_lookup(self, tuples, c):
        for num, chem in tuples:
            if chem == c:
                return num



calculator = Chem_calculator(rules)
#calculator.ore_required()

