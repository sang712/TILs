"""
문제에서 요구하는 대로 구현하였음
"""
N = int(input())
nums = sorted(list(map(int, input().split())))

ans = 0
if nums[-1] == 0:
    print(0)
else:
    for i in range(1, N):
        if nums[N - i - 1] <= i and nums[N - i] >= i:
            print(i)
            break
    else:
        print(N)