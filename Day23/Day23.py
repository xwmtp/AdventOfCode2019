# https://adventofcode.com/2019/day/23

import queue
from Intcode_computer import Intcode_computer

f = open("Input23.txt")
inputs = f.read()
f.close()

code = [int(i) for i in inputs.split(',')]


class Network:
    def __init__(self, use_nat=True, size=50):
        self.queues = dict()
        for i in range(size):
            self.queues[i] = queue.Queue()
        self.queues[255] = queue.Queue()
        self.computers = [Network_computer(i, self.queues) for i in range(size)]
        self.nat = None
        if use_nat:
            self.nat = NAT(255, self.queues)

    def run(self):
        while True:
            for computer in self.computers:
                out = computer.step()
                if out and not self.nat:
                    return out
            if self.nat:
                out = self.nat.step()
                if out:
                    return out




class Network_computer:

    def __init__(self, id, queues):
        self.id = id
        self.computer = Intcode_computer(code, return_outputs=True)
        self.computer.compute([id])
        self.queues = queues

    def step(self):
        if not self.queues[self.id].empty():
            x, y = self.queues[self.id].get(block=False)
            inputs = [x,y]
        else:
           inputs = [-1]
        outputs = self.get_output(inputs)
        if outputs:
            self.queues[outputs[0]].put((outputs[1], outputs[2]))
            if outputs[0] == 255:
                return outputs[2]

    def get_output(self, input):
        outputs = []
        for _ in range(3):
            output = self.computer.compute(input)
            if not output:
                return
            outputs.append(output)
        return outputs


class NAT:

    def __init__(self, id, queues):
        self.id = id
        self.queues = queues
        self.packet = None
        self.last_packet_sent = None

    def step(self):
        if not self.queues[self.id].empty():
            self.packet = self.queues[self.id].get(block=False)

        if self.queues_idle():
            if self.packet == self.last_packet_sent:
                return self.packet[1]
            self.queues[0].put(self.packet)
            self.last_packet_sent = self.packet


    def queues_idle(self):
        for _, queue in self.queues.items():
            if not queue.empty():
                return False
        return True


# --- Part 1 ---
network = Network(use_nat=False)
print(network.run())

# --- Part 2 ---
network = Network(use_nat=True)
print(network.run())