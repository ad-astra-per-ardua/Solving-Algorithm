number = input().strip()
col, row = map(int, input().strip().split())


printcol = 2*col+3
totalPrint = []
for _ in range(printcol):
    totalPrint.append("")
for i in number:
    if i=="1":
        totalPrint[0] += " " + " "*row +" "
        for j in range(col):
            totalPrint[1+j] += " " + " "*row + "|"
        totalPrint[1+col] += " " + " "*row +" "
        for j in range(col):
            totalPrint[1+col+1+j] += " " + " "*row + "|"
        totalPrint[1+col+1+col] += " " + " "*row +" "
    elif i=="2":
        totalPrint[0] += " " + "-"*row + " "
        for j in range(col):
            totalPrint[1+j] += " " + " "*row + "|"
        totalPrint[col+1] += " " + "-"*row + " "
        for j in range(col):
            totalPrint[1+col+1+j] += "|" + " "*row + " "
        totalPrint[1+col+1+col] += " " + "-"*row + " "
    elif i=="3":
        totalPrint[0] += " " + "-"*row + " "
        for j in range(col):
            totalPrint[1+j] += " " + " "*row + "|"
        totalPrint[col+1] += " " + "-"*row + " "
        for j in range(col):
            totalPrint[1+col+1+j] += " " + " "*row + "|"
        totalPrint[1+col+1+col] += " " + "-"*row + " "
    elif i=="4":
        totalPrint[0] += " " + " "*row + " "
        for j in range(col):
            totalPrint[1+j] += "|" + " "*row + "|"
        totalPrint[col+1] += " " + "-"*row + " "
        for j in range(col):
            totalPrint[1+col+1+j] += " " + " "*row + "|"
        totalPrint[1+col+1+col] += " " + " "*row + " "
    elif i == "5":
        totalPrint[0] += " " + "-" * row + " "
        for j in range(col):
            totalPrint[1 + j] += "|" + " " * row + " "
        totalPrint[col + 1] += " " + "-" * row + " "
        for j in range(col):
            totalPrint[1 + col + 1 + j] += " " + " " * row + "|"
        totalPrint[1 + col + 1 + col] += " " + "-" * row + " "
    elif i == "6":
        totalPrint[0] += " " + "-" * row + " "
        for j in range(col):
            totalPrint[1 + j] += "|" + " " * row + " "
        totalPrint[col + 1] += " " + "-" * row + " "
        for j in range(col):
            totalPrint[1 + col + 1 + j] += "|" + " " * row + "|"
        totalPrint[1 + col + 1 + col] += " " + "-" * row + " "
    elif i == "7":
        totalPrint[0] += " " + "-" * row + " "
        for j in range(col):
            totalPrint[1 + j] += " " + " " * row + "|"
        totalPrint[col + 1] += " " + " " * row + " "
        for j in range(col):
            totalPrint[1 + col + 1 + j] += " " + " " * row + "|"
        totalPrint[1 + col + 1 + col] += " " + " " * row + " "
    elif i == "8":
        totalPrint[0] += " " + "-" * row + " "
        for j in range(col):
            totalPrint[1 + j] += "|" + " " * row + "|"
        totalPrint[col + 1] += " " + "-" * row + " "
        for j in range(col):
            totalPrint[1 + col + 1 + j] += "|" + " " * row + "|"
        totalPrint[1 + col + 1 + col] += " " + "-" * row + " "
    elif i == "9":
        totalPrint[0] += " " + "-" * row + " "
        for j in range(col):
            totalPrint[1 + j] += "|" + " " * row + "|"
        totalPrint[col + 1] += " " + "-" * row + " "
        for j in range(col):
            totalPrint[1 + col + 1 + j] += " " + " " * row + "|"
        totalPrint[1 + col + 1 + col] += " " + "-" * row + " "
    elif i == "0":
        totalPrint[0] += " " + "-" * row + " "
        for j in range(col):
            totalPrint[1 + j] += "|" + " " * row + "|"
        totalPrint[col + 1] += " " + " " * row + " "
        for j in range(col):
            totalPrint[1 + col + 1 + j] += "|" + " " * row + "|"
        totalPrint[1 + col + 1 + col] += " " + "-" * row + " "
    for j in range(printcol):
        totalPrint[j] += " "

for i in totalPrint:
    print(i)
