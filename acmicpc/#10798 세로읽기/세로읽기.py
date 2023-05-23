import sys
input = sys.stdin.readline

matA = []
sol = []
for _ in range(6):
    matA.append(list(str(input().strip())))


for i in range(15): # due to loop standard position can't always be max value, fixed to max integer
    for e in range(5):
        try:
            sol.append(matA[e][i])  # if matA[e][i]'s argument is existed, append it to sol list
        except IndexError:
            continue                # Other case, it occurs IndexError index by out of range in that case skip that loop.

print("".join(sol),end="")          # print all exists arguments gathered maxtix sol's argument in one line without any blank.