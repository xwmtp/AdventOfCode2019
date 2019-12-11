from Grid import Grid

class Robot():

    def __init__(self):
        self.heading = 'N'
        self.grid = Grid(default_val=0)
        self.painted_panels = set()
        self.pos = (0, 0)

    def read_color(self):
        return self.grid.get(self.pos)

    def paint(self, color):
        if self.read_color() != color:
            self.grid.put(self.pos, color)
            self.painted_panels.add(self.pos)

    def update_heading(self, change):
        directions = ['N', 'E', 'S', 'W']
        idx = directions.index(self.heading)
        if   change == 'R':
            self.heading = directions[(idx + 1) % 4]
        elif change == 'L':
            self.heading = directions[(idx - 1) % 4]

    def move(self, dist=1):
        x, y = self.pos
        if self.heading == 'N':
            y = y + dist
        elif self.heading == 'E':
            x = x + dist
        elif self.heading == 'S':
            y = y - dist
        elif self.heading == 'W':
            x = x - dist
        self.pos = x, y