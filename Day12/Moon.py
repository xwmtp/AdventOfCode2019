class Moon:

    def __init__(self, x, y, z):
        self.position = {'x': x, 'y': y, 'z': z}
        self.velocity = {'x': 0, 'y': 0, 'z': 0}

    def __str__(self):
        def dct_to_str(dct):
            items = [f"{k}={' ' * (3 - len(str(v)))}{v}" for k, v in dct.items()]
            return ', '.join(items)
        return f'pos <{dct_to_str(self.position)}>, vel <{dct_to_str(self.velocity)}>'

    def __copy__(self):
        copy_moon = Moon(self.position['x'], self.position['y'], self.position['z'])
        copy_moon.velocity = self.velocity.copy()
        return copy_moon

    def equal_on_axis(self, axis, other):
        return self.position[axis] == other.position[axis] and self.velocity[axis] == other.velocity[axis]

    def apply_velocity(self):
        for axis in ['x', 'y', 'z']:
            self.position[axis] += self.velocity[axis]

    def total_energy(self):
        potential_energy = sum([abs(pos) for pos in self.position.values()])
        kinetic_energy   = sum([abs(vel) for vel in self.velocity.values()])
        return potential_energy * kinetic_energy