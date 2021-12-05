import pandas as pd

with open('/Users/davidbender/Desktop/advent-of-code-2021/inputs/dec01.txt','r') as file:
    lines = file.readlines()
    data = list(lines)

clean_data = []
for line in data:
    clean_line = line.rstrip('\n')
    clean_data.append(int(clean_line))

# PART ONE
# Function to process the increase / decrease
def is_increase(first_input: int, second_input):
    if second_input > first_input:
        return 1
    else:
        return 0

def part_one_process(list_of_inputs: list):
    number_of_increases = 0
    previous_input = None
    for item in list_of_inputs:
        if not previous_input:
            previous_input = item
        else:
            change = is_increase(previous_input, item)
            number_of_increases += change
            previous_input = item
    return number_of_increases

print(part_one_process(clean_data))

# PART TWO
def sliding_window(item_list: list, window_size: int = 3):
    sections = []
    offset = 0
    for i in range(len(item_list)):
        section = item_list[offset:offset + window_size]
        sections.append(section)
        offset +=1
    return sections

def part_two_process(list_of_inputs: list):
    sections = sliding_window(list_of_inputs)[:-2]
    number_of_increases = 0
    previous_input = None
    for item in sections:
        if not previous_input:
            previous_input = sum(item)
        else:
            section_sum = sum(item)
            change = is_increase(previous_input, section_sum)
            number_of_increases += change
            previous_input = section_sum
    return number_of_increases

print(part_two_process(clean_data))