blocks = list(map(int, input().split()))
while True:
    if blocks == [1, 2, 3, 4, 5]:
        break
    for i in range(4):
        if blocks[i] > blocks[i + 1]:
            blocks[i], blocks[i + 1] = blocks[i + 1], blocks[i]
            print(*blocks)
