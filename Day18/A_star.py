class Node():

    def __init__(self, state = None, parent=None):
        self.parent = parent
        self.state = state

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.state == other.state


class A_star:

    def __init__(self):
        self.open = []
        self.closed = []
        self.considered = []


    def search(self, start, end, search_object, return_path=True):
        """search_object has to implement adjacents(node) and distance(node1, node2)."""
        self.open = []
        self.closed = []

        start_node = Node(start, None)
        end_node  = Node(end, None)

        self.open.append(start_node)

        while self.open:
            current_node = min(self.open, key=lambda n: n.f)
            self.considered.append(current_node.state)
            #print('open_1',[(n.state, n.f) for n in self.open])
            #print('current_node (min)', current_node.state, current_node.f)
            self.open.remove(current_node)
            self.closed.append(current_node)
            #print('open_2',[(n.state, n.f) for n in self.open])


            if current_node == end_node:
                print('FOUND!')
                if return_path:
                    return self.backtrack(current_node)
                else:
                    return current_node

            children = search_object.adjacents(current_node.state)
            for child in children:
                child_node = Node(child, current_node)

                #print('closed:',self.closed)
                if child_node in self.closed:
                    #print('in closed:', child_node.state, [n.state for n in self.closed])
                    continue

                child_node.g = current_node.g + 1 #distance between neighbours is always 1
                child_node.h = search_object.distance(child_node.state, end_node.state)
                child_node.f = child_node.g + child_node.h

                for n in self.open:
                    if child_node == n and child_node.g > n.g:
                        continue

                self.open.append(child_node)

    def backtrack(self, node):
        path = []
        current = node
        while current is not None:
            path.append(current.state)
            current=current.parent
        return path[::-1]

    def find_in_open(self, node):
        print(f'find:{node.state}, {node.f}, {node.h}')
        for n in self.open:
            if node == n:
                print('found',n.state, n.f, n.g, n.h)
                return n



