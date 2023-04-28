n = int(input())
count = 0

for _ in range(n):
    word = input().strip()
    prev_char = ''
    used_chars = set()

    for char in word:
        if char != prev_char:
            if char in used_chars:
                break
            used_chars.add(prev_char)
            prev_char = char
        else:
            continue
    else:
        count += 1

print(count)
