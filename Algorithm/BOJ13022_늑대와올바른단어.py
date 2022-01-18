word = input()

count = [0, 0, 0, 0]

for char in word:
    if char == 'w':
        if count[1] or count[2] or count[3]:
            break
        count[0] += 1
    elif char == 'o':
        if count[2] or count[3]:
            break
        count[1] += 1
    elif char == 'l':
        if count[3]:
            break
        count[2] += 1
    elif char == 'f':
        count[3] += 1
    else:
        break

    if count[0] < count [1] or count[1] < count[2] or count[2] < count[3]:
        break
    if count[0] == count[1] == count[2] == count[3]:
        count = [0, 0, 0, 0]

if count == [0, 0, 0, 0]:
    print(1)
else:
    print(0)