import math

class Chem_calculator:

    def __init__(self, rules):
        self.rules = rules
        self.chems_own = self.empty_own_dict()
        self.ores = 0

    def ore_required(self, fuel=1):
        self.reset()
        chems_needed = self.rules['FUEL'][1]
        chems_needed = self.multiply_dict(chems_needed, fuel)

        while chems_needed:
            chems_needed = self.fulfill_requirements(chems_needed)

        return self.ores

    def reset(self):
        self.chems_own = self.empty_own_dict()
        self.ores = 0


    def fulfill_requirements(self, chems_needed):
        new_chems_needed = dict()
        for chem, needed in chems_needed.items():

            chem_amount, inputs = self.rules[chem]

            multiplier, own = self.chem_multiplier(chem_amount, needed, self.chems_own[chem])
            self.chems_own[chem] = own
            if multiplier != 0:
                mult_inputs = self.multiply_dict(inputs, multiplier)
                self.add_new_chems(new_chems_needed, mult_inputs)

        return new_chems_needed

    def chem_multiplier(self, amount, needed, own):
        multiplier = 0
        if own >= needed:
            own -= needed
            return multiplier, own

        multiplier = math.floor(needed / amount)
        needed -= amount * multiplier

        if needed == 0:
            return multiplier, own

        if own >= needed:
            own -= needed
            return multiplier, own

        return multiplier + 1, own + amount - needed

    def multiply_dict(self, dct, multiplier):
        mult_dct = dict()
        for key, value in dct.items():
            mult_dct[key] = value * multiplier
        return mult_dct

    def add_new_chems(self, chems, inputs):
        for new_chem, new_amount in inputs.items():
            if new_chem == 'ORE':
                self.ores += new_amount
            else:
                if new_chem in chems.keys():
                    chems[new_chem] += new_amount
                else:
                    chems[new_chem] = new_amount
        return chems

    def empty_own_dict(self):
        dct = dict()
        for chem in self.rules.keys():
            dct[chem] = 0
        return dct