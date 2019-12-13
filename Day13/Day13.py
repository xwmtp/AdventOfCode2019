# https://adventofcode.com/2019/day/13


from Game import Game
from AI import AI

f = open("Input13.txt")
input_string = f.read()
f.close()

code = [int(i) for i in input_string.split(',')]





# --- Part 2 ---
code[0] = 2
game = Game(code)

AI = AI(game)
score = AI.play()
print(score)