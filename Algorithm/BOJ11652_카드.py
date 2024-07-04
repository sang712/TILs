"""
주어진 입력을 딕셔너리 자료 구조를 이용해 카운팅하고
카운팅이 많이 된 순, 수가 작은 순으로 정렬을 사용하여 원하는 값을 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = {}
for _ in range(N):
    num = int(input())
    nums.setdefault(num, 0)
    nums[num] += 1

print(sorted(nums.items(), key=lambda x: (-x[1], x[0]))[0][0])