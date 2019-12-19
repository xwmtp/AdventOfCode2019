# https://adventofcode.com/2019/day/19

from Intcode_computer import Intcode_computer
from Grid import Grid

f = open("Input19.txt")
inputs = f.read()
f.close()

code = [int(i) for i in inputs.split(',')]



# --- Part 1 ---

class Beam():

    def __init__(self, code, x_range=50, y_range=50):
        self.count = 0
        self.code = code
        self.beam_starts = dict()
        self.beam_ends = dict()
        self.grid = self.parse_grid(x_range, y_range)


    def parse_grid(self, x_range, y_range):
        grid = Grid(' ')
        for y in range(y_range):
            prev_in_beam = False
            for x in range(x_range):

                if self.in_beam(x,y):
                    if not prev_in_beam:
                        self.beam_starts[y] = x
                        prev_in_beam = True
                    symbol = '#'
                    self.count += 1
                else:
                    if prev_in_beam:
                        self.beam_ends[y] = x - 1
                        prev_in_beam = False
                    symbol = '.'
                grid.put((x, -y), symbol)

    def in_beam(self, x, y):
        computer = Intcode_computer(self.code)
        output = computer.compute([x, y], return_outputs=True)
        return output == 1

beam = Beam(code)
print(beam.count)


# --- Part 2 ---

def beam_start(row):
    return row + 1 + (row - 1)//12

def beam_end(row):
    return row + (row)//3

def beam_length(row):
    return beam_end(row) - beam_start(row)


def find_fit(ship_size):
    row = 0
    while True:
        ship_top_left_x = beam_end(row) - ship_size + 1
        bottom_fits = beam_start(row+ship_size-1) == ship_top_left_x
        if bottom_fits:
            return ship_top_left_x, row
        row += 1

top_left_x, top_left_y = find_fit(100)
print(10000 * top_left_x + top_left_y)
