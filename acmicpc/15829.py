a = int(input())
str = input()

val = 0
for i, ch in enumerate(str):
    pos = ord(ch) - ord('a') + 1
    val += pos * (31 ** i)

print(val)
