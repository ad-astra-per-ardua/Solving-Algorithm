doc = input()
word = input()

count = start = 0
while start < len(doc):
    pos = doc.find(word, start)
    if pos != -1:
        start = pos + len(word)
        count += 1
    else:
        break

print(count)
