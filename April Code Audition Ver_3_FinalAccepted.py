
ssd_dict = {
    '0': [' - ', '| |', '   ', '| |', ' - '],
    '1': ['   ', '  |', '   ', '  |', '   '],
    '2': [' - ', '  |', ' - ', '|  ', ' - '],
    '3': [' - ', '  |', ' - ', '  |', ' - '],
    '4': ['   ', '| |', ' - ', '  |', '   '],
    '5': [' - ', '|  ', ' - ', '  |', ' - '],
    '6': [' - ', '|  ', ' - ', '| |', ' - '],
    '7': [' - ', '  |', '   ', '  |', '   '],
    '8': [' - ', '| |', ' - ', '| |', ' - '],
    '9': [' - ', '| |', ' - ', '  |', ' - '],
}


number = list(input().strip()) #Added strip() for sample2's input blank but in that case number gose to seperately used list() function

height, width = map(int, input().split())


def segment(num, height, width):
    result = [] # A list to return

    for i in range(5):  # Values of 'ssd_dict' are lists of length == 5
        line = ssd_dict[num][i] # Each element of ssd_dict value becomes 'line'
        if i % 2 == 0:  # Indices 0, 2, 4 (= even numbers) represent horizontal stripes -> multiply by 'width'
            result.append("{}{}{}".format(line[0], line[1:-1] * width, line[-1]))
        else:   # Indices 1, 3 (= odd numbers) represent vertical stripes -> multiply by 'width' and repeat this procedure for 'height' times
            for i in range(height):
                result.append("{}{}{}".format(line[0], line[1:-1] * width, line[-1]))

    return result


results = []
for num in number:
    results.append(segment(num, height, width))


for i in range(len(results[0])):
    print(" ".join(result[i] for result in results)) #Added ' ' (blank) for same for sample output but discard.
