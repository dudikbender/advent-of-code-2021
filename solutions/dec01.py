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
    if first_input > second_input:
        return 0
    else:
        return 1

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
    sliding_section = []
    for item in item_list:
        if len(sliding_section) < window_size:
            sliding_section.append(item)
        else:
            sliding_section = sliding_section[1:]
            sliding_section.append(item)
            sections.append(sliding_section)
    return len(sections)

def part_two_process(list_of_inputs: list):
    number_of_increases = 0
    previous_input = None
    for item in list_of_inputs:
        if not previous_input:
            previous_input = sum(item)
        else:
            section_sum = sum(item)
            change = is_increase(previous_input, section_sum)
            number_of_increases += change
            previous_input = section_sum
    return number_of_increases

sliding_window(clean_data)