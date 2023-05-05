a = int(input())
floor = 1
bee_house = 1

while True:
    if a <= bee_house:
        break
    floor += 1
    bee_house += 6 * (floor - 1)
print(floor)
