def solve(Anum, Lnum):
    cowNum = 0
    cknNum = Anum

    while Lnum > cknNum * 2:
        cowNum += 1
        cknNum -= 1
        Lnum -= 4

    return cowNum, cknNum

Anum = int(input())
Lnum = int(input())
cowNum, cknNum = solve(Anum, Lnum)
print(cowNum, cknNum)
