# https://adventofcode.com/2019/day/11

from Intcode_computer import Intcode_computer
from Droid import Robot


def run_robot(robot, intcode):
    computer = Intcode_computer(intcode)

    while True:
        current_color = robot.read_color()
        new_color = computer.compute([current_color], return_outputs=True)
        new_direction = computer.compute([], return_outputs=True)
        if computer.halted:
            return

        robot.paint(new_color)
        new_direction = 'R' if new_direction else 'L'
        robot.update_heading(new_direction)
        robot.move()


f = open("Input11.txt")
input_string = f.read()
f.close()

code = [int(i) for i in input_string.split(',')]


# --- Part 1 ---

robot = Robot()
run_robot(robot, code)
print(len(robot.painted_panels))


# --- Part 2 ---

robot = Robot()
robot.grid.put((0,0), 1)
run_robot(robot, code)
robot.grid.print({1: 'O', 0: ' '})




