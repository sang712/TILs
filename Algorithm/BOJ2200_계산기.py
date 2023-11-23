"""
각 항별로 무조건 x를 곱해준다고 생각하고
0이 아닌 경우에만 해당 항의 계수를 더한다고 생각해서 풀이하였음
"""
N = int(input())
nums = input().split()

cnt = 1
for i in range(1, N):
    if nums[i] != '0':
        cnt += 1 + len(nums[i])
    cnt += 2
if nums[-1] != '0':
    cnt += 1 + len(nums[-1])
cnt += 1

print(cnt)
