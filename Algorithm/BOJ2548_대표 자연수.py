"""
그냥 정렬해서 중앙값 출력하면 되는 문제였음
"""
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
nums_for_loop = sorted(list(set(nums)))

def sigma_abs(n):
    result = 0
    for num in nums:
        result += abs(n - num)
    return result

ans = 10_000
idx = len(nums_for_loop) // 2
min_sigma_abs = 200_000_000
for i in range(idx, -1, -1):
    temp = sigma_abs(nums_for_loop[i])
    if temp <= min_sigma_abs:
        ans = nums_for_loop[i]
        min_sigma_abs = temp
    else:
        break
for i in range(idx + 1, len(nums_for_loop)):
    temp = sigma_abs(nums_for_loop[i])
    if temp < min_sigma_abs:
        ans = nums_for_loop[i]
        min_sigma_abs = temp
    else:
        break
print(ans)

"""
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[(N-1)//2])
"""