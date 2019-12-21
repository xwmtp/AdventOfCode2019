# https://adventofcode.com/2019/day/20

from Maze import Maze
from Recursive_maze import Recursive_maze

f = open("Input20.txt")
inputs = f.read()
f.close()




# --- Part 1 ---

#maze = Maze(inputs)


#path = maze.a_star.search(maze.start, maze.end, maze)
#print(len(path)-1)

# --- Part 2 ---

def print_levels(considered):
    i = 0
    considered_i = [t[0] for t in considered if t[1] == i]
    while considered_i:
        print('\nLevel:', i)
        maze.print_maze(considered_i)
        considered_i = [t[0] for t in considered if t[1] == i]
        i += 1

maze = Recursive_maze(inputs)

import time
now = time.time()
path = maze.a_star.search((maze.start, 0), (maze.end, 0), maze)
print(time.time() - now)


max_level = max(path, key=lambda t: t[1])
print('Max level:', max_level)

print(path)
print(len(path)-1)

# 396