"""
문제에서 요구하는 내용을 그대로 구현하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

if nums[1] - nums[0] == nums[2] - nums[1]:
    print(nums[-1] + nums[1] - nums[0])
else:
    print(nums[-1] * (nums[1] // nums[0]))