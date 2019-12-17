from copy import copy
import queue

class Maze_solver:

    def __init__(self, map):
        self.map = map
        self.arrow_map = copy(map)
        self.DIRS = ['N', 'W', 'S', 'E']
        self.queue = queue.Queue()


    def path_to_goal(self):
        start = self.map.find('S')[0]
        end = self.map.find('O')[0]
        self.queue.put((start, 0))
        result = self.walk()
        self.follow_arrows(end, start)
        print(self.arrow_map)
        print('map:')
        print(self.map)
        self.fill_oxygen(end)


    def walk(self):
        while not self.queue.empty():
            pos, dist = self.queue.get()
            if self.map.get(pos) == 'O':
                return (pos, dist)
            #print(pos)
            for dir in self.DIRS:
                next_pos = self.next_position(pos, dir)
                next_tile = self.map.get(next_pos)
                already_visited = self.arrow_map.get(next_pos) in self.DIRS
                if next_tile != '#' and not already_visited:
                    self.queue.put((next_pos, dist + 1))
                    self.arrow_map.put(next_pos, self.get_arrow(dir))
            #print(self.arrow_map)
        print('klaar')
        return (pos, dist)

    def follow_arrows(self, end, start):
        pos = end
        count = 0

        while pos != start:

            dir = self.arrow_map.get(pos)
            pos = self.next_position(pos, dir)
            count+=1
        print('COUNT', count)
        return count

    def fill_oxygen(self, end):
        print('\n++___________________-')
        count = 0
        current_border = [end]
        while current_border != []:
            new_border = []
            for pos in current_border:
                for dir in self.DIRS:
                    next_pos = self.next_position(pos, dir)
                    next_tile = self.map.get(next_pos)
                    if next_tile == '.' or next_tile == 'S':
                        self.map.put(next_pos, 'O')
                        new_border.append(next_pos)
            current_border = new_border
            count+=1

            print(self.map,)
            print(count,'\n')

        print('Bubble count:', count)


    def get_arrow(self, dir):
        idx = self.DIRS.index(dir)
        return self.DIRS[(idx + 2) % 4]




    def next_position(self, pos, direction):
        x, y = pos
        if direction == 'N':
            y += 1
        if direction == 'S':
            y -= 1
        if direction == 'W':
            x -= 1
        if direction == 'E':
            x += 1
        return (x,y)


