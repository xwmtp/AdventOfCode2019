# https://adventofcode.com/2019/day/6

import queue


class Orbit_counter():

    def count_orbits(self, orbits):
        self.orbits = orbits
        count = 0
        for a in orbits.keys():
            count += self.count_to_com(a, 0)
        return count

    def count_to_com(self, a, count):
        if a == 'COM':
            return count
        else:
            count += 1
            return self.count_to_com(self.orbits[a], count)




f = open("Input06.txt")
string = f.read()
f.close()

orbit_tuples = [i.split(')') for i in string.split('\n')]

# -- Part 1 ---

orbits_dict = dict()
for (x, y) in orbit_tuples:
    orbits_dict[y] = x

counter = Orbit_counter()
print(counter.count_orbits(orbits_dict))

# --- Part 2 ---

# put orbits in both directions, to create 'graph'
orbits_graph = dict()
for (x, y) in orbits_graph:
    orbits_dict[y] = [x]
for (x, y) in orbits_graph:
    if x != 'COM':
        orbits_dict[x].append(y)

# breadth first search
q = queue.Queue()
state = (orbits_graph['YOU'][0], 0)
seen = []

while True:
    if state[0] != 'COM':
        if 'SAN' in orbits_graph[state[0]]:
            break
        for kid in orbits_graph[state[0]]:
            if kid not in seen:
                q.put((kid, state[1]+1))
    state = q.get()
    seen.append(state[0])

print(state[1])