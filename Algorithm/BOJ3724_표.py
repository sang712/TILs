import sys
input = sys.stdin.readline
for tc in range(int(input())):
    M, N = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    ans = 1
    temp = 1
    for i in range(N):
        temp *= nums[i][0]
    max_num = temp
    
    for j in range(1, M):
        temp = 1
        for i in range(N):
            temp *= nums[i][j]
        if max_num <= temp:
            max_num = temp
            ans = j + 1
    print(ans)    
    