#!/usr/bin/python
import os
print(os.path.abspath('.'))

# Open a file
file = open("input.txt", "r")

solution_msg = []

stacks = [
    ['D','L','J','R','V','G','F'],
    ['T','P','M','B','V','H','J','S'],
    ['V','H','M','F','D','G','P','C'],
    ['M','D','P','N','G','Q'],
    ['J','L','H','N','F'],
    ['N','F','V','Q','D','G','T','Z'],
    ['F','D','B','L'],
    ['M','J','B','S','V','D','N'],
    ['G','L','D']
]

for line in file:
    line = line.replace("\n", "")

    steps = line.split(' ')

    step_move = int(steps[1])
    step_from = int(steps[3])
    step_to = int(steps[5])

    # print(f"move = {step_move}")
    # print(f"from = {step_from}")
    # print(f"to = {step_to}")
    
    for x in range(0,step_move):
        # print(f'From stack: {stacks[step_from-1]}')
        # print(f'To stack: {stacks[step_to-1]}')

        stacks[step_to-1].append(stacks[step_from-1].pop())
        
        # print(f'From stack: {stacks[step_from-1]}')
        # print(f'To stack: {stacks[step_to-1]}')

for stack in stacks:
    solution_msg.append(stack[-1])

# Close opend file
file.close()

print(f'Stacks: {stacks} \n')
print(f'Solution of Part1: {"".join(solution_msg)}')


