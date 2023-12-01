"""
문제의 요구사항대로 구현하였음
"""
N, M = map(int, input().split())

boxes = list(map(int, input().split()))
books = list(map(int, input().split()))

wasted = 0
box_num = 0
for i in range(M):
    while True:
        if boxes[box_num] >= books[i]:
            boxes[box_num] -= books[i]
            break
        else:
            wasted += boxes[box_num]
            box_num += 1
 
for j in range(box_num, N):
    wasted += boxes[j]

print(wasted)