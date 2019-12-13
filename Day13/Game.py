
from Intcode_computer import Intcode_computer
from Grid import Grid

class Game:

    def __init__(self, code):
        self.score = 0
        self.steps = 0
        self.grid = Grid(0, {0:'.', 1:'|', 2:'X', 3:'_', 4:'o'})
        self.engine = Intcode_computer(code)
        self.last_input = 'neutral'
        self.play('neutral')

    def play(self, hold):
        positions = ['left', 'neutral', 'right']
        input = positions.index(hold)-1
        self.last_input = hold
        self.engine.compute([input])
        self.parse_outputs(self.engine.outputs)
        self.steps += 1

    def parse_outputs(self, outputs):
        i = 0
        while i < len(outputs) - 2:
            x, y, tile = outputs[i], outputs[i + 1], outputs[i + 2]
            if x == -1:
                self.score = tile
            else:
                self.grid.put((x, -y), tile)
                if tile == 4:
                    self.ball = (x, y)
                if tile == 3:
                    self.paddle = (x, y)
            i += 3

    def __str__(self):
        return f'score: {self.score}, ball: {self.ball}, last input: {self.last_input}\n{self.grid}'
