string = input()
target = ["U", "C", "P", "C"]
matched = ""
index = 0

for char in string:
    if char == target[index]:
        matched += char
        index += 1
        if index == len(target):
            break

if matched == "UCPC":
    print("I love UCPC")
else:
    print("I hate UCPC")
