N = int(input())
width, height = 1, 1
while (width + 1) * (height + 1) < N:
    if width == height:
        width += 1
    else:
        height += 1
print(2 * (width + height))