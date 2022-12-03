N, r, c = map(int, input().split())

cnt = 0
visited_target = False
def check(size, row, col):
    global visited_target
    if visited_target:
        return
    
    if size == 1:
        global cnt
        cnt += 1
        if row == r and col == c:
            visited_target = True
        return
    
    
    devide = size // 2
    
    check(devide, row, col)
    check(devide, row, col + devide)
    check(devide, row + devide, col)
    check(devide, row + devide, col + devide)

check(2**N, 0, 0)
print(cnt - 1)