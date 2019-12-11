# https://adventofcode.com/2019/day/3

import sys

def coords(wire, val, coordinates):
    """Walk through wire step by step, and save 'val' for the current x,y position in the coordinates dictionary
       Returns a list of all coordinates along the wire (trace) and the dictionary with 'val' at each x, y coordinate (coordinates)."""
    x = 0
    y = 0
    trace = []
    for step in wire:
        direction = step[0]
        step_size = int(step[1:])
        for i in range(1, step_size + 1):
            if direction == 'R':
                x = x + 1
            if direction == 'L':
                x = x - 1
            if direction == 'U':
                y = y + 1
            if direction == 'D':
                y = y - 1

            trace.append((x,y))
            if x not in coordinates.keys():
                coordinates[x] = dict()
            if y not in coordinates[x].keys():
                coordinates[x][y] = set()
            coordinates[x][y].add(val)
    return trace, coordinates

def get_point(x, y, dct):
    if x in dct.keys():
        if y in dct[x].keys():
            return dct[x][y]

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1-x2) + abs(y1-y2)


def find_closest_intersect(coords, debug=False):
    """Looks for intersection by trying coordinates with increasing Manhatten distance from the origin."""
    dist = 1
    while True:
        if debug and dist%100 == 0:
            print('dist:', dist)
        for i in range(dist+1):
            for x_sign in [1, -1]:
                x = i * x_sign
                if x == 0 and x_sign == -1:
                    continue
                for y_sign in [1,-1]:
                    y = (dist - i) * y_sign
                    if y == 0 and y_sign == -1:
                        continue
                    coord = get_point(x,y,coords)
                    if coord and len(coord) > 1:
                        return (x,y)
        dist +=1

def steps_to_intersects(trace, coords):
    """Returns list with all intersects of a traced wire with the other wire, and how many steps along the wire
       you need to take to get to the intersect."""
    intersects = []
    steps = 1
    for i, point in enumerate(trace):
        x, y = point
        vals = get_point(x,y, coords)
        if vals:
            if len(vals) > 1:
                intersects.append((steps, (x,y)))
        steps = steps+1
    return intersects

def minimum_steps_to_intersect(intersects1, intersects2):
    steps = sys.maxsize

    for it1 in intersects1:
        for it2 in intersects2:
            if it1[1] == it2[1]:
                sum_steps = it1[0] + it2[0]
                if sum_steps < steps:
                    steps = sum_steps
    return steps


f = open("Input03.txt")

input = f.readlines()
f.close()

wire1 = input[0].strip().split(',')
wire2 = input[1].strip().split(',')

# --- Part 1 --- #

trace_w1, coords_dict = coords(wire1, '1', dict())
trace_w2, coords_dict = coords(wire2, '2', coords_dict)

closest_intersect = find_closest_intersect(coords_dict)
print(manhattan_distance(closest_intersect, (0,0)))


# --- Part 2 --- #

intersect_steps_w1 = steps_to_intersects(trace_w1, coords_dict)
intersect_steps_w2 = steps_to_intersects(trace_w2, coords_dict)

min_steps = minimum_steps_to_intersect(intersect_steps_w1, intersect_steps_w2)
print(min_steps)




