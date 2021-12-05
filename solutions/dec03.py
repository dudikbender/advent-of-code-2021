import pandas as pd

df = pd.DataFrame()

with open('/Users/davidbender/Desktop/advent-of-code-2021/inputs/dec03.txt','r') as file:
    lines = file.readlines()
    data = []
    for line in list(lines):
        clean_line = line.rstrip('\n')
        data.append(clean_line)

def convert_reading(reading: int, threshold: float = 0.5, gamma:bool = True):
    if gamma:
        if reading > threshold:
            result = 1
        else:
            result = 0
    else:
        if reading > threshold:
            result = 0
        else:
            result = 1
    return result

def generate_reading(data_list: list, gamma: bool = True):
    results = []
    for i in range(12):
        digits = [ int(x[i]) for x in data ]
        reading  = sum(digits) / len(data)
        result = convert_reading(reading, gamma=gamma)
        results.append(str(result))
    return int(''.join(results),2)

gamma = generate_reading(data, gamma=True)
epsilon = generate_reading(data, gamma=False)
print(gamma * epsilon)