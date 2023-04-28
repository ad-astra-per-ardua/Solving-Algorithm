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
    '9' :[' - ', '| |', ' - ', '  |', ' - '],
}

number = input("Enter the number: ").strip()
height, width = map(int, input().strip().split())


def segment(num, height, width):
    result = []

    for i in range(5):
        line = ssd_dict[num][i]
        if i % 2 == 0:
            result.append("{}{}{}".format(line[0], line[1:-1] * width, line[-1]))
        else:
            for _ in range(height):  # changed i to _ since i is already being used in the outer loop
                result.append("{}{}{}".format(line[0], line[1:-1] * width, line[-1]))

    return result

results = []
for num in number:
    results.append(segment(num, height, width))

for i in range(len(results[0])):
    print(" ".join(result[i] for result in results))
