import sys
input = sys.stdin.readline
while True:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    square = h**2 + w**2
    min_square = 22501
    ans_h, ans_w = 0, 0
    for i in range(1, 150):
        for j in range(i+1, 151):
            if i == h and j == w:
                continue
            t_square = i**2 + j**2
            if t_square >= square and min_square > t_square:
                if t_square == square and i < h:
                    continue
                min_square = t_square
                ans_h = i
                ans_w = j
    print(ans_h, ans_w)