# https://adventofcode.com/2019/day/16

from Intcode_computer import Intcode_computer
from Grid import Grid

f = open("Input17.txt")
inputs = f.read()
f.close()

code = [int(i) for i in inputs.split(',')]

class Scaffold_intersections:

    def __init__(self, code):
        computer = Intcode_computer(code)
        computer.compute([])
        self.grid = self.ascii_to_grid(computer.outputs)

    def ascii_to_grid(self, ascii):
        string = ''.join([chr(i) for i in ascii])
        grid = Grid(' ')
        for y, row in enumerate(string.splitlines()):
            for x, char in enumerate(row):
                grid.put((x, -y), char)
        return grid

    def alignment_sum(self):
        intersects = self.get_intersects()
        sum = 0
        for x, y in intersects:
            sum += x * abs(y)
        return sum

    def get_intersects(self):
        intersects = []
        (x1, x2), (y1, y2) = self.grid.range()
        for x in range(x1, x2):
            for y in range(y1, y2):

                if self.is_intersect((x,y)):
                    self.grid.put((x,y), 'O')
                    intersects.append((x,y))
        return intersects



    def is_intersect(self, pos):
        x, y = pos
        for a, b in [(0,1), (0, -1), (1, 0), (-1, 0), (0,0)]:
            if self.grid.get((x+a, y+b)) != '#':
                return False
        return True


scaffold = Scaffold_intersections(code)
alignment_sum = scaffold.alignment_sum()
print(alignment_sum)




class Scaffold_routine:

    def __init__(self, code):
        self.computer = Intcode_computer(code)
        self.routines = {

            'Main' : 'A,B,A,C,A,C,B,C,C,B\n',
            'A'    : 'L,4,L,4,L,10,R,4\n',
            'B'    : 'R,4,L,4,L,4,R,8,R,10\n',
            'C'    : 'R,4,L,10,R,10\n'

            # 'A' : ['L','4','L','4','L','1','0','R','4'],
            # 'B' : ['R','4','L','4','L','4','R','8','R','1','0' ],
            # 'C' : ['R','4','L','1','0','R','1','0']
        }

    def run(self):
        self.computer.compute([])
        self.print_ascii_output(self.computer.outputs)

        self.enter_routines()
        self.computer.compute([ord('n'),ord('\n')])
        self.print_ascii_output(self.computer.outputs)

    def enter_routines(self):
        for routine in self.routines.values():
            for instruction in routine:
                ascii_input = [ord(instr) for instr in instruction]
                self.computer.compute(ascii_input)
            self.print_ascii_output(self.computer.outputs)



    def print_ascii_output(self, ascii):
        print(ascii[-1])
        string = ''.join([chr(i) for i in ascii])

        print(string)




code[0] = 2
routine = Scaffold_routine(code)
routine.run()

