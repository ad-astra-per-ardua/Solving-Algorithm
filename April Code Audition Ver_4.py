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


number = input()
height, width = map(int, input().split())

"""
함수 segment: num을 받아서, 가로를 width배, 세로를 height배 한 7-segment를 반환하는 함수

"""
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

"""
segment 함수를 입력받은 문자열 내의 모든 글자에 대해 적용해주면 된다.
"""
results = []
for num in number:
    results.append(segment(num, height, width))

"""
join 함수로 같은 줄에 있는 애들을 모두 합쳐서 한 줄로 만들어준다.
이걸 모든 줄에 대해서 해준다.
"""
for i in range(len(results[0])):
    print(" ".join(result[i] for result in results))
