def door_to_dorm(students):
    if len(students) == 1:
        return students[0]

    if len(students) == 2:
        return max(students)

    students.sort()

    time = 0
    while len(students) > 3:
        time += min(students[0] * 2 + students[-2] + students[-1],
                    students[0] + students[1] * 2 + students[-1])
        students.pop(-1)
        students.pop(-1)

    if len(students) == 3:
        time += sum(students)
    elif len(students) == 2:
        time += max(students)

    return time


time_list = input("입력 , 로 구분 ").split(",")
time_list = list(map(int, time_list))

print(door_to_dorm(time_list))
