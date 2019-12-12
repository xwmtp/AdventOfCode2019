from itertools import combinations
from copy import copy

class Universe:

    def __init__(self, moons):
        self.moons = moons
        self.steps = 0

    def __str__(self):
        return '\n'.join([str(self.steps)] + [str(moon) for moon in self.moons])

    def __copy__(self):
        copy_system = Universe([copy(m) for m in self.moons])
        copy_system.steps = self.steps
        return copy_system

    def equal_on_axis(self, axis, other):
        if not isinstance(other, Universe) or len(other.moons) != len(self.moons):
            return False
        for i in range(len(self.moons)):
            if not self.moons[i].equal_on_axis(axis, other.moons[i]):
                return False
        return True

    def step(self):
        self.update_velocities()
        self.update_positions()
        self.steps += 1

    def update_velocities(self):
        for moon1, moon2 in combinations(self.moons, 2):
            self.apply_gravity(moon1, moon2)

    def apply_gravity(self, a, b):
        for axis in ['x', 'y', 'z']:
            if a.position[axis] > b.position[axis]:
                a.velocity[axis] -= 1
                b.velocity[axis] += 1
            elif a.position[axis] < b.position[axis]:
                a.velocity[axis] += 1
                b.velocity[axis] -= 1

    def update_positions(self):
        for moon in self.moons:
            moon.apply_velocity()

    def total_energy(self):
        return sum([moon.total_energy() for moon in self.moons])