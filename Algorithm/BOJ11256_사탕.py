import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    J, N = map(int, input().split())

    boxes = []

    for i in range(N):
        R, C = map(int, input().split())
        boxes.append(R*C)

    boxes = sorted(boxes, reverse=True)
    count = 0
    for box in boxes:
        if J > 0:
            J -= box
            count += 1
        else:
            break
    print(count)