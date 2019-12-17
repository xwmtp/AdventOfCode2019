from Grid import Grid
from Intcode_computer import Intcode_computer
from copy import copy

class Droid:

    def __init__(self, computer, map):
        self.map = map
        self.computer = computer
        self.position = (0, 0)
        self.map.put(self.position, 'S')
        self.oxygen = None


    def try_move(self, direction):
        movement_command = [' ', 'N', 'S', 'W', 'E'].index(direction)
        status = self.computer.compute([movement_command], return_outputs=True)
        next_position = self.next_position(direction)
        self.update(status, next_position)
        return status

    def check_direction(self, direction):
        target_pos = self.next_position(direction)
        return self.map.get(target_pos)

    def check_current(self):
        return self.map.get(self.position)

    def next_position(self, direction):
        x, y = self.position
        if direction == 'N':
            y += 1
        if direction == 'S':
            y -= 1
        if direction == 'W':
            x -= 1
        if direction == 'E':
            x += 1
        return (x,y)

    def update(self, status, next_pos):
        #print(target_pos, status)
        if status == 0: #wall
            self.map.put(next_pos, '#')
        if status == 1: #empty
            self.position = next_pos
            self.map.put(next_pos, '.')
        if status == 2: #oxygen
            self.position = next_pos
            self.oxygen = next_pos
            self.map.put(next_pos, 'O')

    def __str__(self):
        current = self.map.get(self.position)
        self.map.put(self.position, 'D')
        string = str(self.map)
        self.map.put(self.position, current)
        return str(self.position) + '\n' + string

    def __copy__(self):
        droid_copy = Droid(copy(self.computer), self.map)
        droid_copy.position = self.position
        droid_copy.oxygen = self.oxygen
        return droid_copy





