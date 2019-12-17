from Grid import Grid
from Droid import Droid
from Intcode_computer import Intcode_computer
from copy import copy
import time

class Map_creator:

    def __init__(self, code):
        self.map = Grid(' ')
        self.code = code
        self.DIRS = ['N', 'W', 'S', 'E']


    def render_map(self):
        now = time.time()
        computer = Intcode_computer(self.code)
        droid = Droid(computer, self.map)
        self.search(droid)

        print(time.time() - now)
        return self.map


    def search(self, droid):
        for dir in self.DIRS:
            next_tile = droid.check_direction(dir)

            if next_tile == ' ':
                status = droid.try_move(dir)
                if status != 0:
                    if dir != self.DIRS[-1]:
                        new_droid = copy(droid)
                        droid.try_move(self.reverse_dir(dir)) # step back
                        self.search(new_droid)
                    else:
                        self.search(droid)

    def reverse_dir(self, dir):
        idx = self.DIRS.index(dir)
        return self.DIRS[(idx+2)%4]