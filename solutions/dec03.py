with open('/Users/davidbender/Desktop/advent-of-code-2021/inputs/dec03.txt','r') as file:
    lines = file.readlines()
    data = []
    for line in list(lines):
        clean_line = line.rstrip('\n')
        data.append(clean_line)

def convert_reading(reading: int, threshold: float = 0.5, most_common:bool = True):
    if most_common:
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

def generate_reading(data: list, gamma: bool = True):
    results = []
    for i in range(12):
        digits = [ int(x[i]) for x in data ]
        reading  = sum(digits) / len(data)
        result = convert_reading(reading, most_common=gamma)
        results.append(str(result))
    return int(''.join(results),2)

gamma = generate_reading(data, gamma=True)
epsilon = generate_reading(data, gamma=False)
#print(gamma * epsilon)

def rating_reader(starting_list: list, oxygen: bool = True):
    data = starting_list
    results = []
    for i in range(12):
        digits = [ int(x[i]) for x in data ]
        reading  = sum(digits) / len(data)
        result = convert_reading(reading, most_common=oxygen)
        print(result)
        results.append(str(result))
        
        new_data = []
        for entry in data:
            if entry[i] == result:
                new_data.append(entry)
        data = new_data
    return int(''.join(results),2)

oxygen = rating_reader(data, oxygen=True)
co2 = rating_reader(data, oxygen=False)
print(oxygen * co2)