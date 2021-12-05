import pandas as pd

with open('/Users/davidbender/Desktop/advent-of-code-2021/inputs/dec02.txt','r') as file:
    lines = file.readlines()
    data = list(lines)

clean_data = []
for line in data:
    clean_line = line.rstrip('\n')
    clean_data.append(clean_line)

# PART ONE
# Starting positions
horizontal_one = 0
depth_one = 0

for line in clean_data:
    direction, distance = line.split()
    distance = int(distance)
    if direction == 'forward':
        horizontal_one = horizontal_one + distance
    elif direction == 'up':
        depth_one = depth_one - distance
    else:
        depth_one = depth_one + distance

print(f'Solution 1: {horizontal_one * depth_one}')

# PART TWO
# Starting positions
horizontal_two = 0
depth_two = 0
aim = 0

for line in clean_data:
    direction, distance = line.split()
    distance = int(distance)
    if direction == 'forward':
        horizontal_two = horizontal_two + distance
        depth_two = depth_two + (distance * aim)
    elif direction == 'up':
        aim = aim - distance
    else:
        aim = aim + distance

print('\n')
print(f'Solution 2: {horizontal_two * depth_two}')