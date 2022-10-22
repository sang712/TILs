'''
파이썬에서 제공하는 sort()함수가 O(nlogn)으로 구현되어 있어 사용해 보았음
추후에 다른 정렬으로 구현해보는 것으로
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort()
for num in nums:
    print(num)