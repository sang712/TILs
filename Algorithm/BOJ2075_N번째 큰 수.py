"""
전체를 다 받아서 정렬한 뒤 출력을 하려니 메모리초과가 되어
입력을 한 줄 받을 때마다 정렬하여 가장 큰 N개의 값만을 남기도록 하였음
"""
N = int(input())
nums = []
for _ in range(N):
    nums.extend(list(map(int, input().split())))
    nums.sort()
    nums = nums[-N:]
print(nums[-N])