
f = open("Input18.txt")
inputs = f.read()
f.close()

from Grid import Grid
from A_star import A_star
import time
from copy import copy

class Maze:

    def __init__(self, string):
        self.keys = dict()
        self.doors = dict()
        self.grid = self.get_grid(string)
        print('done')
        self.a_star = A_star()

    def get_grid(self, string):
        grid = Grid(' ')
        for y, row in enumerate(string.splitlines()):
            for x, char in enumerate(row):
                if char.islower():
                    self.keys[char] = (x, -y)
                if char.isupper():
                    self.doors[char] = (x, -y)
                if char == '@':
                    self.start = (x, -y)

                grid.put((x, -y), char)
        return grid


    def search(self, start, end):
        now = time.time()
        result = self.a_star.search(start, end, self)
        print(f'Search duration {time.time() - now}')
        return result


    def distance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2)

    def adjacents(self, pos):
        adjacent = []
        x, y = pos
        for neigh in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            neigh_char = self.grid.get(neigh)
            if neigh_char!= '#' and neigh_char != ' ':
                adjacent.append(neigh)
        return adjacent

    def print_grid(self, highlights=None):
        if highlights is None:
            highlights = []
        copy_grid = copy(self.grid)
        for x, y in highlights:
            copy_grid.put((x,y),'O')
        print(copy_grid)






maze = Maze(inputs)
print(maze.start)
print(maze.keys)
print(maze.doors)

path = maze.search(maze.start, maze.doors['X'])
#print(path)
#print(len(path))
maze.print_grid()
print(maze.grid)

print(path)

maze.print_grid(maze.a_star.considered)
maze.print_grid(path)




