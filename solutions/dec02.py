import pandas as pd

with open('/Users/davidbender/Desktop/advent-of-code-2021/inputs/dec02.txt','r') as file:
    lines = file.readlines()
    data = list(lines)

clean_data = []
for line in data:
    clean_line = line.rstrip('\n')
    clean_data.append(int(clean_line))