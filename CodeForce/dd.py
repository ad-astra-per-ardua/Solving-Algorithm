a = int(input())

def remove_duplicates_keep_one(arr):
    unique_elements = []
    for element in arr:
        if arr.count(element) == 1:
            unique_elements.append(element)
    return unique_elements

for _ in range(a):
    str_input = input()
    ele = list(str_input)
    unique_chars = list(set(ele))
    temp2 = list(set(ele))
    temp = remove_duplicates_keep_one(str_input)
    a_sub_b = [x for x in temp2 if x not in temp]
    if len(a_sub_b) >= 2:
        print('yes')
    else:
        print('no')